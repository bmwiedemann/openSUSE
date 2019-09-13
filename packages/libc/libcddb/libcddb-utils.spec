#
# spec file for package libcddb-utils
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libcddb-utils
# WARNING: Do not edit this auto generated file.
#%(sh %{_sourcedir}/libcddb_spec-prepare.sh %{_sourcedir} %{name})
# To break libcddb<->libcdio dependency loop, this package is built in two stages.
%define BUILD_CORE 0
%define BUILD_UTILS 1
%define _name libcddb
Version:        1.3.2
Release:        0
Url:            http://libcddb.sourceforge.net/
Summary:        CDDB Access Library Utilities
License:        LGPL-2.1+
Group:          Productivity/Multimedia/Other
%if %BUILD_CORE
# bug437293
%ifarch ppc64
Obsoletes:      libcddb-64bit
%endif
%endif
Source:         http://downloads.sourceforge.net/project/%{_name}/%{_name}/%{version}/%{_name}-%{version}.tar.bz2
Source1:        %{_name}_spec-prepare.sh
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libtool
BuildRequires:  pkg-config
%if %BUILD_UTILS
BuildRequires:  libcdio-devel
%if !%BUILD_CORE
BuildRequires:  libcddb-devel
%endif
%endif
Patch:          libcddb-no-examples.patch

%description
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, and SMTP) to access data on a CDDB server (http://freedb.org). It
tries to be as cross-platform as possible.

%if %BUILD_UTILS
%if %BUILD_CORE

%package -n libcddb-utils
Summary:        CDDB Access Library Utilities
Group:          Productivity/Multimedia/Other

%description -n libcddb-utils
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, and SMTP) to access data on a CDDB server (http://freedb.org). It
tries to be as cross-platform as possible.

%endif
%endif
%if %BUILD_CORE

%package -n libcddb2
Summary:        CDDB Access Library
Group:          System/Libraries
# bug437293
%ifarch ppc64
Obsoletes:      libcddb-64bit
%endif
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
# bug437293
%ifarch ppc64
Obsoletes:      libcddb-devel-64bit
%endif

%description devel
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, and SMTP) to access data on a CDDB server (http://freedb.org). It
tries to be as cross-platform as possible.

%endif

%prep
%setup -q -n %{_name}-%{version}
%if !%BUILD_UTILS
%patch
%endif
%if !%BUILD_CORE
sed -i 's:\(\.\.\|\$(top_builddir)\)/[^/]*/lib\([^ ]*\)\.la:-l\2:g' */Makefile.am
%endif

%build
autoreconf -f -i
%configure\
	--disable-rpath\
	--disable-static\
	--with-pic
%if !%BUILD_CORE
cd examples
%endif
make %{?jobs:-j%jobs}

%install
%if !%BUILD_CORE
cd examples
%endif
make DESTDIR=$RPM_BUILD_ROOT install
%{__rm} -f %{buildroot}%{_libdir}/libcddb.la

%clean
rm -rf $RPM_BUILD_ROOT
%if %BUILD_UTILS

%files -n libcddb-utils
%defattr (-, root, root)
%{_bindir}/*
%endif
%if %BUILD_CORE

%post -n libcddb2 -p /sbin/ldconfig

%postun -n libcddb2 -p /sbin/ldconfig

%files -n libcddb2
%defattr (-, root, root)
%{_libdir}/*.so.2*

%files devel
%defattr (-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cddb
%endif

%changelog
