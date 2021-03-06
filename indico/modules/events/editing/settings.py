# This file is part of Indico.
# Copyright (C) 2002 - 2020 CERN
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see the
# LICENSE file for more details.

from __future__ import unicode_literals

from collections import OrderedDict

from indico.core.settings.converters import OrderedDictConverter
from indico.modules.events.settings import EventSettingsProxy


editing_settings = EventSettingsProxy('editing', {
    'paper_review_conditions': OrderedDict(),
    'slides_review_conditions': OrderedDict(),
    'poster_review_conditions': OrderedDict(),
    'editable_types': ['paper'],
}, converters={
    'paper_review_conditions': OrderedDictConverter,
    'slides_review_conditions': OrderedDictConverter,
    'poster_review_conditions': OrderedDictConverter
})
