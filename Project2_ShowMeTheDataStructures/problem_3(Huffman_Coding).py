import sys
import collections


class Node(object):

    def __init__(self, char=None, priority=None):
        self.char = char
        self.priority = priority
        self.left = None
        self.right = None

    @staticmethod
    def combine_nodes(node_1, node_2):
        """
        Combines two nodes together
        ->param node_1: one of the nodes to fuse
        ->param node_2: another node to fuse
        ->return: nodes fused, being the leaves of a third parent node
        """
        combine_node = Node()

        if node_1.priority <= node_2.priority:
            combine_node.left = node_1
            combine_node.right = node_2
        else:
            combine_node.left = node_1
            combine_node.right = node_2

        combine_node.priority = node_1.priority + node_2.priority

        return combine_node

    def __repr__(self):
        return "Node of character: {} | frequency: {}".format(self.char, self.priority)


class Queue(object):
    def __init__(self, string):
        _ = collections.Counter(string)
        self.arr = [Node(char=letter, priority=_[letter]) for letter in _]
        self.sort()

    def sort(self) -> None:
        """
        Sorts the queue by frequency
        :return: None
        """
        self.arr = sorted(self.arr, key=lambda x: x.priority, reverse=True)

    def combine_step(self) -> None:
        """
        combined the two nodes present on the queue; see Node.combine_nodes()
        :return: None
        """
        low_node_1 = self.arr.pop()
        low_node_2 = self.arr.pop()

        self.arr.append(Node.combine_nodes(
            node_1=low_node_1, node_2=low_node_2))
        self.sort()


class Tree(object):
    def __init__(self, queue: Queue):
        while len(queue.arr) > 1:
            queue.combine_step()

        self.root = queue.arr[0]

    def convert_to_binary(self) -> None:
        """
        converting the tree into binary by chaging Node.char into 1/0 value
        """
        self.root = self._check_binary_code(self.root)
        self.root.freq = 0

    @staticmethod
    def _check_binary_code(node: Node) -> Node:
        """
        checking for 1 or 0 value to be put into Node.char
        """
        if (node.left is None) and (node.right is None):
            return node

        if node.left is not None:
            node.left.freq = 1
            node.left = Tree._check_binary_code(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree._check_binary_code(node.right)

        return node


class HuffmanEncoder(object):
    def __init__(self, tree: Tree):
        self.table = self._create_encoding_table(base_code='', node=tree.root)
        self.encode_dict = None
        self.decode_dict = None

        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self) -> None:
        """
        Encoder dictionary constructor
        :return: None
        """
        encoder_dict = dict()

        for i, element in enumerate(self.table):
            encoder_dict[element[0]] = element[1]

        self.encode_dict = encoder_dict

    def _create_decoder(self) -> None:
        """
        Decoder dictionary constructor
        :return: None
        """
        decoder_dict = dict()

        for i, element in enumerate(self.table):
            decoder_dict[element[1]] = element[0]

        self.decode_dict = decoder_dict

    def encode(self, text: str) -> str:
        """
        Text encoding method, specific for each encoder
        :param text: text to encode, same as used to construct Huffman Encoder
        :return: text encoded with Huffman algorithm
        """
        coded_text = ''
        for char in text:
            coded_text += self.encode_dict[char]

        return coded_text

    def decode(self, encoded_text: str) -> str:
        """
        Text decoding method, specific for each encoder
        :param encoded_text: text to decoded, same as used to construct Huffman Encoder
        :return: text decoded with Huffman algorithm
        """
        decoded_text = ''

        while len(encoded_text) > 0:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decode_dict.keys():
                    decoded_text += self.decode_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1

        return decoded_text

    @staticmethod
    def _create_encoding_table(base_code: str, node: Node) -> list:
        """
        Creates the basic encoding table by traversing the binary-tree
        :param base_code: base code from previous level of the binary tree
        :param node: node of the tree to search characters on
        :return: list of the characters and their corresponding binary encoding
        """
        if (node.left is None) and (node.right is None):
            return [(node.char, base_code + str(node.freq))]

        if node.freq == -1:
            current_code = ''
        else:
            current_code = base_code + str(node.freq)

        coding_dict = []

        if node.char is not None:
            coding_dict.append((node.char, current_code + str(node.freq)))

        if node.left is not None:
            coding_dict.extend(
                HuffmanEncoder._create_encoding_table(current_code, node.left))

        if node.right is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(
                current_code, node.right))

        return coding_dict


def huffman_encoding(data: str) -> (str, HuffmanEncoder):
    """
    Huffman encoding method
    :param data: text desired to be codified
    :return: text encoded and the corresponding text specific encoder
    """

    if len(data) == 0:
        print("Introduce a non null string")
        return

    else:
        temp_queue = Queue(string=data)
        temp_tree = Tree(queue=temp_queue)
        temp_tree.convert_to_binary()
        temp_encoder = HuffmanEncoder(temp_tree)

        return temp_encoder.encode(data), temp_encoder


def huffman_decoding(data: str, encoder: HuffmanEncoder) -> str:
    """
    Huffman decoding method
    :param data: text desired to be decoded
    :param encoder: Huffman encoder used to initially encode the text
    :return: text decoded, i.e. originally restored
    """

    return encoder.decode(data)


if __name__ == "__main__":

    # Normal Cases:
    # Case 1
    print('Case 1:')

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    # The size of the data is: 69
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 0001011011101000111001010010011000000001000011101110100110001111010010

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 69
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: The bird is the word

    # Case 2
    print('Case 2:')

    a_great_sentence = "I love coding"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    # The size of the data is: 62
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: I love coding

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 32
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 0101011010000010010010001001100011001000000000010011000111

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 62
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: I love coding

    # Case 3
    print('Case 3:')

    a_great_sentence = "I love Photoshop"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    # The size of the data is: 65
    print("The content of the data is: {}\n".format(a_great_sentence))
    # The content of the data is: I love Photoshop

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 36
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 01110001001111010011000110100100001000110100001101000000001101000001
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 65
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: I love Photoshop

    # Case 4
    print('Case 4:')

    a_not_so_great_sentence = "aaa"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_not_so_great_sentence)))
    # The size of the data is: 52
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # The content of the data is: aaa

    encoded_data, tree = huffman_encoding(a_not_so_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    # The size of the encoded data is: 24
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # The content of the encoded data is: 000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    # The size of the decoded data is: 52
    print("The content of the encoded data is: {}\n".format(decoded_data))
    # The content of the encoded data is: aaa

    # Case 5
    print('Case 5:')
    a_not_so_great_sentence = ""

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_not_so_great_sentence)))
    # The size of the data is: 49
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # The content of the data is:

    huffman_encoding(a_not_so_great_sentence)
    # Please introduce a non null string