import boto3
from datetime import datetime

# creating an S3 client object
s3 = boto3.client('s3')

# setting the name of the S3 bucket where you want to upload the file
bucket_name = 'pdf-sample-project'

# setting the name of the file you want to upload
file_name = 'shingil.pdf'

# creating a timestamp for the current time
timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

# uploading the file to S3
s3.upload_file(file_name, bucket_name, f'{timestamp}-{file_name}')

# creating a dictionary to store the file name and date of upload
# i'm using current timestamp instead
file_dict = {
    'file_name': f'{file_name}',
    'date_uploaded': timestamp
}

# printing the dictionary
print(file_dict)