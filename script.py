from instagrapi import Client
import time
import random
import os

# Instagram Login
USERNAME = "" # Enter your username 
PASSWORD = "" #Disable 2fa if enabled 
MESSAGE_LINK = "" #Put your link here 
MESSAGED_USERS_FILE = "messaged_users.txt"

# Different message variations to avoid spam detection
messages = [
    "Hello there!",
    "Hi! Hope you're doing well.",
    "Hey, how’s it going?",
    "Yo! What’s up?",
    "Greetings! Hope you’re having a great day.",
    "Hey buddy!",
    "Good day to you!",
    "Hi there!",
    "Hey! Long time no see.",
    "Hello! Hope all is well."
] # Replace with your desired messages 


# Load already messaged users from file
def load_messaged_users():
    if not os.path.exists(MESSAGED_USERS_FILE):
        return set()
    with open(MESSAGED_USERS_FILE, "r") as f:
        return set(line.strip() for line in f.readlines())

# Save new messaged users to file
def save_messaged_user(user_id):
    with open(MESSAGED_USERS_FILE, "a") as f:
        f.write(f"{user_id}\n")

# Initialize Instagram client
cl = Client()
cl.login(USERNAME, PASSWORD)

# Get all followers
followers = list(cl.user_followers(cl.user_id).items())  # Convert to list for indexing
total_followers = len(followers)
processed_users = 0

# Load previously messaged users
messaged_users = load_messaged_users()

# Run the script until all followers are messaged
while processed_users < total_followers:
    daily_count = 0  # Reset daily count

    for i in range(processed_users, min(processed_users + 100, total_followers)):
        user_id, user = followers[i]

        # Skip users who have already been messaged
        if str(user_id) in messaged_users:
            continue

        username = user.username
        full_name = user.full_name if user.full_name else username

        try:
            # Select a random message template
            custom_message = random.choice(messages).format(name=full_name)

            # Send first message (without the link)
            cl.direct_send(custom_message, [user_id])
            print(f"✅ First message sent to {username}")

            # Wait 7-15 seconds before sending the second message (to avoid spam detection)
            time.sleep(random.randint(7, 15))

            # Send second message (only the link)
            cl.direct_send(MESSAGE_LINK, [user_id])
            print(f"✅ Second message (link) sent to {username}")

            # Mark user as messaged
            save_messaged_user(user_id)
            messaged_users.add(str(user_id))

            daily_count += 1

        except Exception as e:
            print(f"❌ Failed to message {username}: {e}")

        # Fixed 75-second delay after messaging each user
        print("⏳ Waiting 75 seconds before next user...")
        time.sleep(75)

        # **Random delay (90-240 sec) only after every 10 users**
        if daily_count % 10 == 0:
            extra_delay = random.randint(90, 240)
            print(f"⏳ Extra random wait time (only after 10 users): {extra_delay} seconds")
            time.sleep(extra_delay)

    processed_users += daily_count  # Update processed users

    # If daily limit is reached, wait 24 hours before continuing
    if daily_count == 100:
        print(f"🚀 Daily limit of 100 users reached. Waiting 24 hours before resuming...")
        time.sleep(24 * 60 * 60)  # 24-hour wait

print("✅ Finished messaging all followers!")
