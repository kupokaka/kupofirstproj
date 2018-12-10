import os
from google.appengine.ext import vendor

# Adding any third party libraries that are not built into the
# bundled GAE runtime.
#
# install libs with: pip install -t lib <library_name>
#
# Also can use requirements.txt to list libs
#    and then run: pip install -t lib -r requirements.txt
#
# Add any libraries installed in the "lib" folder.
#
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))

