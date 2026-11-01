#
# ABOUT
# Label pdf generation for Artisan
#
# COPYRIGHT (C) 2026 Natalie Moore
#
# LICENSE
# This program or module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# MAINTAINER
# Natalie Moore, 2026
#
# AUTHOR
# Natalie Moore, 2023

import logging
import os

from typing import TypedDict, Final

from artisanlib.util import getResourcePath

from blabel import LabelWriter
from PyQt6.QtCore import QDir


_log: Final[logging.Logger] = logging.getLogger(__name__)

class ArtisanLabelWriter():
    def __init__(self, target_directory: str, template_name: str):
        self.basedir = os.path.join(getResourcePath(), "Labels", template_name)
        #raise RuntimeError(self.basedir)

    def generate_label(self, propertiesDialog):
        label_writer = LabelWriter(
            os.path.join(self.basedir, "item_template.html"),
            default_stylesheets=(os.path.join(self.basedir, "style.css"),)
        )
        in_wt, out_wt, units = propertiesDialog.org_weight
        weight_str = f"{out_wt}{units}"
        records = [
            dict(
                url="http://roast.pumpingstationone.org",
                name=propertiesDialog.org_title,
                beans=propertiesDialog.org_beans,
                weight=weight_str,
                roastDate=propertiesDialog.aw.qmc.roastdate.date().toString(),
            )
        ]

        # org_beans, org_title, org_weight, date, (qr code)

        label_writer.write_labels(records, target="/home/natalie/barcode_and_dynamic_picture.pdf")
