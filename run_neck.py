# -*- coding: utf-8 -*-


import logging
from neck import neck_app
neck_app.secret_key = 'erlenmeyer'

from neck import views

neck_app.run(debug=True)