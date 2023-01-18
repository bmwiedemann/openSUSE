#
# spec file for package awesome-vicious
#
# Copyright (c) 2023 SUSE LLC
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


%define packname   vicious

Name:           awesome-vicious
Version:        2.6.0
Release:        0
Summary:        Vicious plugins for awesome
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/vicious-widgets/vicious
Source:         %{url}/archive/v%{version}.tar.gz#/%{packname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       awesome >= 3.4.4
Recommends:     awesome-freedesktop
Recommends:     awesome-shifty
BuildArch:      noarch

%description
Vicious is a modular widget library for the "awesome" window manager,
derived from the "Wicked" widget library. It has some of the old
Wicked widget types, a few of them rewritten, and a good number of new
ones.

Vicious widget types are a framework for creating your own awesome
widgets. Vicious contains modules that gather data about your system,
and a few helper functions that make it easier to register timers,
suspend widgets and so on.

For now Vicious doesn't depend on any third party Lua libraries, to
make it easier to install and use. That means some system utilities
are used instead, where available:

  - hddtemp        for the HDD Temperature widget type
  - alsa-utils     for the Volume widget type
  - wireless_tools for the Wireless widget type
  - curl           for widget types accessing network resources

%prep
%autosetup -n %{packname}-%{version}

%build

%install
install -d %{buildroot}/%{_datadir}/awesome/lib/vicious/contrib
install -d %{buildroot}/%{_datadir}/awesome/lib/vicious/widgets
install -Dm 644 contrib/* %{buildroot}/%{_datadir}/awesome/lib/vicious/contrib
install -Dm 644 widgets/* %{buildroot}/%{_datadir}/awesome/lib/vicious/widgets
install -Dm 644 init.lua  %{buildroot}/%{_datadir}/awesome/lib/vicious
install -Dm 644 helpers.lua  %{buildroot}/%{_datadir}/awesome/lib/vicious
install -Dm 644 spawn.lua  %{buildroot}/%{_datadir}/awesome/lib/vicious

%files
%doc README.md CHANGELOG.rst TODO
%license LICENSE
%dir %{_datadir}/awesome
%dir %{_datadir}/awesome/lib
%{_datadir}/awesome/lib/vicious

%changelog
