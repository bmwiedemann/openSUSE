#
# spec file for package aqbanking
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nürnberg, Germany.
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


%define          build_ofx 1
%define	devversion	5.8
# disable EBICS plugin for older openSUSE versions due to problems linking
# to xmlsec1-gcrypt:
%if 0%{?suse_version} > 1320 || 0%{?leap_version} >= 420300
%define          build_ebics 1
%else
%define          build_ebics 0
%endif
%define          aq_plugindir   %{_libdir}/aqbanking/plugins/35
%define          fronts_libdir  %{aq_plugindir}/frontends
%define          imex_plugindir %{aq_plugindir}/imexporters
%define          imex_datadir   %{_datadir}/%{name}/imexporters
%define          fronts_datadir %{_datadir}/%{name}/frontends
%define          qb_cfgmoddir   %{fronts_libdir}/qbanking/cfgmodules
%define          q4b_cfgmoddir  %{fronts_libdir}/q4banking/cfgmodules

Name:           aqbanking
Version:        5.8.2
Release:        0
Summary:        Library for Online Banking Functions and Financial Data Import and Export
License:        GPL-2.0 or GPL-3.0
Group:          Productivity/Office/Finance
Url:            http://www.aquamaniac.de/aqbanking/
Source:         %{name}-%{version}.tar.gz
Source1:        aqbanking4-handbook-20091231.pdf
#Source2:	%{name}-%{version}.tar.gz.asc
Source3:	%{name}.keyring
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gwenhywfar-devel = 4.20.1
BuildRequires:  gwenhywfar-tools >= 4.20
BuildRequires:  ktoblzcheck-devel >= 1.10
BuildRequires:  pkgconfig
%if !0%{?sles_version}
BuildRequires:  pkgconfig(gtk+-2.0)
%else
BuildRequires:  gtk2-devel
%endif
%if %build_ofx
BuildRequires:  libofx-devel
%endif
%if %build_ebics
BuildRequires:  libltdl-devel
BuildRequires:  xmlsec1-gnutls-devel
%endif
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
AqBanking is a generic online banking interface. It allows multiple
back-ends (currently HBCI) and multiple front-ends (such as KDE, GNOME,
or console) to be used.

%package devel
Summary:        Library for Online Banking Functions and Financial Data Import/Export
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       cmake
Requires:       glibc-devel
Requires:       gwenhywfar-devel >= 4.10.0
Requires:       ktoblzcheck-devel
%if %build_ofx
Requires:       libofx-devel
%endif
%if %build_ebics
Requires:       libltdl-devel
Requires:       xmlsec1-gnutls-devel
%endif

%description devel
AqBanking is a generic OnlineBanking interface. It allows multiple
backends (currently HBCI) and multiple frontends  (e.g. KDE, GNOME,
console) to be used.

%package doc
Summary:        Library for Online Banking Functions and Financial Data Import/Export
License:        SUSE-Free-Art-1.3
Group:          Productivity/Office/Finance
Requires:       %{name} = %{version}

%description doc
AqBanking is a generic OnlineBanking interface. It allows multiple
backends (currently HBCI) and multiple frontends  (e.g. KDE, GNOME,
console) to be used.

This package contains a handbook.

%if %build_ofx

%package ofx
Summary:        Library for Online Banking Functions and Financial Data Import/Export
License:        GPL-2.0+
Group:          Productivity/Office/Finance
Requires:       %{name} = %{version}

%description ofx
AqBanking is a generic OnlineBanking interface. It allows multiple
backends (currently HBCI) and multiple frontends  (e.g. KDE, GNOME,
console) to be used.

%package -n libaqofxconnect7
Summary:        Connector between Aqbanking and OFX
License:        GPL-2.0 or GPL-3.0
Group:          Development/Libraries/C and C++

%description -n libaqofxconnect7
Conncetor between Aqbanking and OFX. Necessary for OFX direct connect
access.

%endif

%if %build_ebics

%package ebics
Summary:        Library for Online Banking Functions and Financial Data Import/Export
License:        GPL-2.0+
Group:          Productivity/Office/Finance
Requires:       %{name} = %{version}

%description ebics
AqBanking is a generic OnlineBanking interface. It allows multiple
backends (currently HBCI) and multiple frontends  (e.g. KDE, GNOME,
console) to be used.

%package -n libaqebics0
Summary:        Connector between Aqbanking and EBICS
License:        GPL-2.0 or GPL-3.0
Group:          Development/Libraries/C and C++

%description -n libaqebics0
Conncetor between Aqbanking and EBICS. Necessary for EBICS access.

%endif
%lang_package

%prep
%setup -q

%build
BACKEND_LIST="aqhbci aqnone aqpaypal"
%if %build_ofx
BACKEND_LIST="$BACKEND_LIST aqofxconnect"
%endif
%if %build_ebics
BACKEND_LIST="$BACKEND_LIST aqebics"
%endif

# quick fix for $CPP being unset and configure failing to handle include dirs properly
CPP=`which cpp`
export CPP
[ -n "$SOURCE_DATE_EPOCH" ] && builddate=--with-build-datetime=@$SOURCE_DATE_EPOCH
%configure\
	--enable-release $builddate \
	--with-backends="$BACKEND_LIST"  \
	--enable-full-doc \
	--with-docpath=%{_docdir}/%{name} \
	--enable-gui-tests
make

%install
%makeinstall
mv %{buildroot}%{_includedir}/aqpaypal %{buildroot}%{_includedir}/%{name}5/
%if %build_ebics
mv %{buildroot}%{_includedir}/aqebics %{buildroot}%{_includedir}/%{name}5/
%endif
find %{buildroot} -type f -name "*.la" -delete -print
# Remove files that we'll have elsewhere
rm %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,ChangeLog,README}
mv %{buildroot}%{_datadir}/doc/aqhbci/aqhbci-tool/README README.aqhbci
mv %{buildroot}%{_datadir}/doc/aqpaypal/aqpaypal-tool/README README.aqpaypal
%if %build_ebics
mv %{buildroot}%{_datadir}/doc/aqebics/aqebics-tool/README README.aqebics
%endif
# Install the handbook
mkdir -p %{buildroot}/%{_docdir}/%{name}
%__install -m 644 %{S:1} %{buildroot}%{_docdir}/%{name}/aqbanking-handbook.pdf
%find_lang %{name}
%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%if %build_ofx

%post ofx -p /sbin/ldconfig

%postun ofx -p /sbin/ldconfig

%post -n libaqofxconnect7 -p /sbin/ldconfig

%postun -n libaqofxconnect7 -p /sbin/ldconfig

%endif

%if %build_ebics

%post ebics -p /sbin/ldconfig

%postun ebics -p /sbin/ldconfig

%post -n libaqebics0 -p /sbin/ldconfig

%postun -n libaqebics0 -p /sbin/ldconfig

%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO README.aqhbci README.aqpaypal
%exclude %{_docdir}/%{name}/%{name}-handbook.pdf
### The original aqbanking files
%{_bindir}/%{name}-cli
%{_libdir}/lib%{name}*.so.*
%dir %{aq_plugindir}/dbio
%{aq_plugindir}/dbio/dtaus.*
%{aq_plugindir}/dbio/swift.*
%{_datadir}/%{name}/aqbanking/
%{_datadir}/%{name}/bankinfo/
%{_datadir}/%{name}/dialogs/
%{_datadir}/%{name}/typemaker2/
%dir %{_datadir}/%{name}/backends
%{aq_plugindir}/bankinfo
%{imex_plugindir}/ctxfile.*
%{imex_plugindir}/csv.*
%{imex_plugindir}/dtaus.*
%{imex_plugindir}/eri2.*
%{imex_plugindir}/openhbci1.*
%{imex_plugindir}/q43.*
%{imex_plugindir}/sepa.*
%{imex_plugindir}/swift.*
%{imex_plugindir}/xmldb.*
%{imex_plugindir}/yellownet.*
%{imex_datadir}/ctxfile
%{imex_datadir}/csv
%{imex_datadir}/dtaus
%{imex_datadir}/eri
%{imex_datadir}/eri2
%{imex_datadir}/openhbci1
%{imex_datadir}/q43
%{imex_datadir}/sepa
%{imex_datadir}/swift
%{imex_datadir}/xmldb/profiles/*
%{imex_datadir}/yellownet/profiles/*
### The aqhbci files
%{_bindir}/aqhbci-tool4
%{_libdir}/libaqhbci.so.*
%{aq_plugindir}/providers/aqhbci.*
%{_datadir}/%{name}/backends/aqhbci
### The aqpaypal files
%{_bindir}/aqpaypal-tool
%{_libdir}/libaqpaypal.so.*
%{aq_plugindir}/providers/aqpaypal.*
%{_datadir}/%{name}/backends/aqpaypal
### The aqnone files
%{_libdir}/libaqnone.so.*
%{aq_plugindir}/providers/aqnone.*
## Directories
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{aq_plugindir}
%dir %{aq_plugindir}/providers
%dir %{_datadir}/%{name}
%dir %{imex_plugindir}
%dir %{imex_datadir}
%dir %{imex_datadir}/xmldb
%dir %{imex_datadir}/xmldb/profiles
%dir %{imex_datadir}/yellownet
%dir %{imex_datadir}/yellownet/profiles
%if !%build_ofx
%{imex_datadir}/ofx
%endif

%files devel
%defattr(-,root,root)
### The aqbanking files
%{_bindir}/%{name}-config
%{_includedir}/%{name}5/
%{_libdir}/cmake/%{name}-%{devversion}/
%{_libdir}/libaqbanking.so
%{_libdir}/libaqhbci.so
%{_libdir}/libaqpaypal.so
%{_libdir}/libaqnone.so
%{_libdir}/libaqbankingpp.so
%{_libdir}/pkgconfig/%{name}.pc
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/%{name}.m4
### The aqhbci files
%{_bindir}/hbcixml3
# .so files from sub-packages
%if %build_ofx
%{_libdir}/libaqofxconnect.so
%endif
%if %build_ebics
%{_libdir}/libaqebics.so
%endif

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/aqbanking-handbook.pdf

%files lang -f %{name}.lang

%if %build_ofx

%files ofx
%defattr(-,root,root)
%{aq_plugindir}/providers/aqofxconnect.*
%{imex_plugindir}/ofx.*
%{imex_datadir}/ofx
%{_datadir}/aqbanking/backends/aqofxconnect

%files -n libaqofxconnect7
%defattr(-,root,root)
%{_libdir}/libaqofxconnect.so.*

%endif

%if %build_ebics

%files ebics
%doc README.aqebics
%defattr(-,root,root)
%{_bindir}/aqebics-tool
%{aq_plugindir}/providers/aqebics.*
#%{imex_plugindir}/ebics.*
#%{imex_datadir}/ebics
%{_datadir}/aqbanking/backends/aqebics

%files -n libaqebics0
%defattr(-,root,root)
%{_libdir}/libaqebics.so.*

%endif

%changelog
