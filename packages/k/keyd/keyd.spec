#
# spec file for package keyd
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


%global libinput_overrides %{_sysconfdir}/libinput/local-overrides.quirks
Name:           keyd
Version:        2.5.0
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
# fix default prefix in Makefile being /usr/local
%make_build PREFIX=%{_prefix}

%install
install -m755 -d %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}/layouts %{buildroot}%{_mandir}/man1 %{buildroot}%{_unitdir}
install -m755 bin/* %{buildroot}%{_bindir}
install -m644 data/keyd.compose %{buildroot}%{_datadir}/%{name}
install -m644 layouts/* %{buildroot}%{_datadir}/%{name}/layouts
cp -r data/gnome-* %{buildroot}%{_datadir}/%{name}
install -m644 data/*.1.gz %{buildroot}%{_mandir}/man1/
install -m644 %{name}.service %{buildroot}%{_unitdir}

%files
%license LICENSE
%doc README.md docs/*.md examples
%{_bindir}/*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_unitdir}/%{name}.service

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
