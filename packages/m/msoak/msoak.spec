#
# spec file for package msoak
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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

Name:           msoak
Version:        0.6
Release:        0
Summary:        A utility to simultaneously subscribe to MQTT servers/topics
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/jpmens/msoak
Source:         https://github.com/jpmens/msoak/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         msoak-makefile.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libmosquitto)
BuildRequires:  pkgconfig(lua5.3)

%description
msoak is a utility to simultaneously subscribe to an arbitrary
number of topics on any number of MQTT brokers and optionally
modify or normalize received payloads before printing them out.
This utility was created for being able to back up to a central
location messages received by a number of brokers; instead of
launching (and having to monitor success of) a large number of
mosquitto_sub(1) programs, msoak took on the job.

msoak uses asynchronous connects to the MQTT brokers so that it
can handle situations in which a broker may temporarily be
unavailable.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}/%{_mandir}/man1
%make_install DESTDIR=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir}

%files
%license LICENSE
%doc README.md
%doc example.config example.lua
%{_bindir}/msoak
%{_mandir}/man1/msoak.1%{?ext_man}

%changelog
