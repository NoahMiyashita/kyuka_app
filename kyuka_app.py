import streamlit as st
import datetime
import random

# タイトル
st.title("🌸 九華リーディング - 宇宙と繋がる魂のナビゲーション")

# 入力フォーム
name = st.text_input("🌟 お名前（ニックネーム可）")

birth_date = st.date_input(
    "生年月日を選択",
    value=datetime.date(1990, 1, 1),
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date(2100, 12, 31)
)
blood_type = st.selectbox("🩸 血液型を選んでください", ["A", "B", "O", "AB"])
element = st.selectbox("🌸 あなたが惹かれる華のエレメント", ["風華", "火華", "水華", "土華", "空華", "雷華", "光華", "闇華", "霊華"])
question = st.text_area("🔮 今、知りたいこと・テーマ（任意）")

# ボタン処理
if st.button("✨ 九華を読み解く ✨") and name:
    # ダミーデータ（本実装では命式や月齢等を用いて出力）
    lucky_color = random.choice(["ローズゴールド", "セージグリーン", "アイスブルー", "ミッドナイトネイビー"])
    lucky_food = random.choice(["酵素たっぷりスムージー", "塩麹入りスープ", "黒ごま団子", "月見だんご"])
    lucky_direction = random.choice(["東北東", "南南西", "西", "北東"])
    lucky_time = random.choice(["午前9時", "午後3時", "満月の夜", "新月前の静寂の時間"])
    past_life = random.choice(["古代エジプトの神官", "ケルトの薬草師", "江戸の芸者", "大航海時代の星読み師"])
    future_life = random.choice(["星間航行のチャネラー", "植物と対話する地球守護者", "次元間ヒーラー"])
    
    # 結果表示
    st.markdown(f"""
    ### 🌟 {name} さんの 九華リーディング結果 🌟

    - 🗓 生年月日: `{birth_date}`
    - 🩸 血液型: `{blood_type}`
    - 🌸 九華エレメント: **{element}**

    #### 🧭 あなたの魂の現在地：
    > 今は **「{element}」** の影響が強く、内なる変容と覚醒のサイクルにいます。

    #### 🌓 月のリズムとあなたの調子：
    - 今回の月相：`満ちゆく月`
    - 調子が上がるタイミング：**月が満ちる直前と新月明け**

    #### 🎨 ラッキーアイテム
    - カラー：`{lucky_color}`
    - フード：`{lucky_food}`
    - 吉方位：`{lucky_direction}`
    - パワーアクションの時間帯：`{lucky_time}`

    #### 🛕 あなたとご縁のある参拝行動
    - 方角：{lucky_direction}
    - 最適時期：次の満月前後
    - 推奨：白または淡紫の装いで、香りあるもの（例：お守り袋にラベンダー）を携帯

    #### 💖 スピリチュアル開花アドバイス
    - 今始めると良いこと：**香りの習い事・自己表現の場作り**
    - 魅力UP行動：**足元からのエネルギーケア（塩浴・足湯）**

    #### 🌌 あなたの魂の軌跡
    - 前世の姿：{past_life}
    - 来世の片鱗：{future_life}

    ---

    🔮 ご質問：「{question if question else '特になし'}」
    > 今のあなたに必要なのは「**余白**」と「**感性の拡張**」。五感を整えながら、宇宙の流れを感じる静けさの時間を持ってください。
    """)
    
    st.caption("©️ 2025 九華リーディング - Produced by 宮下ノア")

