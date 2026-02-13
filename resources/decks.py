from falcon import HTTPUnauthorized

from database import db, User
from timez import Timez_Create_Now


class DecksResources:
    async def on_post(self, req, resp, player_id):
        try:
            user: User = req.context.user
            if user.id == int(player_id):
                pass
            else:
                raise HTTPUnauthorized(description="Warning")
            data = await req.get_media()
            server_time_z = await Timez_Create_Now()
            new_deck = {
                'name': data.get("name"),
                'main_faction': data.get("main_faction"),
                'ally_faction': data.get("ally_faction"),
                'deck_code': data.get("deck_code"),
                'last_played': server_time_z,
                'create_date': server_time_z,
                'modify_date': server_time_z,
            }
            deck = await db.Create_New_Deck(deck=new_deck, user=user)
            resp.media = {
                "name": deck.name,
                "main_faction": deck.main_faction,
                "ally_faction": deck.ally_faction,
                "card_back": deck.card_back,
                "deck_code": deck.deck_code,
                "favorite": deck.favorite,
                "id": deck.id,
                "last_played": str(deck.last_played),
                "create_date": str(deck.create_date),
                "modify_date": str(deck.modify_date),
            }
        except Exception as e:
            print(e)


"""
    async def on_put(self, req, resp, player_id):
        data = await req.get_media()
        print(data.get('name'))
        if data.get('action') == 'change_card_back':
            await db.initialize()
            deck = await db.get_deck(id=data.get('id'))
            deck.card_back = data.get('name')
            await deck.save()
"""
