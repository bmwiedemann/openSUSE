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
%define		devversion 5.99
# disable EBICS plugin for older openSUSE versions due to problems linking
# to xmlsec1-gcrypt:
%if 0%{?suse_version} > 1320 || 0%{?leap_version} >= 420300
%define          build_ebics 1
%else
%define          build_ebics 0
%endif
%define _name aqbanking
%define          aq_plugindir   %{_libdir}/aqbanking/plugins/43
%define          fronts_libdir  %{aq_plugindir}/frontends
%define          imex_plugindir %{aq_plugindir}/imexporters
%define          imex_datadir   %{_datadir}/%{_name}/imexporters
%define          fronts_datadir %{_datadir}/%{_name}/frontends
%define          qb_cfgmoddir   %{fronts_libdir}/qbanking/cfgmodules
%define          q4b_cfgmoddir  %{fronts_libdir}/q4banking/cfgmodules

Name:           aqbanking
Version:        5.99.40
%define _version %{version}beta
Release:        0
Summary:        Library for Online Banking Functions and Financial Data Import and Export
License:        GPL-2.0 or GPL-3.0
Group:          Productivity/Office/Finance
Url:            http://www.aquamaniac.de/aqbanking/
Source:         %{_name}-%{_version}.tar.gz
Source1:        aqbanking6-handbook-20190221.pdf
# Not available for beta:
#Source2:       %%{name}-%%{_version}.tar.gz.asc
Source3:        %{_name}.keyring
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gwenhywfar-devel >= 4.99.19
BuildRequires:  gwenhywfar-tools >= 4.99.19
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
Requires:       gwenhywfar-devel >= 4.99.19
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

%endif
%lang_package

%prep
%setup -q -n %{_name}-%{_version}

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
#	--enable-gui-tests
make

%install
%makeinstall
#mv %{buildroot}%{_datadir}/doc/%{_name} %{buildroot}%{_datadir}/doc/%{name}
#mv %{buildroot}%{_includedir}/aqpaypal %{buildroot}%{_includedir}/%{name}6/
%if %build_ebics
#mv %{buildroot}%{_includedir}/aqebics %{buildroot}%{_includedir}/%{name}6/
%endif
find %{buildroot} -type f -name "*.la" -delete -print
# Remove files that we'll have elsewhere
rm %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,ChangeLog,README}
#mv %{buildroot}%{_datadir}/doc/aqhbci/aqhbci-tool/README README.aqhbci
#mv %{buildroot}%{_datadir}/doc/aqpaypal/aqpaypal-tool/README README.aqpaypal
%if %build_ebics
#mv %{buildroot}%{_datadir}/doc/aqebics/aqebics-tool/README README.aqebics
%endif
# Install the handbook
mkdir -p %{buildroot}/%{_docdir}/%{name}
%__install -m 644 %{S:1} %{buildroot}%{_docdir}/%{name}/aqbanking-handbook.pdf
%find_lang %{_name}
%fdupes %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%if %build_ofx

%post ofx -p /sbin/ldconfig

%postun ofx -p /sbin/ldconfig

%endif

%if %build_ebics

%post ebics -p /sbin/ldconfig

%postun ebics -p /sbin/ldconfig

%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
# README.aqhbci README.aqpaypal
%exclude %{_docdir}/%{name}/aqbanking-handbook.pdf
### The original aqbanking files
%{_bindir}/%{_name}-cli
%{_libdir}/lib%{_name}*.so.*
%dir %{aq_plugindir}/dbio
%{aq_plugindir}/dbio/swift.*
%{_datadir}/%{_name}/aqbanking/
%{_datadir}/%{_name}/bankinfo/
%{_datadir}/%{_name}/dialogs/
%{_datadir}/%{_name}/typemaker2/
%dir %{_datadir}/%{_name}/backends
%{aq_plugindir}/bankinfo
%{imex_plugindir}/camt.*
%{imex_plugindir}/ctxfile.*
%{imex_plugindir}/csv.*
%{imex_plugindir}/eri2.*
%{imex_plugindir}/openhbci1.*
%{imex_plugindir}/q43.*
%{imex_plugindir}/sepa.*
%{imex_plugindir}/swift.*
%{imex_plugindir}/xml.*
%{imex_plugindir}/xmldb.*
%{imex_plugindir}/yellownet.*
%{imex_datadir}/ctxfile
%{imex_datadir}/camt
%{imex_datadir}/csv
%{imex_datadir}/eri
%{imex_datadir}/eri2
%{imex_datadir}/openhbci1
%{imex_datadir}/q43
%{imex_datadir}/sepa
%{imex_datadir}/swift
%{imex_datadir}/xml
%{imex_datadir}/xmldb/profiles/*
%{imex_datadir}/yellownet/profiles/*
### The aqhbci files
%{_bindir}/aqhbci-tool4
#{_libdir}/libaqhbci.so.*
%{aq_plugindir}/providers/aqhbci.*
%{_datadir}/%{_name}/backends/aqhbci
### The aqpaypal files
%{_bindir}/aqpaypal-tool
#{_libdir}/libaqpaypal.so.*
%{aq_plugindir}/providers/aqpaypal.*
%{_datadir}/%{_name}/backends/aqpaypal
### The aqnone files
#{_libdir}/libaqnone.so.*
%{aq_plugindir}/providers/aqnone.*
## Directories
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{aq_plugindir}
%dir %{aq_plugindir}/providers
%dir %{_datadir}/%{_name}
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
%{_bindir}/%{_name}-config
%{_includedir}/%{_name}6/
%{_libdir}/cmake/%{_name}-%{devversion}/
%{_libdir}/libaqbanking.so
#{_libdir}/libaqhbci.so
#{_libdir}/libaqpaypal.so
#{_libdir}/libaqnone.so
#{_libdir}/libaqbankingpp.so
%{_libdir}/pkgconfig/%{_name}.pc
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/%{_name}.m4
### The aqhbci files
#{_bindir}/hbcixml3
# .so files from sub-packages
%if %build_ofx
#{_libdir}/libaqofxconnect.so
%endif
%if %build_ebics
#{_libdir}/libaqebics.so
%endif

%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/aqbanking-handbook.pdf

%files lang -f %{_name}.lang

%if %build_ofx

%files ofx
%defattr(-,root,root)
%{aq_plugindir}/providers/aqofxconnect.*
%{imex_plugindir}/ofx.*
%{imex_datadir}/ofx
%{_datadir}/aqbanking/backends/aqofxconnect

%endif

%if %build_ebics

%files ebics
#doc README.aqebics
%defattr(-,root,root)
%{_bindir}/aqebics-tool
%{aq_plugindir}/providers/aqebics.*
#{imex_plugindir}/ebics.*
#{imex_datadir}/ebics
%{_datadir}/aqbanking/backends/aqebics

%endif

%changelog
