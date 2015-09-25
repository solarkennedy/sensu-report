#!/usr/bin/env python
import time

import sensu_report

def test_pretty_date():
    """ Lets put in some epochs we expect from sensu and make sure it is pretty
    """
    fakenow = int(time.time()-5)
    assert sensu_report.pretty_date(fakenow) == "just now"
