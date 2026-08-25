class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for word in strs:
            encoded_string += f"{len(word)}#{word}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_words = []

        pointer_1 = 0
        pointer_2 = 0

        while pointer_2 < len(s) - 1:
            pointer_1 = pointer_2
            
            while s[pointer_2] != "#":
                pointer_2 += 1

            word_len = int(s[pointer_1:pointer_2])
            start = pointer_2 + 1
            end = start + word_len
            decoded_words.append(s[start : end])

            pointer_2 += word_len + 1

            

        return decoded_words




