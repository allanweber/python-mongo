from mongoengine import *
from post import Post

connect('mongoengine_test', host='localhost', port=27017)

Post.drop_collection()

post_1 = Post(
    title="Sample post",
    content='Some engaging content',
    author='Scott'
)

post_1.save()
print(post_1.title)

# Simulate error
post_2 = Post(content='Content goes here', author='Michael')
try:
  post_2.save()
except Exception as e:
  print(str(e))
