import os

for filename in os.listdir('d:/development/projectplay/projectplay.github.io/img/games'):
	print "<img class='img-responsive' src='/img/games/" + filename + "' />"