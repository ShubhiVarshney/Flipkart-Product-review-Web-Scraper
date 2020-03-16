# Flipkart-Product-review-Web-Scraper
Flipkart product review Web Scraper project is implemented to get the reviews of customers on their product purchase. Libraries such as: - BeautifulSoup, Requests &amp; Flask are used to scrap the text using tags in html file.

TO DO THINGS BEFORE STARTING PROJECT:

1. Create a virtual environment and install the required libraries from requirement.txt file.
   - To create virtual environment, open Anaconda Prompt and type 
      conda create -n yourEnvironmentName
   - To install requirements.txt file after setting up the environment, type
      pip install -r requirement.txt
2. For project testing purpose, install Postman in your PC. 
3. Description about files: - 
   - Scraper.py -> This file will scrap the reviews of the customer from the html page of flipkart (link commented).
   - clsReview.py -> This file will take all the variables created in Scraper.py in a class.
   - ClientApp.py -> This file call the "getReviewsFromURL" method from Scraper.py for execution.
   
 At last, run the ClientApp.py file in Anaconda Prompt. After this, in Postman, pass the host and port followed by "/getreviews" and then pass the two variables i.e. websiteURL & URL in dictionary format.
And, you have have the customer's review scraped!!!
