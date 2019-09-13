#
# spec file for package awesome-branding-openSUSE
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Togan Muftuoglu <toganm@opensuse.org>
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


%define awesome_version %(rpm -q --queryformat '%%{VERSION}' awesome)
%define _version 4.0-v0.1
Name:           awesome-branding-openSUSE
Version:        4.0
Release:        0
Summary:        openSUSE Branding for awesome
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            https://github.com/madanyang/awesome-branding-opensuse
Source:         %{name}-%{_version}.tar.xz
BuildRequires:  awesome-branding-upstream >= 4.0
Requires:       adwaita-icon-theme
Requires:       awesome = %{awesome_version}
Requires:       awesome-freedesktop
Requires:       awesome-vicious
Requires:       light-locker
Requires:       lua-lgi
Requires:       wallpaper-branding-openSUSE
Requires:       typelib(Gtk) = 3.0
Recommends:     awesome-shifty
Supplements:    packageand(awesome:branding-openSUSE)
Conflicts:      otherproviders(awesome-branding)
Provides:       awesome-branding = %{awesome_version}
BuildArch:      noarch

%description
This package provides the openSUSE specific additions both for
functions and look and feel for awesome window manager.

%prep
%setup -q -n %{name}-%{_version}

%build
# Nothing to build.

%install
install -Dpm 0644 rc.lua %{buildroot}%{_sysconfdir}/xdg/awesome/rc.lua
install -Dpm 0644 calendar2.lua %{buildroot}%{_datadir}/awesome/lib/calendar2.lua

mkdir -p %{buildroot}%{_datadir}/awesome/
cp -a themes/ %{buildroot}%{_datadir}/awesome/

%files
%defattr(-,root,root)
%doc README.openSUSE
%dir %{_sysconfdir}/xdg/awesome/
%config(noreplace) %{_sysconfdir}/xdg/awesome/rc.lua
%dir %{_datadir}/awesome/
%{_datadir}/awesome/lib/
%{_datadir}/awesome/themes/

%changelog
