#
# spec file for package oo7
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        0.6.0
Release:        0
Summary:        A Secret Service provider
License:        MIT
URL:            https://github.com/linux-credentials/oo7
Source0:        %{URL}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch0:         python-no-default.patch
Patch1:         use-our-cargo-build.patch
BuildRequires:  cargo-packaging
BuildRequires:  meson >= 1.7
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.92
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd) >= 242
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-portal = %{version}-%{release}

%description
James Bond went on a new mission and this time as a Secret Service provider.

%package cli
Summary:        A CLI application to interact with the system keyring

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
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       xdg-desktop-portal

%description portal
An implementation of org.freedesktop.impl.portal.Secret.

%pre portal
%systemd_user_pre oo7-portal.service

%post portal
%systemd_user_post oo7-portal.service

%preun portal
%systemd_user_preun oo7-portal.service

%postun portal
%systemd_user_postun_with_restart oo7-portal.service

%package daemon
Summary:        A org.freedesktop.secrets server implementation
Provides:       dbus(org.freedesktop.secrets)
Provides:       dbus(org.gnome.keyring)
Conflicts:      gnome-keyring

%description daemon
A D-Bus Secret Service provider. Replacement of the gnome-keyring-daemon.

%pre daemon
%systemd_user_pre oo7-daemon.service

%post daemon
%systemd_user_post oo7-daemon.service

%preun daemon
%systemd_user_preun oo7-daemon.service

%postun daemon
%systemd_user_postun_with_restart oo7-daemon.service

%dnl %%package pam
%dnl Summary:        PAM module for oo7 Secret Service integration
%dnl Requires:       %%{name}-daemon

%dnl %%description pam
%dnl A PAM (Pluggable Authentication Modules) module that integrates with
%dnl the oo7 Secret Service daemon to automatically unlock keyrings during user authentication.

%prep
%autosetup -a1 -p1

%build
%{cargo_build} \
  --workspace \
  --exclude 'python' \
  --exclude 'pam' \
  --no-default-features \
  --features 'tokio openssl_crypto' \
%dnl --features 'kwallet_migration' ## From 0.7+
%{?nil}

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
install -Dm755 %{_builddir}/%{name}-%{version}/target/release/oo7-portal %{buildroot}%{_libexecdir}/oo7-portal
install -Dm755 %{_builddir}/%{name}-%{version}/target/release/oo7-daemon %{buildroot}%{_libexecdir}/oo7-daemon
%dnl install -Dm644 %%{_builddir}/%%{name}-%%{version}/target/release/libpam_oo7.so %%{buildroot}%%{_libdir}/security/pam_oo7.so

for d in portal server; do
  pushd $d
  %meson_install
  popd
done

%files
%license LICENSE
%doc README.md

%files cli
%license LICENSE
%doc cli/README.md
%{_bindir}/oo7-cli

%files -n cargo-credential-oo7
%license LICENSE
%doc cargo-credential/README.md
%{_bindir}/cargo-credential-oo7

%files portal
%license LICENSE
%doc portal/README.md
%dir %{_datadir}/xdg-desktop-portal/
%dir %{_datadir}/xdg-desktop-portal/portals/
%{_datadir}/applications/oo7-portal.desktop
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.oo7.service
%{_datadir}/xdg-desktop-portal/portals/oo7-portal.portal
%{_libexecdir}/oo7-portal
%{_userunitdir}/dbus-org.freedesktop.impl.portal.desktop.oo7.service
%{_userunitdir}/oo7-portal.service

%files daemon
%license LICENSE
%doc server/README.md
%{_libexecdir}/oo7-daemon
%{_datadir}/dbus-1/services/org.freedesktop.secrets.service
%{_userunitdir}/dbus-org.freedesktop.secrets.service
%{_userunitdir}/oo7-daemon.service

%dnl %%files pam
%dnl %%license LICENSE
%dnl %%doc pam/README.md
%dnl %%{_libdir}/security/pam_oo7.so

%changelog
