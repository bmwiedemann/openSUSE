#
# spec file for package rocket.term
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


Name:           rocket.term
Version:        0.2.0
Release:        0
Summary:        Text based chat client for the Rocket.chat messaging solution
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://github.com/gerstner-hub/rocket.term
Source:         https://github.com/gerstner-hub/rocket.term/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python3-setuptools
Requires:       python3-requests
Requires:       python3-urwid
Requires:       python3-websocket-client
BuildArch:      noarch

%description
rocket.term is a text based client for Rocket.chat that runs in a terminal.

%prep
%autosetup -p1

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%license LICENSE
%{python3_sitelib}/*
%{_bindir}/rocketterm

%changelog
