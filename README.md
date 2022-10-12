# Twitter Assist

This django application helps you to download and save twitter threads. Valuable tweets can be saved by mentioning bot name within the tweet using your twitter account. With the help of twiteer API these mentioned tweets can be downloaded from the Dashboard.

# ScreenShots

![image](https://user-images.githubusercontent.com/28696896/185988495-a492daf8-b893-4ecb-af2f-2395af553f48.png)
![image](https://user-images.githubusercontent.com/28696896/185989781-98d6a07e-4e85-4f58-b3a6-b117e798eae8.png)
![image](https://user-images.githubusercontent.com/28696896/185989031-808d9e9d-c0a1-4468-874a-154924cf5d5a.png)

## Team members

1. [Achyuth Mohan](https://github.com/AchyuthMohan)
2. [Adithya Kartha](https://github.com/adithyakartha)
3. [Athul Reji](https://github.com/athulreji)

## How it Works ?

### For users:
  1.  This web application requires the user to have a twitter account.
  2.  Using the provided link, an account can be created by providing credentials like your name, email id, twitter id etc.
  3.  Login using the created username and password and this will take you to the dashboard.
  4.  You will be provided with a bot name and by mentioning this bot name in your tweets, you can download and save the tweet.
  5.  After giving all your tweets you can click the 'download' button in the dashboard.
  6.  Then the browser will download a text file 'mentions.txt' which contains all the tweets along with the timestamp.

### For Developers:
  1.  The program tracks the tweets of user by using Twitter API and Tweepy. You should have a Twitter Developer account to access the API.
  2.  When the user creates an account in the website using twitter id and other details it will be saved in the DB.
  3.  When the user log in into the dashboard, the progrram collects the tweets from user using the API.
  4.  When the user clicks the download button the program writes the current tweets in a text file and this text file will be made available for the user to download.
  5.  The python file containing API keys are 'ignored' for security issues in GitHub repo. A security_keys.py file with api keys must be added to twitter_assist/mainappp directory.

### Libraries Used
[requirements.txt](https://github.com/athulreji/twitter-assist/blob/main/requirements.txt)

## How to configure

[Instructions for setting up project](https://github.com/athulreji/twitter-assist/blob/main/config.md)
