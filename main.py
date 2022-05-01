import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('My 1st App')
""""""
st.write('プログレスバーの表示')
'start!'

#プログレスバーの表示
latest_iteration =st.empty()
bar=st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)
'Done!'

#レイアウトを整える
#サイドバー追加
# condition=st.sidebar.slider('あなたの調子は',0,100,50)
# text=st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの調子は',condition,'です'
# 'あなたの趣味は',text,'です'

#2カラムレイアウト
# left_column,right_column=st.columns(2)
# button=left_column.button('右カラムに文字を表示')
# if button:
#   right_column.write('ここにカラム')

#expander
# expander=st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く')


#スライダー表示
# condition=st.slider('あなたの調子は',0,100,50)
# 'あなたの調子は',condition,'です'

#テキスト入力
# text=st.text_input(
#   'あなたの趣味を教えてください'
# )
# 'あなたの趣味は',text,'です'


#セレクトボックス
# option=st.selectbox(
#   'あなたが好きな数字を教えてください',
#   list(range(1,11))
# )
# 'あなたの好きな数字は',option,'です'


#チェックボックスによるメディアの表示可否,画像表示
# if st.checkbox('Show Image'):
#   img=Image.open('minami_sato.jpg')
#   st.image(img,caption='Name',use_column_width=True)
  

#マップ表示
# df1=pd.DataFrame(
#   np.random.rand(100,2)/[50,50]+[35.69,139.70],
#   columns=['lat','lon']
# )
# st.map(df1)

