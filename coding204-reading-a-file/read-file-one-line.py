# Read from a file one line at a time.
# amwhaley@cisco.com
# twitter: @mandywhaley
# http://developer.cisco.com
# http://developer.cisco.com/learning
# Jan 15, 2015

# * THIS SAMPLE APPLICATION AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY
# * OF ANY KIND BY CISCO, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED
# * TO THE IMPLIED WARRANTIES OF MERCHANTABILITY FITNESS FOR A PARTICULAR
# * PURPOSE, NONINFRINGEMENT, SATISFACTORY QUALITY OR ARISING FROM A COURSE OF
# * DEALING, LAW, USAGE, OR TRADE PRACTICE. CISCO TAKES NO RESPONSIBILITY
# * REGARDING ITS USAGE IN AN APPLICATION, AND IT IS PRESENTED ONLY AS AN
# * EXAMPLE. THE SAMPLE CODE HAS NOT BEEN THOROUGHLY TESTED AND IS PROVIDED AS AN
# * EXAMPLE ONLY, THEREFORE CISCO DOES NOT GUARANTEE OR MAKE ANY REPRESENTATIONS
# * REGARDING ITS RELIABILITY, SERVICEABILITY, OR FUNCTION. IN NO EVENT DOES
# * CISCO WARRANT THAT THE SOFTWARE IS ERROR FREE OR THAT CUSTOMER WILL BE ABLE
# * TO OPERATE THE SOFTWARE WITHOUT PROBLEMS OR INTERRUPTIONS. NOR DOES CISCO
# * WARRANT THAT THE SOFTWARE OR ANY EQUIPMENT ON WHICH THE SOFTWARE IS USED WILL
# * BE FREE OF VULNERABILITY TO INTRUSION OR ATTACK. THIS SAMPLE APPLICATION IS
# * NOT SUPPORTED BY CISCO IN ANY MANNER. CISCO DOES NOT ASSUME ANY LIABILITY
# * ARISING FROM THE USE OF THE APPLICATION. FURTHERMORE, IN NO EVENT SHALL CISCO
# * OR ITS SUPPLIERS BE LIABLE FOR ANY INCIDENTAL OR CONSEQUENTIAL DAMAGES, LOST
# * PROFITS, OR LOST DATA, OR ANY OTHER INDIRECT DAMAGES EVEN IF CISCO OR ITS
# * SUPPLIERS HAVE BEEN INFORMED OF THE POSSIBILITY THEREOF.-->

#.readline() reads in only 1 line of the file at a time.
print ("Read only the first line of the file:")
my_file_object = open("my-file.txt", "r")
print (my_file_object.readline())
print ("\n")
my_file_object.close()