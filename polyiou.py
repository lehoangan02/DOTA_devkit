# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.3.0
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _polyiou
else:
    import _polyiou

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _polyiou.delete_SwigPyIterator

    def value(self):
        return _polyiou.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _polyiou.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _polyiou.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _polyiou.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _polyiou.SwigPyIterator_equal(self, x)

    def copy(self):
        return _polyiou.SwigPyIterator_copy(self)

    def next(self):
        return _polyiou.SwigPyIterator_next(self)

    def __next__(self):
        return _polyiou.SwigPyIterator___next__(self)

    def previous(self):
        return _polyiou.SwigPyIterator_previous(self)

    def advance(self, n):
        return _polyiou.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _polyiou.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _polyiou.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _polyiou.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _polyiou.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _polyiou.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _polyiou.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _polyiou:
_polyiou.SwigPyIterator_swigregister(SwigPyIterator)
class VectorDouble(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _polyiou.VectorDouble_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _polyiou.VectorDouble___nonzero__(self)

    def __bool__(self):
        return _polyiou.VectorDouble___bool__(self)

    def __len__(self):
        return _polyiou.VectorDouble___len__(self)

    def __getslice__(self, i, j):
        return _polyiou.VectorDouble___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _polyiou.VectorDouble___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _polyiou.VectorDouble___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _polyiou.VectorDouble___delitem__(self, *args)

    def __getitem__(self, *args):
        return _polyiou.VectorDouble___getitem__(self, *args)

    def __setitem__(self, *args):
        return _polyiou.VectorDouble___setitem__(self, *args)

    def pop(self):
        return _polyiou.VectorDouble_pop(self)

    def append(self, x):
        return _polyiou.VectorDouble_append(self, x)

    def empty(self):
        return _polyiou.VectorDouble_empty(self)

    def size(self):
        return _polyiou.VectorDouble_size(self)

    def swap(self, v):
        return _polyiou.VectorDouble_swap(self, v)

    def begin(self):
        return _polyiou.VectorDouble_begin(self)

    def end(self):
        return _polyiou.VectorDouble_end(self)

    def rbegin(self):
        return _polyiou.VectorDouble_rbegin(self)

    def rend(self):
        return _polyiou.VectorDouble_rend(self)

    def clear(self):
        return _polyiou.VectorDouble_clear(self)

    def get_allocator(self):
        return _polyiou.VectorDouble_get_allocator(self)

    def pop_back(self):
        return _polyiou.VectorDouble_pop_back(self)

    def erase(self, *args):
        return _polyiou.VectorDouble_erase(self, *args)

    def __init__(self, *args):
        _polyiou.VectorDouble_swiginit(self, _polyiou.new_VectorDouble(*args))

    def push_back(self, x):
        return _polyiou.VectorDouble_push_back(self, x)

    def front(self):
        return _polyiou.VectorDouble_front(self)

    def back(self):
        return _polyiou.VectorDouble_back(self)

    def assign(self, n, x):
        return _polyiou.VectorDouble_assign(self, n, x)

    def resize(self, *args):
        return _polyiou.VectorDouble_resize(self, *args)

    def insert(self, *args):
        return _polyiou.VectorDouble_insert(self, *args)

    def reserve(self, n):
        return _polyiou.VectorDouble_reserve(self, n)

    def capacity(self):
        return _polyiou.VectorDouble_capacity(self)
    __swig_destroy__ = _polyiou.delete_VectorDouble

# Register VectorDouble in _polyiou:
_polyiou.VectorDouble_swigregister(VectorDouble)

def iou_poly(p, q):
    return _polyiou.iou_poly(p, q)

