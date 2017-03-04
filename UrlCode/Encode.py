from sys import argv


class Encode(object):
    reserved = {' ': '+',
                '!': '%21',
                '"': '%22',
                '#': '%23',
                '$': '%24',
                '%': '%25',
                '&': '%26',
                "'": '%27',
                '(': '%28',
                ')': '%29',
                '*': '%2A',
                '+': '%2B',
                ',': '%2C',
                '/': '%2F',
                ';': '%40',
                ':': '%3A',
                '@': '%40',
                '=': '%3D',
                '?': '%3F',
                '[': '%5B',
                ']': '%5D'}

    def encode(self, url):
        encoded_url = ""
        for ch in url:
            if '0' <= ch <= '9':
                encoded_url += ch
            elif 'A' <= ch <= 'Z':
                encoded_url += ch
            elif 'a' <= ch <= 'z':
                encoded_url += ch
            elif ch == '-' or ch == '_' or ch == '.' or ch == '~':
                encoded_url += ch
            elif ch in self.reserved:
                encoded_url += self.reserved[ch]
            else:
                encoded_url += ch

        return encoded_url


if __name__ == '__main__':
    if len(argv) == 2:
        url_to_encode = argv[1]
        print(Encode().encode(url_to_encode))

