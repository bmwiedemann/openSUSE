#
# spec file for package transactional-update-notifier
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2022 Luciano Santos <luc14n0@opensuse.org>
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


Name:           transactional-update-notifier
Version:        1.1.0
Release:        0
Summary:        A notifier for systems using transactional updates
License:        GPL-3.0-only
Group:          System/Base
URL:            https://github.com/89luca89/transactional-update-notifier
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source9:        %{name}.rpmlintrc

BuildRequires:  golang(API) >= 1.18
BuildRequires:  systemd-rpm-macros

Requires:       dbus-1

%description
Add notifications, via Desktop Bus (D-Bus), about transactional updates for
all users currently logged in in a graphical session. Being even possible
for it to be used as a reboot method through transactional-updates.conf(5).


%prep
%autosetup -p 1 -a 1

%build
export GOFLAGS='-mod=vendor -buildmode=pie'
%make_build

%install
%make_install WITH_SYSTEMD_PRESET=0

%pre
%systemd_user_pre     %{name}.service

%post
%systemd_user_post    %{name}.service

%preun
%systemd_user_preun   %{name}.service


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service
%{_datadir}/dbus-1/system.d/org.opensuse.tukit.Updated.conf

%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d

%changelog
