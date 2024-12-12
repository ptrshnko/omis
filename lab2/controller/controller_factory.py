from controller.auth_controller import AuthController
from controller.user_controller import UserController
from controller.excursion_controller import ExcursionController
from controller.travel_controller import TravelController
from controller.mark_controller import MarkController
from controller.slide_controller import SlideController

class ControllerFactory:
    def instantiate_controllers(self, app):
        return [
            AuthController(app),
            UserController(app),
            ExcursionController(app),
            TravelController(app),
            MarkController(app),
            SlideController(app),
        ]
