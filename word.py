def main(text):# Template courtesy of https://www.idkrtm.com/
    from os import path
    from wordcloud import WordCloud 
    import matplotlib.pyplot as plt
    #Set the directory containing your lexicon
    dirname = path.dirname(__file__)
    
    # Read the whole text.
    text = open(path.join(dirname, "output.txt")).read()
    
    # Generate a word cloud object and plot it on the x and y axis
    wordcloud = WordCloud().generate(text)
    
    plt.imshow(wordcloud)
    
    #Turn off the axis. Otherwise you will see a bunch of extra numbers around the word cloud
    plt.axis("off")
    
    #Show the word cloud
    plt.show()