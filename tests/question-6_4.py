test = {
  'name': 'question 6.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(hours_array) == np.ndarray and type(measA_array) == np.ndarray
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> hours_array.shape
          (34,)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> measA_array.shape
          (34,)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(hours_array[[0,1,6,8,12,-2,-1]], [0., 0.06, 0.64, 0.77, 1.35, 3.08, 3.14])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(measA_array[[0,1,14, 22, 29,-2, -1]], [ 1., 1., 0.1, -0.62, -0.97, -1., -1.])
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': 'import numpy as np;',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
