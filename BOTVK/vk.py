import vk_api
token = "245a152f245a152f245a152f7d24315e952245a245a152f794a89413df9bf0a628b4531"
vk = vk_api.VkApi(token=token)
vk._auth_token()
posts = vk.method("wall.get", {"owner_id":"-51324776", "offset": "1", "count": "100"})
print(posts['items'][6]['text'])