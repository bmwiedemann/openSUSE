#
# spec file for package incus-ui
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


%define installdir %{_datadir}/%{name}
Name:           incus-ui-canonical
Version:        0.15.3
Release:        0
Summary:        Canonical lxd-ui patched for Incus
License:        GPL-3.0
URL:            https://github.com/zabbly/incus-ui-canonical
Source0:        https://github.com/zabbly/incus-ui-canonical/archive/refs/tags/incus-%{version}.tar.gz
Source1:        node_modules.spec.inc
%include  %{_sourcedir}/node_modules.spec.inc
BuildRequires:  git
BuildRequires:  local-npm-registry
BuildRequires:  yarn
Requires:       incus
BuildArch:      noarch

%description
This package installs a patched version of lxd-ui to %{_datadir}/incus-ui and provides a systemd drop-in configuration for the Incus service.

%prep
%autosetup -n %name-incus-%{version}
local-npm-registry %{_sourcedir} install --include=dev --no-scripts --no-package-lock

%build
npm run build

%install
# Create the target directory in the install root.
mkdir -p %{buildroot}/%{installdir}

# Move the build files to the installation directory
cp -a build/ui/* %{buildroot}/%{installdir}

# Create the systemd drop-in directory.
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system/incus.service.d/

# Add the drop-in systemd file.
cat << EOF > %{buildroot}%{_prefix}/lib/systemd/system/incus.service.d/50-incus-ui.conf
[Service]
Environment=INCUS_UI=%{installdir}
EOF

%files
%license LICENSE
%{installdir}
%{_prefix}/lib/systemd/system/incus.service.d/
%{_prefix}/lib/systemd/system/incus.service.d/50-incus-ui.conf

%changelog
