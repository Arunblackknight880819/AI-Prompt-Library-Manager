import streamlit as st


# ---------------------------------------
# Initial prompt data
# ---------------------------------------

if "prompts" not in st.session_state:

    st.session_state.prompts = [
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


prompts = st.session_state.prompts


# ---------------------------------------
# Page configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Prompt Library Manager",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------
# Title
# ---------------------------------------

st.title("🤖 AI Prompt Library Manager")

st.write(
    "Manage, search and explore a collection of useful AI prompts."
)


# ---------------------------------------
# Dashboard
# ---------------------------------------

total_prompts = len(prompts)

categories = set()
tools = set()

for prompt in prompts:
    categories.add(prompt["category"])
    tools.add(prompt["ai_tool"])

if total_prompts > 0:
    total_rating = 0

    for prompt in prompts:
        total_rating += prompt["rating"]

    average_rating = total_rating / total_prompts

else:
    average_rating = 0


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Prompts",
    total_prompts
)

col2.metric(
    "Categories",
    len(categories)
)

col3.metric(
    "AI Tools",
    len(tools)
)

col4.metric(
    "Average Rating",
    f"{average_rating:.2f}"
)


st.divider()


# ---------------------------------------
# Sidebar
# ---------------------------------------

st.sidebar.header("Navigation")

option = st.sidebar.radio(
    "Select an operation",
    [
        "View Prompts",
        "Search Prompts",
        "Add Prompt",
        "Highest Rated",
        "Category Statistics",
        "Library Summary"
    ]
)


# =======================================
# 1. View Prompts
# =======================================

if option == "View Prompts":

    st.header("📚 Available Prompts")

    if not prompts:

        st.warning("No prompts available.")

    else:

        for item in prompts:

            with st.expander(
                f"{item['title']} ⭐ {item['rating']}"
            ):

                st.write(
                    f"**Category:** {item['category']}"
                )

                st.write(
                    f"**AI Tool:** {item['ai_tool']}"
                )

                st.write("**Prompt:**")

                st.code(
                    item["prompt"],
                    language="text"
                )


# =======================================
# 2. Search Prompts
# =======================================

elif option == "Search Prompts":

    st.header("🔎 Search Prompts")

    search_type = st.selectbox(
        "Search by",
        [
            "Category",
            "AI Tool"
        ]
    )

    search_value = st.text_input(
        "Enter search value"
    )

    if st.button("Search"):

        results = []

        for item in prompts:

            if search_type == "Category":

                if item["category"].lower() == search_value.lower():

                    results.append(item)

            else:

                if item["ai_tool"].lower() == search_value.lower():

                    results.append(item)


        if results:

            st.success(
                f"{len(results)} prompt(s) found."
            )

            for item in results:

                st.subheader(item["title"])

                st.write(
                    f"Category: {item['category']}"
                )

                st.write(
                    f"AI Tool: {item['ai_tool']}"
                )

                st.write(
                    f"Rating: ⭐ {item['rating']}"
                )

                st.code(item["prompt"])

        else:

            st.warning(
                "No matching prompts found."
            )


# =======================================
# 3. Add Prompt
# =======================================

elif option == "Add Prompt":

    st.header("➕ Add New Prompt")

    title = st.text_input(
        "Prompt Title"
    )

    category = st.text_input(
        "Category"
    )

    ai_tool = st.text_input(
        "AI Tool"
    )

    prompt_text = st.text_area(
        "Prompt"
    )

    rating = st.slider(
        "Rating",
        min_value=0.0,
        max_value=5.0,
        value=4.0,
        step=0.1
    )


    if st.button("Add Prompt"):

        if (
            title.strip()
            and category.strip()
            and ai_tool.strip()
            and prompt_text.strip()
        ):

            new_prompt = {
                "id": len(prompts) + 1,
                "title": title,
                "category": category,
                "ai_tool": ai_tool,
                "prompt": prompt_text,
                "rating": rating
            }

            st.session_state.prompts.append(
                new_prompt
            )

            st.success(
                "Prompt added successfully!"
            )

        else:

            st.error(
                "Please fill in all fields."
            )


# =======================================
# 4. Highest Rated
# =======================================

elif option == "Highest Rated":

    st.header("🏆 Highest-Rated Prompt")

    if prompts:

        highest = prompts[0]

        for item in prompts:

            if item["rating"] > highest["rating"]:

                highest = item

        st.success(
            f"Highest Rating: ⭐ {highest['rating']}"
        )

        st.subheader(
            highest["title"]
        )

        st.write(
            f"**Category:** {highest['category']}"
        )

        st.write(
            f"**AI Tool:** {highest['ai_tool']}"
        )

        st.code(
            highest["prompt"]
        )

    else:

        st.warning(
            "No prompts available."
        )


# =======================================
# 5. Category Statistics
# =======================================

elif option == "Category Statistics":

    st.header("📊 Prompts by Category")

    category_counts = {}

    for item in prompts:

        category = item["category"]

        if category in category_counts:

            category_counts[category] += 1

        else:

            category_counts[category] = 1


    for category, count in category_counts.items():

        st.write(
            f"**{category}:** {count}"
        )

        st.progress(
            count / len(prompts)
        )


# =======================================
# 6. Library Summary
# =======================================

elif option == "Library Summary":

    st.header("📋 Library Summary")

    st.write(
        f"Total prompts: **{total_prompts}**"
    )

    st.write(
        f"Total categories: **{len(categories)}**"
    )

    st.write(
        f"Total AI tools: **{len(tools)}**"
    )

    st.write(
        f"Average rating: **⭐ {average_rating:.2f}**"
    )

    st.subheader(
        "Categories"
    )

    for category in categories:

        st.write(f"• {category}")

    st.subheader(
        "AI Tools"
    )

    for tool in tools:

        st.write(f"• {tool}")