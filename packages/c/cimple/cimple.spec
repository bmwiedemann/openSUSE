#
# spec file for package cimple
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cimple

Version:        2.0.24
Release:        0
Summary:        CIMPLE is an embeddable CIM provider engine
License:        MIT
Group:          System/Management
Url:            http://cimple.org
Source0:        %{name}-%{version}.tar.bz2
Patch1:         %{name}-%{version}-ow-adapter.dif
Patch2:         %{name}-%{version}-gcc.patch
Patch3:         aarch64-support.patch
Patch4:         ppc64le-support.patch
# enable installation of cimlisten tool, kkaempf@suse.de
Patch5:         install-cimlisten.patch
# gcc6 fixes
Patch6:         cimple-2.0.24-gcc6.patch
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  konkretcmpi
BuildRequires:  sblim-cmpi-devel
BuildRequires:  tog-pegasus-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CIMPLE is an embeddable CIM provider engine. It is used to (1) build
providers that will work with a variety of CIM servers and (2) provide
a foundation for implementing CIM-based standards such as WBEM, SMASH,
WSDM, and WS Management.

%package devel
Summary:        Header files for CIMPLE : an embeddable CIM provider engine
Group:          System/Management
Requires:       %{name} = %{version}
Requires:       gcc-c++

%description devel
Header files for CIMPLE : an embeddable CIM provider engine. It is used
to (1) build providers that will work with a variety of CIM servers and
(2) provide a foundation for implementing CIM-based standards such as
WBEM, SMASH, WSDM, and WS Management.

%package cmpi-adapter
Summary:        CMPI Adapter for CIMPLE providers
Group:          System/Management
Requires:       %{name} = %{version}

%description cmpi-adapter
The CMPI Adapter for CIMPLE is a bridge between the universal CMPI
provider interface and CIMPLE providers.  Using this adapter,
CIMPLE providers can run under any CIMOM.

%package pegasus-adapter
Summary:        Pegasus Adapter for CIMPLE providers
Group:          System/Management
Requires:       %{name} = %{version}

%description pegasus-adapter
The Pegasus Adapter for CIMPLE is a bridge between the native Pegasus
C++ provider interface and CIMPLE providers.  Using this adapter,
CIMPLE providers can run under Pegasus without using the CMPI layer.

%package -n brevity
Summary:        Pegasus Client SDK
Group:          System/Management
Requires:       %{name} = %{version}
Requires:       %{name}-devel = %{version}
Requires:       %{name}-pegasus-adapter = %{version}
Requires:       tog-pegasus-devel

%description -n brevity
Brevity is a software development kit for Pegasus (tog-pegasus) clients

%if 0
%package openwbem-adapter
Summary:        OpenWBEM Adapter for CIMPLE providers
Group:          System/Management
Requires:       %{name} = %{version}

%description openwbem-adapter
The OpenWBEM Adapter for CIMPLE is a bridge between the native OpenWBEM
C++ provider interface and CIMPLE providers.  Using this adapter,
CIMPLE providers can run under OpenWBEM without using the CMPI layer.

%package openwbem-devel
Summary:        Header file for CIMPLE providers using the OpenWBEM Adapter
Group:          System/Management
Requires:       %{name} = %{version}
Requires:       %{name}-devel = %{version}
Requires:       %{name}-openwbem-adapter = %{version}
Requires:       openwbem-devel

%description openwbem-devel
Header file for building CIMPLE providers that will use the
cimple-openwbem-adapter. This header is only needed by the
module.cpp file (part of a CIMPLE provider).

%endif

%prep
%setup -q
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export CIMPLE_DEBUG=1
./configure \
        --bindir=%{_bindir}  \
        --libdir=%{_libdir}  \
        --prefix=%{_prefix}  \
        --with-cmpi=/usr/include/cmpi \
        --with-pegasus=/usr
#        --with-openwbem=/usr

make  FLAGS="%{optflags} -fno-strict-aliasing -fPIC" %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir %{buildroot}
%if 0%{?suse_version} > 1110
%make_install
%else
DESTDIR=%{buildroot} make install
%endif
rm -r %{buildroot}/%{_prefix}/share

%check
#make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%{_bindir}/*
%{_libdir}/libcimple.so

%files devel
%defattr(-, root, root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/[a-z]*
%{_includedir}/%{name}/[A-N]*
# skip OpenWBEM_Adapter.h
%{_includedir}/%{name}/Ops.h
%{_includedir}/%{name}/[P-Z]*

%if 0
%files openwbem-adapter
%defattr(-, root, root)
%{_libdir}/libcimpleowadap.so

%files openwbem-devel
%defattr(-, root, root)
%{_includedir}/%{name}/OpenWBEM_Adapter.h
%endif

%files cmpi-adapter
%defattr(-, root, root)
%{_libdir}/libcimplecmpiadap.so

%files pegasus-adapter
%defattr(-, root, root)
%{_libdir}/libcimplepegadap.so

%files -n brevity
%defattr(-, root, root)
%dir %{_prefix}/include/brevity
%{_prefix}/include/brevity/*
%{_libdir}/libbrevity.so

%changelog
