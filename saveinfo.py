
import marshal
import pkg_resources
import sys

import fileinfo

DATA_DIR = 'data/'

def save_data(name, package_info):
    file_name = fileinfo.get_file_name(name)
    with open(file_name, 'wb') as f:
        marshal.dump(package_info, f)

def search_packages_info(query):

    """
    Gather details from installed distributions. Print distribution name,
    version, location, and installed files. Installed files requires a
    pip generated 'installed-files.txt' in the distributions '.egg-info'
    directory.
    """
    installed_packages = dict(
        [(p.project_name.lower(), p) for p in pkg_resources.working_set])


    for name in query:
        normalized_name = name.lower()
        if normalized_name in installed_packages:
            dist = installed_packages[normalized_name]

            try:
                metadata = dist.get_metadata('METADATA')
            except:
                try:
                    metadata = list(dist._get_metadata('PKG-INFO'))
                except:
                    metadata = None

            package = {
                'name': dist.project_name,
                'version': dist.version,
                'requires': [(dep.project_name, dep.specs) for dep in dist.requires()],
                'metadata' : metadata,
            }
            save_data(name, package)

if __name__ == '__main__':
    data = search_packages_info(sys.argv[1:])
