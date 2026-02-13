from datetime import datetime, timezone

import falcon
import falcon.asgi

from database import db


class DeckUpdataResources:
    async def on_put(self, req, resp, player_id, deck_id):
        data = await req.get_media()
        print(type(data.get('deck_code')))
        if data.get('action') == 'fill':
            await db.initialize()
            deck =await db.get_deck(id=deck_id)
            deck.deck_code = data.get('deck_code')
            await deck.save()
        resp.state = falcon.HTTP_200