#
# spec file for package keyd
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


%global libinput_overrides %{_sysconfdir}/libinput/local-overrides.quirks
Name:           keyd
Version:        2.6.0
Release:        0
Summary:        A key remapping daemon for linux
License:        MIT
URL:            https://github.com/rvaiya/keyd
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildRequires:  gcc
Requires:       python3-xlib
Requires(postun): sed
Requires(postun): shadow
Requires(pre):  shadow
%systemd_ordering

%description
Linux lacks a good key remapping solution.
In order to achieve satisfactory results a medley of tools need to be employed
(e.g xcape, xmodmap) with the end result often being tethered to a specified
environment (X11).
keyd attempts to solve this problem by providing a flexible system wide daemon
which remaps keys using kernel level input primitives (evdev, uinput).

%prep
%autosetup

%build
CFLAGS="%{optflags}" %make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix} FORCE_SYSTEMD=1

%check
make test-io

%files
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/keyd-application-mapper
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/keyd-application-mapper.1%{?ext_man}
%{_datadir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_datadir}/doc/%{name}

%pre
getent group keyd >/dev/null 2>&1 || groupadd keyd
if [ $1 -eq 2 ]; then
    # performed only on upgrade
    # remove eventual libinput overrides installed in v2.4.2 not used anymore since v2.4.3
    sed -i -e '/# added by %{name} package: START/,/# added by %{name} package: END/d' %{libinput_overrides} 2> /dev/null || :
    # remove file if it exists and is empty and remove libinput dir if empty
    if [ -f %{libinput_overrides} -a ! -s %{libinput_overrides} ]; then
	rm %{libinput_overrides}
	rm -d %{_sysconfdir}/libinput 2> /dev/null || :
    fi
fi

%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
if [ $1 -eq 0 ]; then
    # performed only on uninstall
    getent group keyd >/dev/null 2>&1 && groupdel keyd
fi

%changelog
