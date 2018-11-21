test = {
  'name': 'question 6.5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(time_array) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> time_array.shape
          (101,)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(time_array[0:2], [0, 0.5])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(time_array[-2:], [49.5, 50])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> type(acc_array) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> acc_array.shape
          (101,)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(acc_array[0:2], [-0.00506375204384, 0.00500006128645])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(acc_array[-2:], [0.495000061286, 0.479565276825])
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'import numpy as np',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.isclose(compute_velocity(2, 4, acc_array), 0.0820085591101)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(compute_velocity(3, 5, acc_array), 0.217477015351)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(compute_velocity(12, 21, acc_array), 62.3006966189)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(compute_velocity(2, 4, acc_list), 0.082)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(compute_velocity(3, 5, acc_list), 0.21599999)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(compute_velocity(12, 9, acc_list), 3.09)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': """
import numpy as np
acc_list = [-0.005, 0.005, 0.010, 0.015, 0.037, 0.025, 0.032, 0.040, 0.067, 0.068]
""",
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
