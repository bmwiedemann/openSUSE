#
# spec file for package libmaa
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


%define soname 4
Name:           libmaa
Version:        1.5.1
Release:        0
Summary:        Library providing many low-level data structures
License:        MIT
URL:            https://github.com/cheusov/libmaa
Source0:        https://downloads.sourceforge.net/dict/%{name}-%{version}.tar.gz
BuildRequires:  mk-configure
BuildRequires:  pkgconfig(zlib)

%description
The libmaa library provides many low-level data structures which can
be used for writing compilers, hash tables, sets, lists,
debugging support, and memory management. libmaa was originally
implemented as a foundation for the "kheperalong" package.

%package -n %{name}%{soname}
Summary:        Library providing many low-level data structures
Group:          System/Libraries

%description -n %{name}%{soname}
The libmaa library provides many low-level data structures which can
be used for writing compilers, hash tables, sets, lists,
debugging support, and memory management. libmaa was originally
implemented as a foundation for the "kheperalong" package.

%package -n %{name}-devel
Summary:        Development files for libmaa
Group:          Development/Libraries/C and C++
Requires:       libmaa%{soname} = %{version}

%description -n %{name}-devel
This RPM contains the development files for libmaa.

%package doc
Summary:        Documentation files for libmaa
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This RPM contains the documentation files for libmaa.

%prep
%autosetup

%define env \
        unset MAKEFLAGS \
        export MKSTATICLIB=no \
        export NOSUBDIR=doc

%build
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
mkc_compiler_settings
%endif
%{env}
%{mkcmake}

%install
%{env}
%{mkcmake} install DESTDIR=%{?buildroot}

%post -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%license doc/LICENSE
%doc README doc/NEWS
%{_libdir}/*.so.*

%files -n %{name}-devel
%{_includedir}/maa*
%{_libdir}/*.so

%files doc
%license doc/LICENSE
%doc doc/*.ps*

%changelog
