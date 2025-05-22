#
# spec file for package oo7
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


Name:           oo7
Version:        0.4.3
Release:        0
Summary:        A Secret Service provider
License:        MIT
URL:            https://github.com/bilelmoussaoui/oo7
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  pkgconfig(systemd) >= 242
Requires:       oo7-daemon
Requires:       oo7-portal

%description
James Bond went on a new mission and this time as a Secret Service provider.

%package cli
Summary:        A CLI application to interact with the system keyring. Replacement of secret-tool

%description cli
A CLI application to interact with the system keyring. Replacement of the secret-tool utility.

%package -n cargo-credential-oo7
Summary:        A cargo credential provider

%description -n cargo-credential-oo7
A cargo credential provider built using oo7 instead of libsecret.

%package portal
Summary:        A org.freedesktop.impl.portal.Secret implementation
Provides:       dbus(org.freedesktop.impl.portal.Secret)
Provides:       dbus(org.freedesktop.impl.portal.desktop.oo7)

%description portal
An implementation of org.freedesktop.impl.portal.Secret.

%package daemon
Summary:        A org.freedesktop.secrets server implementation
Provides:       dbus(org.freedesktop.secrets)
Provides:       dbus(org.gnome.keyring)

%description daemon
A D-Bus Secret Service provider. Replacement of the gnome-keyring-daemon.

%prep
%autosetup -a1

%build
%{cargo_build} --workspace --exclude 'oo7-portal' --exclude 'oo7-daemon'

for d in portal server; do
  pushd $d
  %meson
  %meson_build
  popd
done

%install
install -d %{buildroot}%{_bindir}
install -Dm755 %{_builddir}/%{name}-%{version}/target/release/oo7-cli %{buildroot}%{_bindir}/
install -Dm755 %{_builddir}/%{name}-%{version}/target/release/cargo-credential-oo7 %{buildroot}%{_bindir}/

for d in portal server; do
  pushd $d
  %meson_install
  popd
done

%if %{with test}
%check
%{cargo_test} -- --skip dbus::collection::tests::create_plain_item \
  --skip dbus::service::tests::create_collection \
  --skip dbus::collection::tests::create_encrypted_item

for d in portal server; do
  pushd $d
  %meson_test
  popd
done
%endif

%files
%license LICENSE
%doc README.md

%files cli
%doc cli/README.md
%license LICENSE
%{_bindir}/oo7-cli

%files -n cargo-credential-oo7
%doc cargo-credential/README.md
%license LICENSE
%{_bindir}/cargo-credential-oo7

%files portal
%doc portal/README.md
%license LICENSE
%{_libexecdir}/oo7-portal
%{_datadir}/applications/oo7-portal.desktop
%dir %{_datadir}/xdg-desktop-portal/
%dir %{_datadir}/xdg-desktop-portal/portals/
%{_datadir}/xdg-desktop-portal/portals/oo7-portal.portal
%{_userunitdir}/oo7-portal.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.oo7.service

%files daemon
%doc server/README.md
%license LICENSE
%{_libexecdir}/oo7-daemon
%{_userunitdir}/oo7-daemon.service

%changelog
