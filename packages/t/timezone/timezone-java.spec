#
# spec file for package timezone-java
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           timezone-java
Version:        2024a
Release:        0
Summary:        Time Zone Descriptions
License:        BSD-3-Clause AND SUSE-Public-Domain
Group:          System/Base
URL:            https://www.iana.org/time-zones
Source:         https://www.iana.org/time-zones/repository/releases/tzdata%{version}.tar.gz
Source1:        https://www.iana.org/time-zones/repository/releases/tzcode%{version}.tar.gz
Source2:        https://www.iana.org/time-zones/repository/releases/tzdata%{version}.tar.gz.asc
Source3:        https://www.iana.org/time-zones/repository/releases/tzcode%{version}.tar.gz.asc
Source4:        timezone.keyring
Source5:        %{name}.changes
Patch0:         tzdata-china.diff
Patch3:         iso3166-uk.diff
Patch4:         timezone-2018f-bsc1112310.patch
Patch5:         fat.patch
BuildRequires:  java
BuildRequires:  javazic
BuildRequires:  tzdb
#!BuildIgnore:  tzdata-java
#!BuildIgnore:  tzdata-java8
Requires(pre):  coreutils
Requires(pre):  filesystem
Provides:       tzdata-java = %{version}-%{release}
Provides:       tzdata-java8 = %{version}-%{release}
BuildArch:      noarch

%description
These are configuration files that describe available time zones - this
package is intended for Java Virtual Machine based on OpenJDK.

%prep
%autosetup -p1 -c -a1
sed -ri 's@%{_prefix}/local%{_sysconfdir}/zoneinfo@%{_datadir}/zoneinfo@g' *.[1358]
echo "tzdata%{version}" >> VERSION

%build
# Java 6/7 data
java \
%if %{?pkg_vcmp:%pkg_vcmp java >= 9}%{!?pkg_vcmp:0}
     --add-exports=java.base/sun.security.action=ALL-UNNAMED \
%endif
     -jar %{_javadir}/javazic.jar -V %{version} \
     -d javazi \
     africa antarctica asia australasia europe northamerica \
     southamerica backward etcetera  \
     %{_datadir}/javazic/tzdata_jdk/gmt \
     %{_datadir}/javazic/tzdata_jdk/jdk11_backward
# Java 8/9 data
java -jar %{_javadir}/tzdb.jar \
     -srcdir . -dstfile javazi/tzdb.dat \
     africa antarctica asia australasia europe northamerica \
     southamerica backward etcetera  \
     %{_datadir}/tzdb/tzdata_jdk/gmt \
     %{_datadir}/tzdb/tzdata_jdk/jdk11_backward

%install
install -d -m 0755 %{buildroot}/%{_datadir}
cp -a javazi %{buildroot}%{_datadir}

%files
%license LICENSE
%{_datadir}/javazi

%changelog
