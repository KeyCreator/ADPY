import time

array = range(500)
percent = 100 / len(array)
progress = 0

for item in array:
    time.sleep(0.01)
#    print('.', end='')
    progress += percent
    print('Processing is completed at %3d%%' % progress, end='\r', flush=True)