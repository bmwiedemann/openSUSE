#
# spec file for package txnupd-maintenance-tools
#
# Copyright (c) 2026 Shawn W Dunn <sfalken@kalpadesktop.org>
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


Name:           txnupd-maintenance-tools
Version:        1.1
Release:        0
Summary:        Update Notifier and Maintenance Tools
License:        GPL-3.0-or-later
URL:            https://codeberg.org/KalpaDesktop/txnupd-maintenance-tools
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.zst

# PATCH-FIX-UPSTREAM
Patch0:         0001-txnupd-maint-handle-selinuxenabled.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  dbus-1-common
BuildRequires:  python3-pytest
BuildRequires:  scdoc
BuildRequires:  systemd-rpm-macros
BuildRequires:  zstd

Requires:       python3 >= 3.11
Requires:       python3-dbus-python
Requires:       python3-gobject
Requires:       typelib(Notify)
Requires:       tukit
Requires:       tukitd

Conflicts:      transactional-update-notifier


%description
D-Bus notifier daemon/client for both transactional-update and
dnf5-txnupd transactional systems, and snapshot/system maintenance
tools for transactional systems


%prep
%autosetup -p1

%build
%cmake \
  -DDEFAULT_CONF_DIR=%{_distconfdir} \
  -DINSTALL_SYSTEMD_PRESET=ON
%cmake_build

%install
%cmake_install

%pre
%systemd_user_pre txnupd-notifier.service

%preun
%systemd_user_preun txnupd-notifier.service

%post
%systemd_user_post txnupd-notifier.service

%postun
%systemd_user_postun txnupd-notifier.service

%check
python3 -m pytest -v

%files
%license LICENSE
%doc README.md
%{_bindir}/transactional-update-notifier
%{_bindir}/txnupd-maint
%{_bindir}/txnupd-notifier
%{_bindir}/txnupd-notifier-client
%{_distconfdir}/txnupd-notifier.conf
%{_userpresetdir}/96-txnupd-notifier.preset
%{_userunitdir}/txnupd-notifier.service
%{_datadir}/dbus-1/system.d/org.opensuse.tukit.Updated.conf
%{_mandir}/man?/txnupd*

%changelog

