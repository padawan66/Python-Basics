# This program should take user input continuesly and display the whole input values in . seperated values in a single string

user_input_str = ""
""" while True:
    user_input = input("Say something ")
    if user_input!= "/end":
        if(user_input_str == ""):
            user_input_str = user_input
        else:
            user_input_str = user_input_str.__add__(".").__add__(user_input)
        continue
    else:
        print(user_input_str)
        break """

def sentence_maker(sentence):
    string_sentence = str(sentence)
    interragatives = ("how","why", "when","is", "will", "can","could", "would" ,"have","had" ,"has","are")
    if sentence.startswith(interragatives):
        return (str(sentence).__add__("?").capitalize())
    else :
        return sentence.__add__(".").capitalize()

def initiate_dialog() :
    output_string = ""
    while True:
        user_input = input("Say something ")
        if user_input!= "/end":
            if output_string == "":
                output_string = sentence_maker(user_input)
            elif sentence_maker(user_input).endswith("?") :
                output_string = output_string.__add__(sentence_maker(user_input))
            elif output_string.endswith("."):
                output_string = output_string.__add__(sentence_maker(user_input))
        else:
            print(output_string)
            break

initiate_dialog()

        