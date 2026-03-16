"""macOS platform skills package."""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nova.skills.base import Skill


def register_skills() -> list[dict]:
    """Register all macOS skills.
    
    Returns a list of skill metadata for Nova to load.
    Each skill has its SKILL.md file in its own directory.
    """
    skills: list[dict] = []
    skills_dir = Path(__file__).parent
    
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir() and skill_dir.name != "__pycache__":
            skill_file = skill_dir / "SKILL.md"
            if skill_file.exists():
                skills.append({
                    "name": skill_dir.name,
                    "path": str(skill_dir),
                    "source": "nova-platform-macos"
                })
    
    return skills