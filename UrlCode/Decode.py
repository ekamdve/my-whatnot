from sys import argv


class Decode(object):
    reserved = {'+':' ',
                '%21': '!',
                '%22': '"',
                '%23': '#',
                '%24': '$',
                '%25': '%',
                '%26': '&',
                '%27': "'",
                '%28': '(',
                '%29': ')',
                '%2A': '*',
                '%2B': '+',
                '%2C': ',',
                '%2F': '/',
                '%40': ';',
                '%3A': ':',
                '%40': '@',
                '%3D': '=',
                '%3F': '?',
                '%5B': '[',
                '%5D': ']'}

    def decode(self, encoded_url):
        decoded_url = ""
        i = 0
        while i < len(encoded_url):
            if encoded_url[i] == '%':
                idx = encoded_url[i]
                i += 1
                idx += encoded_url[i]
                i += 1
                idx += encoded_url[i]
                decoded_url += self.reserved[idx]
            else:
                decoded_url += encoded_url[i]

            i += 1

        return decoded_url


if __name__ == "__main__":
    if len(argv) == 2:
        url_to_decode = argv[1]
        print(Decode().decode(url_to_decode))
