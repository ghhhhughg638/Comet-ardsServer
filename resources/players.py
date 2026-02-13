import random

import falcon.asgi
import falcon
from database import db, User


class PlayersResource:
    async def on_put(self, req, resp, player_id):
        data: dict = await req.get_media()
        user: User = req.context.user
        action = data.get('action')
        value = data.get('value')
        if action == 'set-name':
            used_tags = set(await User.filter(player_name=value).values_list('player_tag', flat=True))
            state = False
            if len(used_tags) >= 10000:
                resp.media = {'error': 'too many tag'}
                resp.status = falcon.HTTP_400
                return
            for i in range(30):
                player_tag = random.randint(0, 9999)
                if player_tag not in used_tags:
                    user.player_name = value
                    user.player_tag = player_tag
                    await user.save()
                    state = True
                    resp.media = {
                        'player_name': value,
                        'player_tag': player_tag
                    }
                    return
            if not state:
                tag = 0
                for tag in range(10000):
                    if tag not in used_tags:
                        user.player_name = value
                        user.player_tag = tag
                        await user.save()
                        state = True
                        resp.media = {
                            'player_name': value,
                            'player_tag': tag
                        }
                        return

