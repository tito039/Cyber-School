import hashlib

username_trial = b"ANDERSON"

key_part_static_trial = "picoCTF{1n_7h3_|<3y_of_"

key_part_dynamic1_trial = ""

key_part_static2_trial = "}"

hash = hashlib.sha256(username_trial).hexdigest()

key_part_dynamic1_trial += hash[4]
key_part_dynamic1_trial += hash[5]
key_part_dynamic1_trial += hash[3]
key_part_dynamic1_trial += hash[6]
key_part_dynamic1_trial += hash[2]
key_part_dynamic1_trial += hash[1]
key_part_dynamic1_trial += hash[7]
key_part_dynamic1_trial += hash[8]

# Exibir a flag completa
flag = key_part_static_trial + key_part_dynamic1_trial + key_part_static2_trial
print(flag)