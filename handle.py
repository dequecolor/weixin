# _*_ coding: utf-8 _8_
# filename: handle.py

import hashlib
import web
import reply
import receive

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "hhfhhfhhfhhf514514514514"

            list = [token, timestamp, nonce]
            list.sort()
            shal = hashlib.sha1()
            map(shal.update, list)
            hashcode = shal.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument

    def POST(self):
        try:
            webdata = web.data()
            print("Handle Post webdata is ",webdata)
            print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            #后台打日志
            print('hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            recMsg = receive.parse_xml(webdata)
            print ("isinstance Msg",isinstance(recMsg, receive.Msg))
            print (type(recMsg))
            print ("length of webdata",len(webdata))
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = 'test'
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    return replyMsg.send()
                if recMsg.MsgType == 'image':
                    mediaId = recMsg.MediaId
                    replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                    print(type(replyMsg))
                    return replyMsg.send()
                else:
                    return reply.Msg().send()
            else:
                print("暂且不处理")
                return reply.Msg().send()
        except Exception, Argument:
            return Argument
