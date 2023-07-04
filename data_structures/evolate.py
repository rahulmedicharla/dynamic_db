"""
 This is the implementation of a the custom modular datatype Evolate

"""
from data_types import DataType, ResponseType, NodeInterface
from data_structures.node import Node
from data_structures.singly_linked_list import SinglyLinkedList
from data_structures.sequence import Sequence
from data_structures.tree_map import TreeMap
from data_structures.hash_map import HashMap

class Evolate():

    """
    Params:
        -> data_type (DataType) this is a initializer var that tells which data type to use intiially
    
    Var
        -> rep (SubDataStructure): this is the current representation of the data 

    """
    def __init__(self, data_type = DataType) -> None:
        
        self.rep = None
        self.data_type = None

        
        """
        realtime features to keep track of
            -> total length normalized: 0-1 ratio of size of dataset /1000
            -> insertion deletion frequency: 0-1 ratio of how many insertion & deletion commands there are
            -> search prediction: 0-1 ratio of average search index
            -> search density: 0-1 ratio of how close together search indexes are

        """
        self.total_length_normalized = 0
        self.insertion_deletion_frequency = 0
        self.search_prediction = 0
        self.search_density = 0

        self.total_commands = 0
        self.idt_commands = 0
        self.search_list = []

        #set _rep based on data_type passed in
        if data_type == DataType.SEQUENCE:
            self.rep = Sequence()
            self.data_type = data_type
        elif data_type == DataType.TREE_MAP:
            self.rep = TreeMap()
            self.data_type = data_type
        elif data_type == DataType.HASH_MAP:
            self.rep = HashMap()
            self.data_type = data_type
        else:
            self.rep = SinglyLinkedList()
            self.data_type = DataType.SINGLY_LINKED_LIST


    """
    **************************************************************************************************************
    implementations for six main functions 
    """
    
    def add(self, value: any) -> ResponseType:
        self.total_commands += 1
        self.idt_commands += 1

        temp_node = Node(self.rep.get_length(), value, self.data_type)
        return self.rep.add(temp_node)
    
    def remove(self, key: int) -> NodeInterface or ResponseType:
        self.total_commands += 1
        self.idt_commands += 1

        return self.rep.remove(key)
    
    def get(self, key: int) -> NodeInterface or ResponseType:
        self.total_commands += 1
        self.search_list.append(key)
        return self.rep.get(key)

    def update(self, key: int, value: any) -> ResponseType:
        self.total_commands += 1
        return self.rep.update(key, value)

    def get_length(self) -> int:
        return self.rep.get_length()
    
    def get_size(self) -> int:
        return self.rep.get_size()
    
    def get_data_type(self) -> DataType:
        return self.data_type
    
    def get_features(self) -> tuple:
        self.insertion_deletion_frequency = float(self.idt_commands) / float(self.total_commands)
        self.total_length_normalized = float(self.rep.get_length()) / 1000.0
        
        if self.total_length_normalized > 1:
            self.total_length_normalized = 1

        self.search_prediction = self.get_search_prediction()
        self.search_density = self.get_search_density()


        return self.insertion_deletion_frequency, self.total_length_normalized, self.search_prediction, self.search_density
    
    def get_search_prediction(self) -> float:
        avg_key = 0
        for key in self.search_list:
            avg_key += key
        avg_key = float(avg_key) / float(len(self.search_list))

        return avg_key / float(self.rep.get_length())
    
    def get_search_density(self) -> float:
        avg_key = 0
        for key in self.search_list:
            avg_key += key
        avg_key = float(avg_key) / float(len(self.search_list))

        mean_error = []
        for key in self.search_list:
            diff = abs(key - avg_key)
            mean_error.append(float(diff) / float(self.rep.get_length() -1))

        avg_error = 0
        for error in mean_error:
            avg_error += error
        avg_error = float(avg_error) / float(len(mean_error))

        return avg_error

    def print_items(self) -> ResponseType:
        return self.rep.iterate(self.print)
    
    def print_metadata(self) -> ResponseType:
        return self.rep.print_metadata()

    def print(self, node: NodeInterface) -> ResponseType:
        print("Key: " + str(node.key))
        print("Value: " + str(node.value))
        print("Size: " + str(node.size))
        print("Type: " + str(node.type))
        return ResponseType.SUCCESS
    
    def switch_data_structures(self, new_type: DataType) -> ResponseType:
        #create new data instance
        if new_type == DataType.SEQUENCE:
            new_rep = Sequence()
            self.data_type = new_type
        elif new_type == DataType.TREE_MAP:
            new_rep = TreeMap()
            self.data_type = new_type
        elif new_type == DataType.HASH_MAP:
            new_rep = HashMap()
            self.data_type = new_type
        elif new_type == DataType.SINGLY_LINKED_LIST:
            new_rep = SinglyLinkedList()
            self.data_type = DataType.SINGLY_LINKED_LIST

        index = self.rep.get_length() -1
        while index >= 0:
            node = self.rep.get(index)
            new_node = Node(node.get_key(), node.get_value(), self.data_type)
            new_rep.add(new_node)
            index -= 1
        self.rep = new_rep
        return ResponseType.SUCCESS