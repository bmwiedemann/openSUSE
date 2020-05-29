#
# spec file for package sgtk-menu
#
# Copyright (c) 2020 SUSE LLC
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


Name:           sgtk-menu
Version:        0.2.0
Release:        0
Summary:        GTK menu for sway and i3
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://github.com/nwg-piotr/sgtk-menu
Source:         %{url}/archive/v%{version}.tar.gz
BuildRequires:  python3
BuildRequires:  python3-setuptools
Requires:       python3-gobject
Recommends:     python3-i3ipc

%description
An attempt to create a simple menu, that behaves decently on sway,
but also on i3 window manager. It uses pygobject to create a themeable,
searchable gtk3-based system menu w/ some optional features.

%prep
%setup -q

find . -type f -exec sed -i "s/#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/" {} +

%build
%python3_build

%install
%python3_install

%files
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
