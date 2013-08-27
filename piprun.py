
import subprocess

import fileinfo


def process(package_name):
    if fileinfo.exists(package_name):
        return

    env_name = '%senv' % (package_name, )
    cmds = ['virtualenv envs/%s' % env_name,
        '. envs/%s/bin/activate' % env_name,
        'pip install wheel',
        'pip install numpy',
        'pip install Cython',
        'pip install --no-deps %s' % package_name,
        'python extractdatapip.py %s' % package_name,
        'deactivate',
        'rm -r envs/%s' % (env_name, )
        ]
    cmd = ' && '.join(cmds)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    process('pandas')
