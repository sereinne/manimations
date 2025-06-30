import os


def main():
    path_youtube: str = "media/videos/main/1080p30/YouTubeIntro.mp4"
    path_outro: str = "media/videos/main/1080p30/Outro.mp4"
    path_wipe: str = "media/videos/main/1080p30/WipeEffect.mp4"
    os.system(f"manim main.py && vlc.exe --quiet --play-and-exit {path_wipe}")


if __name__ == "__main__":
    main()
