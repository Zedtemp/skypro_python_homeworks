class Mailing:
  
    def __init__(self, track, from_address, to_address, cost):
        self.toAd = to_address
        self.fromAd = from_address
        self.cost = (cost)
        self.track = (track)


    def __str__(self):
        return (f"Отправление {self.track} из {self.fromAd} "
                f"в {self.toAd} стоимостью {self.cost} рублей")