import broadscope_bailian
import time
import random


class ConsoleColors:
    WHITE = '\033[97m'  # 使用 '\033[97m' 表示白色
    RESET = '\033[0m'


# 配置区域
access_key_id = ""
access_key_secret = ""
agent_key = ""
app_id = ""
session_id = random.randint(1, 999999999)

# 设置全局的 api_key
client = broadscope_bailian.AccessTokenClient(access_key_id=access_key_id, access_key_secret=access_key_secret, agent_key=agent_key)
broadscope_bailian.api_key = client.get_token()


def call_api(prompt):
    """
    调用 API 并返回文本结果
    """
    response = broadscope_bailian.Completions().call(app_id=app_id, prompt=prompt, session_id=session_id)
    return response.get('Data', {}).get('Text', None)

def main():
    while True:
        prompt = input("please enter（请您输入）:").strip()
        if not prompt:
            print(ConsoleColors.WHITE + "Prompt cannot be empty（提示语不能为空）：" + ConsoleColors.RESET)
        else:
            text_result = call_api(prompt)
            for char in text_result:
                print(ConsoleColors.WHITE + char + ConsoleColors.RESET, end='', flush=True)
                time.sleep(0.05)  #采用流式输出
            print()  # 换行

if __name__ == "__main__":
    main()