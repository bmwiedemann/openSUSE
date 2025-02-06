#
# spec file for package timezone
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%global AREA    Etc
%global ZONE    UTC
Name:           timezone
Version:        2025a
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
Recommends:     tzselect

%description
These are configuration files that describe available time zones. You
can select an appropriate time zone for your system with YaST.

%package -n     tzselect
Requires:       %{name} = %{version}
Requires:       awk
Summary:        Helper script to select the timezone
BuildArch:      noarch
Provides:       %{name}:/usr/bin/tzselect

%description -n tzselect
This package contains a helper script to select the timezone.

%prep
%autosetup -p1 -c -a1
sed -ri 's@%{_prefix}/local%{_sysconfdir}/zoneinfo@%{_datadir}/zoneinfo@g' *.[1358]
touch version

%build
unset ${!LC_*}
LANG=POSIX
LC_ALL=POSIX
AREA=%{AREA}
ZONE=%{ZONE}
export AREA LANG LC_ALL ZONE
%make_build TZDIR=%{_datadir}/zoneinfo CC="gcc" CFLAGS="%{optflags} -DHAVE_GETTEXT=1 -DTZDEFAULT='\"%{_sysconfdir}/localtime\"' -DTM_GMTOFF=tm_gmtoff -DTM_ZONE=tm_zone -Dlint" AWK=awk BUGEMAIL="opensuse-support@opensuse.org" KSHELL=/bin/sh
%make_build TZDIR=zoneinfo AWK=awk zones
# Generate posixrules
./zic -b fat -y ./yearistype -d zoneinfo -p %{AREA}/%{ZONE}

%install
mkdir -p %{buildroot}%{_datadir}/zoneinfo
cp -a zoneinfo %{buildroot}%{_datadir}/zoneinfo/posix
cp -al %{buildroot}%{_datadir}/zoneinfo/posix/. %{buildroot}%{_datadir}/zoneinfo
cp -a zoneinfo-leaps %{buildroot}%{_datadir}/zoneinfo/right
mkdir -p %{buildroot}%{_sysconfdir}
rm -f  %{buildroot}%{_sysconfdir}/localtime
rm -f  %{buildroot}%{_datadir}/zoneinfo/posixrules
%if 0%{?suse_version} >= 1230
ln -sf %{_datadir}/zoneinfo/%{AREA}/%{ZONE} %{buildroot}%{_sysconfdir}/localtime
%else
cp -fp %{buildroot}%{_datadir}/zoneinfo/%{AREA}/%{ZONE} %{buildroot}%{_sysconfdir}/localtime
%endif
ln -sf %{_sysconfdir}/localtime      %{buildroot}%{_datadir}/zoneinfo/posixrules
install -m 644 iso3166.tab %{buildroot}%{_datadir}/zoneinfo/iso3166.tab
install -m 644 zone.tab    %{buildroot}%{_datadir}/zoneinfo/zone.tab
install -m 644 zone1970.tab %{buildroot}%{_datadir}/zoneinfo/zone1970.tab
install -m 644 tzdata.zi %{buildroot}%{_datadir}/zoneinfo/tzdata.zi
install -D -m 755 tzselect %{buildroot}%{_bindir}/tzselect
install -D -m 755 zdump    %{buildroot}%{_sbindir}/zdump
install -D -m 755 zic      %{buildroot}%{_sbindir}/zic
install -m 644 -t %{buildroot}%{_datadir}/zoneinfo/ leapseconds leapseconds.awk leap-seconds.list

%files
%license LICENSE
%verify(not link md5 size mtime) %config(missingok,noreplace) %{_sysconfdir}/localtime
%{_datadir}/zoneinfo
%{_sbindir}/zdump
%{_sbindir}/zic

%files -n tzselect
%license LICENSE
%{_bindir}/tzselect

%changelog
