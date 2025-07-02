#
# spec file for package opencloud-desktop-desktop-integration
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


Name:           opencloud-desktop-integration
Version:        1.0.0
Release:        0
Summary:        Nautilus and Nemo integrations for OpenCloud
License:        GPL-2.0-or-later
URL:            https://github.com/opencloud-eu/desktop-shell-integration-nautilus
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/desktop-shell-integration-nautilus-%{version}.tar.gz
BuildRequires:  cmake >= 3.16
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  python-caja
BuildRequires:  python3
BuildRequires:  python3-nautilus
BuildRequires:  python3-nemo

%description
This package provides a Python extension for Nautilus and its forks Nemo and
Caja to provide shell integration for the OpenCloud desktop client for the
GNOME, Cinnamon and MATE desktop environments.

%package -n nautilus-extension-opencloud
Summary:        OpenCloud client integration for nautilus, the GNOME file manager
Requires:       nautilus
Requires:       opencloud-extensions-resources
Requires:       python3-gobject
Requires:       python3-nautilus
Supplements:    (opencloud-desktop and nautilus)
BuildArch:      noarch

%description -n nautilus-extension-opencloud
This package provides a plugin to integrate opencloud client into the nautilus
file manager.

%package -n caja-extension-opencloud
Summary:        OpenCloud client integration for caja file manager
Requires:       caja
Requires:       opencloud-extensions-resources
Requires:       python-caja
Requires:       python3-gobject
Supplements:    (opencloud-desktop and caja)
BuildArch:      noarch

%description -n caja-extension-opencloud
This package provides a plugin to integrate opencloud client into the caja
file manager.

%package -n nemo-extension-opencloud
Summary:        OpenCloud client integration for nemo file manager
Requires:       nemo
Requires:       opencloud-extensions-resources
Requires:       python3-gobject
Requires:       python3-nemo
Supplements:    (opencloud-desktop and nemo)
BuildArch:      noarch

%description -n nemo-extension-opencloud
This package provides a plugin to integrate opencloud client into the nemo
file manager.

%prep
%autosetup -p1 -n desktop-shell-integration-nautilus-%{version}

%build
%cmake -DREQUIRE_OPENCLOUD_RESOURCES=OFF
%cmake_build

%install
%cmake_install

%check

%files -n nautilus-extension-opencloud
%license COPYING
%doc README.md
%{_datadir}/nautilus-python/extensions/*.py

%files -n caja-extension-opencloud
%license COPYING
%doc README.md
%{_datadir}/caja-python/extensions/*.py

%files -n nemo-extension-opencloud
%license COPYING
%doc README.md
%{_datadir}/nemo-python/extensions/*.py

%changelog

