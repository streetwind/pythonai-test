import yaml
import logging.config
import os
from functools import singledispatch
#配置文件读取
class ConfigYaml(object):

    _fileyaml=''
    configini={}

    def init(fileyaml='_config.yml'):
        isfile=os.path.isfile(fileyaml)
        global _fileyaml
        if isfile ==True:
            _fileyaml=fileyaml
        else:
            _fileyaml='_config.yml'
        pass
    #加载yaml配置文件
    def loadYaml():
        global configini
        with open(_fileyaml,encoding='utf-8') as f:
            configini=yaml.safe_load(f)
        pass
class logconfig(object):
    def init():
        console_format='%(asctime)s -   %(thread)d  [%(module)s.%(funcName)s]'\
        '  %(levelname)s:[%(message)s]' 
        logfile_dir=os.path.join(os.getcwd(),"log")
        logfile_name="wind.log"
        if not os.path.isdir(logfile_dir):
            os.mkdir(logfile_dir)
            pass
        logfile_path=os.path.join(logfile_dir,logfile_name)
        logconfig_dic={
            'version':1,
            'disable_existing_loggers':False,
            'formatters':{
                'console':{
                    'format':console_format
                }
            },
            'filters':{},
            'handlers':{
                'console':{
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',  # 打印到屏幕
                    'formatter': 'console'
                },
                'default':{
                    'level': 'DEBUG',
                    'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
                    'formatter': 'console',
                    'filename': logfile_path,  # 日志文件
                    'maxBytes': 1024*1024*5,  # 日志大小 5M
                    'backupCount': 5,
                    'encoding': 'utf-8'
                }
            },
            'loggers':{
                '':{
                    'handlers': ['default', 'console'],
                    'level': 'DEBUG',
                    'propagate': True,
                }
            }
        }
        logging.config.dictConfig(logconfig_dic)
        logger =logging.getLogger(__name__)
        logger.info('日志测试')
        pass

class windconfig(ConfigYaml,logconfig):
    def init():
        logconfig.init()
        ConfigYaml.init()
        ConfigYaml.loadYaml()
        pass

    def get(name):
        try:
            if isinstance(name,str):
                return configini[name]
            if isinstance(name,dict):
                return configini
        except Exception as ex:
            logge.debug(ex) 
