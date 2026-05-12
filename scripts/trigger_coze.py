import os
from pathlib import Path
from cozepy import COZE_CN_BASE_URL, Coze, TokenAuth, Message

def main():
    # 从环境变量获取配置
    coze_token = os.getenv('COZE_TOKEN', 'pat_8jMuWFBh5HLuLs9r3JYH9TlXoy3890qih2VG9klHhCp2LZzVdOqXQTj5T6OudtZk')
    bot_id = os.getenv('BOT_ID', '7638805151256084523')
    
    if not coze_token:
        raise Exception("COZE_TOKEN 未配置")
    
    # 初始化客户端
    coze = Coze(
        auth=TokenAuth(token=coze_token),
        base_url=COZE_CN_BASE_URL
    )
    
    # 方式1：简单文本消息
    response = coze.chat.create(
        bot_id=bot_id,
        user_id="github-actions-scheduler",
        additional_messages=[
            Message.build_user_question("执行定时任务，请触发车场信息心跳消息")
        ]
    )
    
    result = response.messages[-1].content
    print(f"任务执行结果:\n{result}")
    
if __name__ == '__main__':
    main()
