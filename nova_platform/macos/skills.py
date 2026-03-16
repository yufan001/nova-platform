"""macOS platform skills registration."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def register_skills() -> list[dict[str, Any]]:
    """Register macOS skills with Nova.
    
    Returns a list of skill metadata for Nova's skill loader.
    """
    skills_dir = Path(__file__).parent / "skills"
    skills = []
    
    for skill_dir in skills_dir.iterdir():
        if not skill_dir.is_dir():
            continue
        
        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            skills.append({
                "name": skill_dir.name,
                "path": str(skill_md),
                "platform": "darwin",
            })
    
    return skills