def text_create(name,msg):
    desktop_path = '/Users/xuyongqi/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
text_create('hello','hello world)
def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
    return word.replace(censored_word,changed_word)
text_filter('python is lame!')
def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)
    censored_text_create('Try','lame!lame!lame!')