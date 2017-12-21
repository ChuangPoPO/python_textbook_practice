
# coding: utf-8

# In[2]:


from guess import finger_guess
def run():
    computer = finger_guess()
    my = int(input('請輸入1、2、3(【1剪刀】、【2石頭】、【3布】)：'))
    print('電腦出', computer)
    if my == 1 :
        if computer == '剪刀':
            print('平手')
        elif computer == '石頭':
            print('電腦獲勝')
        else :
            print('你贏了!!!')
    elif my == 2:
        if computer == '石頭':
            print('平手')
        elif computer == '布':
            print('電腦獲勝')
        else :
            print('你贏了!!!')
    else :
        if computer == '布':
            print('平手')
        elif computer == '剪刀':
            print('電腦獲勝')
        else :
            print('你贏了!!!')
    
if __name__ == '__main__':
    for i in range(5):
        run()
else :
    print('我不是獨立執行的 python 程式')

