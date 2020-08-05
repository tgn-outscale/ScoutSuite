# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
import hashlib
import hmac
from urllib.parse import quote as urlquote
import requests
import json
# from ScoutSuite.providers.osc.utils import urlquote
from ScoutSuite.providers.base.authentication_strategy import AuthenticationStrategy, AuthenticationException
from osc_sdk_python import Gateway


class OutscaleAuthenticationStrategy(AuthenticationStrategy):
    def authenticate(self, profile=None, osc_access_key=None,
                     osc_secret_access_key=None, **kwargs):
        try:
            session = Gateway()
            return session
        except Exception as e:
            raise AuthenticationException(e)
