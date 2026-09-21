import streamlit as st
from llm_parser import extract_preferences
from recommendation import get_recommendations


st.set_page_config(
    page_title="Smart Food Recommendation System",
    page_icon="🍱",
    layout="centered"
)


st.title("🍱 Smart Food Recommendation System")

st.write(
    "Enter your food preference in natural language. "
    "The system uses LangChain + Gemini to understand your request "
    "and Fuzzy Logic to recommend suitable foods."
)


user_input = st.text_area(
    "Tell me what you want to eat:",
    placeholder="Example: I am very hungry and want a healthy vegetarian breakfast with low calories."
)


if st.button("🔍 Get Recommendations"):

    if not user_input.strip():
        st.warning("Please enter your food preference.")
    else:

        try:
            # Step 1: Extract preferences using LangChain + Gemini
            with st.spinner("Understanding your food preference..."):
                preferences = extract_preferences(user_input)

            st.subheader("🧠 Extracted Preferences")

            col1, col2 = st.columns(2)

            with col1:
                st.write("**Meal:**", preferences["meal"])
                st.write("**Diet:**", preferences["diet"])
                st.write("**Hunger:**", preferences["hunger"])

            with col2:
                st.write(
                    "**Health Preference:**",
                    preferences["health_preference"]
                )
                st.write(
                    "**Calorie Preference:**",
                    preferences["calorie_preference"]
                )

            # Step 2: Apply Fuzzy Logic
            with st.spinner("Applying fuzzy logic..."):
                recommendations = get_recommendations(
                    preferences["hunger"],
                    preferences["health_preference"],
                    preferences["calorie_preference"],
                    preferences["meal"],
                    preferences["diet"]
                )

            st.subheader("🍽️ Recommended Foods")

            if not recommendations:
                st.info(
                    "No matching foods were found for the selected meal and diet."
                )
            else:

                # Show top 3 recommendations
                for i, food in enumerate(recommendations[:3], start=1):

                    st.markdown(
                        f"### {i}. {food['name']}"
                    )

                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        st.metric(
                            "Fuzzy Score",
                            f"{food['score']:.2f}"
                        )

                    with col2:
                        st.metric(
                            "Calories",
                            food["calories"]
                        )

                    with col3:
                        st.metric(
                            "Healthiness",
                            food["healthiness"]
                        )

                    with col4:
                        st.metric(
                            "Filling",
                            food["filling"]
                        )

                    st.divider()

        except Exception as e:

            st.error(
                "Something went wrong while processing your request."
            )

            st.write("Error:", e)


st.markdown("---")

st.caption(
    "Smart Food Recommendation System | "
    "LangChain + Gemini + Fuzzy Logic"
)