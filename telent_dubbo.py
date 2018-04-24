import dubbo_telnet
def coondoubble_data(Host,Port):
    try:
        # 初始化dubbo对象
        conn = dubbo_telnet.connect(Host, Port)
        # 设置telnet连接超时时间
        conn.set_connect_timeout(10)
        # 设置dubbo服务返回响应的编码
        conn.set_encoding('gbk')
        interface = "com.zrj.pay.trade.api.QueryTradeService"
        method = "tradeDetailQuery"
        param = "{'message': 'HelloWorld'}"
        print(conn.invoke(interface, method, param))
        command = 'invoke com.ustc.demo.provider.DemoService.DemoServiceMain("dsdadasd")'
        return  conn.do(command)
    except Exception as e:
        return  e
if __name__=="__main__":
    Host = '127.0.0.1'  # Doubble服务器IP
    Port = 20881  # Doubble服务端口
    interface = 'com.ustc.demo.provider.DemoService'  # 接口
    method = 'DemoServiceMain'  # 方法
    param = 'HelloWorld'  # 参数
    data=coondoubble_data(Host,Port)
    print(data)