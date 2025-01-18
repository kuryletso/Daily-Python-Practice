# Excercise: https://www.hackinscience.org/exercises/bencode-bdecode
#
#
# Solution:

import string
from collections.abc import Generator


def encoder(data: str | int | list | dict) -> str:
    match data:
            case int():
                return f"i{data}e"
            case str():
                return f"{len(data)}:{data}"
            case list():
                return "l" + "".join(encoder(i) for i in data) + "e" 
            case dict():
                d: dict = {key: data[key] for key in sorted(data.keys())}
                return "d" + "".join(encoder(k) + encoder(v) for k, v in d.items()) + "e"
            case _:
                raise ValueError(f"Invalid type encountered: {type(data)}")

def bencode(data: int | str | list | dict) -> bytes:
    if data is None: raise ValueError("Input value required")
    else: return bytes(encoder(data), 'utf-8')




def bdecode_int(data: str) -> tuple:
    item, _, data = data.partition("e")
    return (int(item[1:]), data)

def bdecode_str(data: str) -> tuple:
    length, _, rem = data.partition(":")
    length = int(length)
    output = rem[:length]
    data = rem.replace(output, "", 1)
    return (output, data)


def bdecode_list(data: str) -> Generator:
    while data:
        marker: str = data[0]
        match marker:
            case "e":
                break
            case "d":
                gen = list(bdecode_dict(data[1:]))
                output = {k: v for k,v in gen[:len(gen)-1]}
                data = gen[-1]
                yield output
            case "l":
                gen = list(bdecode_list(data[1:]))
                data = gen[-1]
                yield gen[:len(gen)-1]
            case "i":
                output, data = bdecode_int(data)
                yield output
            case marker if marker in string.digits:
                output, data = bdecode_str(data)
                yield output
    yield data[1:]

def bdecode_dict(data: str) -> Generator:
    rem = data
    while rem:
        key = None
        value = None
        for i in range(2):
            marker: str = rem[0]
            match marker:
                case "e":
                    data = rem[1:]
                    rem = ''
                    break
                case "d":
                    gen = list(bdecode_dict(rem[1:]))
                    if i: value = {k: v for k,v in gen[:len(gen)-1]}
                    else: key = {k: v for k,v in gen[:len(gen)-1]}
                    rem = gen[-1]
                    data = rem
                case "l":
                    gen = list(bdecode_list(rem[1:]))
                    if i: value = gen[:len(gen)-1]
                    else: key = gen[:len(gen)-1]
                    rem = gen[-1]
                    data = rem
                case "i":
                    output, rem = bdecode_int(rem)
                    data = rem
                    if i: value = output
                    else: key = output
                case marker if marker in string.digits:
                    output, rem = bdecode_str(rem)
                    data = rem
                    if i: value = output
                    else: key = output
        if key: yield (key, value)
    yield data


def bdecode(data: bytes) -> str | int | list | dict:
    if isinstance(data, bytes):
        data: str = data.decode()
    marker: str = data[0]
    match marker:
        case "d":
            gen = list(bdecode_dict(data[1:]))
            output = {k: v for k,v in gen[:len(gen)-1]}
            return output
        case "l":
            gen = list(bdecode_list(data[1:len(data)-1]))
            output = gen[:len(gen)-1]
            return output
        case "i":
            output, _ = bdecode_int(data)
            return output
        case marker if marker in string.digits:
            output, _ = bdecode_str(data)
            return output

if __name__ == "__main__":
    data = {'t': 'aa', 'y': 'q', 'q': 'ping', 'a': {'id': '01234567890897653412'}}
    encoded: bytes = bencode(data)
    decoded = bdecode(encoded)
    assert decoded == data
    print(encoded, decoded, sep="\n")