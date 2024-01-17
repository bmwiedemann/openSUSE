#
# spec file for package sblim-sfcc
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


Name:           sblim-sfcc
Version:        2.2.9~rc1
Release:        0
URL:            https://github.com/kkaempf/sblim-sfcc
Summary:        Small Footprint CIM Client Library
License:        EPL-1.0
Group:          System/Management
Source:         %{name}-2.2.9-preview.tar.gz
Source2:        %{name}-rpmlintrc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  libtool
%if 0%{?suse_version}
%if 0%{?suse_version} < 1020
BuildRequires:  curl-devel
%else
BuildRequires:  libcurl-devel
%endif
%else
BuildRequires:  curl-devel
%endif

%description
The small footprint CIM client library is a C API allowing client
applications to interface with CIM implementations (e.g. CIM servers).
Due to it's small memory and disk footprint it is well-suited for
embedded environments.

%package -n libcimcClientXML0
Summary:        Small Footprint CIM Client Library
Group:          System/Libraries

%description -n libcimcClientXML0
Small Footprint CIM Client Library (sfcc) Runtime Libraries

%package -n libcimcclient0
Summary:        CIM C Client Loader Implementation
Group:          System/Libraries

%description -n libcimcclient0
Small Footprint CIM Client Library (sfcc) Runtime Libraries

%package -n libcmpisfcc1
Summary:        Common Manageability Programming Interface of the Small Footprint CIM Client
Group:          System/Libraries

%description -n libcmpisfcc1
Small Footprint CIM Client Library (sfcc) Runtime Libraries

%package devel
Summary:        Development files for the Small Footprint CIM Client Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcimcClientXML0 = %{version}
Requires:       libcimcclient0 = %{version}
Requires:       libcmpisfcc1 = %{version}

%description devel
Small Footprint CIM Client Library (sfcc) Header Files and Link
Libraries

%prep
%setup -q -n %{name}-2.2.9-preview

%build
autoreconf -fi
export CFLAGS="%optflags -fno-strict-aliasing"
%configure \
    --disable-static

# RHEL5 ships with old libtool (see http://www.yolinux.com/TUTORIALS/C++XmlBeansxx.html)
%if 0%{?rhel_version} >= 500 || 0%{?centos_version} >= 500
%if 0%{?rhel_version} < 600 || 0%{?centos_version} < 600
rm -f libtool; ln -s /usr/bin/libtool .
%endif
%endif

make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" install docdir=%{_docdir}/%{name}
rm %{buildroot}%{_libdir}/*.la

%post   -n libcimcClientXML0 -p /sbin/ldconfig
%postun -n libcimcClientXML0 -p /sbin/ldconfig
%post   -n libcimcclient0 -p /sbin/ldconfig
%postun -n libcimcclient0 -p /sbin/ldconfig
%post   -n libcmpisfcc1 -p /sbin/ldconfig
%postun -n libcmpisfcc1 -p /sbin/ldconfig

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/libcimcclient.so
%{_libdir}/libcmpisfcc.so
%{_mandir}/man3/*
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%files -n libcimcClientXML0
%defattr(-,root,root)
%{_libdir}/libcimcClientXML.so.0*
# dlopen'ed lib
%{_libdir}/libcimcClientXML.so

%files -n libcimcclient0
%defattr(-,root,root)
%{_libdir}/libcimcclient.so.0*

%files -n libcmpisfcc1
%defattr(-,root,root)
%{_libdir}/libcmpisfcc.so.1*

%changelog
