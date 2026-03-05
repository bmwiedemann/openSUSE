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
Version:        0.1.0+git20260304.fc915b3
Release:        0
Summary:        Tools to manage systemd-sysext images
License:        GPL-2.0-or-later
URL:            https://github.com/thkukuk/sysextmgr
Source:         %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libeconf)
BuildRequires:  pkgconfig(libsystemd) >= 257
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libzio-devel
Requires:       %{_bindir}/systemd-dissect
#Requires:       /usr/lib/systemd/systemd-pull
Requires:       systemd-container >= 257.6
Provides:       sysextmgrcli = %{version}
Obsoletes:      sysextmgrcli < %{version}

%description
sysextmgr is used to manage systemd-sysext images on the system: list
available extensions, install and update them.
sysextmgrcli is a commandline interface to communicate with the sysextmgr
daemon via varlink.

%package -n sysextmgr-tukit-plugin
Summary:        Plugin for tukit to update sysexe images
Requires:       sysextmgr

%description -n sysextmgr-tukit-plugin
This package contains a plugin for tukit, so that transactional-update not only updates the packages of the host OS, but also the sysext images.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/sysextmgr
echo -e "[default]\nurl=https://download.opensuse.org/tumbleweed/appliances/" > %{buildroot}%{_datadir}/sysextmgr/sysextmgr.conf

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
%{_bindir}/sysextmgrcli
%{_prefix}/lib/systemd/system/sysextmgr.service
%{_prefix}/lib/systemd/system/sysextmgr.socket
%{_prefix}/lib/systemd/system/sysextmgr-cleanup.service
%{_prefix}/lib/systemd/system/sysextmgr-cleanup.timer
%{_libexecdir}/sysextmgrd
%{_tmpfilesdir}/sysextmgr.conf
%dir %{_datadir}/sysextmgr
%{_datadir}/sysextmgr/sysextmgr.conf

%files -n sysextmgr-tukit-plugin
%dir %{_prefix}/lib/tukit
%dir %{_prefix}/lib/tukit/plugins
%{_prefix}/lib/tukit/plugins/50-sysext-update

%changelog
