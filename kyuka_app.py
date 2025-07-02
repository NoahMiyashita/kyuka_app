import streamlit as st
import datetime
import random

# =========================
# 魂華（こんか）アサインロジック
# =========================
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
    return mapping.get(zodiac, '魂華（こんか / Konka）')

# =========================
# Streamlit アプリ本体
# =========================
st.title("🌸 九華リーディング")
st.caption("Produced by 宮下ノア")

name = st.text_input("🧚 お名前（ニックネーム可）")
birth_date = st.date_input("🎂 生年月日を選択", min_value=datetime.date(1900, 1, 1))
question = st.text_area("🔮 今、知りたいこと・テーマ（任意）")

if st.button("✨ リーディングを始める") and name and birth_date:
    month, day = birth_date.month, birth_date.day
    zodiac = get_zodiac_sign(month, day)
    konkah = assign_konka(zodiac)

    # ランダム生成エリア
    lucky_color = random.choice(["ローズゴールド", "セージグリーン", "アイスブルー", "ミッドナイトネイビー"])
    lucky_food = random.choice(["酵素たっぷりスムージー", "塩麹入りスープ", "黒ごま団子", "月見だんご"])
    lucky_direction = random.choice(["東北東", "南南西", "西", "北東"])
    moon_phase = random.choice(["新月", "上弦の月", "満月", "下弦の月"])
    best_transfer_time = random.choice(["来月中旬", "次の満月後", "秋分前後", "今すぐ準備を始めて◎"])
    lucky_underwear = random.choice(["白×レース（柔らかな守り）", "赤系（情熱UP）", "ネイビー（集中力UP）"])
    lucky_pet_style = random.choice(["猫のような自由な付き合い", "犬のような忠誠関係", "小動物のような癒し系交流"])
    lucky_plant_attunement = random.choice(["毎朝ハーブに語りかける", "観葉植物とリズムを合わせる", "花を飾り水を替える瞑想"])
    lucky_shrine = random.choice(["出雲大社（縁結び）", "伊勢神宮（内面の浄化）", "日光東照宮（勝負運UP）"])
    shrine_time = random.choice(["午前7〜9時（清浄）", "夕方4時前後（静寂）"])
    shrine_dress = random.choice(["白 or ラベンダー色の服", "和装 + 木の小物"])

    st.markdown(f"""
    ---
    ## 🌟 {name} さんの 九華リーディング結果 🌟

    - 🗓 生年月日: `{birth_date}`
    - 🔭 太陽星座：**{zodiac}**
    - 🌸 割り当てられた魂華：**{konkah}**
    - 🌕 現在の月相：**{moon_phase}**

    ---
    ### 🔮 開運ガイドライン

    - 💼 **転職に最適な時期**：{best_transfer_time}
    - 💎 ラッキーカラー：{lucky_color}
    - 🍽️ ラッキーフード：{lucky_food}
    - 📍 吉方位：{lucky_direction}
    - 👙 下着のおすすめ：{lucky_underwear}

    ---
    ### 🛕 参拝アドバイス

    - ご縁ある神社：**{lucky_shrine}**
    - 最適時期：**次の {moon_phase} 前後**
    - 推奨時間帯：{shrine_time}
    - 服装＆持ち物：{shrine_dress}（香りあるアイテム推奨）

    ---
    ### 🌱 自然との関係性

    - 🌿 植物との付き合い方：{lucky_plant_attunement}
    - 🐾 動物との距離感：{lucky_pet_style}

    ---
    ### 💖 恋愛・魅力開花

    - 魅力UP行動：**香り・音・色**を意識して生活に取り入れて
    - 勝負の日の行動：**直感に従い、大胆に1歩を踏み出す**

    ---
    ### 💰 金運アドバイス

    - 今は「{random.choice(['お金の知識を学ぶのに最適な時期', '直感的なお金の使い方に注意する時期'])}」です。
    - 学ぶと良いジャンル：**投資・価値観整理・豊かさマインド**

    ---
    ### 🪐 宇宙からのメッセージ

    ご質問：「{question if question else '特になし'}」
    > 今のあなたに必要なのは「**余白**」と「**感性の拡張**」。静かに宇宙のサインを受け取る時間を確保しましょう。

    """)

    st.caption("©️ 2025 九華リーディング - Neo Cosmique Edition")
