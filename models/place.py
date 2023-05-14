#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Place Module

This Module inherits from BaseModel class.
Place Module contains the attributes to be assigned
to the Places created.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class

    Attributes:
        city_id (str): The UUID of City the Place is located
        user_id (str): The UUID of the User of the Place
        name (str): The name of the place
        description (str): Description of the place
        number_rooms (int): The number of rooms
        number_bathrooms (int): The number of bathrooms
        max_guest (int): The max number of guests for the Place
        price_by_night (int): The price per night
        latitude (float): The latitude of the Place
        longitude (float): The longitude of the Place
        amenity_ids (list): A list that contains all the Amenities in the Place

    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
