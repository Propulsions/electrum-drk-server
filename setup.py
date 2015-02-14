from setuptools import setup

setup(
    name="electrum-drk-server",
    version="0.9",
    scripts=['run_electrum_drk_server','electrum-drk-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumdrkserver':'src'
        },
    py_modules=[
        'electrumdrkserver.__init__',
        'electrumdrkserver.utils',
        'electrumdrkserver.storage',
        'electrumdrkserver.deserialize',
        'electrumdrkserver.networks',
        'electrumdrkserver.blockchain_processor',
        'electrumdrkserver.server_processor',
        'electrumdrkserver.processor',
        'electrumdrkserver.version',
        'electrumdrkserver.ircthread',
        'electrumdrkserver.stratum_tcp',
        'electrumdrkserver.stratum_http'
    ],
    description="Darkcoin Electrum Server",
    author="Thomas Voegtlin, Propulsion",
    author_email="thomasv1@gmx.de, Propulsion@DarkcoinTalk.org",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/, https://github.com/Propulsions/electrum-drk-server/",
    long_description="""Server for the Electrum Lightweight Darkcoin Wallet"""
)


