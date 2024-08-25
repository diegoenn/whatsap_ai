{
    "name": "yesser md",
    "description": "I am yesser md Whatsapp MultiDevice Whatsapp Bot built in NodeJs to make experience better",
    "website": "https://telegra.ph/file/37882de26f9ffc60043ef.jpg",
    "repository": "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",
    "logo": "https://telegra.ph/file/37882de26f9ffc60043ef.jpg",
    "keywords": ["yesser md", "yesser md"],
    "success_url": "/",
    "stack": "container",
  
    "env": {
      "OWNER_NAME": {
        "description": "Name for Bot Owner",
        "value": "yesser teach",
        "required": false
      },
  
      "WELCOME": {
        "description": "put 'false' or 'true' to enable & disable WELCOME message ",
        "value": "false",
        "required": false
      },
      "GOODBYE": {
        "description": "put 'false' or 'true' to enable & disable GOODBYE message ",
        "value": "false",
        "required": false
      },
      "BOT_NAME": {
        "description": "Your Bot Name",
        "required": false,
        "value": "yesser md"
      },
      "TIME_ZONE": {
        "description": "Put TIME_ZONE according to your location",
        "required": false,
        "value": "Africa/dar es saalam"
      },
        "SUDO_NUMBERS": {
        "description": "Numbers you wish to be second bot owners",
        "required": false,
        "value": "255621995482,255685957360"
      },
      "READ_COMMAND": {
        "description": " Read bot cmds",
        "required": false,
        "value": "true"
      },
      "WARN_COUNT": {
        "description": " Warn count for users to kick/block when warn limit exceed!",
        "required": false,
        "value": "3"
      },
      "AUTO_SAVE_STATUS": {
        "description": " Auto save whatsapp status",
        "required": false,
        "value": "false"
      },
      "HEROKU_API_KEY": {
        "description": "Put Your Heroku Api Key Here",
        "value": "",
        "required": true
      },
      "HEROKU_APP_NAME": {
        "description": "Put Your Heroku App Name Here",
        "value": "",
        "required": true
      },
      "WAPRESENCE": {
        "description": "Fill the value: 'unavailable'(for nothing) | 'available'(for alwaysonline) | 'composing'(for typing) | 'recording' | 'paused' ",
        "required": false,
        "value": "available"
      },
      "AUTO_READ_STATUS": {
        "description": "Fill the value true if you want bot view your Statuses.",
        "required": false,
        "value": "true"
      },
      "MSGS_IN_LOG": {
        "description": "Fill the value -true- if you want to see Messages in logs.",
        "required": false,
        "value": "false"
      },
      "READ_MESSAGE": {
        "description": "Fill the value true if you want bot to read all messages.",
        "required": false,
        "value": "false"
      },
      "DISABLE_PM": {
        "description": "Make it 'false' if you wanna run bot in your pm (if MODE is Public)",
        "value": "true",
        "required": false
      },
      "PREFIX": {
        "description": "Enter your desired prefix for bot. you can set `all | . | .!*`",
        "value": "."
      },
      "THUMB_IMAGE": {
      "description": "Menu Image",
      "value": "https://telegra.ph/file/37882de26f9ffc60043ef.jpg"
      },
      "OWNER_NUMBER": {
        "description": "The phone numbers of the users who you want to be admin for the bot (should be in international format without + and multiple numbers must be separated by a comma \",\")",
        "value": "255621995482,225685957360"
      },
      "SESSION_ID": {
        "description": "put your SESSION_ID here.",
        "value": ""
      },
      "MODE": {
        "description": "Worktype of your bot. Use public or private, if it is private then only bot number can use it. If public then everyone can use it.",
        "value": "private"
      },
      "STICKER_NAME": {
        "description": "Put Sticker Pack_Name.",
        "value": "yesser teach",
        "required": false
      },
      "STICKER_AUTHOR": {
        "description": "Put Sticker Author_Name.",
        "value": "yesser teach",
        "required": false
      }
    },
    "addons": [{ "plan": "heroku-postgresql:essential-0" }],
    "buildpacks": [
      { "url": "https://github.com/heroku/heroku-buildpack-nodejs#latest" },
      { "url": "https://github.com/carlosdommor/heroku-buildpack-ffmpeg-latest" }
    ]
  
