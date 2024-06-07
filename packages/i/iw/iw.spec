#
# spec file for package iw
#
# Copyright (c) 2024 SUSE LLC
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
Version:        6.9
Release:        0
Summary:        Configuration utility for nl80211 based wireless drivers
License:        ISC
URL:            https://wireless.wiki.kernel.org/en/users/documentation/iw
Source:         iw-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnl-3.0)

%description
iw is a nl80211 based CLI configuration utility for wireless devices. It
supports almost all new drivers that have been added to the kernel
recently.

%prep
%autosetup

%build
# FIXME: -fno-strict-aliasing seems to be obsolete, but upstream Makefile requires it.
# Either it is really obsolete or there is a hidden aliasing use.
%make_build CFLAGS="%{optflags} $(pkg-config --cflags libnl-3.0) -DCONFIG_LIBNL30 -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration"

%install
%make_install

%files
%license COPYING
%doc README
%{_sbindir}/iw
%{_mandir}/man8/iw.8%{?ext_man}

%changelog
