import vk_api
import random


def get_pictures(id):
    token = "245a152f245a152f245a152f7d24315e952245a245a152f794a89413df9bf0a628b4531"
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    posts = vk.wall.get(owner_id=id, count=99, offset=random.randint(1, 500))
    pictures = []
    for post in posts["items"]:
        attachment = post.get("attachments")
        if attachment and attachment[0]["type"] == "photo":
            pictures.append(attachment[0]["photo"]["id"])
    return "photo{}_{}".format(id, random.choice(pictures))
