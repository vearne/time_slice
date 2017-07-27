Introduction
============
sometimes we need calculate time slice, time_slice is package to help you.

Copyright / License
===================

GPLv3

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

for example
===================
```
from time_slice import TimeSliceUtils

def test_merge1():
    t1 = {
        "start_time": "2016-11-01",
        "end_time": "2016-12-01"
    }

    t2 = {
        "start_time": "2016-11-10",
        "end_time": "2016-12-03"
    }

    print TimeSliceUtils.merge([t1, t2])
    
def test_minus():
    t1 = {
        "start_time": datetime(2016, 11, 1),
        "end_time": datetime(2016, 12, 1),
    }

    t2 = {
        "start_time": datetime(2016, 11, 11),
        "end_time": datetime(2016, 11, 14),
    }

    # minus
    print TimeSliceUtils.minus([t1], [t2])
    
```
You can use both string and datetime, beacuse we just use compare relationship between them. 

