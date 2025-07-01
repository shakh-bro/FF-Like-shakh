import os
import json
import logging
from cachetools import TTLCache

logger = logging.getLogger(__name__)

class TokenCache:
    def __init__(self, config_dir="config"):
        self.cache = {}
        self.config_dir = config_dir
        self._load_all_tokens()

    def _load_all_tokens(self):
        for filename in os.listdir(self.config_dir):
            if filename.endswith("_config.json"):
                region = filename.replace("_config.json", "").upper()
                filepath = os.path.join(self.config_dir, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        tokens = [user["password"] for user in data]
                        self.cache[region] = tokens
                        logger.info(f"{region}: {len(tokens)} token loaded")
                except Exception as e:
                    logger.error(f"Failed to load {filename}: {str(e)}")

    def get_tokens(self, region):
        return self.cache.get(region.upper(), [])
def get_headers(token: str):
    return {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB49"
    }