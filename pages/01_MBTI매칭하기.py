import streamlit as st

# MBTI 유형별 특성 및 궁합 정보
mbti_info = {
    "INTJ": {
        "특성": "📚 전략적 사고와 뛰어난 계획 수립 능력을 갖춘 당신은 언제나 목표를 향해 나아갑니다. 독립적이고 창의적인 해결사로서, 복잡한 문제도 척척 해결해내는 타입이에요! 💡",
        "잘_맞는_유형": "ENFP 🎈",
        "잘_안_맞는_유형": "ESFP 🌟"
    },
    "ENFP": {
        "특성": "🎨 상상력이 풍부하고 열정적인 당신은 언제나 새로운 아이디어로 가득 차 있어요! 사람들에게 영감을 주고, 항상 긍정적인 에너지를 전파하는 매력적인 타입입니다! ⚡",
        "잘_맞는_유형": "INFJ 🌱",
        "잘_안_맞는_유형": "ISTJ 🛠"
    },
    # 추가적인 MBTI 유형들...
}

st.title('🎉 나의 MBTI 특성과 궁합 알아보기! 🎉')

# MBTI 입력받기
mbti_type = st.text_input('당신의 MBTI 유형을 입력해주세요 (예: INTJ): ')

# MBTI 유형이 유효한 경우 정보 출력
if mbti_type in mbti_info:
    st.write(f"**{mbti_type}의 특성**: {mbti_info[mbti_type]['특성']}")
    st.write(f"💖 **잘 맞는 유형**: {mbti_info[mbti_type]['잘_맞는_유형']}")
    st.write(f"💔 **잘 안 맞는 유형**: {mbti_info[mbti_type]['잘_안_맞는_유형']}")
else:
    st.write("😅 유효한 MBTI 유형을 입력해주세요. (예: INTJ)")

st.write("🔍 **기억하세요!** MBTI는 재미를 위한 것이며, 궁합은 절대적이지 않아요. 모든 사람은 고유한 매력이 있습니다! 💫")
