#
# spec file for package libzen
#
# Copyright (c) 2022 SUSE LLC
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


%define sover	0
Name:           libzen
Version:        0.4.40
Release:        0
Summary:        C++ utility library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/MediaArea/ZenLib
Source:         https://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
ZenLib is a C++ utility library. It includes classes for handling
strings, configuration, bit streams, threading, translation
and cross-platform operating system functions.

%package -n %{name}%{sover}
Summary:        The ZenLib C++ utility library
Group:          System/Libraries

%description -n %{name}%{sover}
ZenLib is a C++ utility library. It includes classes for handling
strings, configuration, bit streams, threading, translation
and cross-platform operating system functions.

%package -n libzen-devel
Summary:        Include files to develop for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description -n libzen-devel
Include files and mandatory libraries to develop
for %{name}.

%prep
%setup -q -n ZenLib
sed -i 's/\r$//' *.txt

%build
# generate docs
pushd Source/Doc
    doxygen -u 2> /dev/null
    doxygen Doxyfile
popd

pushd Project/GNU/Library
    autoreconf -fiv
    %configure --enable-shared --disable-static
    make %{?_smp_mflags}
popd

%install
pushd Project/GNU/Library
%make_install
popd

sed -i -e '/^Libs_Static/d' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
rm %{buildroot}%{_libdir}/%{name}.la

%fdupes %{buildroot}/%{_prefix}

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root,-)
%doc *.txt
%{_libdir}/libzen.so.%{sover}
%{_libdir}/libzen.so.%{sover}.*

%files -n libzen-devel
%defattr(-,root,root,-)
%doc Source/Doc/Documentation.html
%doc Doc/*
%{_includedir}/ZenLib/
%{_libdir}/libzen.so
%{_libdir}/pkgconfig/*.pc

%changelog
