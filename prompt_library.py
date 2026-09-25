prompts = [
    {
        "id": 1,
        "title": "Python Code Reviewer",
        "category": "Programming",
        "ai_tool": "ChatGPT",
        "prompt": "Review the following Python code and identify bugs, improvements and best practices.",
        "rating": 4.8
    },
    {
        "id": 2,
        "title": "Marketing Copy Generator",
        "category": "Marketing",
        "ai_tool": "Claude",
        "prompt": "Create persuasive marketing copy for the following product.",
        "rating": 4.5
    },
    {
        "id": 3,
        "title": "Data Analysis Assistant",
        "category": "Data Science",
        "ai_tool": "ChatGPT",
        "prompt": "Analyze this dataset and identify important trends, anomalies and insights.",
        "rating": 4.9
    },
    {
        "id": 4,
        "title": "Email Writer",
        "category": "Productivity",
        "ai_tool": "Gemini",
        "prompt": "Write a professional email based on the following information.",
        "rating": 4.3
    },
    {
        "id": 5,
        "title": "Resume Optimizer",
        "category": "Career",
        "ai_tool": "ChatGPT",
        "prompt": "Analyze my resume against this job description and suggest improvements.",
        "rating": 4.7
    }
]


# --------------------------------------------------
# 1. View available prompts
# --------------------------------------------------

def display_prompts(prompt_list):
    if not prompt_list:
        print("No prompts available.")
        return

    print("\n========== PROMPT LIBRARY ==========")

    for prompt in prompt_list:
        print(f"\nID       : {prompt['id']}")
        print(f"Title    : {prompt['title']}")
        print(f"Category : {prompt['category']}")
        print(f"AI Tool  : {prompt['ai_tool']}")
        print(f"Rating   : {prompt['rating']}")
        print(f"Prompt   : {prompt['prompt']}")
        print("-" * 50)


# --------------------------------------------------
# 2. Search by category
# --------------------------------------------------

def search_by_category(category):
    results = []

    for prompt in prompts:
        if prompt["category"].lower() == category.lower():
            results.append(prompt)

    return results


# --------------------------------------------------
# 3. Search by AI tool
# --------------------------------------------------

def search_by_tool(ai_tool):
    results = []

    for prompt in prompts:
        if prompt["ai_tool"].lower() == ai_tool.lower():
            results.append(prompt)

    return results


# --------------------------------------------------
# 4. Add a new prompt
# --------------------------------------------------

def add_prompt():
    print("\n========== ADD NEW PROMPT ==========")

    title = input("Enter prompt title: ")
    category = input("Enter category: ")
    ai_tool = input("Enter AI tool: ")
    prompt_text = input("Enter prompt: ")

    while True:
        try:
            rating = float(input("Enter rating (0-5): "))

            if 0 <= rating <= 5:
                break

            print("Rating must be between 0 and 5.")

        except ValueError:
            print("Please enter a valid number.")

    new_id = len(prompts) + 1

    new_prompt = {
        "id": new_id,
        "title": title,
        "category": category,
        "ai_tool": ai_tool,
        "prompt": prompt_text,
        "rating": rating
    }

    prompts.append(new_prompt)

    print("\nPrompt added successfully!")


# --------------------------------------------------
# 5. Highest-rated prompt
# --------------------------------------------------

def highest_rated_prompt():
    if not prompts:
        return None

    highest = prompts[0]

    for prompt in prompts:
        if prompt["rating"] > highest["rating"]:
            highest = prompt

    return highest


# --------------------------------------------------
# 6. Count prompts by category
# --------------------------------------------------

def count_by_category():
    category_counts = {}

    for prompt in prompts:

        category = prompt["category"]

        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    return category_counts


# --------------------------------------------------
# 7. Library summary
# --------------------------------------------------

def library_summary():

    total_prompts = len(prompts)

    categories = set()
    tools = set()

    total_rating = 0

    for prompt in prompts:
        categories.add(prompt["category"])
        tools.add(prompt["ai_tool"])
        total_rating += prompt["rating"]

    if total_prompts > 0:
        average_rating = total_rating / total_prompts
    else:
        average_rating = 0

    print("\n========== LIBRARY SUMMARY ==========")

    print(f"Total Prompts       : {total_prompts}")
    print(f"Total Categories    : {len(categories)}")
    print(f"Total AI Tools      : {len(tools)}")
    print(f"Average Rating      : {average_rating:.2f}")

    print("\nPrompts by Category:")

    category_counts = count_by_category()

    for category, count in category_counts.items():
        print(f"{category}: {count}")


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

def main():

    while True:

        print("\n======================================")
        print("       AI PROMPT LIBRARY MANAGER")
        print("======================================")

        print("1. View Available Prompts")
        print("2. Search by Category")
        print("3. Search by AI Tool")
        print("4. Add New Prompt")
        print("5. Display Highest-Rated Prompt")
        print("6. Count Prompts by Category")
        print("7. Library Summary")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            display_prompts(prompts)

        elif choice == "2":

            category = input("Enter category: ")

            results = search_by_category(category)

            display_prompts(results)

        elif choice == "3":

            ai_tool = input("Enter AI tool: ")

            results = search_by_tool(ai_tool)

            display_prompts(results)

        elif choice == "4":

            add_prompt()

        elif choice == "5":

            result = highest_rated_prompt()

            if result:
                display_prompts([result])
            else:
                print("No prompts available.")

        elif choice == "6":

            counts = count_by_category()

            print("\n========== CATEGORY COUNTS ==========")

            for category, count in counts.items():
                print(f"{category}: {count}")

        elif choice == "7":

            library_summary()

        elif choice == "8":

            print("Thank you for using AI Prompt Library Manager!")
            break

        else:

            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()