# conda install -c conda-forge googletrans
from googletrans import Translator

def gg_translate(str_input):
    translator = Translator()
    return translator.translate(str_input, src="en",dest='vi').text

gg_translate('hello')
gg_translate('google bye')
