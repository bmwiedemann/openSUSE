#
# spec file for package cockpit-podman
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


Name:           cockpit-podman
Version:        24
Release:        0
Summary:        Cockpit component for Podman containers
License:        LGPL-2.1-or-later
URL:            https://github.com/cockpit-project/cockpit-podman
Source:         https://github.com/cockpit-project/cockpit-podman/releases/download/%{version}/cockpit-podman-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  appstream-glib
Requires:       cockpit-bridge >= 138
Requires:       cockpit-shell >= 138
Requires:       podman >= 2.0.4
#
BuildRequires:  gcc-c++
BuildRequires:  nodejs-devel
BuildRequires:  npm
BuildRequires:  translate-toolkit

%description
Cockpit component for managing Podman containers

%prep
%setup -q -n %name

%build
# Nothing to build

%install
%make_install
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE
%{_datadir}/cockpit
%{_datadir}/metainfo/*

%changelog
