
def get_resource(filename):
    import pkg_resources, os
    return pkg_resources.resource_filename("sequentialdownload", os.path.join("data", filename))
