#
# spec file for package contractor
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


%define         appid org.elementary.contractor
Name:           contractor
Version:        0.3.5
Release:        0
Summary:        A desktop-wide extension service
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/contractor
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
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

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md CODE_OF_CONDUCT.md
%{_bindir}/%{name}
%{_datadir}/dbus-1/services/%{appid}.service

%changelog
