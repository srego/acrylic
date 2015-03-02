# coding: utf-8

from itertools import izip


def datarow_constructor(fields):

    class DataRow(tuple):

        __slots__ = ()

        _fields = tuple(fields)

        def __new__(cls, values):
            return tuple.__new__(cls, tuple(values))

        def __repr__(self):
            return 'DataRow(%s)' % ', '.join([unicode(item) for item in self])

        def __getitem__(self, item):
            if isinstance(item, basestring):
                try:
                    index = self._fields.index(item)  # O(n) time
                except ValueError:
                    raise ValueError("Column `%s` does not exist in DataRow.")
                return super(DataRow, self).__getitem__(index)
            elif isinstance(item, (int, long, slice)):
                return super(DataRow, self).__getitem__(item)
            elif isinstance(item, (list, tuple)):
                columns = []
                for subitem in item:
                    if not isinstance(subitem, basestring):
                        raise KeyError("Multi-column access must be done with "
                                       "a list or tuple of strings. A %s was "
                                       "found in the list." % type(subitem))
                    columns.append(self[subitem])
                return columns
            else:
                raise Exception("Unrecognized index type: %s" % type(item))

        def items(self):
            return izip(self._fields, self)

    return DataRow
