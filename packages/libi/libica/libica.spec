#
# spec file for package libica
#
# Copyright (c) 2018-2020 SUSE LLC
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
Version:        3.6.0
Release:        0
Summary:        Library interface for the IBM Cryptographic Accelerator device driver
License:        CPL-1.0
Group:          Hardware/Other
URL:            https://github.com/opencryptoki/libica
Source:         https://github.com/opencryptoki/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# The icaioctl.h file came from https://sourceforge.net/p/opencryptoki/icadd/ci/master/tree/
Source1:        icaioctl.h
Source2:        README.SUSE
Source3:        sysconfig.z90crypt
Source4:        z90crypt
Source5:        z90crypt.service
Source6:        baselibs.conf
Source7:        %{name}-rpmlintrc
Patch1:         libica-sles15sp2-x25519-x448-fix-handling-of-non-canonical-values.patch
Patch2:         libica-sles15sp2-Fix-DES-and-TDES-key-length.patch
Patch3:         libica-sles15sp2-FIPS-provide-output-iv-as-required-by-FIPS-tests.patch
Patch4:         libica-sles15sp2-icainfo-bugfix-for-RSA-and-EC-related-info-for-softw.patch
Patch5:         libica-sles15sp2-Build-with-pthread-flag.patch
Patch6:         libica-sles15sp2-FIPS-introduce-HMAC-based-library-integrity-check.patch
Patch7:         libica-sles15sp2-FIPS-HMAC-based-library-integrity-check-addon.patch
Patch8:         libica-sles15sp2-FIPS-HMAC-based-library-integrity-check-rename-variables.patch
Patch9:         libica-sles15sp2-Zeroize-local-variables.patch
Patch10:        libica-sles15sp2-FIPS-add-SHA3-KATs-to-fips_powerup_tests.patch
Patch11:        libica-sles15sp2-FIPS-skip-SHA3-tests-if-running-on-hardware-without-.patch
Patch12:        libica-sles15sp2-FIPS-use-full-library-version-for-hmac-filename.patch
Patch13:        libica-sles15sp2-FIPS-fix-inconsistent-error-handling.patch
Patch99:        libica-sles15sp2-FIPS-hmac-key.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fipscheck
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  openssl-devel
PreReq:         %fillup_prereq
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
%autosetup -p 1

%build
mkdir -p include/linux/
cp %{SOURCE1} include/linux/

autoreconf --force --install
%configure CPPFLAGS="-Iinclude -fPIC" CFLAGS="%{optflags} -fPIC" \
  --enable-fips
%make_build clean
%make_build

%define major %(echo %{version} | sed -e 's/[.].*//')

%{expand:%%global __os_install_post {%__os_install_post fipshmac %{buildroot}/%{_libdir}/*.so.%{major} }}

%install
%make_install
mkdir -p %{buildroot}%{_includedir}
cp -p include/ica_api.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcz90crypt
install -D %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.z90crypt
install -D %{SOURCE4} %{buildroot}%{_prefix}/lib/systemd/scripts/z90crypt
install -D -m 644 %{SOURCE5} %{buildroot}%{_prefix}/lib/systemd/system/z90crypt.service

cp -a %{SOURCE2} .
rm -f %{buildroot}%{_libdir}/libica.la
rm -f %{buildroot}%{_datadir}/doc/libica/*
rmdir %{buildroot}%{_datadir}/doc/libica

%check
echo Tests should fail without a hash file
! %make_build check
fipshmac src/.libs/libica.so.%{major}
%make_build check

%pre tools
%service_add_pre z90crypt.service

%post tools
%service_add_post z90crypt.service
%{fillup_only -n z90crypt}

%preun tools
%service_del_preun z90crypt.service

%postun tools
%service_del_postun z90crypt.service

%post   -n libica3 -p /sbin/ldconfig
%postun -n libica3 -p /sbin/ldconfig

%files -n libica3
%defattr(-,root,root)
%{_libdir}/libica.so.%{version}
%{_libdir}/libica.so.%{major}
%{_libdir}/.libica.so.%{major}.hmac

%files tools
%license LICENSE
%doc README.SUSE
%{_sbindir}/rcz90crypt
%attr(0644,root,root) %{_fillupdir}/sysconfig.z90crypt
%{_bindir}/icainfo
%{_bindir}/icastats
%{_mandir}/man1/icainfo.1%{?ext_man}
%{_mandir}/man1/icastats.1%{?ext_man}
%dir %{_prefix}/lib/systemd/scripts
%{_prefix}/lib/systemd/scripts/z90crypt
%{_prefix}/lib/systemd/system/z90crypt.service
# Must be in here, otherwise openssl-ibmca does not find it via DSO_load() bsc#952871
%{_libdir}/libica.so

%files devel
%attr(0644,root,root) %{_includedir}/ica_api.h

%files devel-static
%attr(0644,root,root) %{_libdir}/libica.a

%changelog
