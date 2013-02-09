#!/usr/bin/env python
# coding: utf-8
import web

db = web.database(dbn='mysql', db='todo', user='rkd', pw='123456')

render = web.template.render('templates/', cache=False)

web.config.debug = True

replaceList = [
('(1)', '<img src="/static/images/face/1.gif"/>'),
('(2)', '<img src="/static/images/face/2.gif"/>'),
('(3)', '<img src="/static/images/face/3.gif"/>'),
('(4)', '<img src="/static/images/face/4.gif"/>'),
('(5)', '<img src="/static/images/face/5.gif"/>'),
('(6)', '<img src="/static/images/face/6.gif"/>'),
('(7)', '<img src="/static/images/face/7.gif"/>'),
('(8)', '<img src="/static/images/face/8.gif"/>'),
('(9)', '<img src="/static/images/face/9.gif"/>'),
('(10)', '<img src="/static/images/face/10.gif"/>'),
('(11)', '<img src="/static/images/face/11.gif"/>'),
('(12)', '<img src="/static/images/face/12.gif"/>'),
('(13)', '<img src="/static/images/face/13.gif"/>'),
('(14)', '<img src="/static/images/face/14.gif"/>'),
('(15)', '<img src="/static/images/face/15.gif"/>'),
('(16)', '<img src="/static/images/face/16.gif"/>'),
('(17)', '<img src="/static/images/face/17.gif"/>'),
('(18)', '<img src="/static/images/face/18.gif"/>'),
('(19)', '<img src="/static/images/face/19.gif"/>'),
('(20)', '<img src="/static/images/face/20.gif"/>'),
('(21)', '<img src="/static/images/face/21.gif"/>'),
('(22)', '<img src="/static/images/face/22.gif"/>'),
('(23)', '<img src="/static/images/face/23.gif"/>'),
('(24)', '<img src="/static/images/face/24.gif"/>'),
('(25)', '<img src="/static/images/face/25.gif"/>'),
('(26)', '<img src="/static/images/face/26.gif"/>'),
('(27)', '<img src="/static/images/face/27.gif"/>'),
('(28)', '<img src="/static/images/face/28.gif"/>'),
('(29)', '<img src="/static/images/face/29.gif"/>'),
('(30)', '<img src="/static/images/face/30.gif"/>'),
('(31)', '<img src="/static/images/face/31.gif"/>'),
('(32)', '<img src="/static/images/face/32.gif"/>'),
('(33)', '<img src="/static/images/face/33.gif"/>'),
('(34)', '<img src="/static/images/face/34.gif"/>'),
('(35)', '<img src="/static/images/face/35.gif"/>'),
('(36)', '<img src="/static/images/face/36.gif"/>'),
('(37)', '<img src="/static/images/face/37.gif"/>'),
('(38)', '<img src="/static/images/face/38.gif"/>'),
('(39)', '<img src="/static/images/face/39.gif"/>'),
('(40)', '<img src="/static/images/face/40.gif"/>'),
('(41)', '<img src="/static/images/face/41.gif"/>'),
('(42)', '<img src="/static/images/face/42.gif"/>'),
('(43)', '<img src="/static/images/face/43.gif"/>'),
('(44)', '<img src="/static/images/face/44.gif"/>'),
('(45)', '<img src="/static/images/face/45.gif"/>'),
('(46)', '<img src="/static/images/face/46.gif"/>')
]

config = web.storage(
    email='qichangxing@gmail.com',
    site_name = 'simple-todo',
    site_desc = '',
    static = '/static',
)


web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
web.template.Template.globals['replaceList'] = replaceList
