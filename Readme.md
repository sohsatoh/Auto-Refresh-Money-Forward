# Auto Refresh Money Forward
Money Forwardにおける口座情報の更新を一括で行うスクリプトです。


## Requirements
- Python3
- Selenium
- ChromeDriver


## How to use
~~~
email = 'YOUR_EMAIL_ADDRESS'
password = 'YOUR_PASSWORD'
path = '/usr/lib/chromium-browser/chromedriver'
~~~
の部分を、自分のログイン情報、ChromeDriverのパスに書き換えた後、
~~~
python3 ./moneyforward.py
~~~
で実行してください。

又、定期的に実行する際は、cron等で設定してください。
