#
# spec file for package specRPM_CREATION_NAME
#
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hhdate
Version:        3.0.1
Release:        0
Summary:        A date and time library based on the C++11/14/17 header
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/HowardHinnant/date
Source:         hhdate-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel

%description
A date and time library based on the C++11/14/17 header. Mostly a header-only library.

%package -n %{name}-devel
Summary:        Development files for the hhdate library
Requires:       %{name} = %{version}
BuildArch:      noarch

%description -n %{name}-devel
A date and time library based on the C++11/14/17 header. Mostly a header-only library.

%prep
%setup -q

%build
%cmake -DBUILD_TZ_LIB=ON
%cmake_build

%install
install -D -m 0644 include/date/*   -t %{buildroot}/%{_includedir}/date/
install -D -m 0755 build/libdate-tz.so %{buildroot}/%{_libdir}/libdate-tz.so

%files
%license LICENSE.txt
%{_libdir}/libdate-tz.so

%files -n hhdate-devel
%license LICENSE.txt
%{_includedir}/date/

%changelog

