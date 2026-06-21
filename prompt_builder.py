from styles import STYLE_PROMPTS

def build_prompt(user_prompt, style):

    style_prompt = STYLE_PROMPTS.get(style, "")

    final_prompt = f"""
    {user_prompt},
    {style_prompt},
    architectural visualization,
    interior design magazine quality,
    highly detailed,
    photorealistic,
    ultra realistic,
    8k quality
    """

    return final_prompt.strip()