class ConditionalException(Exception):
    def __init__(self, value="ConditionalException"):
        self.value = value


class InputException(Exception):
    def __init__(self, value, class_name, function_name):
        self.value = value
        self.place = f"{class_name}.{function_name}"

    def __str__(self):
        """Отображение исключения"""
        return f"В функции {self.place} возникла ошибка: \"{self.value}\"\n_____________________"
