#!/usr/bin/python	
# Data spooler/extractor for SQL Server
import win32gui
import win32con
hwnd = win32gui.GetForegroundWindow()

import Queue
import threading
import time
#import getopt
import sys, os
from pprint import pprint
import pprint as pp
#import logging 
#import ora_pipe_tools as st
import re, types
import codecs
import imp
#import pipeline.v101.from_sqlserver as ppl1
#import pipeline.v101.to_sqlserver as ppl2

#import config.common as uargs 
import traceback
from common.v101.exceptions import RowCountError,CopyVectorError,CancelJobError
import argparse
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import win32com.client
import yaml
import Crypto
import paramiko
import zipfile
from ssh_file import  SSHConnection
import shutil
import errno
from config.include.ssh_file import  SSHConnection
#import os
#import sys
#import time
#from pprint import pprint
if sys.platform == "win32":
	import msvcrt
			
			
etl_failed=False
args={}
e=sys.exit
if_stdout=False
if if_stdout:
	#import sys
	out=sys.stdout
	sys.stdout = open('stdout_test.txt', 'w')
#print 'test'
		
"""

C:\Python27\ora_data_pipe

python csv2ora.py -g SCOTT/tiger2@XE  -a SCOTT.Persons_pipe2 -i C:\Python27\ora2ora_data_pipe\shard_0.data -o 1 -r 1  -t "|"

Scripts\pyinstaller.exe -y query_copy\dm.py --log-level DEBUG --onefile
cd C:\Python278
Scripts\pyinstaller.exe -y C:\Python27\csvextractor_1235\csvextractor.py --log-level DEBUG

Scripts\pyinstaller.exe -y C:\Users\alex_buz\Documents\GitHub\DataBuddy\csv_loader.py --log-level DEBUG

Scripts\pyinstaller.exe -y C:\Users\alex_buz\Documents\GitHub\DataBuddy\QueryCopy.py --log-level DEBUG
Scripts\pyinstaller.exe -y C:\Users\alex_buz\Documents\GitHub\DataBuddy\data-buddy.py --log-level DEBUG


csv_extractor -m 'C:\Temp\mysql\bin\' -q mysql_query.sql -j alex  -x mysql_pwd -b test -n localhost -a spool/mysql_data.dump -t "|" -o 3 -r 3 -w mysql2csv


"""
def import_module(filepath):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod
try:
	arglist=sys.argv[1:]
	#print arglist
	copy_vector=None
	#cold import
	def usage(cvarg,copy_vector):
		import __builtin__
		__builtin__.copy_vector = copy_vector
		__builtin__.cvarg = cvarg
		
		#import common.v101.config as conf
		import config.config as conf


	if not arglist:
		cvarg=None
		usage(cvarg,None)
		e(1)
	elif '-h' in arglist or '--help' in arglist:
		cvkey=None
		
		
		if '-h' in arglist:
			cvarg='-h'
			cvkey= arglist.index('-h')		
		else:
			cvarg='--help'
			cvkey= arglist.index('--help')
		if  cvarg:
			pass
		else:	
			cvkey= arglist.index('-w')
			if not cvkey:
				cvkey= arglist.index('--copy_vector')
			if cvkey:				
				(cvarg,copy_vector) = arglist[cvkey:cvkey+2]
				
		usage(cvarg,copy_vector)
		e(0)

	
	def get_copy_vector(default_vector=None):
		if default_vector:
			return default_vector
		else:
			arglist=sys.argv[1:]
			#pprint(arglist)
			#sys.exit(0)
			assert '-w' in arglist, 'Copy vector is not set [-w]'
			cvkey= arglist.index('-w')
			(cvarg,copy_vector) = arglist[cvkey:cvkey+2]
			return copy_vector
			#sys.exit(0)
	copy_vector=get_copy_vector()
	#conf.copyright()


	if 0:	
		parser = argparse.ArgumentParser(description='Datamule.')
		parser.add_argument("cmd", help=argparse.SUPPRESS, nargs="*")
		# Datamule args


		#pprint (params)

		for key,val in core.items():
			#print 'adding %s  %s\t for core' % (val['short'],key)	
			parser.add_argument(val['short'],val['long'], default=val['default'], type=val['type'],  help=val['help'])

	#print ''
	#print copy_vector

	import __builtin__
	__builtin__.copy_vector = copy_vector.upper()
	__builtin__.cvarg = '-w'
	#sys.exit(1)	
	import config.config as conf
	if 0:
		pprint (conf.dbs)
		print 'DataStore | Spooler | Loader | DbShell'
		for k,v in sorted(conf.dbs.items()):
			if k not in conf.ff:
				print v, '|',conf.dbtools['SPOOLER'][k], '|',conf.dbtools['LOADER'][k], '|',conf.dbtools['DBSHELL'][k] 
				
		e(0)
	#conf.set_args(conf.uargs)
	#print dir(conf.uargs)
	#print "','".join(set(conf.dbs.keys()))
	#sys.exit(1)	
	uargs=conf.uargs

	#conf.copyright()
	exitFlag = 0


	verbose = False
	ts= uargs.ts #datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
	#print ts
	#sys.exit(1)
	globalStatus={}
			
	startTime = time.time()
	dbs=conf.dbs 

	#print dbs
	#sys.exit(1)
	#print startTime
	expiration_dt = datetime.datetime(2020,01,01)
	now_dt = datetime.datetime.now()
	#params=conf.params
	#core=params['core']
	if now_dt>expiration_dt:
		print 'Please update %s.' % conf.appname
		sys.exit(0)


			
				
		


	#join(map(lambda x: '[%s ora2%s]' % (cvarg,x),dbs.keys()))
		#print cvarg,copy_vector

	 #str(datetime.datetime.now()).split('.')[0]





	#print copy_vector
	#(log,datadir)=conf.config_log(copy_vector)
	#conf.add_argument(log,copy_vector,parser)
	# From CSV file
	log=conf.log
	if conf.default_vector:
		log.warn('Copy vector is defaulted to %s' % conf.default_vector)
	#args = parser.parse_args()
	args=conf.args
	if not args.debug_level:
		assert args.debug_level, '--debug_level should be set to 0/1/2/3.'
		
	#print args
	#e(0)
	if hasattr(args, 'url') and args.url:
		if (hasattr(args, 'output') and args.output) and (hasattr(args, 'to_file') and args.to_file):
			args.to_file=args.output
	elif hasattr(args, 'url_list') and args.url_list:
		#print args.query_sql_dir
		assert not ( hasattr(args, 'output') and args.output), '--output cannot be set for multiple input URLs'
		ucnt=len(args.url_list.split(','))
		if args.num_of_shards<>ucnt:
			log.warn('Overriding num_of_shards (%s) to be equal number of URLs (%s).' % (args.num_of_shards, ucnt))
			args.num_of_shards=ucnt			
	elif hasattr(args, 'query_sql_dir') and args.query_sql_dir:
		#print args.query_sql_dir
		qcnt=len(os.listdir(args.query_sql_dir))
		if args.num_of_shards<>qcnt:
			log.warn('Overriding num_of_shards (%s) to be equal number of queries (%s).' % (args.num_of_shards, qcnt))
			args.num_of_shards=qcnt
	elif hasattr(args, 'from_partition_list') and args.from_partition_list:
		#print args.query_sql_dir
		pcnt=len(args.from_partition_list.split(','))
		if args.num_of_shards<>pcnt:
			log.warn('Overriding num_of_shards (%s) to be equal number of partitions (%s).' % (args.num_of_shards, pcnt))
			args.num_of_shards=pcnt
	elif hasattr(args, 'from_table_list') and args.from_table_list:
		#print args.query_sql_dir
		tcnt=len(args.from_table_list.split(','))
		if args.num_of_shards<>tcnt:
			log.warn('Overriding num_of_shards (%s) to be equal number of tables (%s).' % (args.num_of_shards, tcnt))
			args.num_of_shards=tcnt
	elif hasattr(args, 'from_sub_partition_list') and args.from_sub_partition_list:
		spcnt=len(args.from_sub_partition_list.split(','))
		if args.num_of_shards<>spcnt:
			log.warn('Overriding num_of_shards (%s) to be equal number of subpartitions (%s).' % (args.num_of_shards, spcnt))
			args.num_of_shards=spcnt	
			
	if 0:
		if hasattr(args, 'input_dirs') and args.input_dirs:
			qcnt=len(os.listdir(args.input_dir))
			if args.num_of_shards<>qcnt:
				log.warn('Overriding num_of_shards (%s) to be equal number of input CSV files (%s).' % (args.num_of_shards, qcnt))
				args.num_of_shards=qcnt
	db_from,db_to = copy_vector.split(conf._to)
	
	#	print copy_vector
	#	db_from,db_to = copy_vector.split('2')
	#e(0)
	#copy_vector=conf.copy_vector
	#sys.exit(1)
	datadir=conf.datadir
	#(pool_size, num_of_shards) = (args.pool_size, args.num_of_shards)
	assert args.pool_size, 'pool_size is not set.'
	assert args.num_of_shards, 'num_of_shards is not set.'
	#pprint(dir(args))
	ff=conf.ff
	dbs=conf.dbs
	(source,target) = copy_vector.split(conf._to)
	#print args.num_of_shards
	if hasattr(args, 'to_file') and args.to_file :
		assert args.num_of_shards<2, 'Cannot export to file if num_of_shards>1\n Use "-D" (-to_dir) instead '
		if 0:
			outd = os.path.dirname(args.to_file)
			outf = os.path.basename(args.to_file)

			if not outd:
				outd= os.path.dirname(os.path.realpath(__file__))
			else:
				if not os.path.isdir(outd):
					os.makedirs(outd)
			args.to_file = os.path.join(outd,outf)
	#print args.to_file
	#e(0)
	#sys.exit(0)
	#print target.upper() 
		
	if source.upper() in ff:
		if target.upper() in 'MYSQL':
			# only serial load
			if args.pool_size>1 or args.num_of_shards>1:
				log.warn('Forcing serial load in MySQL.')
				args.pool_size=1
				args.num_of_shards=1
		from template.v101.load_from_file import load_from_file as etl_tmpl
		#from  template.v101.load_from_csv import load_from_csv as etl_tmpl
	elif target.upper() in ff:
		from template.v101.spool_to_file import spool_to_file as etl_tmpl
	elif target.upper() in dbs and source.upper() in dbs:
		from  template.v101.spool_and_load import spool_and_load as etl_tmpl
	else:
		#log.error('Unsupported copy vector %s.' % copy_vector)
		raise CopyVectorError(copy_vector)

	#e(0)

	#python  datamule.py -w ora11g2csv -o 1 -r 1 -t "|" -c SCOTT.Timestamp_test_from -f SCOTT/tiger2@orcl -e "YYYY/MM/DD" -m "YYYY-MM-DD-HH24.MI.SS.FF" -O "YYYY-MM-DD-HH24:MI:SS.FF" -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"	

	etl = etl_tmpl(log,datadir,conf)
	etl.print_copy_details()
	#print etl
	#e(0)

	
	if 1:
		var = raw_input("Are you sure you want to proceed?(y/n): ")
		#print 'you entered:'
		#pprint(var)
		#time.sleep(1)
		
		if var.upper() not in ('Y','N','YES','NO'):
			
			log.info('Exiting...')
			#time.sleep(1)
			e(0)
			raise CancelJobError(copy_vector)
		if var.upper() in ('N','NO'):
			log.info('Exiting...')
			raise CancelJobError(copy_vector)
	#print 'test'
	#print dir(etl)
	#e(0)
	print ''
	if args.truncate_target:		
		etl.truncate_target()
	(payload,globalStatus)= etl.set_payload()
	#pprint(payload)
	#pprint(globalStatus)
	#print 4
	#sys.exit(0)
	#e(0)	
	if hasattr(args, 'job_pre_etl') and args.job_pre_etl:
		#print 'job_pre_etl'
		#print args.job_pre_etl
		etl_path=os.path.realpath(args.job_pre_etl) 
		assert os.path.isfile(etl_path), '"job_pre_etl" file does not exists\n%s' % etl_path
		import __builtin__
		__builtin__.conf = conf
		pre_etl=import_module(etl_path)
		if hasattr(pre_etl, 'main'):
			#if hasattr(pre_etl, 'main') and pre_etl.main
			pre_etl.main(log,etl)
		else:
		#	pass
			log.warn('JOB-PRE-ETL doesn''t have main() method')
		
	class myThread (threading.Thread):
		def __init__(self, threadID, name, q):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.q = q
		def run(self):
			log.info( "Starting " + self.name)
			process_data(self.name,self.threadID, self.q)
			log.info( "Exiting " + self.name)
		
	def process_data(threadName, threadID, q):
		global globalStatus
		while not exitFlag:
			#print 'pre-aquire'
			queueLock.acquire()
			if not workQueue.empty():
				pld = q.get()
				queueLock.release()
				log.info( "%s processing %s" % (threadName, pld[0]) )
				shard_id=int(pld[0].split('-')[1])
				pprint(pld)
				print 'pd', shard_id
				#e(0)
				if 1:
					(out,status,ins_cnt)=etl.execute(log,pld,ts)
				else:
					try:
						(out,status,ins_cnt)=etl.execute(log,pld,ts)
						#pprint((out,status,ins_cnt))
					except KeyboardInterrupt:
						raise
					except:
						log.error('Error')
						if sys.exc_info()[1]:
							print '#'*60
							print '#'*60						
							print sys.exc_info()[1]
							print '#'*60
							print '#'*60
						#print sys.exc_info()
						(out,status,ins_cnt)=(None, -1,-1)
					if 0:
						try:
							pass
						except WindowsError, err:
							log.error(err)
							(out,status,ins_cnt)=(None, -1,-1)
						except RowCountError,err:
							log.error(err)
							(out,status,ins_cnt)=(None, -1,-1)
						except CopyVectorError,err:
							log.error(err)
							(out,status,ins_cnt)=(None, -1,-1)

					

				#if not ins_cnt>-1:
				#	(out,status,ins_cnt)=(out,-1,-1)
				#status=0
				#print 'INSERTED:' ,ins_cnt
				globalStatus[shard_id]=(status,out,int(ins_cnt))
				if int(args.debug_level):
					print threadName,globalStatus[shard_id]
				log.info( "%s exit status %d" % (threadName,globalStatus[shard_id][0] ))
			else:
				#print 'q empty'
				queueLock.release()

	#Create pool

	threadList=[]

	for i in range(args.pool_size):
		#print 'append thread %d' % i
		threadList.append("Thread-%d" % i)

	#e(0)		
	queueLock = threading.Lock()
	workQueue = Queue.Queue(args.num_of_shards)
	threads = []
	threadID = 1

	# Create new threads
	for tName in threadList:
		thread = myThread(threadID, tName, workQueue)
		thread.start()
		threads.append(thread)
		threadID += 1

	# Fill the queue
	queueLock.acquire()
	for word in payload:
		#print 'loop'
		#pprint( word)
		workQueue.put(word)
	queueLock.release()

	# Wait for queue to empty
	while not workQueue.empty():
		pass

	# Notify threads it's time to exit
	exitFlag = 1

	# Wait for all threads to complete
	for t in threads:
		t.join()

	
	etl.print_stats(globalStatus, startTime)
	#pprint (globalStatus)
	etl_failed=False
	for k, val in globalStatus.items():
		if not etl_failed:
			if val[0]:
				etl_failed=True
	#print etl_failed
	#import win32api
	#print win32api.GetCurrentProcess()
	#e(0)
	win_title=win32gui.GetWindowText(hwnd)
	status_title=''
	if 0:
		if 'cmd.exe' in win_title:
			#win_title='Test'
			pass
		else:
			if etl_failed:
				status_title ='DONE:FAILED:%s' % win_title
				win32gui.SetWindowText(hwnd, status_title)
			else:
				status_title='DONE:SUCCESS:%s' % win_title
				win32gui.SetWindowText(hwnd, status_title)
		
	#while True:
	#win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,200,200,0)
	#	time.sleep(2)
	#e(0)
	if 1:
		#execute post etl
		import __builtin__
		__builtin__.args = args		
		post_etl = import_module(os.path.join(conf.abspath,'config','post_etl.py'))
		post_etl.execute(status_title)
	if if_stdout:
		sys.stdout.close()
		sys.stdout=out
	
except KeyboardInterrupt:
	log.error('KeyboardInterrupt')
	exc_type, exc_value, exc_traceback = sys.exc_info()	
	traceback.print_exception(exc_type, exc_value, exc_traceback)
	etl_failed=True
except NameError, err:
	exc_type, exc_value, exc_traceback = sys.exc_info()	
	traceback.print_exception(exc_type, exc_value, exc_traceback)
	etl_failed=True
except AttributeError, err:
	exc_type, exc_value, exc_traceback = sys.exc_info()	
	traceback.print_exception(exc_type, exc_value, exc_traceback)
	etl_failed=True
except SystemExit, err:
	exc_type, exc_value, exc_traceback = sys.exc_info()	
	traceback.print_exception(exc_type, exc_value, exc_traceback)
	etl_failed=True
except:
	exc_type, exc_value, exc_traceback = sys.exc_info()	
	traceback.print_exception(exc_type, exc_value, exc_traceback)
	etl_failed=True

try:
	
	if int(args.status_pipe_id):
		#time.sleep(1)


		# Get file descriptor from argument
		print 'spID',args.status_pipe_id
		pipearg = int(args.status_pipe_id) #int(sys.argv[1])
		if sys.platform == "win32":
			pipeoutfd = msvcrt.open_osfhandle(pipearg,os.O_WRONLY)
		else:
			pipeoutfd = pipearg

		# Read from pipe
		# Note:  Could be done with os.read/os.close directly, instead of os.fdopen
		#os.write()
		#os.close()
		if 1:
			pipein = os.fdopen(pipeoutfd, 'w')
			#for i in range(1000):
			#print pipein
			#time.sleep(5)
			pipein.write("{'status':%s}" % (not etl_failed))
			#pprint (dir(pipein))
			#pipein.flush()
			#time.sleep(2)
			
			
			pipein.close()
			#time.sleep(2000)
except :
	print "Unexpected error:", sys.exc_info()
	#print 'error--------', e
	
if hasattr(args, 'key_on_exit') and args.key_on_exit:
	os.system('pause')
elif  hasattr(args, 'key_on_exit') and not args.key_on_exit:
	pass
else:
	os.system('pause')