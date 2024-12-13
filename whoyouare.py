import streamlit as st

def main():
    st.title("당신의 취향")
    st.markdown("#### 그간 설문을 바탕으로 선생님들을 4가지 유형으로 구분했습니다.\n아래의 설문을 따라가보면서 선생님이 어떤 유형인지 알아보세요!")

    if "responses" not in st.session_state:
        st.session_state.responses = {}
    responses = st.session_state.responses

    # 결정 트리 로직(조건 완전성 확보)
    def determine_type(responses):
        if responses["Q1"] == "학생들의 창의력과 미래 대비 능력 개발":
            if responses["Q2"] == "학생들이 직접 문제를 탐구하는 프로젝트 제공":
                if responses["Q3"] == "디자인 씽킹을 활용한 문제 해결":
                    return "미래 대비 혁신가"
                elif responses["Q3"] == "학생들이 주도적으로 프로젝트 설계":
                    return "미래 대비 혁신가"
                elif responses["Q3"] == "AI 도구를 활용한 창의적 사고 자극":
                    return "성과 지향 학습자"
                else:
                    return "미래 대비 혁신가"
            elif responses["Q2"] == "창의적 사고를 자극하는 도구 활용":
                return "미래 대비 혁신가"
            elif responses["Q2"] == "팀 기반 창의적 문제 해결":
                return "행복 중심 학습자"
            else:
                return "미래 대비 혁신가"

        elif responses["Q1"] == "학생들의 정서적 성장과 행복 증진":
            if responses["Q2"] == "학생들과 정기적으로 대화하기":
                return "행복 중심 학습자"
            elif responses["Q2"] == "감정 표현을 위한 활동 제공":
                return "미래 대비 혁신가"
            elif responses["Q2"] == "정서적 안정 프로그램 도입":
                return "성과 지향 학습자"
            else:
                return "행복 중심 학습자"

        elif responses["Q1"] == "교사로서의 전문성 개발":
            if responses["Q2"] == "최신 기술과 도구 학습":
                if responses["Q3"] == "최신 기술 트렌드 세미나 참석":
                    return "전문성 개발 탐구자"
                elif responses["Q3"] == "새로운 수업 도구 실습":
                    return "전문성 개발 탐구자"
                elif responses["Q3"] == "교사 역량 강화 워크숍 참여":
                    return "성과 지향 학습자"
                else:
                    return "전문성 개발 탐구자"
            elif responses["Q2"] == "교사 간 협업과 연구":
                return "전문성 개발 탐구자"
            elif responses["Q2"] == "전문적인 컨퍼런스 참여":
                return "성과 지향 학습자"
            else:
                return "전문성 개발 탐구자"

        elif responses["Q1"] == "학생들의 학업 성취 극대화":
            if responses["Q2"] == "정기적인 피드백 제공":
                if responses["Q3"] == "개별 피드백 계획 수립":
                    return "성과 지향 학습자"
                elif responses["Q3"] == "학생 평가 데이터 활용":
                    return "성과 지향 학습자"
                elif responses["Q3"] == "학생 목표 설정 지원":
                    return "행복 중심 학습자"
                else:
                    return "성과 지향 학습자"
            elif responses["Q2"] == "데이터 기반 학습 분석":
                return "성과 지향 학습자"
            elif responses["Q2"] == "개별 학습 계획 수립":
                return "미래 대비 혁신가"
            else:
                return "성과 지향 학습자"

        else:
            return "미래 대비 혁신가"

    # Q1
    q1_options = [
        "학생들의 창의력과 미래 대비 능력 개발",
        "학생들의 정서적 성장과 행복 증진",
        "교사로서의 전문성 개발",
        "학생들의 학업 성취 극대화"
    ]
    q1_default = responses.get("Q1", q1_options[0])
    if q1_default not in q1_options:
        q1_default = q1_options[0]
    q1 = st.radio(
        "Q1. 교육에서 가장 중요하다고 생각하는 목표는 무엇입니까?",
        q1_options,
        index=q1_options.index(q1_default)
    )
    responses["Q1"] = q1

    # Q2
    if q1 == "학생들의 창의력과 미래 대비 능력 개발":
        q2_options = [
            "학생들이 직접 문제를 탐구하는 프로젝트 제공",
            "창의적 사고를 자극하는 도구 활용",
            "팀 기반 창의적 문제 해결"
        ]
        q2_default = responses.get("Q2", q2_options[0])
        if q2_default not in q2_options:
            q2_default = q2_options[0]
        q2 = st.radio(
            "Q2. 창의력을 강화하기 위해 가장 중요하다고 생각하는 활동은 무엇입니까?",
            q2_options,
            index=q2_options.index(q2_default)
        )
    elif q1 == "학생들의 정서적 성장과 행복 증진":
        q2_options = [
            "학생들과 정기적으로 대화하기",
            "감정 표현을 위한 활동 제공",
            "정서적 안정 프로그램 도입"
        ]
        q2_default = responses.get("Q2", q2_options[0])
        if q2_default not in q2_options:
            q2_default = q2_options[0]
        q2 = st.radio(
            "Q2. 정서적 성장을 위해 가장 중요하다고 생각하는 활동은 무엇입니까?",
            q2_options,
            index=q2_options.index(q2_default)
        )
    elif q1 == "교사로서의 전문성 개발":
        q2_options = [
            "최신 기술과 도구 학습",
            "교사 간 협업과 연구",
            "전문적인 컨퍼런스 참여"
        ]
        q2_default = responses.get("Q2", q2_options[0])
        if q2_default not in q2_options:
            q2_default = q2_options[0]
        q2 = st.radio(
            "Q2. 전문성을 강화하기 위해 가장 중요하다고 생각하는 방법은 무엇입니까?",
            q2_options,
            index=q2_options.index(q2_default)
        )
    elif q1 == "학생들의 학업 성취 극대화":
        q2_options = [
            "정기적인 피드백 제공",
            "데이터 기반 학습 분석",
            "개별 학습 계획 수립"
        ]
        q2_default = responses.get("Q2", q2_options[0])
        if q2_default not in q2_options:
            q2_default = q2_options[0]
        q2 = st.radio(
            "Q2. 학업 성과를 높이기 위해 가장 중요한 방법은 무엇이라고 생각하십니까?",
            q2_options,
            index=q2_options.index(q2_default)
        )
    else:
        q2 = "N/A"
    responses["Q2"] = q2

    # Q3 (조건에 따라 표시)
    if q1 == "학생들의 창의력과 미래 대비 능력 개발" and q2 == "학생들이 직접 문제를 탐구하는 프로젝트 제공":
        q3_options = [
            "디자인 씽킹을 활용한 문제 해결",
            "학생들이 주도적으로 프로젝트 설계",
            "AI 도구를 활용한 창의적 사고 자극"
        ]
        q3_default = responses.get("Q3", q3_options[0])
        if q3_default not in q3_options:
            q3_default = q3_options[0]
        q3 = st.radio(
            "Q3. 창의적 사고를 증진하기 위해 가장 효과적인 접근법은 무엇입니까?",
            q3_options,
            index=q3_options.index(q3_default)
        )
    elif q1 == "교사로서의 전문성 개발" and q2 == "최신 기술과 도구 학습":
        q3_options = [
            "최신 기술 트렌드 세미나 참석",
            "새로운 수업 도구 실습",
            "교사 역량 강화 워크숍 참여"
        ]
        q3_default = responses.get("Q3", q3_options[0])
        if q3_default not in q3_options:
            q3_default = q3_options[0]
        q3 = st.radio(
            "Q3. 전문성을 높이기 위한 구체적인 방법은 무엇입니까?",
            q3_options,
            index=q3_options.index(q3_default)
        )
    elif q1 == "학생들의 학업 성취 극대화" and q2 == "정기적인 피드백 제공":
        q3_options = [
            "개별 피드백 계획 수립",
            "학생 평가 데이터 활용",
            "학생 목표 설정 지원"
        ]
        q3_default = responses.get("Q3", q3_options[0])
        if q3_default not in q3_options:
            q3_default = q3_options[0]
        q3 = st.radio(
            "Q3. 피드백의 효과를 극대화하기 위한 방법은 무엇입니까?",
            q3_options,
            index=q3_options.index(q3_default)
        )
    else:
        q3 = "N/A"
    responses["Q3"] = q3

    # Q4
    q4_options = [
        "학생 중심 학습 활동",
        "정서적 유대감 형성",
        "교사 역량 강화",
        "성과 중심 학습"
    ]
    q4_default = responses.get("Q4", q4_options[0])
    if q4_default not in q4_options:
        q4_default = q4_options[0]
    q4 = st.radio(
        "Q4. 수업 방식에서 가장 중요하게 생각하는 요소는 무엇입니까?",
        q4_options,
        index=q4_options.index(q4_default)
    )
    responses["Q4"] = q4

    # Q5
    q5_options = [
        "학생들의 창의적 참여",
        "학생들의 정서적 필요",
        "교사의 전문성 발전",
        "학생들의 학업 성과"
    ]
    q5_default = responses.get("Q5", q5_options[0])
    if q5_default not in q5_options:
        q5_default = q5_options[0]
    q5 = st.radio(
        "Q5. 학습 활동을 계획할 때 가장 우선적으로 고려하는 요소는 무엇입니까?",
        q5_options,
        index=q5_options.index(q5_default)
    )
    responses["Q5"] = q5

    # 결과 도출 버튼
    if st.button("결과 보기"):
        final_result = determine_type(responses)
        st.markdown(f"### 당신의 유형은 **{final_result}**입니다!")

        # 유형별 상세 설명
        explanations = {
            "미래 대비 혁신가": """**미래 대비 혁신가**  

**주요 특징:**  
- AI, 에듀테크, 첨단 기술 활용을 통해 학생들이 미래 사회에 필요한 역량(창의성, 비판적 사고력, 문제 해결력)을 기를 수 있도록 지원  
- 프로젝트 기반 학습, 디자인 씽킹, 코딩·로봇 활용 등 혁신적인 교육방법 적극 도입  

**강점:**  
- 급변하는 교육 환경에 빠르게 대응  
- 학생들의 장기적 성장과 미래 대비 능력 강화  

**약점:**  
- 단기적인 성취나 현재 커리큘럼의 요구 사항을 다소 간과할 수 있음  
- 새로운 기술 및 시도에 집중하는 동안 기본 학습 역량 강화에 소홀할 가능성  

**추천 도구/접근법:**  
- 로봇 키트, 프로그래밍 교육 플랫폼, AI 실험도구(Teachable Machine 등)  
- 디자인 씽킹 워크숍, 메이커스페이스 프로젝트  
""",

            "행복 중심 학습자": """**행복 중심 학습자**  

**주요 특징:**  
- 학생들의 정서적 안정, 심리적 행복, 관계 형성을 우선으로 고려  
- 공감, 협력, 소통을 강조하는 학습 환경 조성  
- 학생들이 학습 과정 자체를 즐기고 만족감을 느끼도록 돕는 교육 철학 지향

**강점:**  
- 긍정적이고 안정된 교실 분위기 조성  
- 학생들의 내적 동기 강화 및 학습 만족도 상승  
- 장기적 관점에서 학생들의 자존감 및 학습 지속성 강화

**약점:**  
- 학업 성취도나 명확한 성과 지표에 상대적으로 덜 집중할 수 있음  
- 학습 목표나 성과 관리 측면에서 부족함을 느낄 가능성

**추천 도구/접근법:**  
- 감정 카드, 협동형 보드게임, 감정일기, 음악·미술 치료 활동  
- Padlet, Jamboard 등 협업툴 활용해 학생들 간 관계 형성 지원  
""",

            "전문성 개발 탐구자": """**전문성 개발 탐구자**  

**주요 특징:**  
- 교사의 전문성 강화와 자기 발전에 초점을 두는 유형  
- 최신 교육 연구, 교수법, 교육기술 트렌드 학습을 통해 전문 역량을 지속적으로 향상  
- 동료 교사와의 협력 연구, 세미나·워크숍 참가 등 학습 공동체 활동에 적극적

**강점:**  
- 교사의 역량 강화로 수업 품질 향상  
- 새로운 교수법 및 기술을 능숙하게 습득하고 적용  
- 학생들에게 더 나은 교육 경험 제공

**약점:**  
- 학생 개별 요구나 정서적 요소보다 교사 자신의 발전 과정에 집중할 우려  
- 너무 많은 전문성 개발 활동이 실질적 수업 적용에 비해 과도할 수 있음

**추천 도구/접근법:**  
- KERIS, EBS 연수원 등 국내외 교육자료 및 온라인 직무연수 활용  
- 전문서적, 학술논문, 교육 관련 컨퍼런스  
- 협업 플랫폼(Notion, Google Workspace)로 동료와 지식·정보 공유  
""",

            "성과 지향 학습자": """**성과 지향 학습자**  

**주요 특징:**  
- 명확한 학습 목표 설정 및 성취도 향상을 핵심 가치로 삼는 유형  
- 데이터 기반 분석, 정기적 피드백, 평가 도구를 통해 학습 효율 극대화  
- 학업 성취도나 시험 성적 등 정량적 지표를 중요하게 다룸

**강점:**  
- 학습 효과성 및 효율성 극대화  
- 구체적인 성과물을 기반으로 한 명확한 목표 관리  
- 학생들의 단기적 성취 향상에 유리

**약점:**  
- 정서적 측면이나 창의적 경험 등 측정하기 어려운 가치를 간과할 수 있음  
- 지나친 성과 중심적 접근으로 인해 학생들의 학습 흥미와 즐거움을 해칠 가능성

**추천 도구/접근법:**  
- Google Forms, Class123, LMS 플랫폼 등 평가 및 피드백 관리 도구  
- 데이터 시각화 툴(Metabase, Tableau Public) 활용한 학습현황 분석  
- 주기적인 피드백 시스템 구축 및 학생 개별 성과 모니터링  
"""
        }

        st.info(explanations.get(final_result, "결과 설명이 없습니다."))
        # 다시하기 버튼 추가
if st.button("다시하기"):
   st.session_state.clear()
   st.experimental_rerun()

if __name__ == "__main__":
    main()
