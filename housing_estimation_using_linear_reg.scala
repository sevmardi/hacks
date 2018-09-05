import org.apache.spark.ml.linalg.Vectors
import org.apache.spark.ml.regression.LinearRegression

val points = spark.createDataFrame(Seq(
(1620000,Vectors.dense(2100)),
(1690000,Vectors.dense(2300)),(1400000,Vectors.dense(2046)),
(2000000,Vectors.dense(4314)),
(1060000,Vectors.dense(1244)),
(3830000,Vectors.dense(4608)),
(1230000,Vectors.dense(2173)),
(2400000,Vectors.dense(2750)),
(3380000,Vectors.dense(4010)),
(1480000,Vectors.dense(1959))
)).toDF("label","features"))

// init linear regression
val lr = new LinearRegression()

// train the model
val model = lr.fit(points)

// create some test dataset 
val test = spark.createDataFrame(Seq(Vectors.dense(2100)).map(Tuple())

// Make predictions for the test data:
val predictions = model.transform(test)





