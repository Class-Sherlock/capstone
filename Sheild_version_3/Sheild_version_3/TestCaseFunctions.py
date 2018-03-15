import tkinter as tk
import urllib.request
import requests
import os
import xml.etree.ElementTree as et
import random


def URLFilter():
    with open('URLreport.txt', 'w') as resultfile:
        st = "Sheild URL test results:" \
             "**********************************************************************************************************\n"
        resultfile.write(st)

        with open('website_list.txt', 'r') as f:
            while (True):
                content = f.readline()
                url = content
                if content == "":
                    break
                try:
                    urllib.request.urlopen(url)
                    out = str(url)
                    result = ("Gained access to %s \n" % out)
                    resultfile.write(result)
                except Exception as e:
                    error = "%s \n" % e
                    resultfile.write(str(error))

        f.close()

        getting_key = "https://192.168.157.10//api/?type=report&async=yes&reporttype=custom&reportname=Test1_report&key=LUFRPT1Db0EwR2txdk5tRHhqWWpZVGxiVUJIYkVPYnM9REJzZXhnWWNhd0FaMmd2Ulk2VzY4dz09"
        # urllib.request.urlopen(getting_key)

        response = requests.get(getting_key, verify=False)

        with open('job_number.xml', 'wb') as file:
            file.write(response.content)

        file.close()

        base_path = os.path.dirname(os.path.realpath(__file__))
        xml_file = os.path.join(base_path, "job_number.xml")
        tree = et.parse(xml_file)
        root = tree.getroot()

        for check in root.iter('job'):
            job_number = check.text

        the_key = "https://192.168.157.10/api/?type=report&async=yes&reporttype=custom&reportname=Test1_report&action=get&job-id=" + job_number + "&key=LUFRPT1Db0EwR2txdk5tRHhqWWpZVGxiVUJIYkVPYnM9REJzZXhnWWNhd0FaMmd2Ulk2VzY4dz09"

        response = requests.get(the_key, verify=False)

        with open('Job_report.xml', 'wb') as file:
            file.write(response.content)

        file_name = 'Job_report.xml'
        file = os.path.abspath(os.path.join(file_name))
        # rest of the code from here will most likely will remain the same
        root = et.parse(file)

        resultfile.write("Firewall log outputs are:"
                         "**********************************************************************************************\n")
        for entry in root.iter('entry'):
            days = entry.find('day-of-receive_time').text
            cat = entry.find('category').text
            action = entry.find('action').text
            website = entry.find('misc').text
            reps = entry.find('repeatcnt').text

            output = '* On %s %s %s was %s repeated block %s \n' % (days, website, cat, action, reps)
            resultfile.write(output)

    resultfile.close()


def FileBlocking():
    with open('download_list.txt', 'r') as f:
        i = 0
        while(True):
                content = f.readline()
                url = content
                if content == "":
                    break
                try:
                    full_name = str(i) +".jpg"
                    i = i +1
                    x = urllib.request.urlretrieve(url, full_name)
                    print('gained access to '+ url)
                except Exception as e:
                     print(e)
                #error correction
                # #GUI status bar, clear it and tell them to input again
                #      print('did not have access to '+ url)