project('clipscreen', 'c')
executable(
    'clipscreen',
    'clipscreen.c',
    dependencies: [
        dependency('cairo'),
        dependency('x11'),
        dependency('xext'),
        dependency('xfixes'),
        dependency('xrandr'),
    ],
    install: true,
)
