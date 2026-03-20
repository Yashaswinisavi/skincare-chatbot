def generate_response(query):
    query = query.lower()

    if "acne" in query:
        return """Acne is caused by clogged pores and excess oil.

🌞 Morning:
• Salicylic acid cleanser  
• Niacinamide serum  
• Oil-free moisturizer  
• Sunscreen  

🌙 Night:
• Cleanser  
• Treatment (salicylic acid)  
• Moisturizer  

🧴 Products:
Dot & Key, Derma Co, Minimalist  

✨ Tips:
• Avoid touching face  
• Stay consistent"""

    elif "oily" in query:
        return """For oily skin:

🌞 Morning:
• Gel cleanser  
• Niacinamide  
• Light moisturizer  
• Matte sunscreen  

🌙 Night:
• Cleanser  
• Salicylic acid  

🧴 Products:
Minimalist, Dot & Key  

✨ Tip: Don’t overwash"""

    else:
        return """Basic skincare routine:

🌞 Morning:
• Cleanser  
• Moisturizer  
• Sunscreen  

🌙 Night:
• Cleanser  
• Moisturizer  

✨ Stay consistent 💖"""