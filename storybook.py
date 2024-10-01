from openai import OpenAI
import streamlit as st
import os

client = OpenAI(api_key = 
os.environ['OPENAI_API_KEY'])

#Story

def story_gen(prompt) : 
  system_prompt = """
  You're a world renowned 50 years experience storyteller. 
  You will be given a concept to generate a healing story     suitable for anxiety person. make sure the story have perfect ending within the tokens.
  """

  prompt = "Depression of abu"

  response = client.chat.completions.create(
      model = 'gpt-4o-mini', 
      messages = [
          {"role" : "system",
           "content" : system_prompt},
          {"role" : "user",
           "content" : prompt}
      ],
      temperature = 1.3, #increase creativity 
      max_tokens = 100

  )

  return response.choices[0].message.content

#Cover 

def cover_gen(prompt) : 
  system_prompt = """
  You're a world renowned 50 years experience storyteller. 
  You will be given a concept to generate a healing story suitable for anxiety person. make sure the story have perfect ending within the tokens.
  """

  prompt = "Depression of abu"

  response = client.chat.completions.create(
      model = 'gpt-4o-mini', 
      messages = [
          {"role" : "system",
           "content" : system_prompt},
          {"role" : "user",
           "content" : prompt}
      ],
      temperature = 1.3, #increase creativity 
      max_tokens = 100

  )

  return response.choices[0].message.content

#Cover art

def image_gen(prompt) : 
  response = client.images.generate(
      model = 'dall-e-2',
      prompt = prompt,
      size = '256x256',
      n = 1
  )

  return response.data[0].url


#Storybook method

def storybook(prompt) :
  story = story_gen(prompt)
  cover = cover_gen(story)
  image = image_gen(cover)

  st.write(image)
  st.write(story)

st.title("Storybook Generator for Kids for fun")
st.divider()

prompt = st.text_area("Enter your story concept:")

if st.button("Generate Storybook"):
  with st.spinner("Please wait..."):
    story = story_gen(prompt)
    cover = cover_gen(story)
    image = image_gen(cover)
    st.balloons()
    st.image(image)
    st.write(story)

