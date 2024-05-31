# https://www.library.illinois.edu/ias/koreancollection/koreanromanizationtable/

# This is a Korean transcriber based on McCune-Reischauer Romanization System for Korean language

from math import floor


# onsets (초성)
onsets = ['k', 'kk', 'n', 't', 'tt', 'l', 'm', 'p', 'pp', 's', 'ss', '', 'ch', 'tch', 'ch’',
           'k’', 't’', 'p’', 'h']

# nuclei (중성)
nuclei = ['a', 'ae', 'ya', 'yae', 'ŏ', 'e', 'yŏ', 'ye', 'o', 'wa', 'wae', 'oe', 'yo',
           'u', 'wŏ', 'we', 'wi', 'yu', 'ŭ', 'ŭi', 'i']

# codas (종성)
codas = ['', 'k', 'kk', 'ks', 'n', 'nj', 'nh', 't', 'l', 'lg', 'lm', 'lb', 'ls', 'lt’', 'lp’',
       'lh', 'm', 'p', 'ps', 's', 'ss', 'ng', 'ch', 'ch’', 'k’', 't’', 'p’', 'h']

# individual graphemes
# https://dylansung.tripod.com/uni/jamo.htm (한국어 자모)

# Hangeul characters are composed of Jamo (자모). 
""" There are are 11172 precomposed Hangeul (한글) glyphs (A glyph is a single representation of a character) in Unicode. 
They are situated in the range U+AC00 (44032) to U+D7A3 (55203).
There are 19 single consonant initials (ㄱ g, ㄴ n, ㄷ d, ㄹ l, ㅁ m, ㅂ b, ㅅ s, ㅇ * (-ng), ㅈ j, ㅊ ch, ㅋ t, ㅌ k, ㅍ p, ㅎ h ), 
5 double consonant initials ( ㄲ gg, ㄸ dd, ㅃ bb, ㅆ ss, ㅉ jj ) and 
21 vowel type jamo (ㅏ a, ㅐ ae, ㅑ ya, ㅒ yae, ㅓ eo, ㅔ e, ㅕ yeo, ㅖ ye, ㅗ o, ㅘ wa, ㅙ wae, ㅚ oe, ㅛ yo, ㅜ u, ㅝ weo, ㅞ we, ㅟ wi, ㅠ yu, ㅡ eu, ㅢ eui (yi), ㅣ i ).  
Zero intial syllables are begun with the jamo ㅇ, but serves as a velar nasal -ng when it appears at the end of a syllable.
The consonant digraphs (ㄳ, ㄵ, ㄶ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅄ) exist only as finals and are transcribed by their actual pronunciation."""
# https://en.wikipedia.org/wiki/McCune%E2%80%93Reischauer

graphemes = {12593: 'k', # ㄱ
             12594: 'kk', # ㄲ
             12595: 'ks', # ㄳ
             12596: 'n', # ㄴ
             12597: 'nj', # ㄵ
             12598: 'nh', # ㄶ
             12599: 't', # ㄷ
             12600: 'tt', # ㄸ
             12601: 'l', # ㄹ
             12602: 'lg', # ㄺ 
             12603: 'lm', # ㄻ
             12604: 'lb', # ㄼ
             12605: 'ls', # ㄽ
             12606: 'lt’', # ㄾ
             12607: 'lp’', # ㄿ
             12608: 'lh', # ㅀ (or 'rh')
             12609: 'm', # ㅁ
             12610: 'p', # ㅂ 
             12611: 'pp', # ㅃ
             12612: 'ps', # ㅄ
             12613: 's', # ㅅ
             12614: 'ss', # ㅆ
             12615: '', # o (*/ng) / Not romanized
             12616: 'ch', # ㅈ 
             12617: 'tch', # ㅉ
             12618: 'ch’', # ㅊ 
             12619: 'k’', # ㅋ
             12620: 't’', # ㅌ
             12621: 'p’', # ㅍ
             12622: 'h', # ㅎ
             12623: 'a', # ㅏ
             12624: 'ae', # ㅐ 
             12625: 'ya', # ㅑ
             12626: 'yae', # ㅒ 
             12627: 'ŏ', # ㅓ
             12628: 'e', # ㅔ 
             12629: 'yŏ', # ㅕ 
             12630: 'ye', # ㅖ
             12631: 'o', # ㅗ
             12632: 'wa', # ㅘ 
             12633: 'wae', # ㅙ 
             12634: 'oe', # ㅚ
             12635: 'yo', # ㅛ
             12636: 'u', # ㅜ
             12637: 'wŏ', # ㅝ 
             12638: 'we', # ㅞ 
             12639: 'wi', # ㅟ 
             12640: 'yu', # ㅠ 
             12641: 'ŭ', # ㅡ 
             12642: 'ŭi', # ㅢ 
             12643: 'i' } # ㅣ  


def transcribe(s, boundary=''):
    '''Takes a Korean string as input and splits
    the syllables into their graphemes.
    Optionally inserts a boundary symbol between syllables.
    Input that is not Korean is returned as is.'''

    output = ""


    length = len(s)

    for i,char in enumerate(s, start=1):

        uni_index = ord(char)
         # the ord() function returns the Unicode code for a character

        if uni_index in graphemes:
            output+=graphemes[uni_index]
            continue

        # if the character is a hangul syllable(음절), split into onset(초성), nucleus(중성), coda(종성)
        elif uni_index in range(44032,55204):
            codepoint = ord(char)-44032

            onset = int(floor(codepoint/588))
            nucleus = int(floor((codepoint-588*(onset))/28))
            coda = (codepoint-588*(onset))-28*int(floor(nucleus))

            output += onsets[onset] + nuclei[nucleus] + codas[coda]

        # if it is no hangul, add to output as is
        else:
            output += char

        if i < length:
            output += boundary

    return output