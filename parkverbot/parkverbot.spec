#
# spec file for package parkverbot
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           parkverbot
Version:        1.2
Release:        0
Url:            http://parkverbot.sf.net/
Summary:        Daemon to prevent hard disk head parking in rotational media
License:        GPL-2.0+
Group:          System/Base

#Git-Clone:	git://git.code.sf.net/p/parkverbot/parkverbot
Source:         http://downloads.sf.net/parkverbot/%name-%version.tar.xz
Source2:        http://downloads.sf.net/parkverbot/%name-%version.tar.asc
Source3:        %name.keyring
BuildRequires:  pkgconfig >= 0.23
BuildRequires:  xz
BuildRequires:  pkgconfig(libHX) >= 3.12
%if 0%{?suse_version} >= 1310
BuildRequires:  systemd-rpm-macros
%endif
%if 0%{?suse_version} >= 1220 && 0%{?suse_version} < 1310
BuildRequires:  systemd
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q

%build
%configure --with-unitdir="%_unitdir"
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%_sbindir/parkverbot
%_mandir/man*/parkverbot*
%if 0%{?_unitdir:1}
%_unitdir/parkverbot@.service
%_unitdir/parkverbot.service
%endif
%doc LICENSE.GPL2

%changelog
