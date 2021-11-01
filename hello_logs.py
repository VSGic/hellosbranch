import logging
import datetime

def make_log_hello(mess, type_mess):

	log_dates = datetime.datetime.now()
	post_file = 'log' + log_dates.strftime("-%Y-%m-%d") + '.log'
	logfile = post_file
	hello_log = logging.getLogger("Hello logs")
	hello_log.setLevel(logging.INFO)
	Hello_handler = logging.FileHandler(logfile)
	hello_formater = logging.Formatter('[%(asctime)s] : [%(levelname)s] : [%(lineno)s]  : [%(message)s]')
	Hello_handler.setFormatter(hello_formater)
	hello_log.addHandler(Hello_handler)
	
	if type_mess == "info":
		hello_log.info(mess)
	else: 
	# type_mess == "error":
		hello_log.error(mess)

	if (hello_log.hasHandlers()):
		hello_log.handlers.clear()
