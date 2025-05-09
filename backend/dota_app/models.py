from mongoengine import Document, StringField, FloatField, EmbeddedDocument, EmbeddedDocumentListField


class  Facet(EmbeddedDocument):
    facet_name = StringField(max_length=255, required=False)
    pick_rate = FloatField(required=False)
    win_rate = FloatField(required=False)


    def to_dict(self):
        return {
            'facet_name': self.facet_name,
            'pick_rate': self.pick_rate,
            'win_rate': self.win_rate
        }

class LanePresence(EmbeddedDocument):
    lane = StringField(max_length=255, required=False)
    presence_rate = FloatField(required=False)
    win_rate = FloatField(required=False)

    def to_dict(self):
        return {
            'lane': self.lane,
            'presence_rate': self.presence_rate,
            'win_rate': self.win_rate

        }

class Item(EmbeddedDocument):
    item_name = StringField(max_length=255, required=False)
    win_rate = FloatField(required=False)

    def to_dict(self):
        return {
            'item_name':self.item_name,
            'win_rate': self.win_rate
        }

class GoodMatchups(EmbeddedDocument):
    counters = StringField(max_length=255, required=False)
    win_rate = FloatField(required=False)

    def to_dict(self):
        return {
            'counters': self.counters,
            'win_rate': self.win_rate
        }

class BadMatchups(EmbeddedDocument):
    countered = StringField(max_length=255 , required=False)
    win_rate = FloatField(required=False)

    def to_dict(self):
        return {
            'countered': self.countered,
            'win_rate': self.win_rate
        }

class Hero(Document):
    name = StringField(max_length=255, required=True)
    hero_id = StringField(max_length=255, required=True, unique=True)
    success_rate= FloatField(required=True)
    pick_rate = FloatField(required=True)
    ban_rate = FloatField(required=True)
    attribute = StringField(max_length=255, required=False)
    GPM= FloatField(required=True)
    XPM= FloatField(required=True)
    KDA= FloatField(required=True)

    facets = EmbeddedDocumentListField(Facet, required=False)
    laning = EmbeddedDocumentListField(LanePresence, required=False)
    items = EmbeddedDocumentListField(Item, required=False)
    good_matchup = EmbeddedDocumentListField(GoodMatchups, required=False)
    bad_matchup = EmbeddedDocumentListField(BadMatchups, required=False)



