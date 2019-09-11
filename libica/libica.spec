#
# spec file for package libica
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           libica
Version:        3.4.0
Release:        0
Summary:        Library interface for the IBM Cryptographic Accelerator device driver
License:        CPL-1.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/libica
Source:         libica-%{version}.tar.gz
Source1:        libica-SuSE.tar.bz2
# The icaioctl.h file came from https://sourceforge.net/p/opencryptoki/icadd/ci/master/tree/
Source3:        icaioctl.h
Source4:        README.SUSE
Source5:        sysconfig.z90crypt
Source6:        baselibs.conf
Source7:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openssl-devel
PreReq:         %fillup_prereq
PreReq:         %insserv_prereq
ExclusiveArch:  s390 s390x

%description
This package contains the interface library routines used by IBM
modules to interface with the IBM eServer Cryptographic Accelerator
(ICA).

%package -n libica3
Summary:        Library interface for the IBM Cryptographic Accelerator
Group:          System/Libraries
Recommends:     libica-tools

%description -n libica3
This package contains the interface library routines used by IBM
modules to interface with the IBM eServer Cryptographic Accelerator
(ICA).

%package tools
Summary:        Utilities for the IBM Cryptographic Accelerator
Group:          Hardware/Other
Obsoletes:      libica < %{version}-%{release}
Obsoletes:      libica-2_3_0
Obsoletes:      libica2
Provides:       libica = %{version}-%{release}
Provides:       libica-plugin = %{version}-%{release}

%description tools
This package contains command-line utilities to inspect the IBM
eServer Cryptographic Accelerator (ICA).

%package        devel
Summary:        Development files for the ICA device driver interface library
Group:          Development/Libraries/C and C++
Requires:       libica3 = %{version}
Requires:       libopenssl-devel
Obsoletes:      libica-2_1_0-devel < %{version}-%{release}
Provides:       libica-2_1_0-devel = %{version}-%{release}
Obsoletes:      libica-2_3_0-devel < %{version}-%{release}
Provides:       libica-2_3_0-devel = %{version}-%{release}

%description devel
This package contains the interface library routines used by IBM
modules to interface with the IBM eServer Cryptographic Accelerator
(ICA).

This subpackage contains the necessary files to compile and link
using the libica library.

%package        devel-static
Summary:        Static Development files for the ICA device driver interface library
Group:          Development/Libraries/C and C++
Requires:       libica-devel

%description devel-static
This package contains the interface library routines used by IBM
modules to interface with the IBM eServer Cryptographic Accelerator
(ICA).

This RPM contains all the tools necessary to compile and link using
the libica library.

%prep
%setup -q -a 1

%build
mkdir -p include/linux/
cp %{SOURCE3} include/linux/

autoreconf --force --install
%configure CPPFLAGS="-Iinclude -fPIC" CFLAGS="%{optflags} -fPIC" \
  --enable-fips
make clean
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_includedir}
%make_install
cp -p include/ica_api.h %{buildroot}%{_includedir}
cp -a SuSE/* %{buildroot}
install -D %{SOURCE5} %{buildroot}%{_fillupdir}/sysconfig.z90crypt
cp -a %{_sourcedir}/README.SUSE .
rm -f %{buildroot}%{_libdir}/libica.la
rm -f %{buildroot}%{_datadir}/doc/libica/*
rmdir %{buildroot}%{_datadir}/doc/libica

%post tools
%{fillup_and_insserv -n boot.z90crypt}

%preun tools
%stop_on_removal boot.z90crypt

%postun tools
%restart_on_update boot.z90crypt
%insserv_cleanup

%post   -n libica3 -p /sbin/ldconfig
%postun -n libica3 -p /sbin/ldconfig

%files -n libica3
%defattr(-,root,root)
%{_libdir}/libica.so.3*

%files tools
%defattr(-, root, root)
%license LICENSE
%doc README.SUSE
%{_initddir}/boot.z90crypt
%{_sbindir}/rcz90crypt
%attr(0644,root,root) %{_fillupdir}/sysconfig.z90crypt
%{_bindir}/icainfo
%{_bindir}/icastats
%{_mandir}/man1/icainfo.1%{?ext_man}
%{_mandir}/man1/icastats.1%{?ext_man}
# Must be in here, otherwise openssl-ibmca does not find it via DSO_load() bsc#952871
%{_libdir}/libica.so

%files devel
%defattr(-, root, root)
%attr(0644,root,root) %{_includedir}/ica_api.h

%files devel-static
%defattr(-, root, root)
%{_libdir}/libica.a

%changelog
