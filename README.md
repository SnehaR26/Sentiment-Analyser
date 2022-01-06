# Sentiment-Analyser
The Aim of this project is to create a sentiment analyzer which takes as input, a tweet about a given movie and as an output tells whether the sentiment of the tweet was positive or negative.

The tweet can be extracted using the code in tweet.py. I have chosen a movie review by using #movie_name as a search parameter. 
The tweet contains a lot of meta data, so our sentiment.ipynb also contains code to trim it and extract just the textual data aka the content of the tweet. 

Once trained, the model is fed the tweet and it classifies whether the tweet(review) was positive or negative.  

I plan to further this project by gathering more data and deducting the overall sentiment for the movie on twitter.

I credit the instructors and material at Udacity for forming a base for this project by helping me understand the concepts of LSTM and RNNs

The dataset can be found at this [link](https://github.com/udacity/deep-learning-v2-pytorch/tree/master/sentiment-rnn/data)
