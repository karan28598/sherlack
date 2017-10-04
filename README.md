# sherlack
--------------
Sherlock Holmes, now in slack to solve all your mysteries! :sunglasses:
![img](https://github.com/karan28598/sherlack/raw/master/sherlock.gif)



## Usage

Just enter `/sherlack [your question]` in a slack channel. The Question will be shown on the same channel visible to you.


## Integrate it with your team

**As the Wolframalpha API allows only 2000 API calls in a month. This can not be used directly. **


1. Go to your channel
2. Click on **Configure Integrations**.
3. Scroll all the way down to **DIY Integrations & Customizations section**.
4. Click on **Add** next to **Slash Commands**.
   - Command: `/sherlack`
   - URL: `https://sherlack.herokuapp.com/sherlack`
   - method: `POST`
   - For the **Autocomplete help text**, check to show the command in autocomplete list.
    - Description: `Sherlock, now in slack to solve all your mysteries`
    - Usage Hint: `/sherlack  "search query"`
  - Descriptiive Level: `Search Query`



## Developing

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

You will need to set the `wol_id` environment variable in `config.py` file in your heroku app in order for this to work. You can read more about it [clicking here](https://devcenter.heroku.com/articles/config-vars#setting-up-config-vars-for-a-deployed-application)





## LICENSE

[MIT LICENSE](https://github.com/karan28598/sherlack/blob/master/LICENSE) (c) Karan Agrawal
