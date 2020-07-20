
import os
 
def main():
	
	baseDirName='./notes'
	archiveDirName = os.path.join(baseDirName,'Archive')
	templateDirName = os.path.join(baseDirName,'Templates')

	if (os.path.exists(archiveDirName) == False) :
		os.makedirs(archiveDirName)

	if (os.path.exists(templateDirName) == False) :
		os.makedirs(templateDirName)
	
	listOfFiles = list()
	for (dirpath, dirnames, filenames) in os.walk(baseDirName) :

		for file in filenames :

			if (file.endswith('.md')) :

				fo = open(os.path.join(dirpath, file), encoding="utf8")
				line = fo.readline()
				line_no = 1

				while line != '' :

					index = line.find('tags:')
					indexArchive = line.find('archived: true')

					if ( indexArchive != -1) :

						currentDirName = os.path.join(dirpath, file)
						
						if (currentDirName != os.path.join(archiveDirName + os.sep + file)) :

							fo.close()
							os.rename(os.path.join(dirpath, file),  os.path.join(archiveDirName + os.sep + file))
							break
					
					if ( indexArchive == -1 & index != -1 & line.count('Templates/') == 1) :

						tags = (line.replace('tags: [','').replace(']','').strip().split(','))

						for tag in tags:

							tag = tag.strip()

							if (tag.find('Templates/') != -1) :

								tagName = tag[tag.find('/')+1:]
								newDirName = os.path.join(templateDirName,tagName)
								oldDirName = os.path.join(dirpath, file)

								if (os.path.exists(newDirName) == False) :
									os.makedirs(newDirName)

								if (oldDirName != os.path.join(newDirName + os.sep + file)) :

									fo.close()
									os.rename(os.path.join(dirpath, file),  os.path.join(newDirName + os.sep + file))

								break

						fo.close()

						break


					if ( indexArchive == -1 & index != -1 & line.count('Notebooks/') == 1) :

						tags = (line.replace('tags: [','').replace(']','').strip().split(','))

						for tag in tags:

							tag = tag.strip()

							if (tag.find('Notebooks/') != -1) :

								tagName = tag[tag.find('/')+1:]
								newDirName = os.path.join(baseDirName,tagName)
								oldDirName = os.path.join(dirpath, file)

								if (os.path.exists(newDirName) == False) :
									os.makedirs(newDirName)

								if (oldDirName != os.path.join(newDirName + os.sep + file)) :

									fo.close()
									os.rename(os.path.join(dirpath, file),  os.path.join(newDirName + os.sep + file))

								break

						fo.close()

						break

					line = fo.readline()
					line_no += 1

				fo.close()

		
if __name__ == '__main__':
	main()