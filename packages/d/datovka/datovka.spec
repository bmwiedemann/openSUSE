#
# spec file for package datovka
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# tests are broken on 32 bits
%ifarch %ix86 %arm
%bcond_with tests
%else
%bcond_without tests
%endif

%if 0%{?suse_version} > 1500
%define qt_version 6
%define qt_version_full 6.2.0
%else
%define qt_version 5
%define qt_version_full 5.4.1
%endif
Name:           datovka
Version:        4.30.1
Release:        0
Summary:        Library to access Czech eGov system "Datove schranky"
License:        GPL-3.0-or-later
Group:          Development/Libraries/Python
URL:            https://www.datovka.cz
Source0:        https://datovka.nic.cz/%{version}/%{name}-%{version}.tar.xz
Source1:        https://datovka.nic.cz/%{version}/%{name}-%{version}.tar.xz.sha256
# PATCH-FIX-UPSTREAM: remove some issues with current .pro file
Patch0:         0001-datovka.pro-fixes.patch
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt%{qt_version}Core) >= %{qt_version_full}
BuildRequires:  cmake(Qt%{qt_version}Gui) >= %{qt_version_full}
BuildRequires:  cmake(Qt%{qt_version}Network) >= %{qt_version_full}
BuildRequires:  cmake(Qt%{qt_version}PrintSupport) >= %{qt_version_full}
BuildRequires:  cmake(Qt%{qt_version}Sql) >= %{qt_version_full}
BuildRequires:  cmake(Qt%{qt_version}Svg) >= %{qt_version_full}
BuildRequires:  cmake(Qt%{qt_version}WebSockets) >= %{qt_version_full}
BuildRequires:  cmake(Qt%{qt_version}Widgets) >= %{qt_version_full}
BuildRequires:  cmake(QuaZip-Qt%{qt_version})
BuildRequires:  pkgconfig(libdatovka) >= 0.8.0
%if %{with tests}
BuildRequires:  qt6-sql-sqlite
BuildRequires:  cmake(Qt%{qt_version}Test) >= %{qt_version_full}
%endif
Recommends:     %{name}-lang
# Included inside with different approach
Obsoletes:      python-dslib < 4.30.0
Provides:       python-dslib = 4.30.0
%if 0%{qt_version} == 6
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt_version_full}
Requires:       qt6-sql-sqlite
BuildRequires:  qt6-tools-linguist
%else
BuildRequires:  libqt5-linguist
Requires:       libqt5-sql-sqlite
%endif

%description
A library for accessing ISDS (Informační system datovych schranek/
Data Box Information System) SOAP services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%{?lang_package}

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

%if 0%{qt_version} == 6
lrelease6 datovka.pro
%{qmake6} PREFIX=%{_prefix} DISABLE_VERSION_CHECK_BY_DEFAULT=1
%{qmake6_build}

%if %{with tests}
pushd tests
%{qmake6}
%{qmake6_build}
popd
%endif

%else # qt5
lrelease-qt5 datovka.pro
%qmake5 PREFIX=%{_prefix} DISABLE_VERSION_CHECK_BY_DEFAULT=1
%make_jobs

%if %{with tests}
pushd tests
%qmake5
%make_jobs
popd
%endif

%endif

%install
%if 0%{qt_version} == 6
%{qmake6_install}
%else
%qmake5_install
%endif

# fix desktop file
sed -i \
    -e 's:Office;:Office;Network;Email;:g' \
    %{buildroot}%{_datadir}/applications/cz.nic.datovka.desktop
rm -rf %{buildroot}%{_datadir}/datovka/doc

%check
%if %{with tests}
pushd tests
# these use disabled legacy functions of openssl
cat >BLACKLIST <<'EOF'
[x509CrtVerify]
*
[verifySignature01]
*
[verifySignature02]
*
[cryptoAddCrl02]
*
[rawTstVerify]
*
[p12ToPem]
*
EOF
./tests -skipblacklisted
popd
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/datovka
%{_datadir}/applications/cz.nic.datovka.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/cz.nic.datovka.metainfo.xml
%dir %{_datadir}/datovka
%dir %{_datadir}/datovka/localisations/
%{_datadir}/datovka/localisations/datovka_cs.qm
%{_datadir}/datovka/localisations/datovka_en.qm
%dir %{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/*

%changelog
