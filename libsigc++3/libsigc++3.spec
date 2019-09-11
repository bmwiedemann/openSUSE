#
# spec file for package libsigc++3
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.0.0
Release:        0
Summary:        Typesafe Signal Framework for C++
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://libsigc.sourceforge.net/
Source0:        https://download.gnome.org/sources/libsigc++/3.0/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  gcc-c++
BuildRequires:  mm-common >= 0.9.12
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
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$((${RANDOM:-256} % 256))
make %{?_smp_mflags} check
unset MALLOC_CHECK_ MALLOC_PERTURB_

%post -n libsigc-3_0-0 -p /sbin/ldconfig
%postun -n libsigc-3_0-0 -p /sbin/ldconfig

%files -n libsigc-3_0-0
%license COPYING
%doc NEWS README.md
%{_libdir}/libsigc-3.0.so.*

%files devel
%doc AUTHORS ChangeLog
%doc %{_datadir}/doc/%{_name}-3.0
%{_libdir}/libsigc-3.0.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/sigc++-3.0
%{_includedir}/sigc++-3.0/
%{_datadir}/devhelp/books/%{_name}-3.0
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
