from shovel import task
import boto3

@task
def hello(name):
	'''hello to the name given as an arg ie shovel hello chris'''
	print('Hello, %s' % name)

@task
def list_buckets():
    '''Prints all S3 buckets in your active region'''
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket)

def not_a_task():
	'''Print I'm not considered a task in shovel'''
	pass