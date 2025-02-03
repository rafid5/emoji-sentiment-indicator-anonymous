import requests
import emoji
from bs4 import BeautifulSoup
import re
import pandas as pd
import nltk
nltk.downloader.download('vader_lexicon')

def get_emoji_info(emoji_icon):
    #Extract emoji information using emoji_icon from https://emojipedia.org
    emoji_name = ((emoji.demojize(emoji_icon)).replace(":","")).replace('_','-').lower()
    #Creating url for emojipedia by appending emoji_name
    base_url = f"https://emojipedia.org/{emoji_name}/"
    try:
        response = requests.get(base_url)
    except:
        print(f"An error occurred: {e}")
        return None
    #Flag emoji's have different form of url
    if(response.status_code != 200):
        try:
            emoji_name  = "flag-"+emoji_name
            base_url = f"https://emojipedia.org/{emoji_name}/"
            response = requests.get(base_url)
        except requests.exceptions.RequestException as e:
            return None
            pass
    try:
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract description
        description_element = soup.find('div', class_='HtmlContent_html-content-container___hgg7').get_text(strip=True)
        # Extract emoji description
        description = soup.find('meta', {'name': 'description'})['content']
        # Find the title element (h3 tag)
        title_element = soup.find('h3').get_text(strip=True)
        # Extract emoji image URL
        image_element = soup.find('img', {'loading': 'lazy'})
        image_url = image_element['src'] if image_element else None
        return {
            'name': emoji_name,
            'title':title_element,
            'description': description_element,
            'image_url': image_url
        }
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_emoji_description(text):
    text_without_emojis = re.sub(r'[^\x00-\x7F]+', '', text)
    emojis = emoji.emoji_list(text)
    emoji_icons = [item['emoji'] for item in emojis]
    emoji_dictionary = {}
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
        else:
            emoji_info = get_emoji_info(emoji_icon)
            if (emoji_info is None):
                return ""
            # save emoji_info result
            emoji_dictionary[emoji_icon]  = emoji_info
    title = ""
    description = ""
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
            if (emoji_info['title'] is None):
                return ""
            title = title + ". "+ emoji_info['title']
            return title

def get_emoji_description(text):
    text_without_emojis = re.sub(r'[^\x00-\x7F]+', '', text)
    emojis = emoji.emoji_list(text)
    emoji_icons = [item['emoji'] for item in emojis]
    emoji_dictionary = {}
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
        else:
            emoji_info = get_emoji_info(emoji_icon)
            if (emoji_info is None):
                return ""
            # save emoji_info result
            emoji_dictionary[emoji_icon]  = emoji_info
    title = ""
    description = ""
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
            if (emoji_info['title'] is None):
                return ""
            title = title + ". "+ emoji_info['title']
            return title

def get_emoji_title(text):
    text_without_emojis = re.sub(r'[^\x00-\x7F]+', '', text)
    emojis = emoji.emoji_list(text)
    emoji_icons = [item['emoji'] for item in emojis]
    emoji_dictionary = {}
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
        else:
            emoji_info = get_emoji_info(emoji_icon)
            if (emoji_info is None):
                return ""
            # save emoji_info result
            emoji_dictionary[emoji_icon]  = emoji_info
    title = ""
    description = ""
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
            if (emoji_info['description'] is None):
                return ""
            title = title + ". "+ emoji_info['description']
            return title

def get_emoji_image_url(text):
    text_without_emojis = re.sub(r'[^\x00-\x7F]+', '', text)
    emojis = emoji.emoji_list(text)
    emoji_icons = [item['emoji'] for item in emojis]
    emoji_dictionary = {}
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
        else:
            emoji_info = get_emoji_info(emoji_icon)
            if (emoji_info is None):
                return ""
            # save emoji_info result
            emoji_dictionary[emoji_icon]  = emoji_info
    title = ""
    description = ""
    for emoji_icon in emoji_icons:
        if emoji_icon in emoji_dictionary:
            emoji_info = emoji_dictionary[emoji_icon]
            if (emoji_info['image_url'] is None):
                return ""
            title = title + ". "+ emoji_info['image_url']
            return title
