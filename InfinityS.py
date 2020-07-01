"""

This Script And Module Was Made By Yash Arora, InfinityS.
This Script Can not be used by any other Person, Company, Third Party Teams Without Permission.
For Permissions or Contact To Owner Of The Script :- InfinitySCommunity@gmail.com
To Submit Your Own Model Contact :- InfinitySCommunity@gmail.com

"""

import os # Current Working Directory
import time # Giving Gap For Processing
from zipfile import ZipFile # To Extract Zip Files
from tqdm import *
def ImageClassifier(): # Extracting The Image Classifier VirtualEnviorment
    os.makedirs('Image Classifier')
    print('Making Model...')
    time.sleep(2.5)
    ic = ZipFile(os.getcwd() + '//MODEL//IMAGE_CLASSIFIER.zip','r')
    ic.printdir()
    time.sleep(2.5)
    print('Finishing Up!')
    ic.extractall()
    print('Done!')
def ObjectDetection(): # Extracting The Object Detection VirtualEnviorment=
    os.makedirs('Object Detection')
    print('Making Model...')
    time.sleep(2.5)
    ic = ZipFile(os.getcwd() + '//MODEL//OD.zip','r')
    ic.printdir()
    time.sleep(2.5)
    print('Finishing Up!')
    ic.extractall()
    print('Done!')
def Chatbot():
    os.makedirs('Chatbot')
    print('Making Model...')
    time.sleep(2.5)
    ic = ZipFile(os.getcwd() + '//MODEL//CHATBOT.zip','r')
    ic.printdir()
    time.sleep(2.5)
    print('Finishing Up!')
    ic.extractall()
    print('Done!')
def StockPrediction():
    os.makedirs('Stock Predictor')
    print('Making Model...')
    time.sleep(2.5)
    ic = ZipFile(os.getcwd() + '//MODEL//STOCK.zip','r')
    ic.printdir()
    time.sleep(2.5)
    print('Finishing Up!')
    ic.extractall()
    print('Done!')
def FaceRecognition():
    os.makedirs('Face Recognition')
    print('Making Model...')
    time.sleep(2.5)
    ic = ZipFile(os.getcwd() + '//MODEL//FR.zip','r')
    ic.printdir()
    time.sleep(2.5)
    print('Finishing Up!')
    ic.extractall()
    print('Done!')
def SpeechRecognition():
    os.makedirs('Speech Recognition')
    print('Making Model...')
    time.sleep(2.5)
    ic = ZipFile(os.getcwd() + '//MODEL//SR.zip','r')
    ic.printdir()
    time.sleep(2.5)
    print('Finishing Up!')
    ic.extractall()
    print('Done!')
print('Starting InfinityS Kernal.')
for i in tqdm(range(100)):
	time.sleep(0.05)
	pass
print('\n')
print('InfinityS Kernal 1.1.5')
print('\n')
while True:
	time.sleep(0.25)
	model = input('Model - ')
	try:
		exec(model)
	except FileExistsError:
		print('\n')
		print('ERROR: Please Delete Or Move The Folder "Image Classifer" As It is needed by InfinityS')
		print('\n')
	except:
		print('\n')
		print('Bad Command.')
		time.sleep(0.25)
		print('\n')
		print('Loading Model Index.')
		for i in tqdm(range(50)):
			time.sleep(0.00005)
			pass
		print('\n')
		print('Choose Model From This Index (Please Type As It Is) - ')
		time.sleep(0.02)
		print('ImageClassifier()')
		time.sleep(0.02)
		print('ObjectDetection()')
		time.sleep(0.02)
		print('Chatbot()')
		time.sleep(0.02)
		print('StockPrediction()')
		time.sleep(0.02)
		print('FaceRecognition()')
		time.sleep(0.02)
		print('SpeechRecognition()')
		print('\n')