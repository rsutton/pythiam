# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path

__all__ = [
    "__title__", "__summary__", "__uri__", "__version__",
    "__author__", "__email__", "__license__", "__copyright__",
]

try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None

__title__ = "prometheus"
__summary__ = "AWS IAM User Account Tool"
__uri__ = "https://github.com/rsutton/prometheus"
__version__ = "1.0.0-alpha"
__author__ = "Raymond Sutton"
__email__ = "ray.sutton@gmail.com"
__license__ = "Apache License, Version 2.0"
__copyright__ = "2018 %s" % __author__