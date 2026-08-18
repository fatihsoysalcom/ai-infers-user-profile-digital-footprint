# This script simulates how an AI might infer a user's profile from their digital footprint.
# It demonstrates how seemingly disparate online activities can reveal personal interests, demographics, and intentions.

# --- Simulate a user's digital footprint ---
# In a real scenario, this data would be collected from various online interactions.
user_footprint = {
    "browsing_history": [
        "https://www.techcrunch.com/ai-developments",
        "https://www.apple.com/iphone-15-pro-review",
        "https://www.traveladvisor.com/best-beaches-thailand",
        "https://www.healthline.com/meditation-benefits",
        "https://www.forbes.com/ai-investment-trends"
    ],
    "search_queries": [
        "latest AI models for text generation",
        "best noise-cancelling headphones 2024",
        "flights to Bangkok in December",
        "mindfulness exercises for stress relief",
        "stock market predictions 2025"
    ],
    "social_media_likes": [
        "post about new AI startups",
        "photo of a tropical beach sunset",
        "article on sustainable living tips",
        "video about personal finance management"
    ]
}

def infer_user_profile(footprint):
    """
    Analyzes the simulated digital footprint to infer user interests, potential demographics, and intent.
    """
    profile = {
        "interests": [],
        "potential_demographics": [],
        "possible_intent": []
    }

    # Define keywords to identify different categories of information
    keywords = {
        "technology": ["ai", "tech", "iphone", "models", "startup", "headphones", "generation"],
        "travel": ["travel", "beach", "flights", "bangkok", "thailand", "tropical"],
        "health_wellness": ["health", "meditation", "mindfulness", "stress", "sustainable living", "wellness"],
        "finance_investment": ["forbes", "investment", "stock market", "finance", "predictions", "management"]
    }

    # Combine all text data from the footprint for analysis
    all_text = " ".join(
        footprint["browsing_history"] +
        footprint["search_queries"] +
        footprint["social_media_likes"]
    ).lower()

    # --- Core AI inference logic: connecting the dots ---
    # This simple rule-based system mimics how AI identifies patterns.

    # Infer interests based on keyword presence
    for interest, terms in keywords.items():
        if any(term in all_text for term in terms):
            profile["interests"].append(interest)

    # Infer potential demographics based on combined interests
    if "technology" in profile["interests"] and "finance_investment" in profile["interests"]:
        profile["potential_demographics"].append("Tech-savvy Investor")
    if "travel" in profile["interests"] and "health_wellness" in profile["interests"]:
        profile["potential_demographics"].append("Health-conscious Traveler")
    elif "technology" in profile["interests"]:
        profile["potential_demographics"].append("Technology Enthusiast")
    elif "health_wellness" in profile["interests"]:
        profile["potential_demographics"].append("Wellness Seeker")

    # Infer possible intent from specific phrases
    if "flights to bangkok" in all_text or "best beaches thailand" in all_text:
        profile["possible_intent"].append("Planning a trip to Southeast Asia")
    if "stock market predictions" in all_text or "ai investment trends" in all_text:
        profile["possible_intent"].append("Researching investment opportunities")
    if "mindfulness exercises" in all_text or "meditation benefits" in all_text:
        profile["possible_intent"].append("Seeking stress relief or self-improvement")

    return profile

# --- Run the inference and display results ---
inferred_profile = infer_user_profile(user_footprint)

print("--- User's Simulated Digital Footprint ---")
for category, items in user_footprint.items():
    print(f"{category.replace('_', ' ').title()}:")
    for item in items:
        print(f"  - {item}")

print("\n--- Inferred User Profile (by AI System) ---")
print(f"Interests: {', '.join(inferred_profile['interests']) if inferred_profile['interests'] else 'None'}")
print(f"Potential Demographics: {', '.join(inferred_profile['potential_demographics']) if inferred_profile['potential_demographics'] else 'None'}")
print(f"Possible Intent: {', '.join(inferred_profile['possible_intent']) if inferred_profile['possible_intent'] else 'None'}")

print("\n--- How AI Connects the Dots (Illustrative) ---")
print("This example shows how an AI system can infer a user's:")
print("- **Interests:** From visited tech sites, search queries about AI/gadgets, and liked posts.")
print("- **Travel Plans:** From searches for flights and travel destinations.")
print("- **Wellness Focus:** From health-related articles and mindfulness searches.")
print("- **Financial Habits:** From investment news and personal finance tips.")
print("Even without direct declarations, seemingly disparate digital traces build a comprehensive profile.")
