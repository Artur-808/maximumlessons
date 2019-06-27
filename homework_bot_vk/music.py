import vk_api
import random

def get_music(id):
    token = "245a152f245a152f245a152f7d24315e952245a245a152f794a89413df9bf0a628b4531"
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()
    posts = vk.audio.get(owner_id=id, count=10, offset=random.randint(1, 10))
    music = []
    for post in posts["items"]:
        attachment = post.get("attachments")
        if attachment and attachment[0]["type"] == "audio":
            music.append(attachment[0]["audio"]["id"])
    return "audio{}_{}".format(id, random.choice(music))