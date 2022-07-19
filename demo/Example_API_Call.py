from eventregistry import *

  
MAX_RESULTS = 1000

  
er = EventRegistry(apiKey = YOUR_API_KEY)

  
iter = QueryTweetsIter(

  
    keywords = QueryItems.OR(["Stop_killing_women", "women", "feminist_strike", "stop_violence_against_women"]),

  
    lang = "ar", location = "Palestine", incident= "killing_women")

for item in iter.execQuery(er,

  
        sortBy = "date",

  
        maxItems = MAX_RESULTS,

  
        returnInfo = ReturnInfo(

  
            tweetInfo = TweetInfoFlags(

  
                bodyLen = 300,

  
                concepts = True,

  
                categories = True)

  
    )):

  
    # actions

  
    print(item)
