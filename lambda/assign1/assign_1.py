import json

def lambda_handler(event, context):
    # Extract the size of the uploaded file
    size = event['Records'][0]['s3']['object']['size']

    print("Size of file : ", size)
    
    print("**************************")
    
    threshold_bytes = 100 * 1024 * 1024  # 100MB in bytes
    
    if size > threshold_bytes:
        alert_message = f"Alert: The file '{event['Records'][0]['s3']['object']['key']}' in bucket '{event['Records'][0]['s3']['bucket']['name']}' exceeds the 100MB threshold. File size: {size/(1024 * 1024)} MB."
    else:
        alert_message = f"Alert: The file '{event['Records'][0]['s3']['object']['key']}' in bucket '{event['Records'][0]['s3']['bucket']['name']}' has size {size/(1024 * 1024)} MB."
        
    print(alert_message)
    # Return a response
    return {
        'statusCode': 200,
        'body': alert_message
    }