#
# spec file for package qtile
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python36 1
%define skip_python2 1
%bcond_without test
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           qtile
Version:        0.18.1
Release:        0
Summary:        A pure-Python tiling window manager
# All MIT except for: libqtile/widget/pacman.py:GPL (v3 or later)
License:        GPL-3.0-or-later AND MIT
Group:          System/X11/Displaymanagers
URL:            http://qtile.org
Source:         https://files.pythonhosted.org/packages/source/q/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  %{python_module cairocffi >= 0.9.0}
BuildRequires:  %{python_module cffi >= 1.1.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.11.0}
BuildRequires:  %{python_module xcffib >= 0.10.1}
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  libpango-1_0-0
BuildRequires:  libpulse-devel
BuildRequires:  libpulse0
BuildRequires:  librsvg
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       python3-cairocffi >= 0.9.0
Requires:       python3-cairocffi-pixbuf >= 0.9.0
Requires:       python3-cffi >= 1.1.0
Requires:       python3-six >= 1.11.0
Requires:       python3-xcffib >= 0.10.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     %{python_module iwlib}
Recommends:     %{python_module keyring}
Recommends:     %{python_module psutil}
Recommends:     %{python_module python-dateutil}
Recommends:     %{python_module python-mpd2}
Recommends:     %{python_module pyxdg}
Recommends:     libxcb-cursor0
Recommends:     pulseaudio
Recommends:     sensors
Suggests:       %{python_module jupyter_console}
Suggests:       %{python_module jupyter_ipykernel}
Suggests:       %{python_module tk}

%if %{with test}
BuildRequires:  %{python_module bowler}
BuildRequires:  %{python_module cairocffi-pixbuf}
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module dbus_next}
BuildRequires:  %{python_module gobject-Gdk}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xdg}
BuildRequires:  ImageMagick
BuildRequires:  dbus-1
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  graphviz
BuildRequires:  libgtk-3-0
BuildRequires:  libnotify
BuildRequires:  libnotify-tools
BuildRequires:  librsvg
BuildRequires:  procps
BuildRequires:  xcalc
BuildRequires:  xclock
BuildRequires:  xeyes
BuildRequires:  xorg-x11-server-extra
BuildRequires:  xrandr
BuildRequires:  xterm
BuildRequires:  xvfb-run

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
%setup -q -n qtile-%{version}
# Fix rpmlint warning
sed -i '/#!\/usr\/bin\/env python/d' libqtile/scripts/cmd_obj.py

%build
%python3_build

%install
# Initial steps from https://github.com/qtile/qtile/blob/master/scripts/ffibuild
./scripts/ffibuild
%python3_install
mkdir -p %{buildroot}%{_datadir}/xsessions/
install -m 644 %{_builddir}/qtile-%{version}/resources/qtile.desktop %{buildroot}%{_datadir}/xsessions/

%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/qtile.desktop

# default selector for xsession
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%fdupes %{buildroot}%{python3_sitearch}

%if %{with test}
%check
mkdir -vp %{_builddir}/%{name}-%{version}/bin
ln -svf %{buildroot}%{_bindir}/qtile %{_builddir}/%{name}-%{version}/bin/qtile
export LC_TYPE=en_US.UTF-8
export PYTHONPATH=%{buildroot}%{python3_sitearch}:${PYTHONPATH}
export PATH="${PWD}/bin:${PATH}"
export PYTHONDONTWRITEBYTECODE=1

%pytest -vv
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
%{python3_sitearch}/*
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/qtile.desktop

%changelog
