#
# spec file for package libsigc++2
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
Name:           libsigc++2
Version:        2.10.2
Release:        0
Summary:        Typesafe Signal Framework for C++
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libsigc.sourceforge.net/
Source:         http://download.gnome.org/sources/libsigc++/2.10/%{_name}-%{version}.tar.xz
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE libsigc++-std-c11.patch dimstar@opensuse.org -- Add -std=c11 to CFLAGS when using libsigc++ to build. This is not upstreamable in this form as the used CXX macro should handle that, so needs more work (and entry points in mm-common)
Patch0:         libsigc++-std-c11.patch
BuildRequires:  gcc-c++
BuildRequires:  m4
BuildRequires:  pkgconfig

%description
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. It is the most
complete library of its kind with the ability to connect an abstract
callback to a class method, function, or function object. It contains
adaptor classes for connection of dissimilar callbacks and has an ease
of use unmatched by other C++ callback libraries.

%package -n libsigc-2_0-0
Summary:        Typesafe Signal Framework for C++
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libsigc-2_0-0
This library implements a full callback system for use in widget
libraries, abstract interfaces, and general programming. It is the most
complete library of its kind with the ability to connect an abstract
callback to a class method, function, or function object. It contains
adaptor classes for connection of dissimilar callbacks and has an ease
of use unmatched by other C++ callback libraries.

%package devel
Summary:        Typesafe Signal Framework for C++
Group:          Development/Libraries/C and C++
Requires:       libsigc-2_0-0 = %{version}
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
if [ $(gcc -dumpversion | awk -F. '{print $1}') -lt 6 ]; then
%patch0 -p1
fi

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
export MALLOC_CHECK_=2 MALLOC_PERTURB_=$((${RANDOM:-256} % 256))
make %{?_smp_mflags} check
unset MALLOC_CHECK_ MALLOC_PERTURB_

%post -n libsigc-2_0-0 -p /sbin/ldconfig
%postun -n libsigc-2_0-0 -p /sbin/ldconfig

%files -n libsigc-2_0-0
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libsigc-2.0.so.*

%files devel
%{_libdir}/libsigc-2.0.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/sigc++-2.0
%{_includedir}/sigc++-2.0/
%{_datadir}/devhelp/books/%{_name}-2.0
%doc %{_datadir}/doc/%{_name}-2.0
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
