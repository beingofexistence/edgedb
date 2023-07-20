#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2016-present MagicStack Inc. and the EdgeDB authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from __future__ import annotations
import typing


class Schema:
    pass


class Reducible:
    """An interface implemented by all non-builtin objects stored in schema."""

    def schema_reduce(self) -> typing.Any:
        """Return a primitive representation of the object.

        The return value must consist of primitive Python objects.
        """
        raise NotImplementedError

    @classmethod
    def schema_restore(
        cls,
        data: typing.Any,
    ) -> Reducible:
        """Restore object from data returned by *schema_reduce*."""
        raise NotImplementedError


class Object:
    pass


class Database(Object):
    pass


class Migration(Object):
    pass


class Constraint(Object):
    pass


class Callable(Object):
    pass


class Function(Callable):
    pass


class Operator(Callable):
    pass


class Cast(Callable):
    pass


class Parameter(Object):
    pass


class Type(Object):
    pass


class ScalarType(Type):
    pass


class ObjectType(Type):
    pass


class Collection(Type):
    pass


class Tuple(Collection):
    pass


class Array(Collection):
    pass


class Range(Collection):
    pass


class MultiRange(Collection):
    pass


class Pointer(Object):
    pass


class Property(Pointer):
    pass


class Link(Pointer):
    pass


class Expression:
    pass
