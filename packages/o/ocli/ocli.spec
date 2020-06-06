#
# spec file for package ocli
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ocli
Version:        0.9.0
Release:        0
Summary:        OwnTracks command line interface publisher 
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/owntracks/ocli
Source:         https://github.com/owntracks/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-FIX-adapted-for-gpsd-3.20.patch
BuildRequires:  gpsd-devel
BuildRequires:  mosquitto-devel
Provides:       owntracks-cli-publisher

%description
This is the OwnTracks command line interface publisher, a.k.a.
ocli, a small utility which connects to gpsd and publishes position
information in OwnTracks JSON to an MQTT broker in order for
compatible software to process location data.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot} BINDIR=%{_bindir} MANDIR=%{_mandir}

%files
%license LICENSE
%doc README.md
%{_bindir}/owntracks-cli-publisher
%{_mandir}/man1/owntracks-cli-publisher.1%{?ext_man}

%changelog
