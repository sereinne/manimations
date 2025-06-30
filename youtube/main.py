from manim import *


class WipeEffect(Scene):
    def construct(self):
        text = Text("Hello, World!")
        line = Line(text.get_corner(RIGHT), text.get_corner(LEFT))
        line.next_to(text, DOWN)
        self.play(Write(text), Write(line))
        self.wait(2)

    pass


class Outro(Scene):
    def construct(self):
        path_manim = "assets/manim.svg"
        path_py = "assets/python.svg"

        manim_label = Text("Made by using")
        manim_logo = SVGMobject(path_manim)
        manim_label.next_to(manim_logo, UP)
        manim_group = VGroup(manim_label, manim_logo)

        python_label = Text("Powered by")
        python_logo = SVGMobject(path_py)
        python_label.next_to(python_logo, UP)
        python_group = VGroup(python_label, python_logo)

        svgs = VGroup(manim_group, python_group)
        svgs.arrange(RIGHT, buff=2.5)
        # svgs = VGroup(manim_logo, manim_label, python_logo, python_label)
        # svgs.arrange(RIGHT, buff=3)

        self.play(*[Write(item) for item in svgs], run_time=1.25)
        self.play(Transform(svgs, Dot()))
        self.play(FadeOut(svgs))


class YouTubeIntro(Scene):
    def construct(self):
        red = ManimColor("#e07a5f")
        green = ManimColor("#87c2a5")
        lightblue = ManimColor("#8ad0fa")
        its_blue = ManimColor("#322d7d")
        its_yellow = ManimColor("#fff500")

        greet = Text("Hi,", font_size=144)

        intro_text = "I'm Muhammad Akbar Ilman Setijadi!"
        intro = Text(
            intro_text,
            t2c={
                intro_text[0:3]: red.to_hex(),
                intro_text[4:12]: green.to_hex(),
                intro_text[13:]: red.to_hex(),
            },
        )

        greet.next_to(intro, UP)
        greet.shift(LEFT * 4.75)

        line = Line(intro.get_corner(LEFT), intro.get_corner(RIGHT))
        line.next_to(intro, DOWN)

        self.play(DrawBorderThenFill(greet), Write(intro))
        self.play(Write(line), run_time=0.75)
        self.play(
            FadeOut(intro, greet),
            line.animate.shift(
                (UP * greet.get_corner(UP)) + (UP * intro.get_corner(UP)) + (UP * 0.5)
            ),
        )

        dot = Dot(line.get_center())
        self.play(Transform(line, dot), run_time=0.5)
        self.play(ShrinkToCenter(line))

        dot_uni = Dot()
        dot_uni.set_color_by_gradient(its_blue.to_hex(), its_yellow.to_hex())

        dot_uni_info = dot_uni.copy()
        dot_uni.shift(RIGHT * 2.5)
        dot_uni_info.shift(LEFT * 2.5)

        self.play(GrowFromCenter(dot_uni), GrowFromCenter(dot_uni_info))

        info = Text("Inforamtion Systems", font_size=24)
        info.move_to(dot_uni_info)
        info.set_color_by_gradient(its_blue.to_hex(), its_yellow.to_hex())
        its = SVGMobject("assets/images.svg")
        its.set_color(its_blue.to_hex())
        its.move_to(dot_uni)

        self.play(Transform(dot_uni, its), Transform(dot_uni_info, info))

        self.wait(1)
