import yaml
import os

class PromptManager:
    def __init__(self, prompt_file: str = "prompts.yaml"):
        self.prompt_file = prompt_file
        self.prompts = {}
        self.load_prompts()

    def load_prompts(self):
        """Loads prompts from the YAML file."""
        if not os.path.exists(self.prompt_file):
            raise FileNotFoundError(f"Prompt file {self.prompt_file} not found.")
        
        with open(self.prompt_file, "r") as f:
            self.prompts = yaml.safe_load(f)

    def get_prompt(self, key: str, default: str = "") -> str:
        """Retrieves a prompt by key."""
        return self.prompts.get(key, default)
