import boto3
from botocore.exceptions import ClientError
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional, List
from XpenseMeter.core.config import settings


def send_email(
    subject: str,
    body: str,
    recipient: List[str],
    cc: List[str] = [],
    bcc: List[str] = [],
    sender: str = None,
    is_html: bool = False,
    file_attachment: str = None,
    filename: str = "document.pdf",
    inline_images: Optional[dict] = None
) -> bool:
    try:
        client = boto3.client('ses', region_name=settings.AWS_REGION)
        if (sender == None):
            sender = settings.MY_EMAIL

        destination = {
                'ToAddresses': recipient
        }
        if cc:
            destination.update({'CcAddresses': cc})
        if bcc:
            destination.update({'BccAddresses': bcc})

        msg = MIMEMultipart()
        msg['Subject'] = subject
        body_type = 'html' if is_html else 'plain'
        email_body = MIMEText(body, body_type)
        msg.attach(email_body)
        
        if file_attachment:
            file_attachment_content = file_attachment.read()
            file_part = MIMEApplication(file_attachment_content, Name=filename)
            file_part['Content-Disposition'] = f'attachment; filename="{filename}"'
            msg.attach(file_part)

        if inline_images:
            for cid, image_data in inline_images.items():
                image = MIMEImage(image_data, name=f"{cid}.png")
                image.add_header('Content-ID', f"<{cid}>")
                msg.attach(image)
        
        #Provide the contents of the email.
        response = client.send_raw_email(
            Destinations=destination['ToAddresses'] + destination.get('CcAddresses', []) + destination.get('BccAddresses', []),
            Source = sender,
            RawMessage={'Data': msg.as_string()}
        )

        if response and response.get('ResponseMetadata', {}).get('HTTPStatusCode', None) == 200 and response.get('MessageId', None):
            return True

    except ClientError as e:
        print('ClientError while sending email: ', str(e))
        return False
    except Exception as e:
        print('Exception while sending email: ', str(e))
        return False