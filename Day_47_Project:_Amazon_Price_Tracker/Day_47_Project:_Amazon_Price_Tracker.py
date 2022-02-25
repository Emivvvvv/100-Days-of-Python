from bs4 import BeautifulSoup
import requests
import smtplib

#You should put you email and password directly to variables. I changed them with input fuction because I'll put my code on github to protect my mail address and pass.
my_email = input("Type your email address >>>")
password = input("Type your password >>>")
to_email = input("Type the email which you want to send a price mail >>>")

headers = {
    "User-Agent": "###",
    "Accept-Language": "###"
}

response = requests.get(url="www.amazon.com.tr/Samsung-R830-Galaxy-Active2-Al%C3%BCminyum/dp/B07Y9PDXLC/ref=pd_day0_1/262-8018770-5017149?pd_rd_w=AZDP7&pf_rd_p=358c812e-c972-4842-a7b9-b79c76c6c0ce&pf_rd_r=5N7E3JFB0Y6MP2R0NV72&pd_rd_r=755775f5-797a-4a0b-839d-6fe4bc1095fb&pd_rd_wg=D6gQo&pd_rd_i=B07Y9PDXLC&psc=1", headers=headers)
amazon_html = response.text
soup = BeautifulSoup(amazon_html, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()[:-1]

year_min = 1406

if price < year_min:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:Product that you looking for has year low price rn!\n\n The price of the product is now: {price}. It is good time to buy rn.")
        connection.close()