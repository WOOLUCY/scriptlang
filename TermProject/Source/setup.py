'''
setup.py
distutils 모듈을 사용해 배포 파일을 생성하는 파일
'''
from distutils.core import setup

setup(
    name='WhereTheHospital',
    version='1.0',

    py_modules=['book_mark', 'gmail_send', 'graph', 'link', 'map', 'server', 'telegram_bot', 'telegram', 'where_hospital'],

    packages=['image', 'font'],
    package_data={
        'image': ['*.png', '*.html','*.jpg','*.gif'],
        'font': ['*.ttf']},
)