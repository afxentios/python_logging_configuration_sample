# Dictionary based on "Configuration dictionary schema" which can passed to dictConfig()
config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basic': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'filters': {
        'info_special': {
            '()': 'config_logger.filters.SameLevelFilter',
            'level': 'logging.INFO',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
            'level': 'DEBUG',
            'stream': 'ext://sys.stdout'
        },
        'info_file_handler': {
            'class': 'logging.RotatingFileHandler',
            'formatter': 'basic',
            'level': 'INFO',
            'filters': ['info_special'],
            'filename': 'info.log',
            'maxBytes': '10485760',
            'backupCount': '20',
            'encoding': 'utf8'
        },
        'error_file_handler': {
            'class': 'logging.RotatingFileHandler',
            'formatter': 'basic',
            'level': 'ERROR',
            'filename': 'error.log',
            'maxBytes': '10485760',
            'backupCount': '20',
            'encoding': 'utf8'
        },
        'warning_file_handler': {
            'class': 'logging.RotatingFileHandler',
            'formatter': 'basic',
            'level': 'WARNING',
            'filename': 'warning.log',
            'maxBytes': '5242880',
            'backupCount': '10',
            'encoding': 'utf8'
        },
        'critical_file_handler': {
            'class': 'logging.RotatingFileHandler',
            'formatter': 'basic',
            'level': 'CRITICAL',
            'filename': 'critical.log',
            'maxBytes': '5242880',
            'backupCount': '10',
            'encoding': 'utf8'
        },
    },
    'loggers': {
        'my_logger': {
            'level': 'ERROR',
            'handlers': ['error_file_handler', 'warning_file_handler'],
            'propagate': False
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console', 'info_file_handler', 'error_file_handler']
    }
}
