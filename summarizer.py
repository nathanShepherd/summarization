from gensim.summarization.summarizer import summarize

print('''
	summarize(text, ratio=0.2, word_count=None, split=False)
        Get a summarized version of the given text.
        
        The output summary will consist of the most representative sentences
        and will be returned as a string, divided by newlines.
''')

text = ""
filename = ""
with open(filename, 'r') as textfile:
        text = textfile.read()

ratio = float(input("Summary ratio: "))
for line in summarize(text, ratio=ratio, split=True):
	print(line)
