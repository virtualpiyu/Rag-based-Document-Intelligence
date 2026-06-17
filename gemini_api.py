# # import os
# # from google import genai

# # # The client automatically picks up the API key from the environment variable
# # client = genai.Client(api_key=os.getenv("AIzaSyCskzYyYV60P_H23R3u6zMVcxPTvL5DZ4w"))

# # # Example of generating content
# # response = client.models.generate_content(
# #     model="gemini-2.5-flash",
# #     contents="Explain how AI works in a few words"
# # )

# # print(response.text)


import os

print(os.getenv("GEMINI_API_KEY"))  

