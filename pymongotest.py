from pymongo import MongoClient

# client = MongoClient('mongodb://localhost:27017')
client = MongoClient('localhost', 27017)

#db = client['pymongo_test']
db = client.pymongo_test

posts = db["posts"]

posts.drop()

post_data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun',
    'author': 'Allan'   
}

result = posts.insert(post_data)
print('Post Result ', result)

post_1 = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
post_2 = {
    'title': 'Virtual Environments',
    'content': 'Use virtual environments, you guys',
    'author': 'Scott'
}
post_3 = {
    'title': 'Learning Python',
    'content': 'Learn Python, it is easy',
    'author': 'Bill'
}

result_many = posts.insert_many([post_1, post_2, post_3])
print("Result of insert many: {0}".format(result_many.inserted_ids))

bill_posts = posts.find_one({'author':'Bill'})
print('Retrivied posts: ', bill_posts)

# Cursor
scotts_post = posts.find({'author':'Scott'})
print_scott = [post for post in scotts_post]
print('List of prints: ', print_scott)