from pathlib import Path

from openai import OpenAI

openai = OpenAI()

def main() -> None:
    response = openai.images.generate(
        model="dall-e-3",
        prompt="a black beautiful cat.",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    print(image_url)


if __name__ == "__main__":
    main()
