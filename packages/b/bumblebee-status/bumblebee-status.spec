#
# spec file for package bumblebee-status
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


Name:           bumblebee-status
Version:        2.0.3
Release:        0
Summary:        Modular, theme-able status line generator for the i3 window manager
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/tobi-wan-kenobi/bumblebee-status/wiki
Source0:        https://github.com/tobi-wan-kenobi/bumblebee-status/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         use-python-3.patch
# In earlier i3 versions, blocks won't have background colors
Requires:       i3 >= 4.12
# Supported Python versions: 2.7, 3.3, 3.4, 3.5, 3.6
#  3.2 is unsupported (missing unicode literals)
Requires:       python >= 3.3
Requires:       python3-netifaces
Requires:       python3-psutil
Requires:       python3-requests
Recommends:     fontaweseome-fonts
Recommends:     powerline-fonts
BuildArch:      noarch
Provides:       bumblebee-status-module-cmus = 1.6.1
Obsoletes:      bumblebee-status-module-cmus <= 1.6.1
Provides:       bumblebee-status-module-dnf = 1.6.1
Obsoletes:      bumblebee-status-module-dnf <= 1.6.1
Provides:       bumblebee-status-module-mocp = 1.6.1
Obsoletes:      bumblebee-status-module-mocp <= 1.6.1
Provides:       bumblebee-status-module-mpd = 1.6.1
Obsoletes:      bumblebee-status-module-mpd <= 1.6.1
Provides:       bumblebee-status-module-redshift = 1.6.1
Obsoletes:      bumblebee-status-module-redshift <= 1.6.1

%description
bumblebee-status is a modular, themeable status line generator for the i3 window manager.
It supports theming and does not require any configuration files.

You can use the mouse wheel up/down to switch workspaces forward and back everywhere throughout the bar.

%prep
%setup -q
%patch1 -p1

%build

%install
mkdir -p "%{buildroot}%{_bindir}"
mkdir -p "%{buildroot}%{_datadir}/licenses/%{name}"
mkdir -p "%{buildroot}%{_datadir}/%{name}/themes/icons"
mkdir -p "%{buildroot}%{_datadir}/%{name}/bumblebee/modules"

# Install main files, themes, modules and icons

# 1. prepare filesystem
install -d %{buildroot}%{_bindir} \
%{buildroot}%{_datadir}/%{buildroot}/{bumblebee/modules,themes/icons}
ln -s %{_datadir}/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

# 2. remove modules:
#    * pacman (only usable on arch linux)
#    * stock (relies on deprecated Yahoo API)
#    * apt (debian)
rm -f bumblebee/modules/{pacman,stock,apt}.py

# 3. copy files from source
cp -a --parents %{name} bumblebee_status/{,modules/}*.py themes/{,icons/}*.json \
%{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/icons
%dir %{_datadir}/licenses/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/bumblebee-status
%{_datadir}/%{name}/bumblebee_status/
%{_datadir}/%{name}/themes/*.json
%{_datadir}/%{name}/themes/icons/*.json

%changelog
