import json
import os
from typing import Dict, List, Optional

class MappingManager:
    def __init__(self, config_path: str = "config/mappings.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """بارگذاری فایل پیکربندی"""
        if not os.path.exists(self.config_path):
            return {
                "metadata": {
                    "version": "1.0.0",
                    "created_at": "2024-04-13",
                    "description": "Android Input Mapper Configuration",
                    "screen_resolution": "1920x1080"
                },
                "games": {}
            }
        
        with open(self.config_path, "r") as f:
            return json.load(f)

    def save_config(self) -> None:
        """ذخیره پیکربندی"""
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=4)

    def get_mappings(self, game_id: str = "default") -> Dict:
        """دریافت mapping‌های یک بازی"""
        return self.config.get("games", {}).get(game_id, {}).get("mappings", {})

    def set_mapping(self, game_id: str, key: str, coordinates: List[int]) -> None:
        """تنظیم mapping جدید"""
        if "games" not in self.config:
            self.config["games"] = {}
        
        if game_id not in self.config["games"]:
            self.config["games"][game_id] = {"name": game_id, "mappings": {}}
        
        self.config["games"][game_id]["mappings"][key] = coordinates
        self.save_config()

    def delete_mapping(self, game_id: str, key: str) -> None:
        """حذف mapping"""
        if game_id in self.config.get("games", {}):
            if key in self.config["games"][game_id]["mappings"]:
                del self.config["games"][game_id]["mappings"][key]
                self.save_config()

    def get_game_list(self) -> List[str]:
        """لیست بازی‌های موجود"""
        return list(self.config.get("games", {}).keys()) 