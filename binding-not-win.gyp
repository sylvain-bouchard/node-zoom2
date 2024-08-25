{
  'targets': [
    {
      'target_name': 'zoom',
      "cflags": ["<!@(pkg-config --cflags yaz)"],
      "libraries": ["<!@(pkg-config --libs yaz)"],
      'include_dirs': [
        "<!(node -e 'require(\"nan\")')",
        "<!@(pkg-config --cflags-only-I yaz | sed 's/-I//g')"
      ],
      'sources': [
        'src/zoom.cc',
        'src/query.cc',
        'src/record.cc',
        'src/errors.cc',
        'src/records.cc',
        'src/options.cc',
        'src/resultset.cc',
        'src/connection.cc'
      ]
    }
  ]
}
