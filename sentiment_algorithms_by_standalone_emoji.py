import pandas as pd
import random

def method_first(list_emoji, dict_sent):
    '''
    list_emoji: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    '''
    #Checking whether we have ground truth or not given emojis
    if not list_emoji[0] in dict_sent:
        return 0
    sentiment = dict_sent[list_emoji[0]]
    return sentiment

def method_last(list_emoji, dict_sent):
    '''
    list_emoji: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    '''
    #Checking whether we have ground truth or not given emojis
    if not list_emoji[-1] in dict_sent:
        return 0
    sentiment = dict_sent[list_emoji[-1]]
    return sentiment

def method_consecutive(list_emoji, dict_sent):
    """
    list_emoji: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    """
    sentiment = 0
    count = 1  # Track consecutive occurrences
    for i in range(0, len(list_emoji)):
        if ((i<len(list_emoji)-1) and (list_emoji[i] == list_emoji[i + 1]) and (list_emoji[i] in dict_sent)):
            # Increment count for consecutive matches
            count += 1
        else:
            # Add sentiment for the previous sequence if it exists in dict_sent
            if count > 1 and list_emoji[i] in dict_sent:
                sentiment += dict_sent[list_emoji[i]] * count
            # Reset count for the new sequence
            count = 1
    return sentiment

def method_repeated(list_emoji, dict_sent):
    '''
    list_emoji: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    '''
    sentiment = 0
    emojis_set = set()
    emojis_repeated_set = set()
    for i in range(len(list_emoji)):
        if list_emoji[i] in emojis_set and list_emoji[i] in dict_sent:
            sentiment += dict_sent[list_emoji[i]]
            emojis_repeated_set.add(list_emoji[i])
        else:
            emojis_set.add(list_emoji[i])
    #Adding weight for the first occurence of repeated emojis
    for emoji in set(emojis_repeated_set):
        sentiment += dict_sent[emoji]
    return sentiment

def method_all(list_emoji, dict_sent):
    '''
    list_emoji: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    '''
    return method_first(list_emoji,dict_sent)+method_consecutive(list_emoji,dict_sent)+method_repeated(list_emoji,dict_sent)+method_last(list_emoji,dict_sent)

def method_BSA(emojis, dict_sent):
    '''
    emojis: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    '''
    emojis_senti_sum = 0
    for i in range(len(emojis)):
        if emojis[i] in dict_sent:
            emojis_senti_sum += dict_sent[emojis[i]]
    return emojis_senti_sum

def method_DPM(emojis, dict_sent):
    '''
    emojis: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    '''
    emojis_senti_sum = 0
    #Update sentiment values
    dpm_dict_sent = {key: (2 if value == 1 else 1 if value == 0 else -2) for key, value in emoji_senti_dict.items()}
    for i in range(len(emojis)):
        if emojis[i] in dpm_dict_sent:
            emojis_senti_sum += dpm_dict_sent[emojis[i]]
    return emojis_senti_sum

def method_Majority_Voting(emojis, dict_sent):
    '''
    emojis: the list of emojis
    dict_sent: dictionary with key of emoji, value of "+1, 0, or -1"
    '''
    sentiment_counts = {1: 0, -1: 0, 0: 0}
    #Count positive, negative, neutral emojis
    for emoji in emojis:
        if emoji in dict_sent:
            sentiment_counts[dict_sent[emoji]] += 1
    positive, negative, neutral = sentiment_counts[1], sentiment_counts[-1], sentiment_counts[0]
    if positive > max(negative, neutral):
        return 1
    elif negative > max(positive, neutral):
        return -1
    elif neutral > max(positive, negative):
        return 0
    # Handle tie cases
    tie_cases = [
        (positive == negative == neutral, [1, 0, -1]),
        (positive == negative > neutral, [1, -1]),
        (negative == neutral > positive, [-1, 0]),
        (positive == neutral > negative, [1, 0]),
    ]
    for condition, choices in tie_cases:
        if condition:
            return random.choice(choices)