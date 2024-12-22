import unittest

from frozen_sorted_set import SortedFrozenSet

from collections.abc import Container, Sized, Iterable, Sequence, Set

# Test class constructor
class TestConstruction(unittest.TestCase):

    def test_construct_empty(self):
        s = SortedFrozenSet([])

    def test_construct_from_non_empty_list(self):
        s = SortedFrozenSet([1, 8, 3, 4, 2])

    def test_construct_from_iterator(self):
        items = [1, 8, 3, 4, 2]
        iterator = iter(items)
        s = SortedFrozenSet(iterator)

    def test_construct_no_args(self):
        s = SortedFrozenSet()

# Test container protocol
class TestContainerProtocol(unittest.TestCase):

    # freshly executed before every test method
    def setUp(self):
        self.s = SortedFrozenSet([1, 8, 3, 4, 2])

    def test_positive_contained(self):
        self.assertTrue(1 in self.s)

    def test_negative_contained(self):
        self.assertFalse(7 in self.s)

    def test_positive_not_contained(self):
        self.assertTrue(7 not in self.s)

    def test_negative_not_contained(self):
        self.assertFalse(1 not in self.s)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedFrozenSet, Container))

# Test sized protocol
class TestSizedProtocol(unittest.TestCase):

    def test_empty_with_default(self):
        s = SortedFrozenSet()
        self.assertEqual(len(s), 0)

    def test_empty(self):
        s = SortedFrozenSet([])
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedFrozenSet([42])
        self.assertEqual(len(s), 1)

    def test_ten(self):
        s = SortedFrozenSet(range(10))
        self.assertEqual(len(s), 10)
    
    def test_with_duplicates(self):
        s = SortedFrozenSet([5, 5, 5])
        self.assertEqual(len(s), 1)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedFrozenSet, Sized))

# Test iterable protocol
class TestIterableProtocol(unittest.TestCase):

    # freshly executed before every test method
    def setUp(self):
        self.s = SortedFrozenSet([7, 2, 1, 1, 9])

    def test_iter(self):
        iterator = iter(self.s)
        self.assertEqual(next(iterator),1)
        self.assertEqual(next(iterator),2)
        self.assertEqual(next(iterator),7)
        self.assertEqual(next(iterator),9)
        self.assertRaises(
            StopIteration,
            lambda: next(iterator)
        )

    def test_for_loop(self):
        expected = [1, 2, 7, 9]
        index = 0
        for item in self.s:
             self.assertEqual(item, expected[index])
             index += 1

    def test_protocol(self):
        self.assertTrue(issubclass(SortedFrozenSet, Iterable))


# Test sequence protocol
class TestSequenceProtocol(unittest.TestCase):

    def setUp(self):
        self.s = SortedFrozenSet([1, 4, 9, 13, 15])

    def test_index_zero(self):
        self.assertEqual(self.s[0], 1)
    
    def test_index_four(self):
        self.assertEqual(self.s[4], 15)

    def test_index_one_beyond_the_end(self):
        with self.assertRaises(IndexError):
            self.s[5]
    
    def test_index_minus_one(self):
        self.assertEqual(self.s[-1], 15)

    def test_index_minus_five(self):
        self.assertEqual(self.s[-5], 1)

    def test_index_one_before_the_beginning(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    def test_slice_from_start(self):
        self.assertEqual(self.s[:3], SortedFrozenSet([1, 4, 9]))

    def test_slice_to_end(self):
        self.assertEqual(self.s[3:], SortedFrozenSet([13, 15]))

    def test_slice_empty(self):
        self.assertEqual(self.s[10:], SortedFrozenSet([]))

    def test_slice_arbitrary(self):
        self.assertEqual(self.s[2:4], SortedFrozenSet([9, 13]))

    def test_slice_step(self):
        self.assertEqual(self.s[0:5:2], SortedFrozenSet([1, 9, 15]))

    def test_slice_full(self):
        self.assertEqual(self.s[:], self.s)

    def test_reversed(self):
        s = SortedFrozenSet([1, 3, 5, 7])
        r = reversed(s)
        self.assertEqual(next(r), 7)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 1)
        self.assertRaises(StopIteration, lambda: next(r))
    
    def test_index_positive(self):
        s = SortedFrozenSet([1, 5, 8, 9])
        self.assertEqual(s.index(8), 2)

    def test_index_negative(self):
        s = SortedFrozenSet([1, 5, 8, 9])
        with self.assertRaises(ValueError):
            s.index(15)

    def test_count_zero(self):
        s = SortedFrozenSet([1, 5, 7, 9])
        self.assertEqual(s.count(15), 0)

    def test_count_one(self):
        s = SortedFrozenSet([1, 5, 7, 9])
        self.assertEqual(s.count(9), 1)

    def test_add_disjoint(self):
        s = SortedFrozenSet([1, 2, 3])
        t = SortedFrozenSet([4, 5, 6])
        self.assertEqual(s + t, SortedFrozenSet([1, 2, 3, 4, 5, 6]))

    def test_add_equal(self):
        s = SortedFrozenSet([2, 4, 6])
        self.assertEqual(s + s, s)

    def test_add_intersecting(self):
        s = SortedFrozenSet([1, 2, 3])
        t = SortedFrozenSet([3, 4, 5])
        self.assertEqual(s + t, SortedFrozenSet([1, 2, 3, 4, 5]))

    def test_add_error_left(self):
        s = SortedFrozenSet([1, 2, 3])
        t = (3, 4, 5)
        with self.assertRaises(TypeError):
            _ = s + t

    def test_add_error_right(self):
        s = (3, 4, 5)
        t = SortedFrozenSet([1, 2, 3])
        with self.assertRaises(TypeError):
            _ = s + t

    def test_repetition_zero_right(self):
        s = SortedFrozenSet([4, 5, 6])
        self.assertEqual(s * 0, SortedFrozenSet())

    def test_repetition_negative_right(self):
        s = SortedFrozenSet([4, 5, 6])
        self.assertEqual(s * -1, SortedFrozenSet())

    def test_repetition_nonzero_right(self):
        s = SortedFrozenSet([4, 5, 6])
        self.assertEqual(s * 100, s)

    def test_repetition_zero_left(self):
        s = SortedFrozenSet([4, 5, 6])
        self.assertEqual(0 * s, SortedFrozenSet())

    def test_repetition_negative_left(self):
        s = SortedFrozenSet([4, 5, 6])
        self.assertEqual(-1 * s, SortedFrozenSet())

    def test_repetition_nonzero_left(self):
        s = SortedFrozenSet([4, 5, 6])
        self.assertEqual(100 * s, s)

    def test_protocol(self):
        self.assertTrue(issubclass(SortedFrozenSet, Sequence))


# Test repr protocol
class TestReprProtocol(unittest.TestCase):

    def test_repr_empty(self):
        s = SortedFrozenSet()
        self.assertEqual(repr(s),"SortedFrozenSet()")
    
    def test_repr_one(self):
        s = SortedFrozenSet([42, 40, 19])
        self.assertEqual(repr(s),"SortedFrozenSet([19, 40, 42])")


# Test equality protocol
class TestEqualityProtocol(unittest.TestCase):

    def test_positive_equal(self):
        self.assertTrue(
            SortedFrozenSet([1, 2, 3]) == SortedFrozenSet([3, 2, 1])
        )

    def test_negative_equal(self):
        self.assertFalse(
            SortedFrozenSet([1, 2, 3]) == SortedFrozenSet([4, 5, 6])
        )

    def test_type_mismatch(self):
        self.assertFalse(
            SortedFrozenSet([1, 2, 3]) == [4, 5, 6]
        )

    def test_identical(self):
        s = SortedFrozenSet([10, 11, 12])
        self.assertTrue(s == s)


# Test inequality protocol
# default __ne__ will negate __eq__ operator
# however we can overide __ne__ if we wanted to
class TestInequalityProtocol(unittest.TestCase):

    def test_positive_unequal(self):
        self.assertTrue(SortedFrozenSet([1, 2, 3]) != SortedFrozenSet([4, 5, 6]))

    def test_negative_unequal(self):
        self.assertFalse(SortedFrozenSet([1, 2, 3]) != SortedFrozenSet([3, 2, 1]))

    def test_type_mismatch(self):
        self.assertTrue(SortedFrozenSet([1, 2, 3]) != [1, 2, 3])

    def test_identical(self):
        s = SortedFrozenSet([10, 11, 12])
        self.assertFalse(s != s)

# Test hashable protocol
class TestHashableProtocol(unittest.TestCase):

    def test_equal_sets_have_the_same_hash_code(self):
        self.assertEqual(
            hash(SortedFrozenSet([1, 2, 3])),
            hash(SortedFrozenSet([1, 2, 3])),
        )

# Test relational set protocol
class TestRelationalSetProtocol(unittest.TestCase):

    def test_lt_positive(self):
        s = SortedFrozenSet({1, 2})
        t = SortedFrozenSet({1, 2, 3})
        self.assertTrue(s < t)

    def test_lt_negative(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({1, 2, 3})
        self.assertFalse(s < t)

    def test_le_lt_positive(self):
        s = SortedFrozenSet({1, 2})
        t = SortedFrozenSet({1, 2, 3})
        self.assertTrue(s <= t)

    def test_le_eq_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({1, 2, 3})
        self.assertTrue(s <= t)

    def test_le_negative(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({1, 2})
        self.assertFalse(s <= t)

    def test_gt_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({1, 2})
        self.assertTrue(s > t)

    def test_gt_negative(self):
        s = SortedFrozenSet({1, 2})
        t = SortedFrozenSet({1, 2, 3})
        self.assertFalse(s > t)

    def test_ge_gt_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({1, 2})
        self.assertTrue(s > t)

    def test_ge_eq_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({1, 2, 3})
        self.assertTrue(s >= t)

    def test_ge_negative(self):
        s = SortedFrozenSet({1, 2})
        t = SortedFrozenSet({1, 2, 3})
        self.assertFalse(s >= t)


# Test set relational methods
class TestSetRelationalMethods(unittest.TestCase):

    def test_issubset_proper_positive(self):
        s = SortedFrozenSet({1, 2})
        t = [1, 2, 3]
        self.assertTrue(s.issubset(t))

    def test_issubset_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [1, 2, 3]
        self.assertTrue(s.issubset(t))

    def test_issubset_negative(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [1, 2]
        self.assertFalse(s.issubset(t))

    def test_issuperset_proper_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [1, 2]
        self.assertTrue(s.issuperset(t))

    def test_issuperset_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [1, 2, 3]
        self.assertTrue(s.issuperset(t))

    def test_issuperset_negative(self):
        s = SortedFrozenSet({1, 2})
        t = [1, 2, 3]
        self.assertFalse(s.issuperset(t))

    def test_isdisjoint_positive(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [4, 5, 6]
        self.assertTrue(s.isdisjoint(t))

    def test_isdisjoint_negative(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [3, 4, 5]
        self.assertFalse(s.isdisjoint(t))


# Test operations set protocol
class TestOperationsSetProtocol(unittest.TestCase):

    def test_intersection(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({2, 3, 4})
        self.assertEqual(s & t, SortedFrozenSet({2, 3}))

    def test_union(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({2, 3, 4})
        self.assertEqual(s | t, SortedFrozenSet({1, 2, 3, 4}))

    def test_symmetric_difference(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({2, 3, 4})
        self.assertEqual(s ^ t, SortedFrozenSet({1, 4}))

    def test_difference(self):
        s = SortedFrozenSet({1, 2, 3})
        t = SortedFrozenSet({2, 3, 4})
        self.assertEqual(s - t, SortedFrozenSet({1}))


# Test set operations methods
class TestSetOperationsMethods(unittest.TestCase):

    def test_intersection(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.intersection(t), SortedFrozenSet({2, 3}))

    def test_union(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.union(t), SortedFrozenSet({1, 2, 3, 4}))

    def test_symmetric_difference(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.symmetric_difference(t), SortedFrozenSet({1, 4}))

    def test_difference(self):
        s = SortedFrozenSet({1, 2, 3})
        t = [2, 3, 4]
        self.assertEqual(s.difference(t), SortedFrozenSet({1}))


# Test set protocol
class TestSetProtocol(unittest.TestCase):
    def test_protocol(self):
        self.assertTrue(issubclass(SortedFrozenSet, Set))


if __name__ == "__main__":
    result = unittest.main()


