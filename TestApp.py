from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.uix.button import Button
from kivy.core.window import Window


class PaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            r = 10
            Color(1, 0, 0)
            Ellipse(pos = (touch.x - r/2, touch.y - r/2), size = (r, r))
            touch.ud['line'] = Line(points = (touch.x, touch.y), width = r/2)

    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x, touch.y)


class TestApp(App):
    def build(self):
        parent = Widget()
        self.painter = PaintWidget()
        parent.add_widget(self.painter)

        parent.add_widget(Button(text = 'CLEAR', on_press = self.clear_canvas, size = (100, 50)))
        parent.add_widget(Button(text = 'SAVE', on_press = self.save_canvas, size = (100, 50), pos = (100, 0)))

        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save_canvas(self, instance):
        self.painter.size = (Window.size[0], Window.size[1])
        self.painter.export_to_png('img.png')


if __name__ == "__main__":
    TestApp().run()
