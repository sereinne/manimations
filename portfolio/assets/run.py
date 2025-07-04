import os


def main():
    path_youtube: str = "output/videos/main/1080p30/YouTubeIntro.mp4"
    path_outro: str = "output/videos/main/1080p30/Outro.mp4"
    # path_exp: str = "output/videos/main/1080p30/Experiment.mp4"
    # path_exp: str = "output/videos/main/1080p30/Foo.mp4"
    # path_exp: str = "output/videos/main/1080p30/Outro.mp4"
    path_exp: str = "output/videos/main/1080p30/MeatAndPotatoes.mp4"
    os.system(f"manim main.py && vlc --play-and-exit {path_exp}")


if __name__ == "__main__":
    main()
