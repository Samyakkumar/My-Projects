class textAnalyzer():
	def __init__(self, text):
		print("Loading Text...")
		self.text = text
		self.words = []
		self.wordFreq = {}
		self.getWords()

	def getWords(self):
		for line in self.text.splitlines():
			for word in line.strip().split(' '):
				self.words.append(word)
				if word in self.wordFreq:
					self.wordFreq[word] += 1
				else:
					self.wordFreq[word] = 1
		return self.words

	def getFrequency(self):
		return self.wordFreq

	def findAll(self, word):
		foundLines = []
		for line in self.text.splitlines():
			if word in line:
				foundLines.append(line)
		return foundLines

theText = '''The Kragujevac massacre was the mass murder of between 2,778 and 2,794 mostly Serb men and boys in Kragujevac[a] by German soldiers on 21 October 1941. It occurred in the German-occupied territory of Serbia during World War II, and came in reprisal for insurgent attacks in the Gornji Milanovac district that resulted in the deaths of 10 German soldiers and the wounding of 26 others. The number of hostages to be shot was calculated based on a ratio of 100 hostages executed for every German soldier killed and 50 hostages executed for every German soldier wounded.

After a punitive operation was conducted in the surrounding villages, during which 422 males were shot and four villages burned down, another 70 male Jews and communists who had been arrested in Kragujevac were shot. Simultaneously, males between the ages of 16 and 60, including high school students, were assembled by German troops and local collaborators, and the victims were selected from amongst them. The selected males were then marched to fields outside the city, shot with heavy machine guns, and their bodies buried in mass graves. Contemporary German military records indicate that 2,300 hostages were shot. After the war, inflated estimates ranged as high as 7,000 deaths, but German and Serbian scholars have now agreed on the figure of nearly 2,800 killed, including 144 high school students. As well as Serbs, other massacre victims included Jews, Romani people, Muslims, Macedonians, Slovenes and members of other nationalities.'''
myText = textAnalyzer(theText)
