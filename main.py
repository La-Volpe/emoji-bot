# -*- coding: utf-8 -*-
import StringIO
import json
import logging
import random
import urllib
import urllib2
#adding utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# standard app engine imports
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import webapp2

TOKEN = 'Your Bot Token'

BASE_URL = 'https://api.telegram.org/bot' + TOKEN + '/'


# ================================

class EnableStatus(ndb.Model):
    # key name: str(chat_id)
    enabled = ndb.BooleanProperty(indexed=False, default=False)


# ================================

def setEnabled(chat_id, yes):
    es = EnableStatus.get_or_insert(str(chat_id))
    es.enabled = yes
    es.put()

def getEnabled(chat_id):
    es = EnableStatus.get_by_id(str(chat_id))
    if es:
        return es.enabled
    return False


# ================================

class MeHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getMe'))))


class GetUpdatesHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'getUpdates'))))


class SetWebhookHandler(webapp2.RequestHandler):
    def get(self):
        urlfetch.set_default_fetch_deadline(60)
        url = self.request.get('url')
        if url:
            self.response.write(json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url})))))


class WebhookHandler(webapp2.RequestHandler):
    def post(self):
        urlfetch.set_default_fetch_deadline(60)
        body = json.loads(self.request.body)
        logging.info('request body:')
        logging.info(body)
        self.response.write(json.dumps(body))

        update_id = body['update_id']
        message = body['message']
        message_id = message.get('message_id')
        date = message.get('date')
        text = message.get('text')
	sticker = message.get('sticker')
        fr = message.get('from')
        chat = message['chat']
        chat_id = chat['id']

        def reply(msg=None, img=None):
            if msg:
                resp = urllib2.urlopen(BASE_URL + 'sendMessage', urllib.urlencode({
                    'chat_id': str(chat_id),
                    'text': msg.decode('utf-8'),
                    'disable_web_page_preview': 'true',
                    'reply_to_message_id': str(message_id),
                })).read()
            elif img:
                resp = multipart.post_multipart(BASE_URL + 'sendPhoto', [
                    ('chat_id', str(chat_id)),
                    ('reply_to_message_id', str(message_id)),
                ], [
                    ('photo', 'image.jpg', img),
                ])
            else:
                logging.error('no msg or img specified')
                resp = None

            logging.info('send response:')
            logging.info(resp)
	#a loop that send your message only once!
	var = 2
	if var == 2:
		if sticker:
	        	reply('من ایموجی بات هستم :) بنابراین نظری در مورد استیکر شما ندارم :)')
			var = var -1
			return

	if text.startswith('/'):			
	    if text == '/start':
		reply('بات روشن شد.لطفا برای به دست آوردن لیست اسامی ایموجی ها دستور /help رو برام بفرستید :)')
		setEnabled(chat_id, True)
	    if text == '/about':
		reply('من ایموجی بات هستم و شما میتونید اسم ایموجی مورد نظرتون رو از لیست انتخاب کنید :) برای ارتباط با سازندم هم میتونید به @farbodgame پیام بدید :)')
	    if text == '/help':
		reply('شما میتونید اسم ایموجی مورد نظر خودتونو از لیست انتخاب کنید و برام بفرستید تا من بهتون جواب بدم: پوزخند,شادی,شکلک,خندان,خنده-شیرین,خنده,چشمک,لپ-گلی,چشمک,خوش-مزه,پکر,چشم-عاشق,لبخند-مغرورانه,بی-توجه,افسرده,سردرگم,بوس-فرستادن,فریاد-ترس,متعجب,سرخ,ماسکی,کسل,گربه-عاشق,دعا,گربه-ترسان,موشک,قطار,اتوبوس,کشتی,زمین,ماه,ستاره,حلزون,مار,اسب,میمون,هشت-پا,ناامید,عرق-سرد,عصبانی,گریه,رضایت,واقع-بین,مشت,دیس-لایک,لایک,دست-زدن,روح,قلب-تیرخورده,ادم-فضایی,قلب,حاله,خنده-شیطانی,بمب,عینک-افتابی,خنثی,گیج,زبان-درازی,نگران,قهقه,تفنگ.   ترکیبی ها: خودکشی,قدم-زدن,و...')
	
        # CUSTOMIZE FROM HERE
	elif text == 'سلام'.strip():
		reply('سلام :)')
	elif text == 'خداحافط'.strip():
		reply('خداحافظ')       
	elif text == 'پوزخند'.strip():
		reply(u'\U0001f601')
	elif text == 'شادی'.strip():
		reply(u'\U0001f602')
	elif text == 'شکلک'.strip():
		reply(u'\U0001f603')
	elif text == 'خندان'.strip():
		reply(u'\U0001f604')
	elif text == 'خنده-شیرین'.strip():
		reply(u'\U0001f605')
	elif text == 'خنده'.strip():
		reply(u'\U0001f606')
	elif text == 'چشمک'.strip():
		reply(u'\U0001f609')
	elif text == 'لپ-گلی'.strip():
		reply(u'\U0001f60A')
	elif text == 'خوشمزه'.strip():
		reply(u'\U0001f60B')
	elif text == 'پکر'.strip():
		reply(u'\U0001f60C')
	elif text == 'چشم-عاشق'.strip():
		reply(u'\U0001f60D')
	elif text == 'لبخند-مغرورانه'.strip():
		reply(u'\U0001f60F')
	elif text == 'افسرده'.strip():
		reply(u'\U0001f614')
	elif text == 'بی-توجه'.strip():
		reply(u'\U0001f612')
	elif text == 'سردرگم'.strip():
		reply(u'\U0001f616')
	elif text == 'بوس-فرستادن'.strip():
		reply(u'\U0001f618')
	elif text == 'سرخ'.strip():
		reply(u'\U0001f633')
	elif text == 'فریاد-ترس'.strip():
		reply(u'\U0001f631')
	elif text == 'متعجب'.strip():
		reply(u'\U0001f632')
	elif text == 'ماسک'.strip():
		reply(u'\U0001f637')
	elif text == 'کسل'.strip():
		reply(u'\U0001f629')
	elif text == 'گربه-عاشق'.strip():
		reply(u'\U0001f63B')
	elif text == 'دعا'.strip():
		reply(u'\U0001f64F')
	elif text == 'گربه-ترسان'.strip():
		reply(u'\U0001f640')
	elif text == 'موشک'.strip():
		reply(u'\U0001f680')
	elif text == 'قطار'.strip():
		reply(u'\U0001f684')
	elif text == 'اتوبوس'.strip():
		reply(u'\U0001f68C')
	elif text == 'کشتی'.strip():
		reply(u'\U0001f6A2')
	elif text == 'زمین'.strip():
		reply(u'\U0001f30f')
	elif text == 'ماه'.strip():
		reply(u'\U0001f319')
	elif text == 'ستاره'.strip():
		reply(u'\U0001f31F')
	elif text == 'حلزون'.strip():
		reply(u'\U0001f40C')
	elif text == 'مار'.strip():
		reply(u'\U0001f40D')
	elif text == 'اسب'.strip():
		reply(u'\U0001f40E')
	elif text == 'میمون'.strip():
		reply(u'\U0001f412')
	elif text == 'هشت-پا'.strip():
		reply(u'\U0001f419')
	elif text == 'ناامید'.strip():
		reply(u'\U0001f61E')
	elif text == 'عرق-سرد'.strip():
		reply(u'\U0001f630')
	elif text == 'عصبانی'.strip():
		reply(u'\U0001f621')
	elif text == 'گریه'.strip():
		reply(u'\U0001f622')
	elif text == 'رضایت'.strip():
		reply(u'\U0001f623')
	elif text == 'واقع-بین'.strip():
		reply(u'\U0001f625')
	elif text == 'مشت'.strip():
		reply(u'\U0001f44A')
	elif text == 'دیس-لایک'.strip():
		reply(u'\U0001f44E')
	elif text == 'لایک'.strip():
		reply(u'\U0001f44D')
	elif text == 'دست-زدن'.strip():
		reply(u'\U0001f44F')
	elif text == 'روح'.strip():
		reply(u'\U0001f47B')
	elif text == 'قلب-تیرخورده'.strip():
		reply(u'\U0001f498')
	elif text == 'قلب'.strip():
		reply(u'\U0001f493')
	elif text == 'ادم-فضایی'.strip():
		reply(u'\U0001f47D')
	elif text == 'حاله'.strip():
		reply(u'\U0001f607')
	elif text == 'خنده-شیطانی'.strip():
		reply(u'\U0001f608')
	elif text == 'بمب'.strip():
		reply(u'\U0001f4A3')
	elif text == 'عینک-افتابی'.strip():
		reply(u'\U0001f60E')
	elif text == 'ترسان'.strip():
		reply(u'\U0001f628')
	elif text == 'خنثی'.strip():
		reply(u'\U0001f610')
	elif text == 'گیج'.strip():
		reply(u'\U0001f615')
	elif text == 'زبان-درازی'.strip():
		reply(u'\U0001f61B')
	elif text == 'نگران'.strip():
		reply(u'\U0001f61F')
	elif text == 'قهقه'.strip():
		reply(u'\U0001f62D')
	elif text == 'تفنگ'.strip():
		reply(u'\U0001f52B')
	elif text == 'خودکشی'.strip():
		reply(u'\U0001f610'u'\U0001f52B')
	elif text == 'قدم-زدن'.strip():
		reply(u'\U0001f60e\u2615\ufe0f\U0001f463')								
	else:
		reply('لطفا نام ایموجی بعدی مورد نظر خود را درست وارد کنید.')
				


app = webapp2.WSGIApplication([
    ('/me', MeHandler),
    ('/updates', GetUpdatesHandler),
    ('/set_webhook', SetWebhookHandler),
    ('/webhook', WebhookHandler),
], debug=True)
