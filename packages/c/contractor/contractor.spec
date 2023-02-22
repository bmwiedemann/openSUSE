#
# spec file for package contractor
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


Name:           contractor
Version:        0.3.5
Release:        0
Summary:        A desktop-wide extension service
License:        GPL-3.0-or-later
Group:          System/Daemons
URL:            https://elementary.io/
Source:         https://github.com/elementary/contractor/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.44.4
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)

%description
An extension service that allows apps to use the exposed functionality of
registered apps. This way, applications do not have to have the functions
hard coded into them.

Designed for Elementary OS.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/contractor
%{_datadir}/dbus-1/services/org.elementary.contractor.service

%changelog
