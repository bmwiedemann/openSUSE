#
# spec file for package owncloud-client-desktop-integration
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           owncloud-client-desktop-integration
Version:        6.1.0
Release:        0
Summary:        Integration for the ownCloud desktop client with various file managers
License:        GPL-2.0-or-later
URL:            https://github.com/owncloud/client-desktop-shell-integration-nautilus
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.16
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  python-caja
BuildRequires:  python3
BuildRequires:  python3-nautilus
BuildRequires:  python3-nemo

%description
This package provides a Python extension for Nautilus and its forks Nemo and
Caja to provide shell integration for the ownCloud desktop client for the
GNOME, Cinnamon and MATE desktop environments.

%package -n nautilus-extension-owncloud
Summary:        Owncloud client integration for nautilus, the GNOME file manager
Requires:       nautilus
Requires:       owncloud-client
Requires:       python3-gobject
Requires:       python3-nautilus
Supplements:    (owncloud-client and nautilus)
BuildArch:      noarch

%description -n nautilus-extension-owncloud
This package provides a plugin to integrate owncloud client into the nautilus
file manager.

%package -n caja-extension-owncloud
Summary:        Owncloud client integration for caja file manager
Requires:       caja
Requires:       owncloud-client
Requires:       python-caja
Requires:       python3-gobject
Supplements:    (owncloud-client and caja)
BuildArch:      noarch

%description -n caja-extension-owncloud
This package provides a plugin to integrate owncloud client into the caja
file manager.

%package -n nemo-extension-owncloud
Summary:        Owncloud client integration for nemo file manager
Requires:       nemo
Requires:       owncloud-client
Requires:       python3-gobject
Requires:       python3-nemo
Supplements:    (owncloud-client and nemo)
BuildArch:      noarch

%description -n nemo-extension-owncloud
This package provides a plugin to integrate owncloud client into the nemo
file manager.

%prep
%autosetup -p1 -n client-desktop-shell-integration-nautilus-%{version}

%build
%cmake -DREQUIRE_OWNCLOUD_RESOURCES=OFF
%cmake_build

%install
%cmake_install

%check

%files -n nautilus-extension-owncloud
%license COPYING
%doc README.md
%{_datadir}/nautilus-python/extensions/*.py

%files -n caja-extension-owncloud
%license COPYING
%doc README.md
%{_datadir}/caja-python/extensions/*.py

%files -n nemo-extension-owncloud
%license COPYING
%doc README.md
%{_datadir}/nemo-python/extensions/*.py

%changelog
