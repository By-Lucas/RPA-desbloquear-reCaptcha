import json
import os
# Input/Output information
num = '1'
file_in = 'audio{0}.flac'.format(num)
file_out = 'audio{0}.json'.format(num)
# Get API key and URL from JSON
f = open('ibm_credentials.json')
json_dict = json.load(f)
API_KEY = json_dict['apikey']
URL = json_dict['url']+'/v1/recognize?model=pt-BR_BroadbandModel'
# Execute cURL command to get information
# and save output to text file
cmd = 'curl -X POST -u "apikey:{0}"\
 --header "Content-Type: audio/flac"\
 --data-binary @{1} "{2}" > {3}'.format(API_KEY, file_in, URL, file_out)
#print(cmd)
result = os.system(cmd)