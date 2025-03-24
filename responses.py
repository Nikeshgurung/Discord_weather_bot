from random import choice, randint




def get_response(user_input: str) -> str:
    lowered:str= user_input.lower()

    if lowered=='':
        return 'well you\'re awfully silent..'
    elif 'hello'in lowered:
        return 'Hello there!'
    elif 'who are you' in lowered:
        return 'I am Ramesh. What is your name?'
    elif 'i am nikesh' in lowered:
        return 'Okay! Nice to meet you, Nikesh.'
    elif 'how are you' in lowered:
        return'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'thankyou' in lowered:
        return 'welcome!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    else:
        return choice(['I do not understand... ',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])

    # raise NotImplementedError('Code is missing...')