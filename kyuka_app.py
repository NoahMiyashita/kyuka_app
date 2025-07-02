import streamlit as st
import datetime

# ==== 魂華アサインロジック ====
def get_zodiac_sign(month, day):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return '牡羊座'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return '牡牛座'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return '双子座'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return '蟹座'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return '獅子座'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return '乙女座'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return '天秤座'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return '蠍座'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return '射手座'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return '山羊座'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return '水瓶座'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return '魚座'

def assign_konka(zodiac):
    # 星座から九華エレメントへ割り当て
    mapping = {
        '牡羊座': '焔華（えんか / Ignis）',
        '牡牛座': '根華（こんか / Terra）',
        '双子座': '風華（ふうか / Aeris）',
        '蟹座': '澄華（ちょうか / Aqua）',
        '獅子座': '光華（こうか / Lucis）',
        '乙女座': '命華（みょうか / Vitae）',
        '天秤座': '風華（ふうか / Aeris）',
        '蠍座': '闇華（あんか / Umbra）',
        '射手座': '魂華（こんか / Konka）',
        '山羊座': '根華（こんか / Terra）',
        '水瓶座': '空華（くうか / Caelum）',
        '魚座': '澄華（ちょうか / Aqua）',
    }
    return mapping.get(zodiac, "魂華（こんか / Konka）")

# ==== UI ====
st.title("🌸 九華リーディング - Neo Cosmique Ver.")
st.caption("Produced by 宮下ノア")

st.markdown("あなたの魂華（こんか）を読み解き、人生の羅針盤を手に入れましょう。")

name = st.text_input("お名前（ニックネーム可）")
birth_date = st.date_input("生年月日を選択", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())

question = st.text_area("🔮 今、知りたいこと・テーマ（任意）")

if st.button("✨ リーディングを始める") and name and birth_date:
    month = birth_date.month
    day = birth_date.day
    zodiac = get_zodiac_sign(month, day)
    konkah = assign_konka(zodiac)

    st.markdown(f"""
    ---
    ## 🌟 {name} さんの 九華リーディング結果 🌟

    - 🗓 生年月日: `{birth_date}`
    - 🔭 太陽星座：**{zodiac}**
    - 🌸 割り当てられた魂華：**{konkah}**

    ---
    ### 🔮 リーディングメッセージ

    > あなたの魂は今、**{konkah}**の影響下にあります。
    > この時期は、自然体のまま「{konkah}」の質を生かす行動にシフトすると運が開けます。

    - ラッキーアクション：内なる直感の声に従う
    - サポートアイテム：ヒーリングストーン / 月光浴
    - 魅力UP：香り・音・色の感覚を日常に取り入れて

    ---
    🪐 ご質問：「{question if question else '特になし'}」
    > 宇宙からのメッセージを静かに受け取る時間を、意識的に取ってください。

    """)
