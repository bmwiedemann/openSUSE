#
# spec file for package cockpit-machines
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


Name:           cockpit-machines
Version:        327
Release:        0
Summary:        Cockpit user interface for virtual machines
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/cockpit-project/cockpit-machines
Source:         https://github.com/cockpit-project/cockpit-machines/archive/refs/tags/%{version}.tar.gz#/cockpit-machines-%{version}.tar.gz
Source10:       package-lock.json
Source11:       node_modules.spec.inc
Source12:       update_version.sh
%include %_sourcedir/node_modules.spec.inc
Patch10:        hide-docs.patch
Patch11:        load-css-overrides.patch
BuildArch:      noarch
BuildRequires:  appstream-glib
BuildRequires:  make
Requires:       cockpit-bridge >= 215
%if 0%{?suse_version}
Requires:       libvirt-daemon-qemu
%else
Requires:       libvirt-daemon-kvm
%endif
Requires:       libvirt-client
Requires:       libvirt-dbus >= 1.2.0
Requires:       qemu-spice
Requires:       virt-install
# Optional components
Recommends:     libosinfo
Recommends:     python3-gobject-base
#
BuildRequires:  cockpit-devel >= 293
BuildRequires:  local-npm-registry
BuildRequires:  sassc

%description
Cockpit component for managing virtual machines.

If "virt-install" is installed, you can also create new virtual machines.

%prep
%autosetup -p1
local-npm-registry %{_sourcedir} install --include=dev --ignore-scripts || ( find ~/.npm/_logs -name '*-debug.log' -print0 | xargs -0 cat; false)

%build
export PREFIX=%_prefix
mkdir -p pkg/lib
cp -r %{_datadir}/cockpit/devel/lib/* pkg/lib
NODE_ENV=production npm run build

%install
export PREFIX=%_prefix
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
