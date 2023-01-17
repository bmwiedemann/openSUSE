#
# spec file for package librevenge
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


%global apiversion 0.0
%global pkgextension 0_0-0
Name:           librevenge
Version:        0.0.5
Release:        0
Summary:        A base library for writing document import filters
License:        LGPL-2.1-or-later OR MPL-2.0
Group:          Development/Libraries/C and C++
URL:            https://sourceforge.net/p/libwpd/wiki/librevenge/
Source:         https://downloads.sourceforge.net/project/libwpd/%{name}/%{name}-%{version}/%{name}-%{version}.tar.xz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.

%package -n %{name}-%{pkgextension}
Summary:        A base library for writing document import filters
License:        LGPL-2.1-or-later OR MPL-2.0
Group:          System/Libraries

%description -n %{name}-%{pkgextension}
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.

%package -n %{name}-stream-%{pkgextension}
Summary:        A base library for writing document import filters (stream implementations)
# src/lib/RVNGOLEStream.{h,cpp} are BSD3c
License:        BSD-3-Clause AND (LGPL-2.1-or-later OR MPL-2.0)
Group:          System/Libraries

%description -n %{name}-stream-%{pkgextension}
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.
This package contains the different stream implementations.

%package -n %{name}-generators-%{pkgextension}
Summary:        A base library for writing document import filters
License:        LGPL-2.1-or-later OR MPL-2.0
Group:          System/Libraries

%description -n %{name}-generators-%{pkgextension}
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.
This package contains classes to be used by converters that generate
documents using %{name}s APIs.

%package devel
Summary:        Development files for %{name}
License:        LGPL-2.1-or-later OR MPL-2.0
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{pkgextension} = %{version}-%{release}
Requires:       %{name}-generators-%{pkgextension} = %{version}-%{release}
Requires:       %{name}-stream-%{pkgextension} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation of %{name} API
License:        LGPL-2.1-or-later OR MPL-2.0
Group:          Documentation/Other
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-werror \
	--enable-pretty-printers \
	--disable-silent-rules \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_docdir}/%{name}

%post -n %{name}-%{pkgextension} -p /sbin/ldconfig
%postun -n %{name}-%{pkgextension} -p /sbin/ldconfig
%post -n %{name}-stream-%{pkgextension} -p /sbin/ldconfig
%postun -n %{name}-stream-%{pkgextension} -p /sbin/ldconfig
%post -n %{name}-generators-%{pkgextension} -p /sbin/ldconfig
%postun -n %{name}-generators-%{pkgextension} -p /sbin/ldconfig

%check
%if 0%{?suse_version} >= 1500
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make %{?_smp_mflags} check
%endif

%files -n %{name}-%{pkgextension}
%license COPYING.*
%doc README NEWS
%{_libdir}/%{name}-%{apiversion}.so.*

%files -n %{name}-stream-%{pkgextension}
%{_libdir}/%{name}-stream-%{apiversion}.so.*

%files -n %{name}-generators-%{pkgextension}
%{_libdir}/%{name}-generators-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}

%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/%{name}-generators-%{apiversion}.so
%{_libdir}/%{name}-stream-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc
%{_libdir}/pkgconfig/%{name}-generators-%{apiversion}.pc
%{_libdir}/pkgconfig/%{name}-stream-%{apiversion}.pc
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load%{_prefix}
%dir %{_datadir}/gdb/auto-load%{_libdir}
%{_datadir}/gdb/auto-load%{_libdir}/%{name}-%{apiversion}-gdb.py*
%{_datadir}/gdb/auto-load%{_libdir}/%{name}-stream-%{apiversion}-gdb.py*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/python

%files doc
%license COPYING.*
%doc %{_docdir}/%{name}

%changelog
