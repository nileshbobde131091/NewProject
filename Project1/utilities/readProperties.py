import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUser():
        username=config.get('common info','user')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password

    @staticmethod
    def getLockedUser():
        username = config.get('common info', 'lockeduser')
        return username
