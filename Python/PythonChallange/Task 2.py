# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

alphabet = ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")

# k->m
message = "map"

my_message = ""
for i in range(0,len(message)):
    if message[i] == "." or message[i] == "("or message[i] == ")":
        my_message += message[i]
    elif alphabet.find(message[i]) == -1:
        my_message += " "
    else:
        my_message += alphabet[alphabet.find(message[i])+2]

print (my_message)


# # 
# from string import maketrans

# alphabet = ("abcdefghijklmnopqrstuvwxyz")
# alphabet_moved = ("cdefghijklmnopqrstuvwxyzab")

# message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# print(message.maketrans(alphabet,alphabet_moved))
