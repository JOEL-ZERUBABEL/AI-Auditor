
import json
import streamlit as st

from main import (
    StarupModel,
    Starup,
    CEO,

    INVESTMENT,
    Investment,
    RiskAnalyst,
    Verdict,Career,CareerModel
)

st.set_page_config(
    page_title="Decision Boardroom",
    layout="wide")

st.title("AI Decision Boardroom")

boardroom = st.sidebar.selectbox(
    "Select Boardroom",
    [
        "Startup Boardroom",
        "Investment Boardroom",
        'Career Boardroom'])

if boardroom == "Startup Boardroom":

    st.header("Startup Boardroom")

    startup_name = st.text_input("Startup Name")

    industry = st.text_input("Industry")

    year = st.number_input(
        "Year",
        min_value=2024,
        max_value=2035,
        value=2026)

    budget = st.number_input(
        "Budget",
        min_value=0)

    team_size = st.number_input(
        "Team Size",
        min_value=1)

    if st.button("Analyze Startup"):

        data = StarupModel(
            startup_name=startup_name,
            industry=industry,
            year=year,
            budget=budget,
            team_size=team_size
        )

        startup = Starup()
        report = startup.advisor(data)

        ceo = CEO()
        ceo_report = ceo.Ceoo(report)

        st.subheader("📋 Advisor Report")
        st.info(report)

        try:
            
            import json

            ceo_data = json.loads(ceo_report)
            st.subheader("👨‍💼 CEO Decision Board")
            col1, col2 = st.columns(2)
            with col1:
                st.metric(
                "CEO Score",
                ceo_data["score"])

            with col2:
                st.metric(
                "Approval %",
                ceo_data["rating_percentage"])

            st.success( ceo_data["response"])
            st.subheader("✅ Next Steps")
            timeline = ceo_data["timeline"]

            if isinstance(timeline, dict):
                for phase, activities in timeline.items():
                    st.markdown(f"### {phase}")
                    for activity in activities:
                        st.write(f"📌 {activity}")

            else:
                for item in timeline:
                    st.write(f"📌 {item}")

        except Exception as e:
            st.error(
                    f"JSON Parsing Error: {e}")
            st.subheader("Raw CEO Report")
            st.code(ceo_report,language="json")
            
elif boardroom == "Investment Boardroom":

    st.header("Investment Boardroom")

    asset_name = st.text_input("Asset Name")

    investment_amount = st.number_input(
        "Investment Amount",
        min_value=0.0)

    investment_duration = st.number_input(
        "Investment Duration (Years)",
        min_value=1)

    risk_tolerance = st.selectbox(
        "Risk Tolerance",
        [
            "Low",
            "Medium",
            "High"
        ])

    investment_goal = st.text_input(
        "Investment Goal")

    if st.button("Analyze Investment"):
        data = INVESTMENT(
            asset_name=asset_name,
            investment_amount=investment_amount,
            investment_duration=investment_duration,
            risk_tolerance=risk_tolerance,
            investment_goal=investment_goal
        )

        investment = Investment()
        report = investment.analyzer(data)

        risk = RiskAnalyst()
        risk_report = risk.analyzer(report)

        verdict = Verdict()
        final_report = verdict.analyzer(
            report,
            risk_report
        )
        st.subheader("Investment Report")
        st.code(report, language="json")

        st.subheader("Risk Report")
        st.code(risk_report, language="json")

        st.subheader("Final Verdict")
        st.code(final_report, language="json")

        try:

            report_data = json.loads(report)

            st.subheader("Investment Summary")

            st.success(
                report_data["recommendation"]
            )

            st.write(
                "**Growth Potential:**",
                report_data["growth_potential"]
            )

            st.write(
                "**Market Outlook:**",
                report_data["market_outlook"]
            )

        except:
            pass

elif boardroom == "Career Boardroom":

    st.header("Career Boardroom")

    courses = st.text_area("Courses (comma separated)")

    interest = st.text_area("Interests (comma separated)")

    if st.button("Analyze Career"):

        career_data = CareerModel(
            courses=[
                x.strip()
                for x in courses.split(",")
            ],
            interest=[
                x.strip()
                for x in interest.split(",")
            ])

        career = Career()
        report = career.analyzer(
            career_data)

        st.subheader("Career Report")
        st.info(report)