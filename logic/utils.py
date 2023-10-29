import openai
import ast

openai.api_key = "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"

def get_oai_completion(messages, temperature=0.1, model="gpt-4"):

    #streaming by default
    response = openai.ChatCompletion.create(
        model = model,
        messages=messages,
        stream=True,
        temperature=0
    )

    collected_events = []
    completion_text = ''
    old_length = 0
    # iterate through the stream of events
    for event in response:

        collected_events.append(event)
        delta = event['choices'][0]['delta']

        if 'content' in delta:
            completion_text += delta["content"]
            # only print the new content
            print(completion_text[old_length:], end='', flush=True) 
            old_length = len(completion_text)

    return completion_text