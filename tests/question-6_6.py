test = {
  'name': 'question 6.6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> file_array.shape
          (100, 2)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np; file_array = np.loadtxt("ex8_out.dat", usecols=(2, 5))',
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> np.allclose(file_array[0], [-4., 0.])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(file_array[50], [0.04, 0.4])
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.allclose(file_array[-1], [4., 0.])
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': 'import numpy as np; file_array = np.loadtxt("ex8_out.dat", usecols=(2, 5))',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
