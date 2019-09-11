#
# spec file for package tripwire
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tripwire
Summary:        A tool to observe the filesystem
License:        GPL-2.0-or-later
Group:          Productivity/Security
Version:        2.4.3.7
Release:        0
Url:            https://github.com/Tripwire/tripwire-open-source
Source:         https://github.com/Tripwire/tripwire-open-source/releases/download/%{version}/tripwire-open-source-%{version}.tar.gz
Source1:        twcfg.txt
Source2:        README.SUSE
Patch0:         tripwire-2.4.1.2-src-policyconfig.patch
Patch1:         tripwire-2.4.3.7-config-dir-location.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  procps
Provides:       Tripwire = %version-%release

%description
By using tripwire, it is possible to observe the filesystem. tripwire
generates a database, controlled by a configuration file, of all
files, their checksums, etc. and it reports changes.

%prep
%setup -q -n tripwire-open-source-%{version}
%patch0 -p1
%patch1 -p1
cp %{S:2} .
autoreconf -f -i

%build
%configure
make CFLAGS="%{optflags}" CPPFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}/etc/tripwire
mkdir -p %{buildroot}/var/lib/tripwire/report
mkdir -p %{buildroot}/%{_mandir}/man4
mkdir -p %{buildroot}/%{_mandir}/man5
mkdir -p %{buildroot}/%{_mandir}/man8
mkdir -p %{buildroot}/usr/sbin
install -m 644 %{S:1} %{buildroot}/etc/tripwire
install -m 700 bin/* %{buildroot}/usr/sbin
for i in `find man -type f -name "*.?"`; do install -m 644 "$i" "%{buildroot}/%{_mandir}/${i#man}"; done

%post
# Transition from old system
if [ -f /etc/tw.cfg ] && [ ! -f /etc/tripwire/tw.cfg ]
then
    mv /etc/tw.cfg /etc/tripwire/tw.cfg
fi

%check
make check

%files
%defattr(-,root,root)
%doc COPYING ChangeLog COMMERCIAL MAINTAINERS TRADEMARK policy/*.txt README.SUSE
%doc %{_mandir}/*/*
%attr(750,root,root) %dir /etc/tripwire
%attr(750,root,root) %dir /var/lib/tripwire
%dir /var/lib/tripwire/report
/usr/sbin/*
%config /etc/tripwire/twcfg.txt

%changelog
