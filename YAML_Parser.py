import glob
import yaml
import pickle

print('\nInitiating Parsing......')
files = []
for name in glob.glob('C:/Users/IS Lab/Downloads/semgrep-rules-develop/**/*.yaml', recursive=True):
    files.append(name)
size_of_files = len(files)
print('\nTotal Number of Rules to parse\n')
print(size_of_files)
print('*************')
counter = 0

owasp_A1 = []
owasp_A2 = []
owasp_A3 = []
owasp_A4 = []
owasp_A5 = []
owasp_A6 = []
owasp_A7 = []
owasp_A8 = []
owasp_A9 = []
owasp_A10 = []

A1 = 'Broken Authentication'
A_1 = 'Broken Access Control'
A2 = 'Cryptographic Failures'
A_2 = 'Sensitive Data Exposure'
A3 = 'Injection'
A_3 = 'Cross-Site Scripting'
A4 = 'Insecure Design'
A5 = 'Security Misconfiguration'
A_5 = 'XML External Entities'
A6 = 'Vulnerable and Outdated Components'
A_6 = 'Using Components with Known Vulnerabilities'
A7 = 'Identification and Authentication Failures'
A8 = 'Software and Data Integrity Failures'
A_8 = 'Insecure Deserialization'
A9 = 'Security Logging and Monitoring Failures'
A10 = 'Server-Side Request Forgery'

for doc in files:
    with open(files[counter],'r',encoding="utf8") as rule:
        data = yaml.safe_load(rule)
        if A1 in str(data):
            owasp_A1.append(data['rules'][0]['id'])
        if A_1 in str(data):
            owasp_A1.append(data['rules'][0]['id'])
        if A2 in str(data):
            owasp_A2.append(data['rules'][0]['id'])
        if A_2 in str(data):
            owasp_A2.append(data['rules'][0]['id'])
        if A3 in str(data):
            owasp_A3.append(data['rules'][0]['id'])
        if A_3 in str(data):
            owasp_A3.append(data['rules'][0]['id'])
        if A4 in str(data):
            owasp_A4.append(data['rules'][0]['id'])
        if A5 in str(data):
            owasp_A5.append(data['rules'][0]['id'])
        if A6 in str(data):
            owasp_A6.append(data['rules'][0]['id'])
        if A_6 in str(data):
            owasp_A6.append(data['rules'][0]['id'])
        if A7 in str(data):
            owasp_A7.append(data['rules'][0]['id'])
        if A8 in str(data):
            owasp_A8.append(data['rules'][0]['id'])
        if A_8 in str(data):
            owasp_A8.append(data['rules'][0]['id'])
        if A9 in str(data):
            owasp_A9.append(data['rules'][0]['id'])
        if A10 in str(data):
            owasp_A10.append(data['rules'][0]['id'])

    counter = counter + 1

High = owasp_A3 + owasp_A8 + owasp_A10
Medium = owasp_A4 + owasp_A5 + owasp_A6 + owasp_A7
Low = owasp_A1 + owasp_A2 + owasp_A9

print('Total Number Of High Criticality Rules : ', len(High))

print('Total Number Of Medium Criticality Rules : ', len(Medium))

print('Total Number Of Low Criticality Rules : ', len(Low))
print(High)
print(Medium)
print(Low)

with open('High.pkl', 'wb') as f:
    pickle.dump(High, f)

with open('Medium.pkl', 'wb') as f:
    pickle.dump(Medium, f)
with open('Low.pkl', 'wb') as f:
    pickle.dump(Low, f)