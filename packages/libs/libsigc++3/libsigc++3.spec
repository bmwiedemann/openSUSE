#
# spec file for package libsigc++3
#
# Copyright (c) 2024 SUSE LLC
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


%define _name libsigc++
Name:           libsigc++3
Version:        3.6.0
Release:        0
Summary:        Typesafe Signal Framework for C++
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://libsigcplusplus.github.io/libsigcplusplus/
Source0:        https://download.gnome.org/sources/libsigc++/3.6/%{_name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. It is the most
complete library of its kind with the ability to connect an abstract
callback to a class method, function, or function object. It contains
adaptor classes for connection of dissimilar callbacks and has an ease
of use unmatched by other C++ callback libraries.

%package -n libsigc-3_0-0
Summary:        Typesafe Signal Framework for C++
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libsigc-3_0-0
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. It is the most
complete library of its kind with the ability to connect an abstract
callback to a class method, function, or function object. It contains
adaptor classes for connection of dissimilar callbacks and has an ease
of use unmatched by other C++ callback libraries.

%package devel
Summary:        Typesafe Signal Framework for C++
Group:          Development/Libraries/C and C++
Requires:       libsigc-3_0-0 = %{version}
Requires:       libstdc++-devel

%description devel
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. It is the most
complete library of its kind with the ability to connect an abstract
callback to a class method, function, or function object. It contains
adaptor classes for connection of dissimilar callbacks and has an ease
of use unmatched by other C++ callback libraries.

%prep
%autosetup -p1 -n %{_name}-%{version}

# Remove executable bit in NEWS...
chmod -x NEWS

%build
%meson
%meson_build

%install
%meson_install

%check
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$((${RANDOM:-256} % 256))
%meson_test
unset MALLOC_CHECK_ MALLOC_PERTURB_

%ldconfig_scriptlets -n libsigc-3_0-0

%files -n libsigc-3_0-0
%license COPYING
%doc NEWS README.md
%{_libdir}/libsigc-3.0.so.*

%files devel
%doc ChangeLog
%{_libdir}/libsigc-3.0.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/sigc++-3.0
%{_includedir}/sigc++-3.0/

%changelog
