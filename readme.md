# OCR - Bot
A Simple Discord Bot for OCR. Deployable on Heroku.

Check out my implementation of this [OCR-BOT](https://discord.com/api/oauth2/authorize?client_id=805507110363201547&permissions=2048&scope=bot)

As a personal preference, this bot requires no command to do OCR. So add it to a separate channel and make sure other channels are not visible to it.


# Instructions:
 - Clone the repo
 - Install all the requirements
     ```sh
    pip install -r requirements.txt
    ```
- These requirements include "opencv-headless", if you are trying it on a machine which doesn't support it, install the [normal OpenCV](https://pypi.org/project/opencv-python/) library.

- Install tesserct-ocr using this command:
    - On Ubuntu
      ```
      sudo apt-get install tesseract-ocr
      ```
    - On Mac
      ```
      brew install tesseract
      ```
    - On Windows, download installer from [here](https://github.com/UB-Mannheim/tesseract/wiki)
 
- ### Don't forget to add your "BOT_TOKEN" in the "bot.py" file.

- Run the python bot using the command: 
    ```sh
    python bot.py
   ```
    or
    ```sh
    python3 bot.py
    ```
 
