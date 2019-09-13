#
# spec file for package qtile
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           qtile
Version:        0.14.2
Release:        0
Summary:        A pure-Python tiling window manager
# All MIT except for: libqtile/widget/pacman.py:GPL (v3 or later)
License:        MIT AND GPL-3.0-or-later
Group:          System/X11/Displaymanagers
URL:            http://qtile.org
Source:         https://files.pythonhosted.org/packages/source/q/qtile/qtile-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-cairocffi >= 1.0.2
BuildRequires:  python3-cffi >= 1.11.5
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.11.0
BuildRequires:  python3-xcffib >= 0.8.1
Requires:       python3-cairocffi >= 0.9.0
Requires:       python3-cairocffi-pixbuf >= 0.9.0
Requires:       python3-cffi >= 1.11.5
Requires:       python3-six >= 1.11.0
Requires:       python3-xcffib >= 0.8.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     libxcb-cursor0
Recommends:     python3-iwlib
Recommends:     python3-keyring
Recommends:     python3-psutil
Recommends:     python3-python-dateutil
Recommends:     python3-python-mpd2
Recommends:     python3-pyxdg
Suggests:       python3-jupyter_console
Suggests:       python3-jupyter_ipykernel
BuildArch:      noarch

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
# Fix rpmlint warnings
sed -i 's/#!\/usr\/bin\/env bash/#!\/bin\/bash/' %{_builddir}/qtile-%{version}/bin/dqtile-cmd
sed -i '/#!\/usr\/bin\/env python/d' %{_builddir}/qtile-%{version}/libqtile/scripts/qtile_cmd.py

%build
%python3_build

%install
%python3_install
mkdir -p %{buildroot}%{_datadir}/xsessions/
install -m 644 %{_builddir}/qtile-%{version}/resources/qtile.desktop %{buildroot}%{_datadir}/xsessions/

# default selector for xsession
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%fdupes %{buildroot}%{python3_sitelib}

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
%{_bindir}/iqshell
%{_bindir}/qtile
%{_bindir}/qtile-run
%{_bindir}/qtile-top
%{_bindir}/qshell
%{_bindir}/qtile-cmd
%{_bindir}/dqtile-cmd
%{python3_sitelib}/*
%{_mandir}/man1/qtile.1%{?ext_man}
%{_mandir}/man1/qshell.1%{?ext_man}
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/qtile.desktop

%changelog
