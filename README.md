## Inspiration

Our collective interest in reading news articles and implementing Natural Language Processing methods were a great inspiration for the project. We were also motivated by the problem that most people in try to avoid reading negative articles. We came with a creative solution to solve all these problems

## What It Does

Don't have the time to read the full article? Trying to avoid reading negative news articles? This project is made just for you! After pasting the link of the the article, it will create a summary and classify if it is a positive or negative article. It will also give the users a similar NYT article to the article pasted. This app will also give a the most common tags found in the article that are relevant

**Key features:**
- Summarize the article in the 3 to 4 sentences
- Check whether the article is a positive or negative article based on sentimental analysis of the article
- Gives out the most relevant tags (one word token) for the article so you would know what categories the article falls under
- Also gives out the user a New York Times article which is similar to the original article pasted if the user wishes to know more about the topic

## How We Built it

We used python modules from BERT created by Hugging Face. We then worked on classifying the most popular tags of the article by getting a score that was implemented using a transformer by hugging face. We then worked on getting the NYTimes API to get a similar result which included some words of the headline of the original article if a reader wants to know more about the topic discussed in the article. At the end we used Streamlit.io to create a creative and responsive web app and implemented our project in there.


## Future Viability

We see a clear path towards making PocketAnalyst a sustainable product that makes a real difference in its users' lives. We see our product as one that will work well in partnership with other businesses, especially brokerage firms, similar to what CreditKarma does with credit card companies. We believe that giving consumers access to a free chatbot to help them invest will make their investment experiences easier, while also freeing up time in financial advisors' days.

## Challenges We Ran Into

We tried to implement this project on cloud by using either GCP or Streamlit cloud. Unfortunately, we were unable to get those implemented in the given amount of time. We also ran into issue of sorting the tags and presenting the user the most relevant tags of an article.

## Accomplishments That We Are Proud Of

Completing the project was a great achievement for us! We are also proud of the accomplishment of using NLP models in a hackathon. 

## What We Learned

We learned how to implement a NLP model in the real-world scenario. We also learned the challenges a NLP model implementation faces and what are some ways to overcome those challenges. This was our first time using streamlit.io cloud to host a our app, which was a great learning curve for us

## What's Next for PocketAnalyst

This isn't the last you've heard from us!

Going forward, we will be working on:
- Better extraction of the article. 
- More detailed and improved summarization of the article
- Increased accuracy of the sentimental analysis of the article
- Checking the political bias of the article using Machine Learning



