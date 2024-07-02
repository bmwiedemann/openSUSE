#
# spec file for package wg-info
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


Name:           wg-info
Version:        20240702.9b5c479
Release:        0
Summary:        Enhanced version of 'wg show' showing peer names and online status
License:        AGPL-3.0-or-later
URL:            https://github.com/asdil12/wg-info
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3
Requires:       wireguard-tools

%description
Better wireguard status script

This script allows you to actually know, which peer in the `wg show` output is which by assigning them a name.
Also you can see, which peers are actually online as `wg-info` will ping them and set the color (red/green) accordingly.
To save time, this is done for all the peers in parallel.

The output is colored (if writing to a tty or explicitly requested) using terminal sequences, HTML or be just plain text.

%prep
%autosetup

%build

%install
install -D -m 0755 ./wg-info %{buildroot}%{_bindir}/wg-info

%files
%license LICENSE
%doc README.md
%{_bindir}/wg-info

%changelog
