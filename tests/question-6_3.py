test = {
  'name': 'question 6.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(readTempDenFile) == types.FunctionType
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(param) # wrong number of argument
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(temp_air_list) == list and type(dens_air_list) == list
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(temp_water_list) == list and type(dens_water_list) == list
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import types; import inspect; param = inspect.signature(readTempDenFile).parameters
""",
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(x, [-10.0, -5.0, 0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(y, [1.341, 1.316, 1.293, 1.269, 1.247, 1.225, 1.204, 1.184, 1.164])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> temp_air_list == x and dens_air_list == y
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
get_ipython().magic(\'matplotlib agg\')
import matplotlib.pyplot as plt
import numpy as np; 
x, y = readTempDenFile(\"data/density_air.dat\")
""",
      'teardown': "get_ipython().magic(\'matplotlib notebook\')",
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(x, [0.0, 4.0, 15.0, 20.0, 25.0, 37.0, 50.0, 100.0])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(y, [999.8425, 999.975, 999.1026, 998.2071, 997.0479, 993.3316, 988.04, 958.3665])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> temp_water_list == x and dens_water_list == y
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
get_ipython().magic(\'matplotlib agg\')
import matplotlib.pyplot as plt
import numpy as np; 
x, y = readTempDenFile(\"data/density_water.dat\")
""",
      'teardown': "get_ipython().magic(\'matplotlib notebook\')",
      'type': 'doctest'
    }
  ]
}
