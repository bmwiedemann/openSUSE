#
# spec file for package libica
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           libica
Version:        4.3.0
Release:        0
Summary:        Library interface for the IBM Cryptographic Accelerator device driver
License:        CPL-1.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/libica
Source:         https://github.com/opencryptoki/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        README.SUSE
Source2:        sysconfig.z90crypt
Source3:        z90crypt
Source4:        z90crypt.service
Source5:        %{name}-rpmlintrc
###
Patch01:        libica-FIPS-make-it-possible-to-specify-fipshmac-binary.patch
Patch99:        libica-sles15sp5-FIPS-hmac-key.patch
###
Patch110:       libica-4.3.0-01-disable-CEX-usage-in-OpenSSL-for-all-tests.patch
Patch111:       libica-4.3.0-02-correct-rc-handling-with-s390_pcc-function.patch
Patch112:       libica-4.3.0-03-Use-__asm__-instead-of-asm.patch
###

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fipscheck
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openssl
BuildRequires:  openssl-devel
Requires(post): %fillup_prereq
ExclusiveArch:  s390 s390x

%description
This package contains the interface library routines used by IBM
modules to interface with the IBM eServer Cryptographic Accelerator
(ICA).

%package -n libica4
Summary:        Library interface for the IBM Cryptographic Accelerator
Group:          System/Libraries
Recommends:     libica-tools

%description -n libica4
This package contains the interface library routines used by IBM
modules to interface with the IBM eServer Cryptographic Accelerator
(ICA).

%package tools
Summary:        Utilities for the IBM Cryptographic Accelerator
Group:          Hardware/Other
Obsoletes:      libica < %{version}-%{release}
Obsoletes:      libica-2_3_0 < %{version}-%{release}
Obsoletes:      libica2 < %{version}-%{release}
Obsoletes:      libica3 < %{version}-%{release}
Provides:       libica = %{version}-%{release}
Provides:       libica-2_3_0 = %{version}-%{release}
Provides:       libica-plugin = %{version}-%{release}
Provides:       libica2 = %{version}-%{release}
Provides:       libica3 = %{version}-%{release}

%description tools
This package contains command-line utilities to inspect the IBM
eServer Cryptographic Accelerator (ICA).

%package        devel
Summary:        Development files for the ICA device driver interface library
Group:          Development/Libraries/C and C++
Requires:       libica4 = %{version}
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
%autosetup -p 1

%build
autoreconf --force --install
%configure CPPFLAGS="-Iinclude -fPIC" CFLAGS="%{optflags} -fPIC" \
  --enable-fips

%make_build clean
%make_build FIPSHMAC=fipshmac BUILD_VERSION="FIPS-SUSE-%version-%release"

%define major %(echo %{version} | sed -e 's/[.].*//')

%{expand:%%global __os_install_post {%__os_install_post fipshmac %{buildroot}/%{_libdir}/*.so.%{version} }}

%install
%make_install FIPSHMAC=fipshmac
make fipsinstall FIPSHMAC=fipshmac DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_includedir}
cp -p include/ica_api.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcz90crypt
install -D %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.z90crypt
install -D %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/scripts/z90crypt
install -D -m 644 %{SOURCE4} %{buildroot}%{_prefix}/lib/systemd/system/z90crypt.service
# It is installed 444 and then the __os_install_post cannot update it once the debuginfo is stripped
# We need it early because there is %{buildroot}/%{_libdir}/.*.so.%{major}.hmac symlink pointing at it
# and the dangling symlink test would fail
chmod 644 %{buildroot}/%{_libdir}/.*.so.%{version}.hmac

cp -a %{SOURCE1} .
rm -vf %{buildroot}%{_libdir}/libica*.la
rm -f %{buildroot}%{_datadir}/doc/libica/*
rmdir %{buildroot}%{_datadir}/doc/libica
# rm %{buildroot}/%{_sysconfdir}/libica/openssl3-fips.cnf
# rmdir %{buildroot}/%{_sysconfdir}/libica

%check
%make_build check FIPSHMAC=fipshmac

%pre tools
%service_add_pre z90crypt.service

%post tools
%service_add_post z90crypt.service
%{fillup_only -n z90crypt}

%preun tools
%service_del_preun z90crypt.service

%postun tools
%service_del_postun z90crypt.service

%post   -n libica4 -p /sbin/ldconfig
%postun -n libica4 -p /sbin/ldconfig

%files -n libica4
%{_libdir}/libica.so.%{version}
%{_libdir}/libica.so.%{major}
%{_libdir}/.libica.so.%{version}.hmac
%{_libdir}/.libica.so.%{major}.hmac
%{_libdir}/libica-cex.so.%{version}
%{_libdir}/libica-cex.so.%{major}
%{_libdir}/.libica-cex.so.%{version}.hmac
%{_libdir}/.libica-cex.so.%{major}.hmac
### Enable FIPS
%dir %{_sysconfdir}/libica
%{_sysconfdir}/libica/openssl3-fips.cnf
###

%files tools
%license LICENSE
%doc README.SUSE
%{_sbindir}/rcz90crypt
%attr(644,root,root) %{_fillupdir}/sysconfig.z90crypt
%{_bindir}/icainfo
%{_bindir}/icainfo-cex
%{_bindir}/icastats
%{_mandir}/man1/icainfo.1%{?ext_man}
%{_mandir}/man1/icainfo-cex.1%{?ext_man}
%{_mandir}/man1/icastats.1%{?ext_man}
%dir %{_prefix}/lib/systemd/scripts
%{_prefix}/lib/systemd/scripts/z90crypt
%{_prefix}/lib/systemd/system/z90crypt.service
# Must be in here, otherwise openssl-ibmca does not find it via DSO_load() bsc#952871
%{_libdir}/libica.so

%files devel
%{_includedir}/ica_api.h
%{_libdir}/libica-cex.so

%files devel-static
%{_libdir}/libica.a
%{_libdir}/libica-cex.a

%changelog
