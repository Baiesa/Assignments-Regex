'''
Task 1: Product Description Keyword Tagging

Problem Statement:
You have a list of product descriptions. Your task is to tag each product based on keywords in the description. 
For instance, tag products as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.
'''

import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

electronics_keywords = ["smartphone", "tablet", "laptop", "electronics"]
apparel_keywords = ["t-shirt", "shirt", "pants", "dress", "apparel"]
kitchen_keywords = ["kitchen", "knife", "cookware", "kettle", "kitchenware"]


def tag_product(description):
    if any(re.search(keyword, description, re.IGNORECASE) for keyword in electronics_keywords):
        return "Electronics"
    elif any(re.search(keyword, description, re.IGNORECASE) for keyword in apparel_keywords):
        return "Apparel"
    elif any(re.search(keyword, description, re.IGNORECASE) for keyword in kitchen_keywords):
        return "Home & Kitchen"
    else:
        return "Other"


tagged_products = [tag_product(description) for description in descriptions]

for i, product in enumerate(tagged_products, start=1):
    print(f"Product {i}: {product}")
