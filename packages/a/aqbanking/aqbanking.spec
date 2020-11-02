#
# spec file for package aqbanking
#
# Copyright (c) 2020 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define          cmake_config_version 6.2
%define          build_ofx 1
%define          _name aqbanking
%define          aq_plugindir   %{_libdir}/aqbanking/plugins/44
%define          fronts_libdir  %{aq_plugindir}/frontends
%define          imex_plugindir %{aq_plugindir}/imexporters
%define          imex_datadir   %{_datadir}/%{_name}/imexporters
%define          fronts_datadir %{_datadir}/%{_name}/frontends
%define          qb_cfgmoddir   %{fronts_libdir}/qbanking/cfgmodules
%define          q4b_cfgmoddir  %{fronts_libdir}/q4banking/cfgmodules
Name:           aqbanking
Version:        6.2.5
Release:        0
Summary:        Library for Online Banking Functions and Financial Data Import and Export
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Office/Finance
URL:            https://www.aquamaniac.de/aqbanking/
Source:         %{name}-%{version}.tar.gz
Source1:        %{name}-%{version}.tar.gz.asc
Source2:        aqbanking6-handbook-20190221.pdf
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  gwenhywfar-devel >= 5.2.0.1
BuildRequires:  gwenhywfar-tools >= 5.2.0.1
BuildRequires:  ktoblzcheck-devel >= 1.10
BuildRequires:  libltdl-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlsec1-gnutls-devel
Recommends:     %{name}-lang
%if %{build_ofx}
BuildRequires:  libofx-devel
%endif

%description
AqBanking is a generic online banking interface. It allows multiple
back-ends (currently HBCI) and multiple front-ends (such as KDE, GNOME,
or console) to be used.

%package devel
Summary:        Library for Online Banking Functions and Financial Data Import/Export
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       cmake
Requires:       glibc-devel
Requires:       gwenhywfar-devel >= 5.2.0.1
Requires:       ktoblzcheck-devel
Requires:       libltdl-devel
Requires:       xmlsec1-gnutls-devel
%if %{build_ofx}
Requires:       libofx-devel
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

%if %{build_ofx}
%package ofx
Summary:        Library for Online Banking Functions and Financial Data Import/Export
License:        GPL-2.0-or-later
Group:          Productivity/Office/Finance
Requires:       %{name} = %{version}

%description ofx
AqBanking is a generic OnlineBanking interface. It allows multiple
backends (currently HBCI) and multiple frontends  (e.g. KDE, GNOME,
console) to be used.

%endif

%package ebics
Summary:        Library for Online Banking Functions and Financial Data Import/Export
License:        GPL-2.0-or-later
Group:          Productivity/Office/Finance
Requires:       %{name} = %{version}

%description ebics
AqBanking is a generic OnlineBanking interface. It allows multiple
backends (currently HBCI) and multiple frontends  (e.g. KDE, GNOME,
console) to be used.

%lang_package

%prep
%setup -q

%build
BACKEND_LIST="aqhbci aqnone aqpaypal"
%if %{build_ofx}
BACKEND_LIST="$BACKEND_LIST aqofxconnect"
%endif
BACKEND_LIST="$BACKEND_LIST aqebics"

# quick fix for $CPP being unset and configure failing to handle include dirs properly
CPP=`which cpp`
export CPP
[ -n "$SOURCE_DATE_EPOCH" ] && builddate=--with-build-datetime=@$SOURCE_DATE_EPOCH
%configure\
  --enable-release $builddate \
  --with-backends="$BACKEND_LIST"  \
  --enable-full-doc \
  --with-docpath=%{_docdir}/%{name} \

make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
# Remove files that we'll have elsewhere
rm %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,ChangeLog,README}

# Install the handbook
mkdir -p %{buildroot}/%{_docdir}/%{name}
install -m 644 %{SOURCE2} %{buildroot}%{_docdir}/%{name}/aqbanking-handbook.pdf
%find_lang %{_name}

%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{build_ofx}
%post ofx -p /sbin/ldconfig
%postun ofx -p /sbin/ldconfig
%endif

%post ebics -p /sbin/ldconfig
%postun ebics -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%exclude %{_docdir}/%{name}/aqbanking-handbook.pdf
%dir %{_datadir}/%{_name}
%dir %{_datadir}/%{_name}/backends
%dir %{_libdir}/aqbanking
%dir %{_libdir}/aqbanking/plugins
%dir %{aq_plugindir}
%dir %{aq_plugindir}/dbio
%dir %{aq_plugindir}/providers
%dir %{imex_datadir}
%dir %{imex_datadir}/xmldb
%dir %{imex_datadir}/xmldb/profiles
%dir %{imex_datadir}/yellownet
%dir %{imex_datadir}/yellownet/profiles
%dir %{imex_plugindir}
%{_bindir}/%{_name}-cli
%{_bindir}/aqhbci-tool4
%{_bindir}/aqpaypal-tool
%{_datadir}/%{_name}/aqbanking/
%{_datadir}/%{_name}/backends/aqhbci
%{_datadir}/%{_name}/backends/aqpaypal
%{_datadir}/%{_name}/bankinfo/
%{_datadir}/%{_name}/dialogs/
%{_datadir}/%{_name}/typemaker2/
%{_libdir}/lib%{_name}*.so.*
%{aq_plugindir}/bankinfo
%{aq_plugindir}/dbio/swift.*
%{aq_plugindir}/providers/aqhbci.*
%{aq_plugindir}/providers/aqnone.*
%{aq_plugindir}/providers/aqpaypal.*
%{imex_datadir}/camt
%{imex_datadir}/csv
%{imex_datadir}/ctxfile
%{imex_datadir}/eri
%{imex_datadir}/eri2
%if !%{build_ofx}
%{imex_datadir}/ofx
%endif
%{imex_datadir}/openhbci1
%{imex_datadir}/q43
%{imex_datadir}/sepa
%{imex_datadir}/swift
%{imex_datadir}/xml
%{imex_datadir}/xmldb/profiles/*
%{imex_datadir}/yellownet/profiles/*
%{imex_plugindir}/camt.*
%{imex_plugindir}/csv.*
%{imex_plugindir}/ctxfile.*
%{imex_plugindir}/eri2.*
%{imex_plugindir}/openhbci1.*
%{imex_plugindir}/q43.*
%{imex_plugindir}/sepa.*
%{imex_plugindir}/swift.*
%{imex_plugindir}/xml.*
%{imex_plugindir}/xmldb.*
%{imex_plugindir}/yellownet.*

%files devel
%license COPYING
%dir %{_datadir}/aclocal
%{_bindir}/%{_name}-config
%{_datadir}/aclocal/%{_name}.m4
%{_includedir}/%{_name}6/
%{_libdir}/cmake/%{_name}-%{cmake_config_version}/
%{_libdir}/libaqbanking.so
%{_libdir}/pkgconfig/%{_name}.pc

%files doc
%{_docdir}/%{name}/aqbanking-handbook.pdf

%files lang -f %{_name}.lang

%if %{build_ofx}
%files ofx
%license COPYING
%{_datadir}/aqbanking/backends/aqofxconnect
%{aq_plugindir}/providers/aqofxconnect.*
%{imex_datadir}/ofx
%{imex_plugindir}/ofx.*

%endif

%files ebics
%license COPYING
%{_bindir}/aqebics-tool
%{_datadir}/aqbanking/backends/aqebics
%{aq_plugindir}/providers/aqebics.*

%changelog
