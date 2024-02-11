import string

COMMAND_UI = r'''
/＜<$sec9>＞
| <HP> |$sec10 /$sec11|
| <MP> |$sec12 /$sec13|
| <AP> |$sec15 /$sec16|
\ <LIMIT> [$sec14]
「 $sec98」________________________
/　[1]$sec1  <$sec5>　   
|　[2]$sec2  <$sec6>
|　[3]$sec3  <$sec7>
|　[4]$sec4  <$sec8>
|　[5]もどる　  
|　[6]リミット 
\__________________________________[TURN $sec99 ]
( info )(Thank you for playing!!)
'''
BATTLE_UI = string.Template(COMMAND_UI)

SELECT_PLAYER = '''
[][][][][][][][][][][][][][][][][][]
[]  ( info )あなたの分身を選んでください
[]　[1]盗賊　　　　　<= PUSH 1      
[]　[2]みならい騎士　<= PUSH 2
[]　[3]召喚士　　　　<= PUSH 3
[][][][][][][][][][][][][][][][][][]

'''