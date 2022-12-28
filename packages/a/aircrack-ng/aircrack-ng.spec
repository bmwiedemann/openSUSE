#
# spec file for package aircrack-ng
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without unstable
%bcond_without sqlite
%bcond_with asan
Name:           aircrack-ng
Version:        1.7
Release:        0
Summary:        A set of tools for auditing wireless networks
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.aircrack-ng.org/
Source0:        https://download.aircrack-ng.org/%{name}-%{version}.tar.gz
Source1:        README.SUSE
Patch1:         s390x-enablement-cpustats.patch
BuildRequires:  autoconf
BuildRequires:  ethtool
BuildRequires:  expect
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel >= 1.2.0
BuildRequires:  libnl3-devel >= 3.2
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-graphviz
BuildRequires:  python3-setuptools
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(hwloc)
BuildRequires:  pkgconfig(libpcre) >= 3.0.0
%if 0%{?with sqlite}
BuildRequires:  sqlite3-devel
%endif
Requires:       ethtool
Requires:       python3-graphviz
Requires:       wireless-tools

%description
Aircrack-ng is a suite of tools to assess network security.
The main capabilities of aircrack-ng is to monitor, attack, test and crack WiFi networks
for auditing purposes.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
Development files for %{name}.

%prep
%setup -q
%patch1 -p1
find patches/ -type f -exec sed -i 's|\r||g' {} +
cp "%{SOURCE1}" .
# Force python3 interpreter
sed -i -e 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' scripts/versuck-ng/versuck-ng
# Drop shebang
find . -type f -name "lib*Parse.py" -exec sed -i -e '/^#!\//, 1d' {} \;

%build
# GCC LTO objects must be "fat" to avoid assembly errors
export CFLAGS="-ffat-lto-objects -fcommon"
autoreconf -fiv
%configure \
%if 0%{?with asan}
           --enable-asan \
%endif
           --with-experimental=%{?with_unstable:yes --with-ext-scripts}%{?!with_unstable:no} \
           --enable-static=yes \
           --enable-shared=no \
           --docdir="%{_docdir}/%{name}" \
           --with-sqlite3=%{?with_sqlite:yes}%{?!with_sqlite:no} \
           --with-gcrypt \
           --enable-libnl
%make_build

%install
%make_install
rm patches/old/ieee80211_inject.patch
find %{buildroot} -type f \( -name "*.la" -o -name "*.a" \) -delete -print
%if %{with unstable}
rm %{buildroot}%{_prefix}/local/lib/python3*/site-packages/aircrack-ng/air*-install_files.txt
rm %{buildroot}%{_datadir}/airgraph-ng/.keepthisfolder
%endif

%check
%make_build check

%files
%license LICENSE LICENSE.OpenSSL
%doc AUTHORS ChangeLog README README.SUSE
%doc patches
%{_bindir}/aircrack-ng
%{_bindir}/airdecap-ng
%{_bindir}/airdecloak-ng
%{_bindir}/ivstools
%{_bindir}/kstats
%{_bindir}/makeivs-ng
%{_bindir}/packetforge-ng
%{_bindir}/wpaclean
%{_sbindir}/airbase-ng
%{_sbindir}/aireplay-ng
%{_sbindir}/airmon-ng
%{_sbindir}/airodump-ng
%{_sbindir}/airodump-ng-oui-update
%{_sbindir}/airserv-ng
%{_sbindir}/airtun-ng
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%if %{with unstable}
%doc %{_docdir}/%{name}/Apple.sample.txt
%doc %{_docdir}/%{name}/dropRules.conf.example
%{_bindir}/airdrop-ng
%{_bindir}/airgraph-ng
%{_bindir}/airodump-join
%{_bindir}/besside-ng-crawler
%{_bindir}/buddy-ng
%{_bindir}/versuck-ng
%{_sbindir}/airventriloquist-ng
%{_sbindir}/besside-ng
%{_sbindir}/easside-ng
%{_sbindir}/tkiptun-ng
%{_sbindir}/wesside-ng
%{python3_sitelib}/air*
%{_datadir}/airgraph-ng
%endif
%if %{with sqlite}
%{_bindir}/airolib-ng
%endif

%files devel
%{_includedir}/aircrack-ng

%changelog
