# Client와 Application System과의 관계
# Client은 Application의 Sub System을 몰라도, 정해진 interface만을 이용해 구현 가능. 
# --> 복잡한 Sub System 은 알필요가 없다. Client 입장에서. 


class Hotelier:
    def bookHotel(self):
        print("Succesfully booked Hotel.!!")


class Florist:
    def setFlowerRequirements(self):
        print("Roses are used for Decorations!!")


class Caterer:
    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served")


class Musician:
    def setMusicType(self):
        print("Jazz and Classical will be played")


class EventManager:
    def __init__(self) -> None:
        print("Marriage Event Manager::")
    
    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()
        
        self.florist = Florist()
        self.florist.setFlowerRequirements()
        
        self.caterer = Caterer()
        self.caterer.setCuisine()
        
        self.musician = Musician()
        self.musician.setMusicType()


class Client:
    def __init__(self) -> None:
        print("Arrived!. ready to aranger")
    
    def askEventManager(self):
        em = EventManager()
        em.arrange()


you = Client()
you.askEventManager()