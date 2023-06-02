CSV Processing API
This is an API that allows you to upload a CSV file with data about songs, dates, and number of plays, and then process it to generate a new CSV file with the total number of plays for each song on each date.

Installation

Navigate to the project directory: cd test_bmat
Install the required: 

https://www.python.org/downloads/
pip install uuid
pip install flask

Starting the API Server
To start the API server, run the following command:

python app.py
flask run 
This will start the server on port 5000.

Uploading a CSV File
To upload a CSV file for processing, you can use the following endpoint:

POST /process_csv
You can use any HTTP client to make a request to this endpoint, such as cURL or Postman. You'll need to include the CSV file as the body of the request. The file should be in the following format:


Song,Date,Number of Plays
Umbrella,2020-01-02,200
Umbrella,2020-01-01,100
In The End,2020-01-01,500
Umbrella,2020-01-01,50
In The End,2020-01-01,1000
Umbrella,2020-01-02,50
In The End,2020-01-02,500

Retrieving the Resulting CSV File
Once the CSV file has been processed, you can retrieve the resulting CSV file using the following endpoint:

GET /get_result/{task_id}
Replace {task_id} with the ID of the processing task that was returned when you uploaded the CSV file.

This will return the resulting CSV file as a download.

Notes
If you have any questions or issues, please reach out to [godie8a@hotmail.com].