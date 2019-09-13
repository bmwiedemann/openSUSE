#
# spec file for package qgo
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           qgo
Version:        2.0.0
Release:        0
Summary:        A Go Board and SGF Editor
License:        GPL-2.0+
Group:          Amusements/Games/Board/Other
Url:            https://github.com/pzorin/qgo
Source:         https://github.com/pzorin/qgo/archive/qt4-final.tar.gz
#PATCH-FIX-UPSTREAM fix gcc6 narrowing conversion from int to char inside {}
Patch:          qgo-2.0.0-gcc6.patch
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(alsa)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A Go board, sgf editor and client for IGS/NNGS/WINGS based on the Qt
library. Go is an ancient boardgame, very common in Japan, China and
Korea.

%prep
%setup -q -n %{name}-qt4-final
%patch -p1

%build
qmake -makefile  %{name}.pro QMAKE_CFLAGS="%{optflags}" QMAKE_CXXFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_bindir}
cp src/ressources/pics/qgo*.{png,xpm} %{buildroot}%{_datadir}/pixmaps/
install -m 644 src/qgo.desktop %{buildroot}%{_datadir}/applications/
install -m 755 build/qgo %{buildroot}%{_bindir}/qgo
%suse_update_desktop_file qgo Game BoardGame

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.md
%{_bindir}/qgo
%{_datadir}/pixmaps/qgo*
%{_datadir}/applications/qgo.desktop

%changelog
