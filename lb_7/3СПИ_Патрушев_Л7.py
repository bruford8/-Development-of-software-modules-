class TextPrinter:
    def __init__(self, text: str):
        self.text = text

    def render(self) -> str:
        return self.text


class TextDecorator(TextPrinter):
    def __init__(self, component: TextPrinter):
        self.component = component

    def render(self) -> str:
        return self.component.render()


class UpperCaseDecorator(TextDecorator):
    def render(self) -> str:
        return self.component.render().upper()


class BorderDecorator(TextDecorator):
    def render(self) -> str:
        text = self.component.render()
        border = "*" * (len(text) + 4)
        return f"{border}\n* {text} *\n{border}"


class ExclamationDecorator(TextDecorator):
    def render(self) -> str:
        return self.component.render()


if __name__ == "__main__":
    text = TextPrinter("Привет, мир")

    decorated = ExclamationDecorator(
        BorderDecorator(
            UpperCaseDecorator(text)
        )
    )

    print(decorated.render())
