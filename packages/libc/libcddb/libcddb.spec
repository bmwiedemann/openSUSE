#
# spec file
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


%define flavor @BUILD_FLAVOR@%{nil}
%define BUILD_UTILS 0
%if "%{flavor}" == "utils"
%define BUILD_UTILS 1
%define nsuffix -utils
%endif
# To break libcddb<->libcdio dependency loop, this package is built in two stages.
%define _name libcddb
Name:           libcddb%{?nsuffix}
Version:        1.3.2
Release:        0
Summary:        CDDB Access Library Utilities
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://libcddb.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/%{_name}/%{_name}/%{version}/%{_name}-%{version}.tar.bz2
Source2:        baselibs.conf
Patch0:         libcddb-no-examples.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if %{BUILD_UTILS}
BuildRequires:  libcddb-devel
BuildRequires:  libcdio-devel
%endif

%description
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, and SMTP) to access data on a CDDB server (http://freedb.org). It
tries to be as cross-platform as possible.

%if ! %{BUILD_UTILS}
%package -n libcddb2
Summary:        CDDB Access Library
Group:          System/Libraries
#
Provides:       %{_name} = %{version}
#opensuse 10.3
Obsoletes:      %{_name} <= 1.3.0

%description -n libcddb2
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, and SMTP) to access data on a CDDB server (http://freedb.org). It
tries to be as cross-platform as possible.

%package devel
Summary:        CDDB Access Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcddb2 = %{version}

%description devel
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, and SMTP) to access data on a CDDB server (http://freedb.org). It
tries to be as cross-platform as possible.
%endif

%prep
%setup -q -n %{_name}-%{version}
%if !%{BUILD_UTILS}
%patch0
%else
sed -i 's:\(\.\.\|\$(top_builddir)\)/[^/]*/lib\([^ ]*\)\.la:-l\2:g' */Makefile.am
%endif

%build
autoreconf -f -i
%configure\
	--disable-rpath\
	--disable-static
%if %{BUILD_UTILS}
cd examples
%endif
%make_build

%install
%if %{BUILD_UTILS}
cd examples
%endif
%make_install
rm -f %{buildroot}%{_libdir}/libcddb.la

%if %{BUILD_UTILS}
%files
%{_bindir}/*

%else

%ldconfig_scriptlets -n libcddb2

%files -n libcddb2
%{_libdir}/*.so.2*

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cddb
%endif

%changelog
