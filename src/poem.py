""" Poem data structures."""
from pathlib import Path

class Poem:
    """ Poem data structure."""
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content.strip()  # Remove leading/trailing spaces

    def __str__(self):
        """Convert poem content and title to a string."""
        return f"Title: {self.title}\n{self.content}"

    @classmethod
    def from_file(cls, path: Path):
        """Generate a Poem instance from a text file."""
        try:
            with open(path, "r", encoding="utf-8") as file:
                lines = file.readlines()
            
            # Assume the first line is the title and the rest is the content
            title = lines[0].strip()
            content = "".join(lines[1:]).strip()
            
            return cls(title, content)
        
        except FileNotFoundError:
            print(f"Error: File '{path}' not found.")
            return None
    
class PoemCollection:
    """ Collection class for multiple poems."""
    def __init__(self):
        self.poems = []
        self.entity_name = "Gedicht"
    
    def add(self, poem: Poem):
        self.poems.append(poem)
    
    def __str__(self):
        return "\n\n".join([str(idx+1)+f". {self.entity_name}\n"+ str(poem) for idx,poem in enumerate(self.poems)])