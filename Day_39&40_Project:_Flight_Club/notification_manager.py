import smtplib

EMAIL_PROVIDER_SMTP_ADDRESS = ''
MY_EMAIL = ''
MY_PASSWORD = ''


class NotificationManager:

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )