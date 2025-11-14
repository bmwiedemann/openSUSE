#
# spec file for package synce4l
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           synce4l
Version:        1.1.1
Release:        0
Summary:        Synchronous Ethernet (SyncE)
License:        GPL-2.0-only
URL:            https://github.com/intel/synce4l
Source0:        https://github.com/intel/synce4l/archive/%version/synce4l-%version.tar.gz
Source1:        synce4l.service
BuildRequires:  libnl3-devel
%{?systemd_requires}

%description
synce4l is a software implementation of Synchronous Ethernet (SyncE) according
to ITU-T Recommendation G.8264. The design goal is to provide logic to
supported hardware by processing Ethernet Synchronization Messaging Channel
(ESMC) and control Ethernet Equipment Clock (EEC) on Network Card Interface
(NIC).

Application can operate in two mutually exclusive input modes: line or
external. Both modes are described in next paragraphs.

The best source selection is done according to ITU-T Recommendations G.781 and
G.8264. Two network options are supported: option 1 and option 2.

%prep
%autosetup

%build
%make_build EXTRA_CFLAGS="$RPM_OPT_FLAGS -Wno-error" EXTRA_LDFLAGS="$RPM_LD_FLAGS"

%install
%make_install prefix=%_prefix mandir=%_mandir

install -m 644 -p configs/synce4l_dpll.cfg -D %buildroot%_sysconfdir/synce4l.conf
install -m 644 -p -D -t %buildroot%_unitdir %SOURCE1

%post
%systemd_post synce4l.service

%preun
%systemd_preun synce4l.service

%postun
%systemd_postun_with_restart synce4l.service

%files
%license COPYING
%doc *.md
%_mandir/*/*
%config(noreplace) %_sysconfdir/synce4l.conf
%_sbindir/synce4l
%_unitdir/synce4l.service

%changelog
