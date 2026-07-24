from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    normalized = ingredients.lower()
    is_valid = any(
        ingredient in normalized
        for ingredient in light_spell_allowed_ingredients()
    )
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"
