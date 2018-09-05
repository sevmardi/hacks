import spark.implicits._

import org.apache.spark.ml.recommendation.ALS
import org.apache.spark.ml.recommendation.ALS.Rating
import org.apache.spark.ml.recommendation.ALSModel
import org.apache.spark.ml.evaluation.RegressionEvaluator

val als = new ALS().setMaxIter(5).setRegParam(0.01).setUserCol("userId").setItemCol("movieId").setRatingCol("rating")

val ratings = Seq(Rating(0, 2, 3), Rating(0, 3, 1), Rating(0, 5, 2), Rating(1, 2, 2)).toDF("userId", "movieId", "rating")
val Array(traning, testing) = ratings.randomSplit(Array(0.8, 0.2))

// make sure that RDD have at least one record
assert(traning.count > 0)
assert(testing.count > 0)

// drop NaNs
model.setColdStartStrategy("drop")
val predictions = model.transform(testing)

val evaluator = new RegressionEvaluator().setMetricName("rmse").setLabelCol("rating").setPredictionCol("prediction")
val rmse = evaluator.evaluate(predictions)

println(s"Root-mean-square error = $rmse")

// Model is ready for recommendations

// Generate top 10 movie recommendations for each user
val userRecs = model.recommendForAllUsers(10)
userRecs.show(truncate = false)

// Generate top 10 user recommendations for each movie
val movieRecs = model.recommendForAllItems(10)
movieRecs.show(truncate = false)

// Generate top 10 movie recommendations for a specified set of users
// Use a trick to make sure we work with the known users from the input
val users = ratings.select(als.getUserCol).distinct.limit(3)
val userSubsetRecs = model.recommendForUserSubset(users, 10)
userSubsetRecs.show(truncate = false)

// Generate top 10 user recommendations for a specified set of movies
val movies = ratings.select(als.getItemCol).distinct.limit(3)
val movieSubSetRecs = model.recommendForItemSubset(movies, 10)
movieSubSetRecs.show(truncate = false)

System.exit(0)

