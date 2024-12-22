import unittest
import inspect

from bitfield import BitFieldMeta


class TestBitField(unittest.TestCase):
    

    def test_define_bitfield(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

    def test_instantiate_default_bitfield(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        _ = DateBitField()

    def test_instantiate_bitfield_with_field_value(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        _ = DateBitField(day=23)

    def test_bitfield_without_fields_raises_type_error(self):

        with self.assertRaises(TypeError):
            class DateBitField(metaclass=BitFieldMeta):
                pass

    def test_mismatched_constructor_argument_names_raises_type_error(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5
            month: 4
            year: 14

        with self.assertRaises(TypeError) as exc_info:
            _ = DateBitField(day=13, mnth=5, yr=1999)
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField.__init__() got unexpected arguments: "
            "'mnth', 'yr'"
        )

    def test_non_integer_annotation_values_raises_type_error(self):

        with self.assertRaises(TypeError) as exc_info:

            class DateBitField(metaclass=BitFieldMeta):
                day: str("Wednesday")
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' has annotation 'Wednesday' "
            "that is not an integer"
        )

    def test_zero_field_width_raises_type_error(self):

        with self.assertRaises(TypeError) as exc_info:

            class DateBitField(metaclass=BitFieldMeta):
                day: 0
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' has non-positive field width 0"
        )

    def test_negative_field_width_raises_type_error(self):

        with self.assertRaises(TypeError) as exc_info:

            class DateBitField(metaclass=BitFieldMeta):
                day: -1
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' has non-positive field width -1"
        )

    def test_field_name_with_leading_underscore_raises_type_error(self):

        with self.assertRaises(TypeError) as exc_info:

            class DateBitField(metaclass=BitFieldMeta):
                _day: 5
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field '_day' begins with underscore"
        )

    def test_initialization_out_of_lower_bound_range_raises_type_error(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        with self.assertRaises(ValueError) as exc_info:
            _ = DateBitField(day=-1)
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value -1 "
            "which is out of range 0-31 for a 5 bit fields"
        )

    def test_initialization_out_of_upper_bound_range_raises_type_error(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        with self.assertRaises(ValueError) as exc_info:
            _ = DateBitField(day=32)
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value 32 "
            "which is out of range 0-31 for a 5 bit fields"
        )

    def test_fields_are_default_initialized_to_zero(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField()
        self.assertEqual(d.day, 0)

    def test_field_values_can_be_retreived(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField(day=17)
        self.assertEqual(d.day, 17)

    def test_conversion_to_int(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5
            month: 4
            year: 14

        d = DateBitField(day=25, month=3, year=2010)
        i = int(d)
        self.assertEqual(
            i,
            # underscres in numeric literals are ignored
            0b00011111011010_0011_11001
            # <--------2010> <-3> <-25>
        )

    def test_conversion_to_bytes(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5
            month: 4
            year: 14

        d = DateBitField(day=25, month=3, year=2010)
        b = d.to_bytes()
        self.assertEqual(
            b,
            # underscres in numeric literals are ignored
            (0b00011111011010_0011_11001).to_bytes(3, 'little', signed=False)
             # <--------2010> <-3> <-25>
        )

    def test_assigning_out_of_lower_range_value_to_field_raises_value_error(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField()
        with self.assertRaises(ValueError) as exc_info:
            d.day = -1
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value -1 "
            "which is out of range 0-31 for a 5 bit fields"
        )

    def test_assigning_out_of_upper_range_value_to_field_raises_value_error(self):

        class DateBitField(metaclass=BitFieldMeta):
            day: 5

        d = DateBitField()
        with self.assertRaises(ValueError) as exc_info:
            d.day = 32
        self.assertEqual(
            str(exc_info.exception),
            "DateBitField field 'day' got value 32 "
            "which is out of range 0-31 for a 5 bit fields"
        )


if __name__ == "__main__":

    unittest.main()

    # class DateBitField(metaclass=BitFieldMeta):
    #     day: 5

    # b = DateBitField
    # print(dir(b))
    # print(inspect.get_annotations(b))
    # print(b._field_widths)

    # class DateBitField(metaclass=BitFieldMeta):
    #         day: 5
    #         month: 4
    #         year: 14
    
    # b = DateBitField(day=13, month=5, year=1999)
    # print(dir(b))
    # print(b._field_widths)




