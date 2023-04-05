#! /usr/bin/python3


def tupleise(*values):
  """
  Return a tuple based on the arguments - if there are none then return an
  empty tuple or if there are more than one create and return a new tuple from
  the arguments. If there is one arg, if it is iterable but not a string then
  create a tuple from its items, otherwise return tuple with a single-element
  equal to that argument.
    >>> tupleise(5)
    (5,)
    >>> tupleise("moo")
    ('moo',)
    >>> tupleise("moo", "cow")
    ('moo', 'cow')
    >>> tupleise(1,2,3)
    (1, 2, 3)
    >>> tupleise((1,3), (4,5))
    ((1, 3), (4, 5))
    >>> tupleise([1,3,"x"])
    (1, 3, 'x')
    >>> tupleise(tuple([1,3,"x"]))
    (1, 3, 'x')
    >>> tupleise(frozenset([1,3,"x"]))
    (1, 3, 'x')
    >>> tupleise(range(10))
    (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    >>> type(x*2 for x in range(10))
    <class 'generator'>
    >>> tupleise(x*2 for x in range(10))
    (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
    >>> type(tupleise(x*2 for x in range(10)))
    <class 'tuple'>
    >>> tupleise(True)
    (True,)
    >>> tupleise()
    ()
    >>> type(tupleise())
    <class 'tuple'>
    >>> tupleise(None)
    (None,)
    >>> tupleise(False)
    (False,)
    >>> tupleise("")
    ('',)
    >>> tupleise(lambda x: x+1) #doctest: +ELLIPSIS
    (<function <lambda> at 0x...>,)
    >>> type(tupleise(lambda x: x+1)[0])
    <class 'function'>
  """

  if not len(values):
    return tuple()
  elif len(values) > 1 or type(values[0]) is str:
    return tuple(values)

  value = values[0]

  if hasattr(value, "__iter__"):
      return tuple(iter(value))

  return (value, )


def joinifvalid(iterable, sep="\n"):
  r"""
  Filters the iterable to exclude non-True values, and then joins
  the remaining items with a separator.
  
    >>> joinifvalid(["Control", "Alt"], "+")
    'Control+Alt'
    >>> joinifvalid(["Control", "", "Alt"], "+")
    'Control+Alt'
    >>> joinifvalid(["", "",], "+") == ""
    True
    >>> joinifvalid(["Control", "Alt"], ", ")
    'Control, Alt'
    >>> print(joinifvalid(["Control", "", "Alt"], "\n"))
    Control
    Alt
  """

  return sep.join(filter(None, iterable))


if __name__ == "__main__":
    import doctest, sys

    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    if "-f" in sys.argv:
      flags |= doctest.REPORT_ONLY_FIRST_FAILURE
    doctest.testmod(optionflags=flags)
