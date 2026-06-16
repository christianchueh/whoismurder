
import google.generativeai as genai
import os
api_keys = os.getenv('DISCORD_TOKEN')


genai.configure(api_key=api_keys)

# 初始化時就定義好它是誰
ai_persona = "你是一個年輕很潮的dancer,回復的時候往往會加入一些年輕人的用語"
model = genai.GenerativeModel(
model_name='gemini-3.1-flash-lite-preview',
system_instruction=ai_persona
)




chat = model.start_chat(history=[])
while True:
  msg = input("你:")
  if msg == "q":
    break
  if msg == "遊戲1":
    response = chat.send_message("請你在心中默想1_100的一個數字來讓我猜,我猜得太大就說太大並且調整數字範圍,猜得太小就回應太小依樣條整數字範圍")
  else:
    response = chat.send_message(msg,generation_config={
    "temperature": 0.2,
    "top_p": 0.9,
    "max_output_tokens": 200,
})
  print(f"阿吉:{response.text}")
# 練習:取消下方註解看看記憶長什麼樣子
# print(f"對話筆數: {len(chat.history)}")
