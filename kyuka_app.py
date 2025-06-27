

import streamlit as st
import datetime

# タイトル
st.title("九華リーディング：魂の羅針盤")

# サブタイトル
st.subheader("あなたの内なる運命と使命を読み解きます")

# 入力フォーム
name = st.text_input("お名前（ニックネーム可）")

birth_date = st.date_input(
    "生年月日を選択",
    min_value=datetime.date(1900, 1, 1),
    max_value=datetime.date.today()
)


blood_type = st.selectbox("血液型を選んでください", ["A", "B", "O", "AB"])
element = st.selectbox("五大エレメントで直感に近いものは？", ["風", "火", "水", "土", "空（エーテル）"])
question = st.text_area("今、読み解きたいテーマや悩みがあれば記入してください")

# ボタンが押されたら処理開始
if st.button("九華を読み解く"):
    # 仮のロジック（ここを後でAI連携に切り替え予定）
    st.success("🌟 九華リーディング結果 🌟")
    st.markdown(f"""
    **{name}** さんのリーディング結果をお伝えします。

    - 🌕 生年月日から見た魂のリズムは `{birth_date}` 生まれ。
    - 🩸 血液型 `{blood_type}` 型のあなたは、人との関係性に独自の調和を持つタイプ。
    - 🌬 五大エレメント：**{element}** があなたの本質です。
    - 💫 現在のテーマ：「{question if question else '特に無し'}」

    ---
    🔮 **リーディングメッセージ：**
    > 今、あなたの魂は【変容】のタイミングにあります。{element}のエネルギーを意識して、深呼吸しながら日常に小さな変化を取り入れてください。
    """)

# フッター
st.caption("©️ 2025 九華リーディング by 宮下ノア")

