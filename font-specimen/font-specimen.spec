#
# spec file for package font-specimen
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libmaj  0
Name:           font-specimen
Version:        20150202
Release:        0
Summary:        Font Specimen Creator
License:        GPL-2.0+
Group:          Productivity/Publishing/Other
Url:            https://github.com/pgajdos/font-specimen/
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libpng-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Creates specimen for given installed font and script it
sufficiently coverages. Run font-specimen without
parameters to see usage.

%package -n libfont-specimen%{libmaj}
Summary:        Library for Creating Font Specimen
Group:          System/Libraries

%description -n libfont-specimen%{libmaj}
Library that allows to create specimens for installed
font.

%package devel
Summary:        Development Files for libspecimen%{libmaj}
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libfont-specimen%{libmaj} = %{version}

%description devel
Header and development files for font-specimen library.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
export INCLUDEDIR="%{_includedir}"
export LIBDIR="%{_libdir}"
export BINDIR="%{_bindir}"
export PKG_CONFIG_DIR="%{_libdir}/pkgconfig"
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%post -n libfont-specimen%{libmaj} -p /sbin/ldconfig

%postun -n libfont-specimen%{libmaj} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ChangeLog README.md
%{_bindir}/*

%files -n libfont-specimen%{libmaj}
%defattr(-,root,root)
%{_libdir}/libfont-specimen.so.%{libmaj}*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libfont-specimen.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
