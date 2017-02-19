#  python setup.py bdist_egg
# use above command to create plugin egg



from setuptools import setup

__plugin_name__ = "SequentialDownload"
__author__ = "Hrushikesh Mohapatra"
__author_email__ = "hrushikesh.iitb@gmail.com"
__version__ = "1.0"
__url__ = "-"
__license__ = "GPLv3"
__description__ = "-"
__long_description__ = """---"""
__pkg_data__ = {__plugin_name__.lower(): ["template/*", "data/*"]}

setup(
    name=__plugin_name__,
    version=__version__,
    description=__description__,
    author=__author__,
    author_email=__author_email__,
    url=__url__,
    license=__license__,
    long_description=__long_description__ if __long_description__ else __description__,

    packages=[__plugin_name__.lower()],
    package_data = __pkg_data__,

    entry_points="""
    [deluge.plugin.core]
    %s = %s:CorePlugin
    [deluge.plugin.gtkui]
    %s = %s:GtkUIPlugin
    [deluge.plugin.web]
    %s = %s:WebUIPlugin
    """ % ((__plugin_name__, __plugin_name__.lower())*3)
)
