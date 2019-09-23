#
# spec file for package alpine-branding-openSUSE
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           alpine-branding-openSUSE
Version:        0
Release:        0
Summary:        Configuration for the Alpine mail client
License:        WTFPL
Group:          Productivity/Networking/Email/Clients

Source:         pine.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       alpine-branding
Conflicts:      otherproviders(alpine-branding)
Enhances:       packageand(alpine:branding-openSUSE)

%description
The package provides a system-wide configuration file for the Alpine
text/ncurses mail client. This enables some features that would
otherwise be disabled by default, including threading, additional
keybindings, color, threading.

%prep

%build

%install
c="%buildroot/%_sysconfdir"
mkdir -p "$c"
install -pm0644 "%{S:0}" "$c/"

%files
%defattr(-,root,root)
%config %_sysconfdir/pine.conf

%changelog
