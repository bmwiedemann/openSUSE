#
# spec file for package horst
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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


Name:           horst
Version:        5.1
Release:        0
Summary:        IEEE 802.11 wireless LAN analyzer
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            http://br1.einfach.org/tech/horst/
Source:         https://github.com/br101/horst/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
Recommends:     iw
BuildRequires:  pkgconfig(ncursesw)
Patch0:         horst-ncurses6w.patch

%description
horst is an IEEE 802.11 WLAN analyzer with a text interface. Its
basic function is similar to tcpdump, Wireshark or Kismet, but it
shows different, aggregated information. It is made for debugging
wireless LANs with a focus on getting a quick overview instead of
deep packet inspection and has features for ad-hoc (IBSS) mode and
mesh networks.

%prep
%setup -q
%patch0 -p1
if [ -z "$SOURCE_DATE_EPOCH" ]; then
# Remove build time references so build-compare can do its work
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i "s/__DATE__/\"$FAKE_BUILDDATE\"/" *.c
sed -i "s/__TIME__/\"$FAKE_BUILDTIME\"/" *.c
fi

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -Dpm0755 horst %{buildroot}/%{_bindir}/horst
install -Dpm0644 horst.conf %{buildroot}/%{_sysconfdir}/horst.conf
install -Dpm0644 horst.8 %{buildroot}/%{_mandir}/man1/horst.8
install -Dpm0644 horst.conf.5 %{buildroot}/%{_mandir}/man5/horst.conf.5

%files
%doc LICENSE README.md
%{_bindir}/horst
%config %{_sysconfdir}/horst.conf
%{_mandir}/man*/*

%changelog
