#
# spec file for package libwpg
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


%define libname libwpg-0_3-3
Name:           libwpg
Version:        0.3.2
Release:        0
Summary:        Library to read and parse graphics in WordPerfect Graphics format
License:        LGPL-2.1+ AND MPL-2.0+
Group:          Productivity/Publishing/Word
Url:            http://libwpg.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.0
BuildRequires:  pkgconfig(libwpd-0.10) >= 0.10.0

%description
libwpg is a C++ library to read and parse graphics in WPG (WordPerfect
Graphics) format. It is cross-platform, at the moment it can be build
on Microsoft Windows and Linux.

%package -n %{libname}
Summary:        Library to read and parse graphics in WordPerfect Graphics format
Group:          System/Libraries

%description -n %{libname}
libwpg is a C++ library to read and parse graphics in WPG (WordPerfect
Graphics) format.

%package devel
Summary:        Files for Developing with libwpg
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libwpg is a C++ library to read and parse graphics in WPG (WordPerfect
Graphics) format. It is cross-platform, at the moment it can be build
on Microsoft Windows and Linux.

This package contains the libwpg development files.

%package devel-doc
Summary:        Documentation for the libwpg API
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
This package contains documentation for the libwpg API.

%package tools
Summary:        Tools for converting WordPerfect Graphics files
Group:          Productivity/Publishing/Word

%description tools
Tools to work with graphics in WPG (WordPerfect Graphics) format.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-static \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# manpages
mkdir -p %{buildroot}%{_mandir}/man1
for i in wpg2raw wpg2svg; do
	LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
	help2man -N -o %{buildroot}%{_mandir}/man1/$i.1 %{buildroot}%{_bindir}/$i
done
# documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -p AUTHORS COPYING.LGPL COPYING.MPL ChangeLog %{buildroot}%{_docdir}/%{name}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libwpg*.pc
%{_includedir}/libwpg-*

%files devel-doc
%doc %{_docdir}/%{name}/html

%files tools
%{_bindir}/*
%{_mandir}/man1/*.1*
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/[A-Z]*

%changelog
