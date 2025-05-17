import json
import os
from typing import Dict, Any

class AppConfig:
    """
    Configuration class for application settings.
    """
    def __init__(self):
        """Initialize configuration with default values"""
        self.config_file = "app_config.json"
        self.default_config = {
            "db_path": "Employee.db",
            "theme": "Light"
        }
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file or use defaults"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except Exception:
                return self.default_config.copy()
        return self.default_config.copy()
    
    def save(self) -> bool:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
            return True
        except Exception:
            return False
    
    def get_db_path(self) -> str:
        """Get database path"""
        return self.config.get("db_path", self.default_config["db_path"])
    
    def set_db_path(self, path: str) -> None:
        """Set database path"""
        self.config["db_path"] = path
    
    def get_theme(self) -> str:
        """Get UI theme"""
        return self.config.get("theme", self.default_config["theme"])
    
    def set_theme(self, theme: str) -> None:
        """Set UI theme"""
        self.config["theme"] = theme