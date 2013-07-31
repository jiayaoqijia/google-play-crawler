import subprocess 
import os

num = "2" 

p = subprocess.Popen("java -jar googleplaycrawler-0.2.jar -f crawler.conf categories|cut -f1 -d ';'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) 
count = 1;
for line in p.stdout.readlines():
	if count == 1:
		count = count + 1
		continue

	line = line.rstrip()
	print line
	if not os.path.exists(line):
		os.mkdir(line)
	os.chdir("./"+line)
	cmd = "java -jar ../googleplaycrawler-0.2.jar -f ../crawler.conf list "+line+" -s apps_topselling_free -n " + num+"|cut -f2 -d ';'"
	#print cmd
	q = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	count1 = 1;
	#print os.getcwd() 
	for subline in q.stdout.readlines():
		if count1 == 1:
			count1 = count1 + 1
			continue
		subline = subline.rstrip()
		print subline
		
		r = subprocess.Popen("java -jar ../googleplaycrawler-0.2.jar -f ../crawler.conf download "+subline, shell=True)
		r.wait()
	subretval = q.wait()
	os.chdir("../")
retval = p.wait()
