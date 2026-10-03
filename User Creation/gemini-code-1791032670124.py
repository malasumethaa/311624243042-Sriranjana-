import json
import os
from datetime import datetime

class UserCreationManager:
    def __init__(self, registry_file="user_registry.json"):
        self.registry_file = registry_file

    def create_users(self):
        """Milestone 1A: Creates initial system users."""
        users = [
            {"user_id": "U001", "email": "admin@domain.com", "status": "ACTIVE"},
            {"user_id": "U002", "email": "editor@domain.com", "status": "ACTIVE"},
            {"user_id": "U003", "email": "viewer@domain.com", "status": "ACTIVE"}
        ]
        
        data = {"users": users, "created_at": datetime.now().isoformat()}
        with open(self.registry_file, 'w') as f:
            json.dump(data, f, indent=4)
            
        print("Milestone 1A (Users Creation) completed successfully.")