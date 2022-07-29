class Proxy:
    def __init__(self,realSubject) -> None:
        self.realSubject = realSubject
    def do():
        raise NotImplementedError

# RemoteProxy
class SocketProxy(Proxy):
    def __init__(self,url) -> None:
        self.url = url
    def do(self,param,callBack):
        self.req(param,callBack)
    def req(self,param,callBack):
        print("encode param",param)
        print("do req ",self.url)
        callBack()
        
# VirtualProxy
class LoadImgProxy(Proxy):
    def __init__(self,imgLoader) -> None:
        self.imgLoader = imgLoader
        self.imgCache = {}

    def loadImg(self,imgName):
        if imgName not in self.imgCache:
            print("use default \n"+self.getDefaultImg())
            img = self.imgLoader.load(imgName)
            self.imgCache[imgName] = img
        print("load finish")
        print(self.imgCache[imgName])

    def getDefaultImg(self):
        return "**\n**"

class ImgLoader:
    def load(self,imgName):
        return imgName+"\n"+imgName

if __name__ == "__main__":
    socketProxy = SocketProxy("potatoo.com")
    socketProxy.do(["map@update",1],lambda:print("req succ"))

    loadImgProxy = LoadImgProxy(ImgLoader())
    loadImgProxy.loadImg("##")
    loadImgProxy.loadImg("//")
    loadImgProxy.loadImg("##")