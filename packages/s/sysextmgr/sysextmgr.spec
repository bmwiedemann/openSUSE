#
# spec file for package sysextmgr
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


Name:           sysextmgr
Version:        0.0+git20250718.e2565a6
Release:        0
Summary:        Tools to manage sysext-images on MicroOS
License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/sysextmgr
Source:         %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd) >= 257
BuildRequires:  pkgconfig(libeconf)
Requires:       /usr/bin/systemd-dissect
#Requires:       /usr/lib/systemd/systemd-pull
Requires:       systemd-container >= 257.6
Requires:       sysextmgrcli

%description
sysextmgr is used to create and manage json files of dependencies
from systemd-sysext images.

%package -n sysextmgrcli
Summary:        Command line interface for sysextmgr

%description -n sysextmgrcli
sysextmgrcli is a commandline interface to communicate with the sysextmgr daemon via varlink.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%pre
%service_add_pre sysextmgr.socket sysextmgr-cleanup.timer

%preun
%service_del_preun sysextmgr.socket sysextmgr-cleanup.timer

%post
%service_add_post sysextmgr.socket sysextmgr-cleanup.timer

%postun
%service_del_postun sysextmgr.socket sysextmgr-cleanup.timer


%files
%license LICENSE.GPL2 LICENSE.LGPL2.1
%{_prefix}/lib/systemd/system/sysextmgr.service
%{_prefix}/lib/systemd/system/sysextmgr.socket
%{_prefix}/lib/systemd/system/sysextmgr-cleanup.service
%{_prefix}/lib/systemd/system/sysextmgr-cleanup.timer
%{_libexecdir}/sysextmgrd

%files -n sysextmgrcli
%license LICENSE.GPL2 LICENSE.LGPL2.1
%{_bindir}/sysextmgrcli

%changelog
