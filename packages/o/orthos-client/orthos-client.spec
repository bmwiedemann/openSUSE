#
# spec file for package orthos-client
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


Name:           orthos-client
Version:        1.0.102+git.a6bbc34
Release:        0
Summary:        Command line client for orthos2
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Boot/Servers
URL:            https://github.com/openSUSE/orthos2
Source:         orthos2-%{version}.tar.gz
Requires:       python3-base
Requires:       python3-pytz
BuildArch:      noarch

%description
Command line client that provides a shell like command
line interface based on readline.

%prep

%setup -q -n orthos2-%{version}

%build

%install
mkdir -p %{buildroot}/%{_bindir}

install orthos2 %{buildroot}/%{_bindir}/orthos2


%files
%attr(755, root, root) %{_bindir}/orthos2

%changelog
