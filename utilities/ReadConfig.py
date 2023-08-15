import configparser

config = configparser.RawConfigParser()

filepath = "D:\Python Project\sauceDemo\configuration\config.ini"
config.read(filepath)
class Readconfig:
    @staticmethod
    def GetUserName():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data','password')
        return password