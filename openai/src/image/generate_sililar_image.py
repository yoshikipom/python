from openai import OpenAI
client = OpenAI()

response = client.images.create_variation(
    image=open("./test_data/cat.png", "rb"),
    n=2,
    size="256x256"
)

image_url = response.data[0].url
print(image_url)

for data in response.data:
    print(data.url)
