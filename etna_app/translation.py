from modeltranslation.translator import translator, TranslationOptions

from .models import *

class HBTranslationOptions(TranslationOptions):
    fields = ('header',)

class HSTranslationOptions(TranslationOptions):
    fields = ('sadalanan_melumatlar',)


translator.register(Haqqimizda_basliq, HBTranslationOptions)



translator.register(Haqqimizda_melumatlari, HSTranslationOptions)
