from manim import *

# manim compiles each scene sequentially

mutebrown = ManimColor("#524632")


class Intro(Scene):
    def construct(self):
        font = "JetBrainsMono Nerd Font"
        # terminal like caret symbol
        caret = Text(">", font=font)
        caret.set_color(mutebrown)

        # text to type
        introduction = Text("Hi! I'm Muhammad Akbar Ilman Setijadi", font=font).scale(
            0.75
        )
        introduction.set_color(mutebrown)
        caret.next_to(introduction, LEFT)

        # cursor shape
        cursor = Rectangle(
            color=mutebrown,
            height=0.75,
            width=0.25,
        )

        # promo text
        # promo = Text("Follow me on", weight=BOLD).scale(0.35)
        # promo.set_color(mutebrown)
        # promo.to_corner(DOWN)
        # icons
        # github = SVGMobject("./assets/github_icon.svg").scale(0.15)
        # instagram = SVGMobject("./assets/instagram.svg").scale(0.15)
        # linkedin = SVGMobject("./assets/linkedin.svg").scale(0.15)
        # svg_group = VGroup(github, instagram, linkedin)
        # svg_group.arrange(RIGHT, 0.25)
        # svg_group.next_to(promo, DOWN * 0.75)
        # self.add(svg_group)

        self.add(caret)

        self.play(TypeWithCursor(introduction, cursor), Blink(cursor, blinks=4))
        self.play(UntypeWithCursor(introduction[:-1], cursor), run_time=0.85)
        self.play(Blink(cursor))

        clear = Text("clear", font=font).scale(0.75)
        clear.set_color(mutebrown)
        clear.next_to(caret, RIGHT)

        self.play(TypeWithCursor(clear, cursor), Blink(cursor, blinks=2))
        self.play(FadeOut(caret, clear, cursor), run_time=0.01)


class Outro(Scene):
    def construct(self):
        info_manim = Text("Manim").scale(0.25).set_color(mutebrown)
        manim_label = Text("Powered by").set_color(mutebrown)
        manim_icon = SVGMobject("./assets/manim.svg").scale(0.75)

        info_python = Text("Python").scale(0.25).set_color(mutebrown)
        python_label = Text("Made with").set_color(mutebrown)
        python_icon = SVGMobject("./assets/python.svg").scale(0.75)

        manim_subgroup = VGroup(manim_label, manim_icon, info_manim)
        manim_subgroup.arrange(DOWN, buff=0.5)

        python_subgroup = VGroup(python_label, python_icon, info_python)
        python_subgroup.arrange(DOWN, buff=0.5)

        group = VGroup(python_subgroup, manim_subgroup)
        group.arrange(RIGHT, buff=0.75)

        self.play(
            Write(manim_label),
            Write(python_label),
            GrowFromPoint(manim_icon, manim_icon.get_center()),
            Write(info_manim),
            GrowFromPoint(python_icon, python_icon.get_center()),
            Write(info_python),
            run_time=1.5,
        )
        self.wait(0.5)

        self.play(Unwrite(manim_subgroup), Unwrite(python_subgroup))
        self.wait(0.75)
