#
# spec file for package ax25-apps
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define src_ver 0.0.8-rc5
Name:           ax25-apps
Version:        0.0.8~rc5
Release:        0
Summary:        AX.25 ham radio applications
License:        GPL-2.0-or-later
URL:            https://linux-ax25.in-berlin.de/
Source:         https://linux-ax25.in-berlin.de/pub/ax25-apps/%{name}-%{src_ver}.tar.xz
Patch0:         call.c.diff
Patch1:         add-missing-includes.patch
BuildRequires:  libax25-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncursesw)

%description
This package provides specific user applications for hamradio that use AX.25
Net/ROM or ROSE network protocols:

 * axcall: a general purpose AX.25, NET/ROM and ROSE connection program.
 * axlisten: a network monitor of all AX.25 traffic heard by the system.
 * ax25ipd: an RFC1226 compliant daemon which provides encapsulation of
   AX.25 traffic over IP.
 * ax25mond: retransmits data received from sockets into an AX.25 monitor
   socket.

%prep
%autosetup -p1 -n %{name}-%{src_ver}

%build
%configure \
	--program-transform-name='s@^call$@ax&@;s@^listen$@ax&@' \
	--docdir=%{_docdir}/%{name} \
	%{nil}
%make_build

%install
%make_install installconf
# installed via %%license macro
rm %{buildroot}%{_docdir}/%{name}/COPYING.ax25ipd

%check
%make_build check

%files
%license COPYING ax25ipd/COPYING.ax25ipd
%doc ChangeLog README AUTHORS NEWS
%{_bindir}/axcall
%{_bindir}/axlisten
%{_sbindir}/ax25ipd
%{_sbindir}/ax25mond
%{_sbindir}/ax25rtctl
%{_sbindir}/ax25rtd
%{_sysconfdir}/ax25/*.conf
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man5/*.5%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}
%{_docdir}/%{name}

%changelog
