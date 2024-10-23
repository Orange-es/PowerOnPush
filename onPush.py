import datetime

import cv2
import requests
import  uuid
# 拍照片并存储
def capture_image_from_camera():
    # 打开默认的摄像头（通常是笔记本内置的摄像头，索引为0）
    cap = cv2.VideoCapture(0)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("无法打开摄像头")
        return None

    print("摄像头已打开，请等待拍照...")
    
    # 丢弃初始的几帧以确保捕获到的是最新的图像  
    for _ in range(5):  # 可以根据需要调整丢弃的帧数  
        ret, _ = cap.read()  
        if not ret:  
            print("无法读取初始帧")  
            cap.release()  
            return None  

    # 读取一帧图像
    ret, frame = cap.read()

    # 检查是否成功读取到图像
    if not ret:
        print("无法读取图像")
        cap.release()
        return
       
     # 释放摄像头
    cap.release()

    # 获取当前日期和时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 设置文本属性
    font = cv2.FONT_HERSHEY_SIMPLEX  # 字体
    font_scale = 1  # 字体大小
    font_thickness = 2  # 字体粗细
    text_color = (255, 255, 255)  # 字体颜色（白色）
    text_size = cv2.getTextSize(current_time, font, font_scale, font_thickness)[0]  # 获取文本大小

    # 计算文本位置（右下角）
    text_x = frame.shape[1] - text_size[0] - 10  # 减去文本宽度和额外的间距
    text_y = frame.shape[0] - text_size[1] - 10  # 减去文本高度和额外的间距

    # 在图像上绘制文本
    cv2.putText(frame, current_time, (text_x, text_y), font, font_scale, text_color, font_thickness, cv2.LINE_AA)

    # 使用uuid
    unique_id = uuid.uuid4()

    # 定义保存图像的路径和文件名
    image_path = str(unique_id)+".jpg"
    localImage_Path = 'G:\\Pycharm\\PythonProject\\compareData\\PowerOnPush\\' + image_path
    

    # 保存图像
    cv2.imwrite(localImage_Path, frame)
    print(f"图像已保存到 {image_path}")


    return image_path

    # 显示图像（可选）
    # cv2.imshow("Captured Image", frame)
    # cv2.waitKey(0)  # 等待按键按下
    # cv2.destroyAllWindows()  # 关闭所有窗口




def pushMes(title,desp):
    # 构建请求的URL，可以包含查询参数
    url = 'https://sctp775tpvpchldzraqedxxsqjobb9.push.ft07.com/send'
    params = {
        'title': title,
        'desp': desp,
        'tags': '开机、解锁进入系统'
    }

    # 发送GET请求，并传递查询参数
    response = requests.get(url, params=params)

    # 检查响应状态码
    if response.status_code == 200:
        # 读取响应内容（假设响应是JSON格式的）
        content = response.json()
        print(content)
    else:
        print(f"请求失败，状态码：{response.status_code}")

if __name__ == "__main__":
    try:
        imgPath = capture_image_from_camera()
    except:
        print("照相机出现问题了...请检查一下...")
    pushTitle = '开机、解锁进入系统'
    # 获取当前日期和时间
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pushDesp = "#### 日期：\n"+current_time+'\n#### 图片地址：\n'+imgPath
    try:
        pushMes(pushTitle,pushDesp)
    except:
        print("消息未发送...请检查一下...")