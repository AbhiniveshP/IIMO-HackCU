# IIMO-HackCU

Devpost Link :https://devpost.com/software/indian-premier-league

## Inspiration
As every match played is considered important and in general, any sports team would like to know the favorable conditions which can help them to win. Here we tried to know the stats and win/loss conditions for multiple combinations ranging from the venue, teams, runs etc. These visualizations with enormous filters will help the team to chose accordingly making all the possible favorable conditions.
## What it does
The final visualization in kibana, will give an overall idea among different seasons information on the number of wins, number of wickets, number of runs and each team scorecard. Thus, we can understand the holistic behavior of each team with the respective season.
## How we built it
The brief description of the entire pipeline would be as follows-
The data from the local computer has been uploaded to Google Storage Bucket using Command Line Interface. Then, it was passed on to Google Pub/Sub platform using Google Cloud Dataflow which was again using the CLI platform. The content from the events as messages on Pub/Sub has been extracted using Google Cloud Functions along with integrating Google Maps API. The load balancer then handles the incoming traffic and sends it onto one of the two Google Compute Engines or the instances. These are finally computed on the Kibana platform to generate the required visualizations.
## Challenges we ran into
The data that has to be uploaded from local PC to the Google Cloud Platform has been cumbersome as there were around 180000 json files that have to be sent as messages to Google Pub/Sub. So, instead of directing those files to Pub/Sub, we had to first store it on Google Storage Bucket. Even uploading files to the Bucket has not been possible using GCP Web UI and we had to switch to using Command Line Interface instead of Web UI.
## Accomplishments that we're proud of
Before starting the hackathon, none of our team members were aware of the Google Cloud Platform. In a single day, all of us were able to understand the ins and outs of few of the GCP platforms that we used for the development of our project which was Google Storage, Google DataFlow, Google Pub/Sub, Google Compute Engine, Load Balancer and also using these with the help of Command Line Interface and not solely depending on the Web UI. We also were able to connect the dots of how we integrate and use each of these platforms with one another.
## What we learned
We have learned to incorporate Google Cloud Platform in visualizing the stats of the player and the teams from which we can determine the accuracy of the team win.we also have learned to work collectively as team.we got to collaborate with a lot of other team members from which we have got a lot of inspiration and lot of knowledge.
## What's next for Indian Premier League Visualizations
.In order, to have a better visualization. The next steps are to get the data of each player by the team. The player data will contain his strength in the game, batting style, bowling style as well as the past history of the players since the game inception in India. Based on the data, we plan to analyze each player's previous scoring history and provide the how well the player can do better based on circumstances.



Team Meambers: <br/>
Nithin Veer Reddy<br/>
Abhinivesh Palusa<br/>
Lokin Sai Makkenna<br/>
Mohan Dwarampudi<br/>
