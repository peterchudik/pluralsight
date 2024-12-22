from positive import Positive

class Planet:
    def __init__(
        self,
        name,
        radius_metres,
        mass_kilograms,
        orbital_period_seconds,
        surface_temperature_kelvin,
    ):
        # This is using bellow property setters
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    # using property getter and setter we can protect and validate nonsensical values
    # negative aspect is that the code exploded and ve have lot of duplicate code
    # self encapsulation = allways acessing attributes via encapsulating properties
    # property object is descriptor
    # A descriptor is what we call any object that defines __get__(), __set__(), or __delete__().
    # Optionally, descriptors can have a __set_name__() method.

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value

    #############################################################################
    # @property
    # def radius_metres(self):
    #     return self._radius_metres

    # @radius_metres.setter
    # def radius_metres(self, value):
    #     if value <= 0:
    #         raise ValueError(f"radius_metres value {value} is not positive.")
    #     self._radius_metres = value

    # @property
    # def mass_kilograms(self):
    #     return self._mass_kilograms

    # @mass_kilograms.setter
    # def mass_kilograms(self, value):
    #     if value <= 0:
    #         raise ValueError(f"mass_kilograms value {value} is not positive.")
    #     self._mass_kilograms = value

    # @property
    # def orbital_period_seconds(self):
    #     return self._orbital_period_seconds

    # @orbital_period_seconds.setter
    # def orbital_period_seconds(self, value):
    #     if value <= 0:
    #         raise ValueError(f"orbital_period_seconds value {value} is not positive.")
    #     self._orbital_period_seconds = value

    # @property
    # def surface_temperature_kelvin(self):
    #     return self._surface_temperature_kelvin

    # @surface_temperature_kelvin.setter
    # def surface_temperature_kelvin(self, value):
    #     if value <= 0:
    #         raise ValueError(f"surface_temperature_kelvin value {value} is not positive.")
    #     self._surface_temperature_kelvin = value

    #############################################################################
    # except property decorators, we use "old" syntax
    # old" syntax is step back from property decorator syntax

    # def _get_radius_metres(self):
    #     return self._radius_metres

    # def _set_radius_metres(self, value):
    #     if value <= 0:
    #         raise ValueError(f"radius_metres value {value} is not positive.")
    #     self._radius_metres = value

    # # at the class definition, this property object is linked to Class !!! not to the instance
    # radius_metres = property(
    #     fget=_get_radius_metres,
    #     fset=_set_radius_metres,
    # )

    # def _get_mass_kilograms(self):
    #     return self._mass_kilograms

    # def _set_mass_kilograms(self, value):
    #     if value <= 0:
    #         raise ValueError(f"mass_kilograms value {value} is not positive.")
    #     self._mass_kilograms = value

    # mass_kilograms = property(
    #     fget=_get_mass_kilograms,
    #     fset=_set_mass_kilograms,
    # )

    # def _get_orbital_period_seconds(self):
    #     return self._orbital_period_seconds

    # def _set_orbital_period_seconds(self, value):
    #     if value <= 0:
    #         raise ValueError(f"orbital_period_seconds value {value} is not positive.")
    #     self._orbital_period_seconds = value

    # orbital_period_seconds = property(
    #     fget=_get_orbital_period_seconds,
    #     fset=_set_orbital_period_seconds,
    # )

    # def _get_surface_temperature_kelvin(self):
    #     return self._surface_temperature_kelvin

    # def _set_surface_temperature_kelvin(self, value):
    #     if value <= 0:
    #         raise ValueError(f"surface_temperature_kelvin value {value} is not positive.")
    #     self._surface_temperature_kelvin = value

    # surface_temperature_kelvin = property(
    #     fget=_get_surface_temperature_kelvin,
    #     fset=_set_surface_temperature_kelvin,
    # )

    #############################################################################
    # defining properties using ur own descriptor

    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()
