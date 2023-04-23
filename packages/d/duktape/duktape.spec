#
# spec file for package duktape
#
# Copyright (c) 2023 SUSE LLC
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


%define sover 207
Name:           duktape
Version:        2.7.0
Release:        0
Summary:        Embeddable Javascript engine
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://duktape.org/
Source0:        https://duktape.org/%{name}-%{version}.tar.xz
Patch0:         duktape-link-m.patch
BuildRequires:  gcc
BuildRequires:  pkgconfig

%description
Duktape is an embeddable Javascript engine, with a focus on portability and
compact footprint.

%package -n     lib%{name}%{sover}
Summary:        The core library for %{name}
Group:          System/Libraries

%description -n lib%{name}%{sover}
Embeddable Javascript engine.

This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description    devel
Embeddable Javascript engine.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%autosetup -p1

%build
%make_build -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%install
%make_install -f Makefile.sharedlibrary INSTALL_PREFIX=%{_prefix} LIBDIR=/%{_lib}

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%doc AUTHORS.rst
%license LICENSE.txt
%{_libdir}/libduktape.so.*
%{_libdir}/libduktaped.so.*

%files devel
%{_includedir}/duk_config.h
%{_includedir}/duktape.h
%{_libdir}/libduktape.so
%{_libdir}/libduktaped.so
%{_libdir}/pkgconfig/duktape.pc

%changelog
