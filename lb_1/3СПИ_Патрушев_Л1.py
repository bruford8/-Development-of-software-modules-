class SettingsManager:
    _instance = None # Тут хранится экземпляр класса, это переменная такая

    def __new__(cls):
        if cls._instance is None: # Тут идет проверка занято ли место в переменной
            cls._instance = super(SettingsManager, cls).__new__(cls)
            cls._instance._theme = "Black" # Это настройки приложения
            cls._instance._ui_language = "Russian"
            cls._instance._config_path = "path/to/config"
        return cls._instance

    @property # Это декоратор который превращает метод класса в атрибут, доступный только для чтения
    def theme(self):
        return self._theme # Возвращает тему приложения

    @theme.setter # Метод вызываемый при попытке установить значение
    def theme(self, value):
        self._theme = value # Устанавливает тему приложения

    @property
    def language(self):
        return self._ui_language # Возвращает язык приложения

    @language.setter # Метод вызываемый при попытке установить значение
    def ui_language(self, value):
        self._ui_language = value # Устанавливает язык приложения

    @property
    def config_path(self):
        return self._config_path # Возвращает путь к конфигу

    @config_path.setter # Метод вызываемый при попытке установить значение
    def config_path(self, value):
        self._config_path = value # Устанавливает путь конфига

    def __str__(self): # Возвращает атрибуты в строковом варианте
        return f"SettingsManager(theme='{self.theme}', language='{self.language}', config_path='{self.config_path}')"

if __name__ == "__main__":

    # Создаем первый экземпляр
    settings1 = SettingsManager()
    print("Первый экземпляр:", settings1)

    # Изменяем настройки через первый экземпляр
    settings1.theme = "dark"
    settings1.ui_language = "ru"
    settings1.config_path = "config/custom.ini"

    print("После изменений через первый экземпляр:", settings1)

    # Создаем второй экземпляр
    settings2 = SettingsManager()
    print("Второй экземпляр:", settings2)

    # Проверяем, что это тот же объект
    print("settings1 is settings2:", settings1 is settings2)

    # Изменяем настройки через второй экземпляр
    settings2.theme = "blue"
    settings2.ui_language = "fr"

    print("После изменений через второй экземпляр:")
    print("Первый экземпляр:", settings1)
    print("Второй экземпляр:", settings2)

    # Проверяем, что изменения видны в обоих "экземплярах"
    print("Темы совпадают:", settings1.theme == settings2.theme)
    print("Языки совпадают:", settings1.language == settings2.language)
    print("Пути конфигурации совпадают:", settings1.config_path == settings2.config_path)