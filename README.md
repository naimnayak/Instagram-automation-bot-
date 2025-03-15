# Instagram Direct Message Automation

This script automates sending direct messages (DMs) to your Instagram followers using the `instagrapi` library. It sends a personalized message followed by a link to your startup or brand. The script is designed to avoid spam detection by incorporating random delays and message variations.

---

## Prerequisites

1. **Python 3.x** - Make sure Python is installed on your system.
2. **Instagram Account** - You need an Instagram account with 2FA (Two-Factor Authentication) **disabled**.
3. **Instagrapi Library** - Install the required library using pip.

---

## Installation

1. Clone this repository or download the script.
2. Install the `instagrapi` library:

   ```bash
   pip install instagrapi

## Open the script and fill in the following details:
USERNAME = ""  # Enter your Instagram username
PASSWORD = ""  # Enter your Instagram password (2FA must be disabled)
MESSAGE_LINK = ""  # Replace with your link

## Save the file.

## Usage

1. Run the script:

python script.py

2. The script will:
    Load your followers.
    Send a personalized message to each follower.
    Follow up with a second message containing your link.
    Avoid spamming by adding random delays between messages.

3. Daily Limit: The script is set to message a maximum of 100 users per day to avoid Instagram's restrictions. After reaching the limit, it will wait 24 hours before resuming.

4. Messaged Users: The script keeps track of messaged users in a file named messaged_users.txt. This ensures that users are not messaged multiple times.

## Customization

1. Message Variations: Edit the messages list in the script to customize the messages sent to your followers.
2. Delays: Adjust the delays in the script to suit your needs:
    Fixed delay after each user: time.sleep(75)
    Random delay after every 10 users: random.randint(90, 240)

## Important Notes

Instagram Limits: Be cautious of Instagram's daily messaging limits to avoid getting your account flagged or banned.
2FA: Ensure that 2FA is disabled on your account, as the script cannot handle 2FA.
Ethical Use: Use this script responsibly and avoid spamming users.

## Troubleshooting

Login Issues: If you encounter login issues, double-check your username and password, and ensure 2FA is disabled.
Spam Detection: If Instagram flags your account, increase the delays between messages or reduce the daily limit.

## License

This project is open-source and free to use. Use it responsibly!

## Disclaimer

This script is for educational purposes only. The author is not responsible for any misuse or account restrictions imposed by Instagram.
