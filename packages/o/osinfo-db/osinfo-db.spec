#
# spec file for package osinfo-db
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           osinfo-db
Version:        20201015
Release:        0
Summary:        Osinfo database files
License:        LGPL-2.1+ and GPL-2.0+
Group:          System/Management
BuildArch:      noarch
Url:            https://gitlab.com/libosinfo/osinfo-db
Source:         https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
Patch21:        add-oes-support.patch
Patch22:        add-caasp40-support.patch
Patch24:        add-win-2k19-media-info.patch
Patch25:        fix-sle15sp1-volume-id-string.patch
Patch26:        SLE-add-info-about-UEFI-support.patch
Patch27:        fix-tumbleweed-order.patch
Patch28:        add-leap15.3-support.patch
Patch29:        add-sle15sp3-support.patch

BuildRequires:  intltool
BuildRequires:  osinfo-db-tools

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%prep
%setup -q
%patch21 -p1
%patch22 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1

%build
cd %{_builddir}
tar -cJf x.tar.xz osinfo-db-%{version}

%install
osinfo-db-import --root %{buildroot} --dir %{_datadir}/osinfo "%{_builddir}/x.tar.xz"

%files
%defattr(-,root,root,-)
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
