## Contributing to the bot :rocket:
All contributions are welcome! :hugs:

**NOTE:** This document is made while keeping all types of contributors in mind. You may skip to [Setup instructions](#setup-instructions)
if you're familiar with Git and GitHub.

### Installing and setting up git :nerd_face:
- **Follow this guide:** https://docs.github.com/en/github/getting-started-with-github/set-up-git#setting-up-git

### Installing python :snake:
- **For Linux:** Python comes pre-installed on most linux distributions. If its not on yours, then you'll have to use your package manager to install it.
- **For Windows:** Install it from here: https://www.python.org/downloads/windows/

### Forking and cloning this repo
- While signed in to github, click the `Fork` button at the top right corner of the page.

  When you fork a repo, a new copy of your own of that repo is created. You'll use this copy to make your changes.

- After forking the repo, clone your fork to your local machine by:
  ```bash
  git clone https://github.com/YOUR_USERNAME/bot
  ```

Well done! Now you have the code on your local system! :v:

### Setup Instructions

###### Get a bot from BotFather to test your changes locally  :robot:
1. Ping [BotFather](https://t.me/botfather) on Telegram
2. Send `/start`
3. Send `/newbot` to create a new bot
4. You'll be prompted for a name and username for your bot, send them
* You'll get a bot API token similar to: `xxxxxxxxxx:xxx-xxxx_TE9i5t9Fm4Pf9lyopLvw7Gk4ag`

###### Installing python dependencies: :trollface:
1. Install pip using your system's package manager:
  - Example for ubuntu: 
    `sudo apt install python3-pip`
  
  - Verify the installation by: 
    `pip3 --version`
  
2. Clone this repository and install python dependencies using: 
`pip3 install -r requirements.txt`

3. Set two environment variables from your terminal namely, 
   ```bash
   export bot_name="<your bot's name that you presented to botfather>"
   export token="<token presented by botfather>"
   ```
   
4. Make a file `data_file.json` and write `{}` in it
5. Run the bot with:
`python3 bot.py`

6. Add the bot to a group and test if its working. If it works, then you're good to go. If it does not then try repeating the steps or googling your problem.
7. If you're still unable to get it working after step 6, ask for help on JODC's telegram channel.

### Making pull requests :cake:
1. `cd` into the cloned project directory on your local machine and create a new branch by
    ```bash
    git checkout -b "Branch-Name"
    ```
  
2. Make changes according to the issue.
3. Test the changes and if applicable take a screenshot of the chat.
4. After you're satisfied with the changes that you've done, add the changes with `git add`
  ```bash
  git add .
  ```
  
5. Commit the changes using `git commit`
  ```bash
  git commit -m "A short message which briefly describes the changes you made"
  ```
  
6. Push the changes to your fork on GitHub using `git push`
  ```bash
  git push -u origin "Branch-Name from step 1"
  ```
  
7. Open your forked repo on GitHub and click the **Pull request** button to create a pull request. Describe a little about your changes and attach the 
screenshot you took here :sparkles:

See [this](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) for help with pull requests.

TODO: Add PR templates 

### Making Issues :hand:
Feel free to open an issue for
- reporting a bug
- proposing a new feature
- proposing an enhancement in current feature
- proposing improvment in docs
- anything you think is missing

How to open an issue
1. Open the bot repo on github: https://github.com/JIITODC/bot
2. Click on the issues tab 
3. Click on the green colored **New Issue** button.
4. Describe the issue so that it is easy for someone to understand it.
See [this](https://docs.github.com/en/free-pro-team@latest/github/managing-your-work-on-github/creating-an-issue) for help with creating issues.

TODO: Add Issue templates
