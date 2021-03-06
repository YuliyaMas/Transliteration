from collections import defaultdict
from nltk import ngrams


class Translitteration:

    def rule_cy_lt(self):

        file = open("regle_BGN.txt", encoding="utf-8").readlines()
        rules = defaultdict(str)

        for line in file:
            for rule in line.split("\n"):
                if len(rule.split("\t")) > 1:
                    rules[rule.split("\t")[0]] = rule.split("\t")[1].strip("\n")
        return rules

    def translit_file_cy_lt(self, input_text):
        output = ""
        rules = self.rule_cy_lt()
        char = list(ngrams(input_text, 1))
        i = 0

        while i < len(char)-3:

            three = "".join(char[i]+char[i+1]+char[i+2])
            # print(three)
            two = "".join(char[i]+char[i+1])
            # print(two)
            one = "".join(char[i])

            if three in rules.keys():
                new_char = rules.get(three)
                # print("3. ok")
                output += "".join(new_char)
                # print(new_file)
                i += 3
            elif two in rules.keys():
                new_char = rules.get(two)
                # print("2. ok")
                output += "".join(new_char)
                # print(new_file)
                i += 2
            elif one in rules.keys():
                new_char = rules.get(one)
                # print("1. ok")
                output += "".join(new_char)
                # print(new_file)
                i += 1
            else:
                output += "".join(one)
                # print("4. pas ok")
                i += 1
        # print(i)
        two = "".join(char[i]+char[i+1])
        if two in rules.keys():
            output += "".join(rules.get(two))
        elif char[i] and char[i+1] in rules.keys():
            output += "".join(rules.get(char[i]))
            output += "".join(rules.get(char[i+1]))
        else:
            output += "".join(two)
        # output = texte.output_lat_text(output)
        return output
