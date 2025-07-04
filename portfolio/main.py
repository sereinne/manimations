from manim import *

LIGHTBLUE = ManimColor("#7daea3")
AQUA = ManimColor("#89b482")
LIGHTGREEN = ManimColor("#a9b665")
BLUE_GRADIENT = [LIGHTBLUE, AQUA, LIGHTGREEN]

RED = ManimColor("#ff5f5f")
GREEN = ManimColor("#afaf5f")
YELLOW = ManimColor("#d7af5f")
RED_GRADIENT = [YELLOW, GREEN, RED]


class Outro(Scene):
    def construct(self):
        info_manim = Text("Manim").scale(0.25).set_color(GREEN)
        manim_label = Text("Powered by")
        manim_icon = SVGMobject("./assets/manim.svg").scale(0.75)

        info_python = Text("Python").scale(0.25).set_color(GREEN)
        python_label = Text("Made with")
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

    pass


class MeatAndPotatoes(Scene):
    def construct(self):
        # promo text
        promo = Text("More details about me on").scale(0.5).set_color(RED.to_hex())
        # gh group
        gh_label = Text("Github").scale(0.25).set_color(GREEN.to_hex())
        gh_icon = SVGMobject("./assets/github_icon.svg").scale(0.5)
        # linkedin group
        linkedin_label = Text("LinkedIn").scale(0.25).set_color(GREEN.to_hex())
        linkedin_icon = SVGMobject("./assets/linkedin.svg").scale(0.5)
        # instagram group
        ig_label = Text("Instagram").scale(0.25).set_color(GREEN.to_hex())
        ig_icon = SVGMobject("./assets/instagram.svg").scale(0.5)

        # subgroups
        gh_group = VGroup(gh_icon, gh_label)
        gh_group.arrange(DOWN, buff=0.35)

        linkedin_group = VGroup(linkedin_icon, linkedin_label)
        linkedin_group.arrange(DOWN, buff=0.35)

        instagram_group = VGroup(ig_icon, ig_label)
        instagram_group.arrange(DOWN, buff=0.35)

        group = VGroup(gh_group, instagram_group, linkedin_group)
        group.arrange(RIGHT, buff=0.5)

        promo.next_to(group, (UP * 1.75))

        self.play(
            Write(promo),
            LaggedStart(
                Write(gh_label),
                GrowFromPoint(gh_icon, gh_icon.get_center()),
                Write(ig_label),
                GrowFromPoint(ig_icon, ig_icon.get_center()),
                Write(linkedin_label),
                GrowFromPoint(linkedin_icon, linkedin_icon.get_center()),
                lag_ratio=1,
            ),
            run_time=2.5,
        )

        self.wait(0.5)

        self.play(
            Unwrite(promo),
            LaggedStart(Unwrite(group), lag_ratio=0.5),
            run_time=1.85,
        )

        self.wait(0.75)

    pass


class Intro(Scene):
    def construct(self):
        pfp = SVGMobject("./assets/github_pfp.svg").scale(0.75)
        greet = Text("Hi, There!")
        name = Text("I'm Muhammad Akbar Ilman Setijadi!").scale(0.5)

        tag_pair = Group(pfp, greet, name)
        tag_pair.arrange(DOWN, buff=0.85)

        blue_gradient = color_gradient(BLUE_GRADIENT, len(name))
        name.set_color_by_gradient(blue_gradient)
        greet.set_color_by_gradient(blue_gradient)

        self.play(
            Write(pfp),
            LaggedStart(
                Write(greet),
                Write(name),
                lag_ratio=1,
            ),
            run_time=2.5,
        )

        self.wait(0.5)

        self.play(
            LaggedStart(
                Unwrite(pfp),
                Unwrite(name),
                Unwrite(greet),
                lag_ratio=1,
            ),
            run_time=1.85,
        )

        self.wait(0.75)
