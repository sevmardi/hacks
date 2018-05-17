import org.apache.spark.ml.regression.LinearRegression
import org.apache.spark.ml.evaluation.RegressionEvaluator

import org.apache.spark.ml.tuning.{
  ParamGridBuilder,
  TrainValidationSplit
}

// Load data as DataFrame:
val data = spark.read.format("libsvm").load
("s3a://sparkcookbook/housingdata/realestate.libsvm")

// Split data into training and test sets:
val Array(training, test) = data.randomSplit
(Array(0.7, 0.3))

// Instantiate linear regression:

val lr = new LinearRegression().setMaxIter(10)

// parameter grid 
val paramGrid = new ParamGridBuilder()
.addGrid(lr.regParam, Array(0.1,0.01))
.addGrid(lr.fitIntercept)
.addGrid(lr.elasticNetParam, Array(0.0, 0.5, 1.0))
.build()

// Create a training validation split:
val trainValidationSplit = new TrainValidationSplit()
.setEstimator(lr)
.setEvaluator(new RegressionEvaluator)
.setEstimatorParamMaps(paramGrid)
.setTrainRatio(0.8)

// train the model 
val model = trainValidationSplit.fit(training)

// Do the predictions on the test dataset:
val predications = model.transform(test)


// Evaluate the predictions 
val evaluator = new RegressionEvaluator()
evaluator.evaluate(predictions)


