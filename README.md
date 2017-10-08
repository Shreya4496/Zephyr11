# Zephyr11
PROBLEM STATEMENT
TEAM ZEPHYR

“Inspire customers to travel with VISTARA”

ADDRESSING WHAT?

Vistara Buddy is a service used for increasing the customer base for Vistara by
 providing the following functionalities:

Offers personalized promotional vouchers/coupons/travel offers not only to Vistara users who are registered on our web portal but also to the potential users who aren’t registered with Vistara yet, thus attracting more traffic towards it.
Events related to user’s interests are shown along with Vistara Flight Offers for the event’s location to inspire customers to travel. 
Location for events trending on twitter is given to Vistara so that they can create promotional events for these trending locations.
Prediction of potential stations by tracking trending locations.

ADDRESSING WHY?

The Vistara Buddy is designed to inspire customers to travel with “Vistara”.  We plan to increase the customer base of Vistara. Since it is relatively new airlines, we have proposed an idea that uses personalised promotional strategies to divert more new customers towards it.

We have considered two categories of customers:
Business travellers
Leisure based travel

During business tourism (traveling), individuals are still working and being paid, but are doing so away from both their workplace and home. They are primarily concerned about quick booking and timely services and hardly concern themselves with promotional offers or holiday season.

We are targeting leisure based travel customers who are in constant search for events of their interests, and affordable travel plans. This is achieved by mining user’s twitter timeline. We analyse the user’s posts, his followers and his follows and categorize his interests using natural language processing. This produces a set of possible categories towards which user is inclined, like politics, beauty and fashion. We then find latest events in these categories happening across the globe and return them to user.

We can use this to promote existing offers by the Airlines, and also suggest them various promotional schemes based on user trend.

We have not limited this domain to Vistara customers, but also extended this to non-Vistara customers by mining the local trends, like Sunburn festival and Vaishnodevi, and promote flight offers to these popular destinations using marketing strategies and also try to send email notifications to them.
 
ADDRESSING HOW?


				Fig 1 : model for customer classification


Given the data we are performing the following :

For Vistara Customers:
Access user’s twitter timeline, his tweets, retweets, friends( following) and their descriptions
Collect this data 
Perform Tokenization (breaking up the text)
Classification of tokens into categories (eg politics, cricket, fashion, food etc)
Find trending events using these categories
Extract locations of these trending events
Provide promotional offers to these locations (eg reduced prices, cashback/ loyalty points, Seat upgradation, free lounge passes on airport etc)

For Non- Vistara Customers (registered on twitter):
Mine topics on twitter on basis of their interests(follows and followers) and extract the corresponding location
Find trending events based on these locations
Recommend flights to these locations to all users with promotional offers

For Non- Vistara Customers (not registered on twitter)
Mine trending topics on twitter and extract the corresponding location
Find trending events based on these locations
Recommend flights to these locations to the users via email provided that we have the data. Also, use this data to chalk out strategic marketing strategies

Predicting new stations based on trending locations
Record all the locations obtained by mining twitter profiles of the customers and by mining trending topics by locations
Store the locations along with their frequency (if the obtained location is already in the database increment its frequency else add a new entry)
By observing the database on a weekly or monthly basis we can predict which locations are best suitable for new stations.

Mapping the existing vistara offers with new trend based promotional offers
Using separate models for trend based offers and already existing vistara offers
Check whether 


7. Prediction of potential stations by tracking trending locations.
Using separate models for trend based offers and already existing vistara offers
Check whether there are any clashes between them
Prove vistara offers to customers and trend based offers to vistara for future.








