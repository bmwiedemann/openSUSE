#
# spec file for package eperiodique
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) specCURRENT_YEAR SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           eperiodique
Version:        0.5
Release:        0
Summary:        Periodic table of elements in EFL
License:        BSD-2-Clause
Group:          Amusements/Teaching/Other
Url:            http://eperiodique.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(edje) >= 1.8.0
BuildRequires:  pkgconfig(eina) >= 1.8.0
BuildRequires:  pkgconfig(elementary) >= 1.8.0
BuildRequires:  pkgconfig(evas) >= 1.8.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
Graphical application that display the periodic table of the elements. It shows
basic data for each element, pictures, Bohr models and lattice structures.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%{buildroot}" %{?_smp_mflags}
mkdir %{buildroot}%{_datadir}/pixmaps
rm -rf %{buildroot}%{_datadir}/doc
mv %{buildroot}%{_datadir}/icons/%{name}.png %{buildroot}/%{_datadir}/pixmaps/
%{find_lang} %{name}
%if 0%{?suse_version}
%fdupes %{buildroot}%{_datadir}/%{name}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog README COPYING TODO AUTHORS NEWS
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*

%changelog
