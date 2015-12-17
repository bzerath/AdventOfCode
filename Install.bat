if exist Clean\ del Clean\ /q /s

rem D'ABORD ON COPIE TOUS LES FICHIERS DANS UN DOSSIER PROPRE, PUIS ON TRAVAILLE DESSUS (compilation et installer)

rem Copie des dossiers en excluant les .pyc
echo .pyc > excludedfileslist.txt
xcopy Csv 		Clean\Csv\ 		/E
xcopy Extra 	Clean\Extra\ 	/E
xcopy Scripts 	Clean\Scripts\ 	/E /exclude:excludedfileslist.txt
xcopy Servers 	Clean\Servers\ 	/E /exclude:excludedfileslist.txt
xcopy Xml 		Clean\Xml\ 		/E
del excludedfileslist.txt

rem Copie les fichiers de la racine
xcopy Copyright.txt 				Clean\
xcopy LiteATS_Launcher.bat 			Clean\		
xcopy Main.py 						Clean\			
xcopy mtTkinter.py	 				Clean\			
xcopy "README LiteAts_U500.txt" 	Clean\
xcopy Variables.py 					Clean\
xcopy Configuration.ini 			Clean\
xcopy setup.py 						Clean\

rem Maintenant on a un dossier tout propre (dont on peut se servir plus tard, pour le zipper par exemple).

rem Compile LiteATS
cd Clean
C://Python27//python setup.py py2exe

rem Rapatrie les fichiers dont on a besoin dans /dist pour que le logiciel marche...
xcopy Xml 		dist\Xml\ 		/E
xcopy Extra 	dist\Extra\ 	/E
xcopy Configuration.ini 	dist\
xcopy "README LiteAts_U500.txt" 	dist\

rem Creation de l'installer
cd ..
"C:\Program Files (x86)\NSIS\makensis" /V2 LiteATS_U500_Setup_Genius_general.nsi 

xcopy "Setup LiteATS U500 v1.1.1.exe"	Clean\
del "Setup LiteATS U500 v1.1.1.exe"


pause