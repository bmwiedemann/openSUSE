#
# spec file for package timezone
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


Name:           timezone
Summary:        Time Zone Descriptions
License:        BSD-3-Clause AND SUSE-Public-Domain
Group:          System/Base
URL:            http://www.iana.org/time-zones
# COMMON-BEGIN
Version:        2022g
Release:        0
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
# COMMON-END
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%global AREA    Etc
%global ZONE    UTC

%description
These are configuration files that describe available time zones. You
can select an appropriate time zone for your system with YaST.

%prep
%setup -q -c -a 1
# COMMON-PREP-BEGIN
%patch0 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
sed -ri 's@/usr/local/etc/zoneinfo@%{_datadir}/zoneinfo@g' *.[1358]
# COMMON-PREP-END

touch version

%build
unset ${!LC_*}
LANG=POSIX
LC_ALL=POSIX
AREA=%{AREA}
ZONE=%{ZONE}
export AREA LANG LC_ALL ZONE
make %{?_smp_mflags} TZDIR=%{_datadir}/zoneinfo CFLAGS="%{optflags} -DHAVE_GETTEXT=1 -DTZDEFAULT='\"/etc/localtime\"' -DTM_GMTOFF=tm_gmtoff -DTM_ZONE=tm_zone -Dlint" AWK=awk BUGEMAIL="opensuse-support@opensuse.org"
make %{?_smp_mflags} TZDIR=zoneinfo AWK=awk zones
# Generate posixrules
./zic -b fat -y ./yearistype -d zoneinfo -p %{AREA}/%{ZONE}

%install
mkdir -p %{buildroot}%{_prefix}/share/zoneinfo
cp -a zoneinfo %{buildroot}%{_prefix}/share/zoneinfo/posix
cp -al %{buildroot}%{_prefix}/share/zoneinfo/posix/. %{buildroot}%{_prefix}/share/zoneinfo
cp -a zoneinfo-leaps %{buildroot}%{_prefix}/share/zoneinfo/right
mkdir -p %{buildroot}/etc
rm -f  %{buildroot}/etc/localtime
rm -f  %{buildroot}%{_prefix}/share/zoneinfo/posixrules
%if 0%{?suse_version} >= 1230
ln -sf %{_prefix}/share/zoneinfo/%{AREA}/%{ZONE} %{buildroot}/etc/localtime
%else
cp -fp %{buildroot}%{_prefix}/share/zoneinfo/%{AREA}/%{ZONE} %{buildroot}/etc/localtime
%endif
ln -sf /etc/localtime      %{buildroot}%{_prefix}/share/zoneinfo/posixrules
install -m 644 iso3166.tab %{buildroot}%{_prefix}/share/zoneinfo/iso3166.tab
install -m 644 zone.tab    %{buildroot}%{_prefix}/share/zoneinfo/zone.tab
install -m 644 zone1970.tab %{buildroot}%{_prefix}/share/zoneinfo/zone1970.tab
install -m 644 tzdata.zi %{buildroot}%{_prefix}/share/zoneinfo/tzdata.zi
install -D -m 755 tzselect %{buildroot}%{_bindir}/tzselect
install -D -m 755 zdump    %{buildroot}%{_sbindir}/zdump
install -D -m 755 zic      %{buildroot}%{_sbindir}/zic

%files
%defattr(-,root,root)
%verify(not link md5 size mtime) %config(missingok,noreplace) /etc/localtime
%{_datadir}/zoneinfo
%{_bindir}/tzselect
%{_sbindir}/zdump
%{_sbindir}/zic

%changelog
