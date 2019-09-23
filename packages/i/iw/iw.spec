#
# spec file for package iw
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


Name:           iw
Version:        5.3
Release:        0
Summary:        Configuration utility for nl80211 based wireless drivers
License:        ISC
Group:          Hardware/Wifi
Url:            https://wireless.wiki.kernel.org/en/users/documentation/iw
Source:         https://kernel.org/pub/software/network/iw/iw-%{version}.tar.xz
Source2:        https://kernel.org/pub/software/network/iw/iw-%{version}.tar.sign
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnl-3.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
iw is a nl80211 based CLI configuration utility for wireless devices. It
supports almost all new drivers that have been added to the kernel
recently.

%prep
%setup -q

%build
# FIXME: -fno-strict-aliasing seems to be obsolete, but upstream Makefile requires it.
# Either it is really obsolete or there is a hidden aliasing use.
make %{?_smp_mflags} CFLAGS="%{optflags} $(pkg-config --cflags libnl-3.0) -DCONFIG_LIBNL30 -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration" V=1

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING README
%{_sbindir}/iw
%{_mandir}/man8/iw.8%{ext_man}

%changelog
