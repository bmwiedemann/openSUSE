#
# spec file for package librevenge
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global apiversion 0.0
%global pkgextension 0_0-0
Name:           librevenge
Version:        0.0.4
Release:        0
Summary:        A base library for writing document import filters
License:        LGPL-2.1+ or MPL-2.0+
Group:          System/Libraries
Url:            http://sourceforge.net/p/libwpd/wiki/librevenge/
Source:         http://downloads.sourceforge.net/libwpd/%{name}-%{version}.tar.xz
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.

%package -n %{name}-%{pkgextension}
Summary:        A base library for writing document import filters
License:        LGPL-2.1+ or MPL-2.0+
Group:          System/Libraries

%description -n %{name}-%{pkgextension}
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.

%package -n %{name}-stream-%{pkgextension}
Summary:        A base library for writing document import filters (stream implementations)
License:        (LGPL-2.1+ or MPL-2.0+) and BSD-3-Clause
Group:          System/Libraries
# src/lib/RVNGOLEStream.{h,cpp} are BSD3c

%description -n %{name}-stream-%{pkgextension}
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.
This package contains the different stream implementations.

%package -n %{name}-generators-%{pkgextension}
Summary:        A base library for writing document import filters
License:        LGPL-2.1+ or MPL-2.0+
Group:          System/Libraries

%description -n %{name}-generators-%{pkgextension}
%{name} is a base library for writing document import filters. It has
interfaces for text documents, vector graphics, spreadsheets and
presentations.
This package contains classes to be used by converters that generate
documents using %{name}s APIs.

%package devel
Summary:        Development files for %{name}
License:        LGPL-2.1+ or MPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{pkgextension} = %{version}-%{release}
Requires:       %{name}-generators-%{pkgextension} = %{version}-%{release}
Requires:       %{name}-stream-%{pkgextension} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation of %{name} API
License:        LGPL-2.1+ or MPL-2.0+
Group:          Documentation/Other
%if 0%{?suse_version} > 1200
BuildArch:      noarch
%endif

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
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_docdir}/%{name}

%post -n %{name}-%{pkgextension} -p /sbin/ldconfig

%postun -n %{name}-%{pkgextension} -p /sbin/ldconfig

%post -n %{name}-stream-%{pkgextension} -p /sbin/ldconfig

%postun -n %{name}-stream-%{pkgextension} -p /sbin/ldconfig

%post -n %{name}-generators-%{pkgextension} -p /sbin/ldconfig

%postun -n %{name}-generators-%{pkgextension} -p /sbin/ldconfig

%if 0%{?suse_version} > 1300
%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
make %{?_smp_mflags} check
%endif

%files -n %{name}-%{pkgextension}
%defattr(-,root,root)
%doc COPYING.* README NEWS
%{_libdir}/%{name}-%{apiversion}.so.*

%files -n %{name}-stream-%{pkgextension}
%defattr(-,root,root)
%{_libdir}/%{name}-stream-%{apiversion}.so.*

%files -n %{name}-generators-%{pkgextension}
%defattr(-,root,root)
%{_libdir}/%{name}-generators-%{apiversion}.so.*

%files devel
%defattr(-,root,root)
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
%{_datadir}/gdb/auto-load%{_libdir}/%{name}-%{apiversion}.py*
%{_datadir}/gdb/auto-load%{_libdir}/%{name}-stream-%{apiversion}.py*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/python

%files doc
%defattr(-,root,root)
%doc COPYING.*
%doc %{_docdir}/%{name}

%changelog
