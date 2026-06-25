from dotenv import load_dotenv
import os

load_dotenv()

name = os.getenv("MY_NAME")
language = os.getenv("FAVORITE_LANGUAGE")
course= os.getenv("Course")

print(f"Name: {name}")
print(f"Favorite language: {language}")
print(f"The course is : {course}")