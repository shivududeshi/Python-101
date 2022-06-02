import re


class Myset(dict):

    def __init__(self, mails_dict=None):
        if mails_dict is not None:
            self.read_file(mails_dict)

    def __or__(self, other):
        return self.union(other)

    def __and__(self, other):
        return self.intersection(other)

    def __sub__(self, other):
        return self.minus(other)

    def union(self, dict_2):
        """
        Finding the union of given two dictionaries
        py:function::

        Args:
            dict_1,dict_2 (dict): dictionaries to find union

        Returns:
            dict: dictionary of union of given dictionaries.
        """
        ret = Myset()
        for x in self:
            ret[x] = 1
        for y in dict_2:
            if y not in ret:
                ret[y] = 1
        return ret

    def intersection(self, dict_2):
        """
        Finding the intersection of given two dictionaries
        py:function::

        Args:
            dict_1,dict_2 (dict): dictionaries to find intersection

        Returns:
            dict: dictionary of intersection of given dictionaries.
        """
        duplicate_dict = Myset()
        for x in self:
            if x in dict_2:
                duplicate_dict[x] = 1
        return duplicate_dict

    def minus(self, dict_2):
        """
        Finding minus of given two dictionaries
        py:function::

        Args:
            dict_1,dict_2 (dict): dictionaries to find minus

        Returns:
            dict: dictionary of minus of given dictionaries.
        """
        duplicate_dict = Myset()
        for x in self:
            if x not in dict_2:
                duplicate_dict[x] = 1
        return duplicate_dict

    def read_file(self, file_name):
        """
        Check for valid mails in given file

        Args:
            file_name (str): file containing strings

        Returns
            dict: return dictionary of valid mails as keys.
        """
        # regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+')
        regex = re.compile(r'([A-Za-z][A-Za-z0-9]+[.-_])*[A-Za-z][A-Za-z0-9]*@([A-Za-z][A-Za-z0-9]+[-])*[A-Za-z][A-Za-z0-9]*\.([A-Za-z]{2,})+')
        with open(file_name, 'r') as f:
            for x in f.readlines():
                email = x.rstrip('\n').lower()
                if re.fullmatch(regex, email):
                    if email not in self:
                        self[email] = 1

    def write_file(self, out_file):
        """
        Write input to file
        py:function::

        Args:
            self(dict), out_file(text file): dictionary to write into file
        Returns:
            None
        """
        with open(out_file, 'w') as f3:
            f3.write('\n'.join(self))
