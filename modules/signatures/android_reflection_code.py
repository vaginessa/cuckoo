# Copyright (C) Check Point Software Technologies LTD.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

from lib.cuckoo.common.abstracts import Signature

class AndroidReflectionCode(Signature):
    name = "android_reflection_code"
    description = "Application Uses Reflection Methods (Static)"
    severity = 3
    categories = ["android"]
    authors = ["Check Point Software Technologies LTD"]
    minimum = "0.5"

    def run(self):
        try:
            if self.results["apkinfo"]["static_method_calls"]["is_reflection_code"] is True:
                return True
            else:
                return False
        except:
            return False