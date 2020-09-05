#
# spec file for package parkverbot
#
# Copyright (c) 2020 SUSE LLC
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


Name:           parkverbot
Version:        1.3
Release:        0
Summary:        Daemon to prevent hard disk head parking in rotational media
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://inai.de/projects/parkverbot/

#Git-Clone:	git://git.inai.de/parkverbot
Source:         https://inai.de/files/parkverbot/%name-%version.tar.xz
Source2:        https://inai.de/files/parkverbot/%name-%version.tar.asc
Source3:        %name.keyring
BuildRequires:  pkg-config >= 0.23
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  pkgconfig(libHX) >= 3.12

%description
Modern rotational hard disks have a misfeature involving the regular
automatic unloading of the heads, measurable by the SMART attribute
"Load_Cycle_Count", that causes latency on wake-up, and while the
manufacturers sell this as "green", it is believed to cause reduced
hard disk life.

The parkverbot daemon will periodically issue small read requests in
order to keep the hardware from going to its head-unloaded idle
state.

%prep
%autosetup -p1

%build
%configure --with-unitdir="%_unitdir"
%make_build

%install
%make_install

%pre
%service_add_pre parkverbot.service

%post
%service_add_post parkverbot.service

%preun
%service_del_preun parkverbot.service

%postun
%service_del_postun parkverbot.service

%files
%_sbindir/parkverbot
%_mandir/man*/parkverbot*
%_unitdir/parkverbot*.service
%license LICENSE.GPL2

%changelog
