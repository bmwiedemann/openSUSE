#
# spec file for package osinfo-db
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


Name:           osinfo-db
Version:        20221130
Release:        0
Summary:        Osinfo database files
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/Management
URL:            https://gitlab.com/libosinfo/osinfo-db
Source:         https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
Patch21:        add-oes-support.patch
Patch22:        add-caasp40-support.patch
Patch23:        add-win-2k19-media-info.patch
Patch24:        fix-tumbleweed-order.patch
Patch25:        add-opensuse-leap-15.5-support.patch
Patch26:        add-sle15sp5-support.patch
Patch27:        add-slem5.3-support.patch
Patch28:        add-slem5.4-support.patch
BuildRequires:  intltool
BuildRequires:  osinfo-db-tools
BuildArch:      noarch

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%prep
%autosetup -p1

%build
cd %{_builddir}
tar -cJf x.tar.xz osinfo-db-%{version}

%install
osinfo-db-import --root %{buildroot} --dir %{_datadir}/osinfo "%{_builddir}/x.tar.xz"

%files
%dir %{_datadir}/osinfo/
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema

%changelog
