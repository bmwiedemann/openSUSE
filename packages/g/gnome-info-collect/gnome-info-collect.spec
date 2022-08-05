#
# spec file for package gnome-info-collect
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gnome-info-collect
Version:        1.0.5
Release:        0
Summary:        A simple utility to collect system information
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/vstanek/gnome-info-collect
Source:         https://gitlab.gnome.org/vstanek/gnome-info-collect/-/archive/v1.0-5/gnome-info-collect-v1.0-5.tar.gz
BuildRequires:  gobject-introspection
Requires:       python3-gobject
Requires:       python3-requests
BuildArch:      noarch

%description
A GNOME system and user data collection tool.

The collected data is anonymous and is sent to a secure server.
The data will be used only for the purpose of enhancing usability and user experience of GNOME.

%prep
%autosetup -p1 -n %{name}-v1.0-5
sed -i "s|bin/env python3$|bin/python3|g" client/client.py

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp client/client.py %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
