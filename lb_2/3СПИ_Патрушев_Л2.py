class The_Projector: # Класс проектор
    def projector_on(self): # Метод что бы включить проектор
        print("Проектор включен.")


class Sound_System: # Класс звкуковая система
    def sound_system_on(self): # Метод что бы включить звуковую систему
        print("Звуковая система включена.")


class DVD: # Класс DVD
    def dvd_on(self): # Метод что бы включить DVD
        print("Видео система включена.")


class HomeTheaterFacade: # Это сам фасад
    def __init__(self):
        self._the_projector = The_Projector()
        self._sound_system_on = Sound_System()
        self._dvd_on = DVD()

    def onTheProjector(self):
        self._the_projector.projector_on()

    def onSoundSystem(self):
        self._sound_system_on.sound_system_on()

    def onDVD(self):
        self._dvd_on.dvd_on()

if __name__ == '__main__':

    facade = HomeTheaterFacade()
    facade.onDVD()
    facade.onSoundSystem()
    facade.onTheProjector()
