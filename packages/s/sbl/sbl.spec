#
# spec file for package sbl
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


Name:           sbl
Version:        3.5.0.20130317.git7a75bc29
Release:        0
Summary:        Screen reader for the Linux console
License:        GPL-2.0-or-later
Group:          Hardware/Other
Source:         sbl-%{version}.tar.bz2
Source1:        sbl.service
Source2:        brld.service
Patch1:         sbl-shared.patch
Patch2:         sbl-nostrip.patch
Patch3:         sbl-install_perms.patch
Patch4:         sbl-libdir.patch
Patch5:         sbl-init-scripts.patch
Patch6:         sbl-sppkdev.patch
Patch7:         sbl-orca-python3.patch
BuildRequires:  bluez-devel
BuildRequires:  gcc-c++
BuildRequires:  libusb-devel
BuildRequires:  orca
BuildRequires:  python3-base
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

%description
SUSE blinux is a screen reader for the Linux console. It supports
braille displays.

%package orca
Summary:        brld-orca brlapi
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       orca

%description orca
this python module enables orca to use brld for braille output

%prep
%setup -q
%patch1
%patch2
%patch3
%if "%{_lib}" == "lib64"
%patch4 -p1
%endif
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags} -D_POSIX_C_SOURCE=2 -D_BSD_SOURCE" \
	LIB_CFLAGS="%{optflags} -D_POSIX_C_SOURCE=2 -D_BSD_SOURCE -fPIC $(pkg-config speech-dispatcher --cflags)"

%install
%make_install LIBINSTPATH=%{_libdir}
rm -f %{buildroot}%{_initddir}/sbl
rm -f %{buildroot}%{_initddir}/brld
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/sbl.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/brld.service
rm -f %{buildroot}%{_sbindir}/rcsbl
rm -f %{buildroot}%{_sbindir}/rcbrld
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcsbl
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcbrld

%pre
%service_add_pre sbl.service brld.service

%preun
%service_del_preun brld.service sbl.service

%post
/sbin/ldconfig
%service_add_post sbl.service brld.service

%postun
/sbin/ldconfig
%service_del_postun brld.service sbl.service

%files
%defattr (-,root,root,755)
%doc doc/* Changelog
%dir %{_sysconfdir}/sbl
%config %{_sysconfdir}/sbl/keymap
%config %{_sysconfdir}/sbl/profile
%config %{_sysconfdir}/sbl/spkfilter
%config %{_sysconfdir}/sbl.conf
%dir %{_libexecdir}/sbl
%{_libexecdir}/sbl/lib
%{_sysconfdir}/sbl/brltbl
%{_sysconfdir}/sbl/spk
%{_sbindir}/sbl
%{_sbindir}/rcsbl
%{_sbindir}/brld
%{_sbindir}/rcbrld
%{_libdir}/libbrld.so*
%{_unitdir}/sbl.service
%{_unitdir}/brld.service
%{_mandir}/man8/brld.8.gz
%{_mandir}/man8/sbl.8.gz

%files orca
%defattr (-,root,root,755)
%dir %{python3_sitearch}/orca
%{python3_sitearch}/orca/brlapi.py*

%changelog
