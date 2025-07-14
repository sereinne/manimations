from manim import *
from manim.utils.color.XKCD import LIGHTGREEN


class YoutubeIntro(Scene):
    def construct(self):
        code_font = "JetBrainsMono Nerd Font"
        caret = Text("$", weight=BOLD, font=code_font, height=0.75).set_color(GREEN)

        mauve = ManimColor("#D9AAF7")
        name = "Authendo"

        authendo = Text(name, font=code_font).set_color(mauve)
        cursor = Rectangle(
            height=0.75,
            width=0.25,
        ).set_color(GREEN)
        caret.next_to(authendo, LEFT)
        self.add(caret)
        self.play(TypeWithCursor(authendo, cursor), run_time=0.8)
        self.wait(0.35)
        self.play(UntypeWithCursor(authendo[:-1], cursor), run_time=0.35)
        self.wait(0.2)

    pass
