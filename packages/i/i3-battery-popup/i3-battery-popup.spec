#
# spec file for package i3-battery-popup
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


Name:           i3-battery-popup
Version:        1.1.1
Release:        0
Summary:        Script that shows messages to the user when the battery is almost empty
License:        MIT
URL:            https://github.com/rjekker/i3-battery-popup
Source0:        https://github.com/rjekker/i3-battery-popup/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
A script that shows messages to the user when the battery is almost empty.
Put something like this into your i3/sway config:
exec --no-startup-id i3-battery-popup -n -i %{_datadir}/icons/breeze/status/32/battery-caution.svg -s %{_datadir}/i3-battery-popup/i3-battery-popup.wav

%prep
%autosetup

%build
sed -i -e 's|%{_bindir}/env bash|/bin/bash|' i3-battery-popup

%install
install -D -m755 -t  %{buildroot}%{_bindir} i3-battery-popup
install -D -m644 -t  %{buildroot}%{_datadir}/i3-battery-popup i3-battery-popup.wav

%files
%license LICENSE
%doc README.md
%{_datadir}/i3-battery-popup
%{_bindir}/i3-battery-popup

%changelog
