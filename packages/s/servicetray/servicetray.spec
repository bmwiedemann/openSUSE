#
# spec file for package servicetray
#
# Copyright (c) 2025 SUSE LLC
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


%define use_python python3
%define pythons %{use_python}
Name:           servicetray
Version:        0.1
Release:        0
Summary:        Tool to start and stop systemd services as a normal user via a tray applet
License:        GPL-3.0-or-later
URL:            https://codeberg.org/aylen384/%{name}
Source0:        https://codeberg.org/aylen384/servicetray/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  fdupes
BuildRequires:  sudo
Requires:       python3
Requires:       python3-pyside6
Requires:       sudo
Requires:       systemd
BuildArch:      noarch

%description
Tool to start and stop systemd services as a normal user via a tray applet.
Services that this tool can manage are configured via %{_sysconfdir}/servicetray.toml.

%prep
%autosetup -n %{name}

%build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_sbindir}/%{name}_systemctl
%{_prefix}%{_sysconfdir}/sudoers.d/%{name}
%{_datadir}/servicetray
%config %{_sysconfdir}/%{name}.toml

%changelog
