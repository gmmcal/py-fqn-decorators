
from setuptools import setup
setup(**{'author': 'Mattias Sluis',
 'author_email': 'mattias.sluis@kpn.com',
 'classifiers': ['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Topic :: Internet :: WWW/HTTP'],
 'description': 'Easily create multi-purpose decorators that have access to '
                'the FQN of the original function.',
 'include_package_data': True,
 'install_requires': [],
 'long_description': 'FQN Decorators\n'
                     '==============\n'
                     '\n'
                     '.. image:: '
                     'https://secure.travis-ci.org/kpn-digital/py-fqn-decorators.svg?branch=master\n'
                     '    :target:  '
                     'http://travis-ci.org/kpn-digital/py-fqn-decorators?branch=master\n'
                     '\n'
                     '.. image:: '
                     'https://img.shields.io/codecov/c/github/kpn-digital/py-fqn-decorators/master.svg\n'
                     '    :target: '
                     'http://codecov.io/github/kpn-digital/py-fqn-decorators?branch=master\n'
                     '\n'
                     '.. image:: '
                     'https://img.shields.io/pypi/v/fqn-decorators.svg\n'
                     '    :target: '
                     'https://pypi.python.org/pypi/fqn-decorators\n'
                     '\n'
                     '.. image:: '
                     'https://readthedocs.org/projects/fqn-decorators/badge/?version=latest\n'
                     '    :target: '
                     'http://fqn-decorators.readthedocs.org/en/latest/?badge=latest\n'
                     '\n'
                     '\n'
                     'Installation\n'
                     '------------\n'
                     '.. start_installation\n'
                     '\n'
                     'At the command line::\n'
                     '\n'
                     '    $ pip install fqn-decorators\n'
                     '\n'
                     '\n'
                     '.. end_installation\n'
                     '\n'
                     'Usage\n'
                     '-----\n'
                     '.. start_usage\n'
                     '.. py:currentmodule:: fqn_decorators.decorators\n'
                     '\n'
                     'Introduction\n'
                     '------------\n'
                     '\n'
                     'By extending the :class:`~Decorator` class you can '
                     'create simple decorators.\n'
                     'Implement the :meth:`~Decorator.before` and/or '
                     ':meth:`~Decorator.after` methods to perform actions '
                     'before or after execution of the decorated item.\n'
                     'The :meth:`~Decorator.before` method can access the '
                     'arguments of the decorated item by changing the '
                     ':attr:`~Decorator.args` and :attr:`~Decorator.kwargs` '
                     'attributes.\n'
                     'The :meth:`~Decorator.after` method can access or change '
                     'the result using the :attr:`~Decorator.result` '
                     'attribute.\n'
                     'The :meth:`~Decorator.exception` method can be used for '
                     'do something with an Exception that has been raised.\n'
                     'In all three methods the :attr:`~Decorator.fqn` and '
                     ':attr:`~Decorator.func` attributes are available.\n'
                     '\n'
                     'Simple decorator\n'
                     '----------------\n'
                     '\n'
                     'Create a simple decorator::\n'
                     '\n'
                     '    import fqn_decorators\n'
                     '    import time\n'
                     '\n'
                     '    class time_it(fqn_decorators.Decorator):\n'
                     '\n'
                     '        def before(self):\n'
                     '            self.start = time.time()\n'
                     '\n'
                     '        def after(self):\n'
                     '            duration = time.time() - self.start\n'
                     '            print("{0} took {1} '
                     'seconds".format(self.fqn, duration))\n'
                     '\n'
                     '\n'
                     '    @time_it\n'
                     '    def my_function():\n'
                     '        time.sleep(1)\n'
                     '\n'
                     '    >>>my_function()\n'
                     '    __main__.my_function took 1.00293397903 seconds\n'
                     '\n'
                     '\n'
                     'Decorator with arguments\n'
                     '------------------------\n'
                     '\n'
                     'It is also very easy to create a decorator with '
                     'arguments.\n'
                     '\n'
                     '.. note::\n'
                     '    It is not possible to create decorators with '
                     '*non-keyworded* arguments.\n'
                     '    To create a decorator that supports non-keyworded '
                     'arguments see the :ref:`Advanced Usage '
                     '<usage_advanced_non_keyword_decorators>` section.\n'
                     '\n'
                     'Example::\n'
                     '\n'
                     '    import fqn_decorators\n'
                     '    import time\n'
                     '\n'
                     '    class threshold(fqn_decorators.Decorator):\n'
                     '\n'
                     '        def before(self):\n'
                     '            self.start = time.time()\n'
                     '\n'
                     '        def after(self):\n'
                     '            duration = time.time() - self.start\n'
                     "            treshold = self.params.get('threshold')\n"
                     '            if threshold and duration > threshold:\n'
                     "                raise Exception('Execution took longer "
                     "than the threshold')\n"
                     '\n'
                     '\n'
                     '    @threshold(threshold=2)\n'
                     '    def my_function():\n'
                     '        time.sleep(3)\n'
                     '\n'
                     '    >>> my_function()\n'
                     '    Exception: Execution took longer than the threshold\n'
                     '\n'
                     '\n'
                     'Async Decorator\n'
                     '---------------\n'
                     '\n'
                     "There's also support for decorating coroutines (or any "
                     'awaitable), for Python >=3.5 only.\n'
                     '\n'
                     'The implementation is the same as with the sync version, '
                     'just inherit from\n'
                     ':class:`~fqn_decorators.async.AsyncDecorator` instead.\n'
                     '\n'
                     'Example::\n'
                     '\n'
                     '    import asyncio\n'
                     '    import time\n'
                     '    from fqn_decorators.async import AsyncDecorator\n'
                     '\n'
                     '    class time_it_async(AsyncDecorator):\n'
                     '\n'
                     '        def before(self):\n'
                     '            self.start = time.time()\n'
                     '\n'
                     '        def after(self):\n'
                     '            duration = time.time() - self.start\n'
                     '            print("{0} took {1} '
                     'seconds".format(self.fqn, duration))\n'
                     '\n'
                     '    @time_it_async\n'
                     '    async def coro():\n'
                     '        await asyncio.sleep(1)\n'
                     '\n'
                     '    >>> loop = asyncio.get_event_loop()\n'
                     '    >>> loop.run_until_complete(coro())\n'
                     '    __main__.coro took 1.001493215560913 seconds\n'
                     '\n'
                     '\n'
                     '.. end_usage\n',
 'name': 'fqn-decorators',
 'packages': ['fqn_decorators'],
 'tests_require': ['tox'],
 'url': 'https://github.com/kpn-digital/py-fqn-decorators',
 'version': '1.2.0',
 'zip_safe': False})
