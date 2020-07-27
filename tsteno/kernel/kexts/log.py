import datetime
from enum import Enum
from colorama import Fore
from .kext_base import KextBase


class LogLevel(Enum):
    CRITICAL = 0
    ERROR = 1
    WARNING = 2
    NORMAL = 3
    MESSAGE = 4
    DEBUG = 5


class Log(KextBase):
    __slots__ = ['log_level', 'log_handlers']

    def __init__(self, kernel):
        super().__init__(kernel)

        self.log_level = kernel.get_option_value(
            'kext_extensions', 'log', 'log_level'
        )
        self.log_handlers = []

        self.register_log_handler(self.__default_log_handler)

    def register_log_handler(self, handler):
        self.log_handlers.append(handler)

    def write(self, msg, level=LogLevel.NORMAL):
        if level.value > self.log_level.value:
            return

        format_message = '[{}] [{}]: {}'.format(
            self.get_kernel().get_kid(),
            datetime.datetime.now().isoformat(),
            msg
        )

        for handler in self.log_handlers:
            handler(format_message, level)

    def __default_log_handler(self, msg, level):
        status = ''
        color = Fore.RESET

        if level == LogLevel.ERROR:
            status = 'ERROR'
            color = Fore.RED
        elif level == LogLevel.NORMAL:
            status = 'INFO'
        elif level == LogLevel.DEBUG:
            status = 'DEBUG'
            color = Fore.BLUE

        msg = '{}[{}] {} {}'.format(color, status, msg, Fore.RESET)

        print(msg)
