
class JSONFile:
    """This is the actual file format that we use"""

    def request(self) -> None:
        print("This is JSON file already")


class XMLFile:
    """Incompatible file format"""

    def specific_request(self) -> None:
        print("Convert this to JSON asap!")

    
class XMLToJSON(JSONFile, XMLFile):
    """adaptor class"""
    
    def request(self):
        print("Converting... to JSON")


def user_format(target: JSONFile):
    print(target.request(), end="")


def main():
    target = JSONFile()
    user_format(target)

    json_conv = XMLFile()
    print(json_conv.specific_request())

    converter = XMLToJSON()
    user_format(converter)

if __name__ == "__main__":
    main()