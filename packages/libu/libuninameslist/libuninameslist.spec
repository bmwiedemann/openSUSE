#
# spec file for package libuninameslist
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


%define real_version 0.4.20140731

Name:           libuninameslist
Version:        20140731
Release:        0
%define somajor 0
Summary:        A library providing Unicode character names and annotations
License:        BSD-3-Clause
Group:          System/Libraries
Url:            https://github.com/fontforge/libuninameslist
# As previous version was higher number than latest release from new project,
# we have to use the release date as version
Source0:        https://github.com/fontforge/libuninameslist/archive/%{real_version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libuninameslist provides Unicode name and annotation data from the official Unicode Character Database.

%package     -n %{name}%{somajor}
Summary:        A library providing Unicode character names and annotations
Group:          System/Libraries

%description -n %{name}%{somajor}
libuninameslist provides Unicode name and annotation data from the official Unicode Character Database.

%package        devel
Summary:        Header files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name}%{somajor} = %{version}

%description    devel
This package contains header files for %{name}.

%prep
%setup -q -n %{name}-%{real_version}

%build
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print

%post   -n %{name}%{somajor} -p /sbin/ldconfig

%postun -n %{name}%{somajor} -p /sbin/ldconfig

%files -n %{name}%{somajor}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/*.so.%{somajor}*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/libuninameslist.pc
%{_includedir}/*

%changelog
