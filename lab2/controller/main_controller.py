from controller.controller_factory import ControllerFactory

class MainController:
    def __init__(self, app):
        self.app = app
        self.factory = ControllerFactory()
        self.controllers = []

    def control(self):
        # Создаем экземпляры всех контроллеров через фабрику
        self.controllers = self.factory.instantiate_controllers(self.app)

        # Запускаем контроль каждого контроллера
        for controller in self.controllers:
            controller.control()

        # Показываем стартовое окно
        self.app.show_window("start_screen")
