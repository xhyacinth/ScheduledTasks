import os
from pathlib import Path
from cozepy import COZE_CN_BASE_URL, Coze, TokenAuth, Message
from datetime import datetime

def main():
    # 从环境变量获取配置
    coze_token = 'pat_8jMuWFBh5HLuLs9r3JYH9TlXoy3890qih2VG9klHhCp2LZzVdOqXQTj5T6OudtZk'
    bot_id = '7638805151256084523'
    
    if not coze_token:
        raise Exception("COZE_TOKEN 未配置")
    
    # 初始化客户端
    coze = Coze(
        auth=TokenAuth(token=coze_token),
        base_url=COZE_CN_BASE_URL
    )

    response = None
    
    # 任务1：车场心跳
    # response = coze.chat.create(
    #     bot_id=bot_id,
    #     user_id="github-actions-scheduler",
    #     additional_messages=[
    #         Message.build_user_question_text("请执行定时任务：触发车场信息心跳消息")
    #     ]
    # )
    
    # 方式2：每日反馈
    if 12 <= datetime.now().hour <= 14:
        response = coze.chat.create(
            bot_id=bot_id,
            user_id="github-actions-scheduler",
            additional_messages=[
                Message.build_user_question_text("请执行定时任务：提醒每日反馈消息")
            ]
        )
    
    print(f"任务执行结果:\n{response}")
    
if __name__ == '__main__':
    main()
