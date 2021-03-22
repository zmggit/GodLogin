from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver import ActionChains


# 初始
def main():

    global bro
    bro = webdriver.Chrome()
    bro.maximize_window()
    # 不叫他检测出是机器人
    bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    bro.get("https://login.taobao.com/member/login.jhtml")
    time.sleep(1)
    # 手机号
    bro.find_element_by_name("fm-login-id").send_keys("15257175937")
    time.sleep(1)
    # 密码
    bro.find_element_by_name("fm-login-password").send_keys("zmg970208")
    time.sleep(1)
    # 获取图片并且保存
    action(bro)
    time.sleep(4)
    #getimage(bro)
    # ===================================================================================

# 验证码操作图片


def getimage(bro):

    # 将当前界面进行截图保存
    picture_url = bro.save_screenshot('taobao.png')
    try:
        # 根据xpath语法找到滑块验证码
        bro.switch_to_frame("baxia-dialog-content")
        code_img_ele = bro.find_element_by_xpath("//*[@id='nc_1__scale_text']/span")
        print("%s ：找到元素！！！" % code_img_ele)
    except BaseException as msg:
        print("%s ：没有找到元素！！！" % msg)

    location = code_img_ele.location  # 验证码图片左上角的坐标 x,y
    size = code_img_ele.size  # 验证码的标签对应的长和宽
    print(size)
    # 左上角和右下角的坐标
    rangle = (
        int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height'])
    )
    i = Image.open("./taobao.png")
    # code_img_name = './tb.png'
    # crop裁剪
    frame = i.crop(rangle)  # 得到滑块验证码图片
    # 登录
    action(bro)
    # 获取旺旺号

def action(bro):
    # 动作链
    #actions = ActionChains(bro)
    # 长按且点
    # actions.click_and_hold(code_img_ele)
    # move_by_offset(x,y) x水平方向,y竖直方向
    # perform()让动作链立即执行
    # actions.move_by_offset(300, 0).perform()
    # 通过验证码大小
    # time.sleep(0.5)
    # 释放动作链
    # actions.release()
    bro.find_element_by_xpath("//*[@id='login-form']/div[4]/button").click()  # 根据xpath语法找到登录按钮点击登录
    time.sleep(10)
    # bro.quit()  # 关闭浏览器


if __name__ == "__main__":
    main()
