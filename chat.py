import openai

openai.api_key = 'ask_from_opeani_they_will_give_you '


def get_api_response(prompt: str) -> str or  None:
    text: str or  None = None

    try:
        response: dict = openai.Completion.create(
    model='text-davinci-003 ',    # response created by openai model as name  mentioned in single quotes
    prompt=prompt,  # prompt got in parameter of this function
    temperature=0.9,  # higher the temperature the more random my bot is going to be
    max_tokens=150, # minimum length of response
    top_p=1, #alternative value to the temperature
    frequency_penalty=0, # repetition of response lines 
    presence_penalty=0.6, # how an AI can talk about new subjects low penalty AI repeats itself so it good to have more
    stop=[' Humans:',' AI:'] # once it got into this words it stop generating reponse

           
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text') 

    except Exception as e:
        print('ERROR:', e)

    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)  # this function is used to add all the measage in the list the user and bot creates
                           # such that hsitory is maintained


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nAI: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    prompt_list: list[str] = ['You are a potato and will answer as a potato',
                              '\nHuman: What time is it?',
                              '\nAI: I have no idea, I\'m a potato!']

    while True:
        user_input: str = input('Nirbhay type ')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'assitant : {response}')


if __name__ == '__main__':

    main()