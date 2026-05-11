import os
import shutil
import subprocess


def deploy_ultroid(user_id, api_id, api_hash, bot_token, session_string, mongo_url):
    template_dir = "/root/userbot-panel/templates/ultroid"
    instance_dir = f"/root/userbot-panel/instances/{user_id}"

    # Copy template jika belum ada
    if not os.path.exists(instance_dir):
        shutil.copytree(template_dir, instance_dir)

    # Buat file .env
    env_content = f"""
API_ID={api_id}
API_HASH={api_hash}
BOT_TOKEN={bot_token}
SESSION={session_string}
MONGO_URI={mongo_url}
LOG_CHANNEL=0
HEROKU_API=
HEROKU_APP_NAME=
"""

    with open(f"{instance_dir}/.env", "w") as f:
        f.write(env_content.strip())

    # Jalankan Ultroid di background
    cmd = (
        f"screen -dmS ultroid_{user_id} "
        f"bash -c 'cd {instance_dir} && "
        f"source venv/bin/activate && "
        f"python3 -m pyUltroid'"
    )

    subprocess.run(cmd, shell=True)
