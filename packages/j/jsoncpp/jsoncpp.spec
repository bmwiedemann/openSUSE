#
# spec file for package jsoncpp
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


%define sover   26
Name:           jsoncpp
Version:        1.9.6
Release:        0
Summary:        C++ library that allows manipulating with JSON
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/open-source-parsers/jsoncpp
Source0:        https://github.com/open-source-parsers/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base
%{?suse_build_hwcaps_libs}

%description
JSON is a lightweight data-interchange format. It can represent numbers,
strings, ordered sequences of values, and collections of name/value pairs.

JsonCpp is a C++ library that allows manipulating JSON values, including
serialization and deserialization to and from strings. It can also preserve
existing comment in unserialization/serialization steps, making it a convenient
format to store user input files.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
JSON is a lightweight data-interchange format. It can represent numbers,
strings, ordered sequences of values, and collections of name/value pairs.

JsonCpp is a C++ library that allows manipulating JSON values, including
serialization and deserialization to and from strings. It can also preserve
existing comment in unserialization/serialization steps, making it a convenient
format to store user input files.

%package -n lib%{name}%{sover}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n lib%{name}%{sover}
JSON is a lightweight data-interchange format. It can represent numbers,
strings, ordered sequences of values, and collections of name/value pairs.

JsonCpp is a C++ library that allows manipulating JSON values, including
serialization and deserialization to and from strings. It can also preserve
existing comment in unserialization/serialization steps, making it a convenient
format to store user input files.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
pushd %{buildroot}%{_includedir}/json/
# From 1.9.1 to 1.9.2, features.h has been renamed json_features.h
# so, create a symlink for compatibility
ln -s json_features.h features.h
# From 1.9.2 to 1.9.3, autolink.h has been dropped and config.h must be used
# so, create a symlink for compatibility
ln -s config.h autolink.h
popd

%check
%meson_test

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%license LICENSE
%doc AUTHORS README.md
%dir %{_libdir}/cmake/%{name}/
%dir %{_libdir}/cmake
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/%{name}Config.cmake
%{_libdir}/cmake/%{name}/%{name}-namespaced-targets.cmake
%{_libdir}/lib%{name}.so
%{_includedir}/json/

%changelog
