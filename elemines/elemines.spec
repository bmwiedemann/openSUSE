#
# spec file for package elemines
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           elemines
Version:        0.2.3
Release:        0
Summary:        Simple game to train concentration and memory
License:        BSD-2-Clause and GPL-2.0
Group:          Amusements/Games/Logic
Url:            http://elemines.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(etrophy)
BuildRequires:  pkgconfig(evas)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Picture based game to train concentration and memory.

%prep
%setup -q

%build
%if 0%{?sles_version} != 11
autoreconf -ifv
%endif
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}
dos2unix OFL.txt

%install
make install DESTDIR="%buildroot"
rm -rf %{buildroot}/usr/share/doc/elemines
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/elemines.png %{buildroot}%{_datadir}/pixmaps/
find %{buildroot}/%{_libdir} -name '*.la' -exec rm {} \;
%find_lang %{name}

%clean
%{?buildroot:rm -rf %{buildroot}}
%files -f %{name}.lang
%defattr(-,root,root)
%doc README COPYING ChangeLog GPLv2.txt NEWS OFL.txt README.artwork TODO
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/*
%{_mandir}/man1/*
%{_datadir}/pixmaps/*
%{_libdir}/eleminesql.so

%changelog
