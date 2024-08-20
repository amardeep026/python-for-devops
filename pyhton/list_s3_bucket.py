# import boto3
# # Function to list S3 buckets
# def list_s3_buckets():
#     # Create an S3 client
#     s3_client = boto3.client('s3')
    
#     # Call the list_buckets method to get all buckets
#     response = s3_client.list_buckets()
    
#     # Get bucket names from the response
#     buckets = [bucket['Name'] for bucket in response['Buckets']]
    
#     return buckets

# # Call the function to get the list of buckets
# buckets = list_s3_buckets()

# # Print each bucket name
# print("S3 Buckets:")
# for bucket in buckets:
#     print(bucket)

import boto3

# Create an S3 client using the default AWS configuration
s3 = boto3.client('s3')

# List all buckets
buckets = s3.list_buckets()

print("Buckets:")
for bucket in buckets['Buckets']:
    print(f"- {bucket['Name']}")
