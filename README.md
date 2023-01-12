# GPT-3 Discord Bot

This is a Discord bot script that utilizes GPT-3 from OpenAI. It can understand and respond to a wide range of prompts and questions, making it a valuable addition to any Discord community.

## Getting Started

These instructions will help you set up and run the bot on your local machine.

### Prerequisites

- You will need to have a Discord bot set up. If you don't have one already, you can create one by following the instructions [here](https://discordpy.readthedocs.io/en/latest/discord.html). Make sure to copy the bot token, you will need it later.

- Create a role in your discord server named "gpt" and assign it to the users that you want to allow to use the bot.

- To use the GPT-3 model, you will need to have an OpenAI API key. You can sign up for one [here](https://beta.openai.com/signup/).

- You will also need to have Python and the Discord and OpenAI libraries installed.

### Installing

1. Clone or download the script from this repository.

2. Open the script in a code editor and replace the placeholder text for the Discord bot token and OpenAI API key with your actual token and key.

3. Run the script by executing `python bot.py` in your command prompt. Make sure you are in the same directory as the script.

4. Once the bot is running, you can activate it by typing the command `/chat` followed by a prompt or question in any text channel where the bot has access to.

5. The bot will respond with a relevant and coherent answer. The bot can handle a wide variety of topics, including general knowledge, current events, and even creative writing prompts.

## Troubleshooting

- Make sure that you have installed the `discord` and `openai` library by running `pip install discord openai` on your command prompt.

- This script requires a paid plan on OpenAI to use GPT-3 as the engine.

- As always, it's a good idea to thoroughly test the bot in a development or staging environment before deploying it to a production environment.

## Authors

* **OpenAI** - *GPT-3 model* - [OpenAI](https://openai.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
