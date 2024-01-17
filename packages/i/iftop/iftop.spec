#
# spec file for package iftop
#
# Copyright (c) 2021 SUSE LLC
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


%define         pkg_version 1.0pre4
Name:           iftop
Version:        0.99.4
Release:        0
Summary:        Real-Time Interface Bandwidth Usage
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://www.ex-parrot.com/~pdw/iftop/
Source0:        https://www.ex-parrot.com/~pdw/iftop/download/iftop-%{pkg_version}.tar.gz
Patch0:         MAC-address-format.patch
Patch1:         001-Avoid-32-bit-overflow-for-rates-when-calculating-bar.patch
Patch2:         002-scale-up-to-tbit.patch
Patch3:         003-rateidx_init-fix.patch
Patch4:         004-iftop-unlimited_text_output.patch
Patch5:         0001-Prefer-ncurses6w.patch
Patch6:         006-iftop-choose_first_running_interface.patch
Patch7:         007-iftop-declare-extern-vars.patch
BuildRequires:  automake
BuildRequires:  libpcap-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(ncursesw)
%else
BuildRequires:  ncurses-devel
%endif

%description
iftop does for network usage what top(1) does for CPU usage. It listens
to network traffic on a named interface and displays a table of current
bandwidth usage by pairs of hosts. It is handy for explaining why the
network links slow.

%prep
%setup -q -n %{name}-%{pkg_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if 0%{?suse_version} >= 1500
%patch5 -p1
%endif
%patch6 -p1
%if 0%{?suse_version} >= 1500
%patch7 -p1
%endif

%build
autoreconf -fiv
%configure
%make_build %{?smp_mflags} CPPFLAGS=-DUSE_GETIFADDRS

%install
%make_install

%files
%license COPYING
%doc README ChangeLog TODO
%{_sbindir}/iftop
%{_mandir}/man8/iftop.8%{?ext_man}

%changelog
