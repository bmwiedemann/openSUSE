#
# spec file for package qtile
#
# Copyright (c) 2024 SUSE LLC
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


%global _minimum_wlroots_ver 0.17.0
%global _conflict_wlroots_ver 0.18.0

Name:           qtile
Version:        0.26.0
Release:        0
Summary:        A pure-Python tiling window manager
# All MIT except for: libqtile/widget/pacman.py:GPL (v3 or later)
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Displaymanagers
URL:            http://qtile.org
Source0:        https://files.pythonhosted.org/packages/source/q/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Source3:        %{name}-portals.conf
BuildRequires:  fdupes
BuildRequires:  gcc
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
BuildRequires:  python3-pywlroots >= %{_minimum_wlroots_ver}
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  python3-xcffib >= 1.4.0
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wlroots) >= %{_minimum_wlroots_ver}
BuildConflicts: pkgconfig(wlroots) >= %{_conflict_wlroots_ver}
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
Requires:       gdk-pixbuf-loader-rsvg
Requires:       pango-tools
Requires:       python3-cairocffi >= 0.9.0
Requires:       python3-cairocffi-pixbuf
Requires:       python3-cffi >= 1.1.0
Requires:       python3-pywayland
Requires:       python3-pywlroots
Requires:       python3-xcffib >= 0.10.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
Recommends:     xdg-desktop-portal-gtk
Recommends:     xdg-desktop-portal-wlr
Recommends:     xorg-x11-server-extra
# XDP-WLR alternative. This could be installed with no-recommends flag
Suggests:       xdg-desktop-portal-hyprland
# v0.21.0 has lots of additional failures on i586
ExcludeArch:    %{ix86} %arm %arm64

# Tests
BuildRequires:  ImageMagick
BuildRequires:  dbus-1
BuildRequires:  dbus-1-tools
BuildRequires:  graphviz
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  gtk3-tools
BuildRequires:  libgtk-3-0
BuildRequires:  libnotify
BuildRequires:  libnotify-tools
BuildRequires:  procps
BuildRequires:  python3-bowler
BuildRequires:  python3-cairocffi-pixbuf
BuildRequires:  python3-curses
BuildRequires:  python3-dbus_next
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-importlib-resources
BuildRequires:  python3-isort
BuildRequires:  python3-libcst
# BuildRequires:  python3-mypy
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-isort
BuildRequires:  python3-pyxdg
BuildRequires:  xcalc
BuildRequires:  xclock
BuildRequires:  xeyes
BuildRequires:  xorg-x11-server-extra
BuildRequires:  xrandr
BuildRequires:  xterm
BuildRequires:  xvfb-run
BuildRequires:  xwayland

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
sed -i '/#!\/usr\/bin\/env python/d' setup.py

# Disable use of scm
sed -i '65s/True/False/' setup.py

%build
export CFLAGS="%optflags $(pkg-config --cflags wayland-client libinput xkbcommon wlroots) -I/usr/include/wlr"
export LDFLAGS="-L%{_libdir}/libwlroots.so.12"
# Initial steps from https://github.com/qtile/qtile/blob/master/scripts/ffibuild
export PYTHONPATH="$PWD:$PYTHONPATH"
./scripts/ffibuild -v
%python3_pyproject_wheel

%install
export CFLAGS="%optflags $(pkg-config --cflags wayland-client libinput xkbcommon wlroots) -I/usr/include/wlr"
export LDFLAGS="-L%{_libdir}/libwlroots.so.12"
# Initial steps from https://github.com/qtile/qtile/blob/master/scripts/ffibuild
export PYTHONPATH="$PWD:$PYTHONPATH"
./scripts/ffibuild -v
%python3_pyproject_install
mkdir -p %{buildroot}%{_datadir}/xsessions/
install -m 644 %{_builddir}/qtile-%{version}/resources/qtile.desktop %{buildroot}%{_datadir}/xsessions/
# XDP >= 0.18.0 requires a portal for the environment and onwards
install -Dpm 0644 -t %{buildroot}%{_datadir}/xdg-desktop-portal/ %{SOURCE3}

%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/qtile.desktop

# default selector for xsession
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%fdupes %{buildroot}%{%python3_sitearch}

%check
mkdir -vp ${PWD}/bin
ln -svf %{buildroot}%{_bindir}/qtile ${PWD}/bin/qtile
export CFLAGS="%optflags $(pkg-config --cflags wayland-client libinput xkbcommon wlroots) -I/usr/include/wlr"
export LC_TYPE=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitearch}:%{python3_sitearch}:$PWD
export PATH="${PWD}/bin:${PATH}"
export PYTHONDONTWRITEBYTECODE=1
# Workaround for broken pytest
# https://github.com/openSUSE/python-rpm-macros/issues/170#issuecomment-2152944000
%{_bindir}/xvfb-run %{_bindir}/python%{python_version} -m pytest -vvv -rs --backend x11 --backend wayland

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/qtile.desktop 20

%postun
if [ ! -f %{_datadir}/xsessions/qtile.desktop ] ; then
  %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/qtile.desktop
fi

%files
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop
%license LICENSE
%doc CHANGELOG README.rst
%{_bindir}/qtile
%{python3_sitearch}/*qtile*/
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/qtile.desktop
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf

%changelog
