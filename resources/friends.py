import falcon.asgi
import falcon
from database import db


class FriendResource:
    async def on_post(self, req, resp, player_id):
        data = await req.get_media()

        friend_tag = data.get('friend_tag')
        friend_name = data.get('friend_name')
        await db.initialize()
        print(friend_name,friend_tag)
        if friend_tag == 0:
            print('改名')
            await db.updata_user(user_id=player_id, player_name=friend_name)
        resp.state = falcon.HTTP_200
