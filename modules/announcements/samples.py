# Copyright 2012 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Sample announcements."""

__author__ = 'Pavel Simakov (psimakov@google.com)'

import datetime


SAMPLE_ANNOUNCEMENT_1 = {
    'edit_url': None,
    'title': 'Site is up',
    'date': datetime.date(2012, 10, 6),
    'is_html': False,    
    'is_draft': True,
    'html': """
Site is ready so the course can be started.
        """}

SAMPLE_ANNOUNCEMENTS = [SAMPLE_ANNOUNCEMENT_1]

