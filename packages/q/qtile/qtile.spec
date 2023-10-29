#
# spec file for package qtile
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_with     test
%define pythons python3
Name:           qtile
Version:        0.23.0
Release:        0
Summary:        A pure-Python tiling window manager
# All MIT except for: libqtile/widget/pacman.py:GPL (v3 or later)
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Displaymanagers
URL:            http://qtile.org
Source0:        https://files.pythonhosted.org/packages/source/q/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# Patch0:         https://github.com/qtile/qtile/pull/3985.patch#/0000-fix-and-new-features-on-latest-wlroots.patch
BuildRequires:  gcc
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  librsvg
BuildRequires:  pango-devel
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
BuildRequires:  python3-cairocffi >= 1.6.0
BuildRequires:  python3-cffi >= 1.1.0
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pycairo >= 1.25.1
BuildRequires:  python3-pywlroots
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  python3-xcffib >= 1.4.0
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wlroots)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
Requires:       python3-cairocffi >= 0.9.0
Requires:       python3-cairocffi-pixbuf >= 0.9.0
Requires:       python3-cffi >= 1.1.0
Requires:       python3-pycairo >= 1.25.1
Requires:       python3-pywayland
Requires:       python3-pywlroots
Requires:       python3-xcffib >= 0.10.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     libxcb-cursor0
Recommends:     pipewire
Recommends:     pipewire-pulseaudio
Recommends:     python3-iwlib
Recommends:     python3-keyring
Recommends:     python3-psutil
Recommends:     python3-python-dateutil
Recommends:     python3-python-mpd2
Recommends:     python3-pyxdg
Recommends:     sensors
Suggests:       python3-jupyter_console
Suggests:       python3-jupyter_ipykernel
Suggests:       python3-tk
# v0.21.0 has lots of additional failures on i586
ExcludeArch:    %{ix86} %arm %arm64

%if %{with test}
BuildRequires:  ImageMagick
BuildRequires:  dbus-1
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  graphviz
BuildRequires:  libgtk-3-0
BuildRequires:  libnotify
# libnotify-tools seems to introduce more fails in v0.21.0
# BuildRequires:  libnotify-tools
BuildRequires:  librsvg
BuildRequires:  procps
BuildRequires:  python3-bowler
BuildRequires:  python3-cairocffi-pixbuf
BuildRequires:  python3-curses
BuildRequires:  python3-dbus_next
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-mypy
BuildRequires:  python3-pytest
BuildRequires:  python3-pyxdg
BuildRequires:  xcalc
BuildRequires:  xclock
BuildRequires:  xeyes
BuildRequires:  xorg-x11-server-extra
BuildRequires:  xrandr
BuildRequires:  xterm
BuildRequires:  xvfb-run
BuildRequires:  xwayland
%endif

%description
A pure-Python tiling window manager.
* Extensible in that personal layouts, widgets and commands can be created.
* Configured in Python.
* Command shell that allows all aspects of Qtile to be managed and
  inspected.
* Remote scriptability to set up workspaces,
  manipulate windows, update status bar widgets and more.
* Qtile is unit-tested using this remote scriptability feature.

%prep
%autosetup -p1
# Fix rpmlint warning
sed -i '/#!\/usr\/bin\/env python/d' libqtile/scripts/cmd_obj.py

# Disable use of scm
sed -i '104s/True/False/' setup.py

%build
export CFLAGS="%optflags $(pkg-config --cflags wayland-client libinput xkbcommon wlroots) -I/usr/include/wlr"
# Initial steps from https://github.com/qtile/qtile/blob/master/scripts/ffibuild
export PYTHONPATH="$PWD:$PYTHONPATH"
./scripts/ffibuild -v
%pyproject_wheel

%install
export CFLAGS="%optflags $(pkg-config --cflags wayland-client libinput xkbcommon wlroots) -I/usr/include/wlr"
# Initial steps from https://github.com/qtile/qtile/blob/master/scripts/ffibuild
export PYTHONPATH="$PWD:$PYTHONPATH"
./scripts/ffibuild -v
%pyproject_install
mkdir -p %{buildroot}%{_datadir}/xsessions/
install -m 644 %{_builddir}/qtile-%{version}/resources/qtile.desktop %{buildroot}%{_datadir}/xsessions/

%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/qtile.desktop

# default selector for xsession
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%python_expand %fdupes %{buildroot}%{python3_sitearch}

%if %{with test}
%check
export CFLAGS="%optflags $(pkg-config --cflags wayland-client libinput xkbcommon wlroots) -I/usr/include/wlr"
export PYTHONPATH=%{buildroot}%{python3_sitearch}:%{python3_sitearch}
%pytest -vv -rs --backend x11
%pytest -vv -rs --backend wayland
%endif

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/qtile.desktop 20

%postun
[ -f %{_datadir}/xsessions/qtile.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/qtile.desktop

%files
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop
%license LICENSE
%doc CHANGELOG README.rst
%{_bindir}/qtile
%{python3_sitearch}/*qtile*/
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/qtile.desktop

%changelog
