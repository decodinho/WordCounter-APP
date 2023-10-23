# WordCounter-APP
This app have been created by GEDEON NOkBAK in order to count the number of words in a .pdf .docx etc file.

At the beginning, the user will download a file on the homeWordCounter.html page. After clicking on a button, an API is triggering(we choose AWS and API Gateway service to handle this part of the process). The API Gateway will trigger a Lambda serverless function (uploadToS3) that will in turn strore the file in an s3 bucket.

Once the file strored, it will notify by s3 PUT Notification process that the file is ready and directly a second lambda function (triggerEMRJob) will start a spark job on an EMR cluster. The spark job is written in python(wordOccurrencies.py).

The result of the operation is stored in a .txt file (results.txt) in a S3 bucket.

The second page boutoncompteur.html contains a button  if hit will call a REST API that will trigger a lambda function so that the result could be displayed on screen.
This project could be trivial in the first gaze, but implement it show that you need a basic knowledge of the datapipeline process, ETL knowledge, Apache Spark RDD mastering. It also shows that you master in a sufficient way the main data services involved in a data process.
