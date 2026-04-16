import re


#  any data you want to tokenize
with open("psychology of money.txt", "r", encoding="utf-8") as f:
    raw_data = f.read()

# symbols
my_symbols = r"([!@#$%^&*()_+|~`=\\\[\]{};:'\",.<>/?\s]+)"
token_text = re.split(my_symbols, raw_data)
token_text = [word.strip() for word in token_text if word.strip()]
# print(token_text[:30])
# print(len(token_text))


order_Token_Text = sorted(set(token_text))
order_Token_Text.extend(["<|endoftext|>","<|unk|>"])
# print(order_Token_Text[:300])
vocabulary = {token: i for i, token in enumerate(order_Token_Text)}
# print(vocabolary)


# class tokenizer
class Tokenizer1:
    def __init__(self,vocabulary):
        self.string_in_int_out = vocabulary
        self.int_in_string_out = {i:s for s,i in vocabulary.items()}

    def encode(self, text):
        # split the words
        my_symbols = r"([!@#$%^&*()_+|~`=\\\[\]{};:'\",.<>/?\s]+)"
        token_text = re.split(my_symbols, text)
        # first strip is actually striping spaces and \n and secondone is to print the remaining string left after the strip                 
        token_text = [word.strip() for word in token_text if word.strip()]
        # id
        token_ids = [self.string_in_int_out[s] for s in token_text]
        return token_ids
    
    def decode(self, token_ids):
        # string
        text = " ".join([self.int_in_string_out[i] for i in token_ids])
        clean_text = re.sub(r"\s+([!@#$%^&*()_+|~`=\\\[\]{};:'\",.<>/?])", r"\1", text)
        return clean_text
    

tokenizer_obj_1 = Tokenizer1(vocabulary)

# test
# text = "He also had a relationship with money I’d describe as a mix of insecurity and childish stupidity."
# token_ids = tokenizer_obj_1.encode(text)
# print(token_ids)

# # ids =[6206, 3529, 3107, 6638, 6203, 5711, 6830, 2747, 3912, 70]
# # token_text = tokenizer.decode(ids)
# # print(token_text)

class Tokenizer2:
    def __init__(self,vocabulary):
        self.string_in_int_out = vocabulary 
        self.int_in_string_out = {i:s for s,i  in vocabulary.items()} 

    def encode(self,text):
        symbols = r"([!@#$%^&*()_+|~`=\\\[\]{};:'\",.<>/?\s]+)"
        token_text = re.split(symbols,text)
        token_text = [word.strip() for word in token_text if word.strip()]
        #first word = print word if word in self.str or unk for word in vocab
        unknown_id = self.string_in_int_out.get("<|unk|>")
        ids = [self.string_in_int_out.get(w, unknown_id) for w in token_text]
        return ids

    def decoder(self,token_id):
        #symbols =
        text = " ".join([self.int_in_string_out[i] for i in token_id])
        text = re.sub(r"\s+([!@#$%^&*()_+|~`=\\\[\]{};:'\",.<>/?])",r"\1",text)
        return text
    
tokenizer_obj_2 = Tokenizer2(vocabulary)

text = "their greatest fear was puru"
token_id = tokenizer_obj_2.encode(text)
# print(token_id)

ids = [6206, 3529, 3107, 6638, 6898]
token_ids = tokenizer_obj_2.decoder(ids)
print(token_ids)
