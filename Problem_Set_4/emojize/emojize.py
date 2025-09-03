import emoji 

in_moji = input("Input: ")
out_moji = emoji.emojize(in_moji, language = "alias" )

print(f"Output: {out_moji}")