import vk
import json

session = vk.Session()
vkapi = vk.API(session)

user = vkapi.users.get(user_id = 94852538, fields = 'domain,sex,city,bdate', v=5.74, access_token = '546ae2bb546ae2bb546ae2bb57540c190d5546a546ae2bb0f8275d55f6c0c371405a331')
# print(json.dumps(user))
#domain,sex,city,bdate
user = user[0]
friends = vkapi.friends.get(user_id = 94852538, fields = 'domain', v=5.74, access_token = '546ae2bb546ae2bb546ae2bb57540c190d5546a546ae2bb0f8275d55f6c0c371405a331')
# print(friends)

friends_ids = [item['id'] for item in friends['items']]
user['friends'] = []

counter = 0

for friend_id in friends_ids:
	friend = vkapi.users.get(user_id = friend_id, fields = 'domain,sex,city,bdate', v=5.74, access_token = '546ae2bb546ae2bb546ae2bb57540c190d5546a546ae2bb0f8275d55f6c0c371405a331')[0]
	# try:
	# 	photos = vkapi.photos.get(user_id = friend_id, album_id = 'profile', v=5.74, access_token = '546ae2bb546ae2bb546ae2bb57540c190d5546a546ae2bb0f8275d55f6c0c371405a331')	
	# except vk.exceptions.VkAPIError:	
	# 	photos = []
	# friend['photos'] = photos
	friend['friends'] = []
	counter += 1
	print(counter)
	# inner_counter = 0
	# inner_friends = vkapi.friends.get(user_id = friend_id, fields = 'domain', v=5.74, access_token = '546ae2bb546ae2bb546ae2bb57540c190d5546a546ae2bb0f8275d55f6c0c371405a331')
	# inner_friends_ids = [item['id'] for item in inner_friends['items']]
	# for inner_friend_id in inner_friends_ids:
	# 	inner_friend = vkapi.users.get(user_id = friend_id, fields = 'domain,sex,city,bdate', v=5.74, access_token = '546ae2bb546ae2bb546ae2bb57540c190d5546a546ae2bb0f8275d55f6c0c371405a331')[0]
	# 	# try:
	# 	# 	photos = vkapi.photos.get(user_id = friend_id, album_id = 'profile', v=5.74, access_token = '546ae2bb546ae2bb546ae2bb57540c190d5546a546ae2bb0f8275d55f6c0c371405a331')	
	# 	# except vk.exceptions.VkAPIError:	
	# 	# 	photos = []
	# 	# inner_friend['photos'] = photos
	# 	friend['friends'].append(inner_friend)
	# 	inner_counter += 1
	# 	print('inner: {}'.format(inner_counter))
	user['friends'].append(friend)
	# print(len(user_ids))

with open('res.json', 'w') as out: 
	print(json.dump(user, out))


# print(json.dumps(photos))

