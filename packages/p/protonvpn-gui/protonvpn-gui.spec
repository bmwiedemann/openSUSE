#
# spec file for package protonvpn-gui
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


Name:           protonvpn-gui
Version:        1.7.0
Release:        0
Summary:        Official ProtonVPN GUI
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/ProtonVPN/linux-app
Source:         https://github.com/ProtonVPN/linux-app/archive/refs/tags/%{version}.tar.gz#/linux-app-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gobject-introspection
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       gtk3
Requires:       python3-gobject-Gdk
Requires:       python3-protonvpn-nm-lib >= 3.7.0
Requires:       python3-psutil
Provides:       protonvpn = %{version}
BuildArch:      noarch

%description
The ProtonVPN GUI is intended for every ProtonVPN service user.

%prep
%setup -q -n linux-app-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}/

mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_datadir}/applications
cp rpmbuild/SOURCES/protonvpn-logo.png %{buildroot}/%{_datadir}/pixmaps/protonvpn.png
cp rpmbuild/SOURCES/protonvpn.desktop %{buildroot}/%{_datadir}/applications/protonvpn.desktop

%suse_update_desktop_file -c protonvpn ProtonVPN "ProtonVPN GUI Client" protonvpn protonvpn Network

%files
%doc README.md
%license LICENSE COPYING.md
%{_datadir}/applications/protonvpn.desktop
%{_datadir}/pixmaps/protonvpn.png
%{python3_sitelib}/protonvpn_gui
%{python3_sitelib}/protonvpn_gui-*-py*.*-info
%{_bindir}/protonvpn

%changelog
