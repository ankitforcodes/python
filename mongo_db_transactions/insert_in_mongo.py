import pymongo
from datetime import datetime
from datetime import date
#import datetime


current_date = date.today()
current_time = datetime.now()
readable_date_time = datetime.now()
readable_date = current_date.strftime("%b-%d-%Y")
readable_time = current_time.strftime("%H:%M:%S")

print(readable_date_time)
print(readable_date)
print(readable_time)

question_json = {
	"question": "How is the better PM?",
	"options": ["Modi", "Rahul Gandhi"],
	"category": ["politics", "inidianpolitics"],
	"subcategory": [],
	"tags": ["modi", "rahulgandhi", "bjp", "congress", "india"],
	"qid": 0,
	"q_hash_id": "",
	"trend_quotient": 0,
	"views": 1,
	"total_votes": 0,
	"votes": {
		"Modi": 0,
		"Rahul Gandhi": 0
	},
	"created_by": "ankitforcodes",
	"create_date": readable_date,
	"create_time": readable_time,
	"last_modified_date": readable_date,
	"last_modified_time": readable_time,
	"insert_date_time": datetime.now()
}



myclient = pymongo.MongoClient("mongodb+srv://ankit:ankit12168#@cluster0-zrq5o.mongodb.net/opinions_v1?retryWrites=true&w=majority")
db = myclient['opinions_v1']
#table_name = db['questions_v1']
#table_name = 'questions_v1'
result = db.questions_v1.insert_one(question_json)