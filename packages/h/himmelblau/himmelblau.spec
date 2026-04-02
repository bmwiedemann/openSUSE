#
# spec file for package himmelblau
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


%define chrome_nm_dir       /etc/opt/chrome/native-messaging-hosts
%define chromium_nm_dir     /etc/chromium/native-messaging-hosts
%define chrome_policy_dir   /etc/opt/chrome/policies/managed
%define chromium_policy_dir /etc/chromium/policies/managed
%define chrome_ext_dir      /usr/share/google-chrome/extensions

# SELinux macros
%if 0%{?suse_version} >= 1600
%define _selinux_sharedir   /usr/share/selinux
%define _selinux_pkgdir     %{_selinux_sharedir}/packages
%define _selinux_docdir     %{_docdir}/himmelblau-selinux/selinux
%endif

Name:           himmelblau
Version:        2.3.9+git0.a9fd29b
Release:        0
Summary:        Interoperability suite for Microsoft Azure Entra Id
License:        GPL-3.0-or-later
URL:            https://github.com/himmelblau-idm/himmelblau
Group:          Productivity/Networking/Security
Source:         %{name}-%{version}.tar.bz2
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  binutils
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  patchelf
BuildRequires:  systemd-rpm-macros
%if !0%{?suse_version}
BuildRequires:  authselect
%endif
BuildRequires:  autoconf
BuildRequires:  ca-certificates
BuildRequires:  checkpolicy
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  dbus-1-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  jq
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libunistring-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkg-config
BuildRequires:  policycoreutils
BuildRequires:  policycoreutils-devel
BuildRequires:  python3
BuildRequires:  sqlite3-devel
BuildRequires:  systemd-mini
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  wget
%if 0%{?suse_version} >= 1600
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-tools
%endif
ExclusiveArch:  %{rust_tier1_arches}
%if 0%{?suse_version} >= 1600
Requires:       make
Requires:       policycoreutils
Requires:       selinux-policy-devel
%endif
Recommends:     cron
Recommends:     krb5
Recommends:     libnss_himmelblau2
Recommends:     pam-himmelblau
Recommends:     system-user-tss

%description
Himmelblau is an interoperability suite for Microsoft Azure Entra Id
and Intune, which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n pam-himmelblau
Summary:        Azure Entra Id authentication PAM module
Requires:       %{name} = %{version}
Recommends:     oddjob_mkhomedir
Suggests:       authselect

%description -n pam-himmelblau
Himmelblau is an interoperability suite for Microsoft Azure Entra Id
and Intune, which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n libnss_himmelblau2
Summary:        Azure Entra Id authentication NSS module
Requires:       %{name} = %{version}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

Provides:       nss-himmelblau

%description -n libnss_himmelblau2
Himmelblau is an interoperability suite for Microsoft Azure Entra Id
and Intune, which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n himmelblau-sshd-config
Summary:        Azure Entra Id SSHD Configuration
Requires:       %{name} = %{version}
Requires:       openssh-server
BuildRequires:  openssh-server
BuildArch:      noarch

%description -n himmelblau-sshd-config
Himmelblau is an interoperability suite for Microsoft Azure Entra Id
and Intune, which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n himmelblau-sso
Summary:        Azure Entra Id Browser SSO
Requires:       %{name} = %{version}
Recommends:     curl
Recommends:     jq
Recommends:     libfuse2

%description -n himmelblau-sso
Himmelblau SSO provides Azure Entra Id browser single sign-on via
Firefox, Chromium, Google Chrome, and Microsoft Edge (where installed),
using native messaging and managed browser policies. It also provides
web apps for common Office 365 applications (Teams, Outlook, etc).

%package -n himmelblau-qr-greeter
Summary:        Azure Entra Id DAG URL QR code GNOME Shell extension
Requires:       gnome-shell
Recommends:     systemd-container
BuildArch:      noarch

%description -n himmelblau-qr-greeter
GNOME Shell extension that adds a QR code to authentication prompts
when a MS DAG URL is detected.

%prep
%autosetup -a1

%build
make rpm-servicefiles
# The generated hsm-pin-init unit hardcodes /usr/libexec, but `%{_libexecdir}`
# differs across SUSE releases (for example SLE15SP7 uses /usr/lib).
sed -i 's|^ExecStart=/usr/libexec/himmelblau-init-hsm-pin$|ExecStart=%{_libexecdir}/himmelblau-init-hsm-pin|' platform/opensuse/himmelblau-hsm-pin-init.service
%if !(0%{?suse_version} >= 1600)
export HIMMELBLAU_ALLOW_MISSING_SELINUX=1
%endif
%{cargo_build} --workspace --exclude himmelblau-fuzz
%if 0%{?suse_version} >= 1600
pushd src/selinux/src
make -f %{_selinux_sharedir}/devel/Makefile NAME=himmelblaud
popd
%endif
%if !0%{?suse_version}
make authselect
%endif

%check
%if !(0%{?suse_version} >= 1600)
export HIMMELBLAU_ALLOW_MISSING_SELINUX=1
%endif
%{cargo_test} --workspace --exclude himmelblau-fuzz

%install
# NSS
install -D -d -m 0755 %{buildroot}/%{_libdir}
install -D -d -m 0755 %{buildroot}/%{_tmpfilesdir}
strip --strip-unneeded target/release/libnss_himmelblau.so
patchelf --set-soname libnss_himmelblau.so.2 target/release/libnss_himmelblau.so
install -m 0755 target/release/libnss_himmelblau.so %{buildroot}/%{_libdir}/libnss_himmelblau.so.2
install -m 0644 src/nss/src/nss-himmelblau.tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/nss-himmelblau.conf

# PAM
install -D -d -m 0755 %{buildroot}/%{_pam_moduledir}
install -D -d -m 0755 %{buildroot}/usr/lib/pam-config.d
strip --strip-unneeded target/release/libpam_himmelblau.so
install -m 0755 target/release/libpam_himmelblau.so %{buildroot}/%{_pam_moduledir}/pam_himmelblau.so
install -m 0644 platform/opensuse/pam-config %{buildroot}/usr/lib/pam-config.d/himmelblau.conf
%if !0%{?suse_version}
install -D -d -m 0755 %{buildroot}/%{_datadir}/authselect/vendor/himmelblau/
install -m 0755 platform/el/authselect/* %{buildroot}/%{_datadir}/authselect/vendor/himmelblau/
%endif

# Himmelblau
install -D -d -m 0755 %{buildroot}%{_sbindir}
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -D -d -m 0755 %{buildroot}/%{_sysconfdir}/himmelblau
install -D -d -m 0755 %{buildroot}%{_datarootdir}/dbus-1/services
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/krb5.conf.d
install -D -d -m 0755 %{buildroot}/%{_unitdir}/display-manager.service.d/
install -d -m 0600 %{buildroot}%{_localstatedir}/cache/himmelblau-policies
install -D -d -m 0755 %{buildroot}%{_datadir}/doc/himmelblau/
install -D -d -m 0755 %{buildroot}/%{_tmpfilesdir}/
install -D -d -m 0755 %{buildroot}%{_mandir}/man1
install -D -d -m 0755 %{buildroot}%{_mandir}/man5
install -D -d -m 0755 %{buildroot}%{_mandir}/man8
install -D -d -m 0755 %{buildroot}%{_libexecdir}
strip --strip-unneeded target/release/himmelblaud
strip --strip-unneeded target/release/himmelblaud_tasks
strip --strip-unneeded target/release/broker
strip --strip-unneeded target/release/aad-tool
install -m 0644 src/config/himmelblau.conf.example %{buildroot}/%{_sysconfdir}/himmelblau/himmelblau.conf
install -m 0644 src/config/gdm3_service_override.conf %{buildroot}/%{_unitdir}/display-manager.service.d/override.conf
install -m 0755 target/release/aad-tool %{buildroot}/%{_bindir}/
install -m 0644 platform/opensuse/himmelblaud-tasks.service %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblaud.service %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblau-hsm-pin-init.service %{buildroot}/%{_unitdir}/
install -m 0755 src/daemon/scripts/himmelblau-init-hsm-pin %{buildroot}/%{_libexecdir}/
install -m 0755 target/release/himmelblaud %{buildroot}/%{_sbindir}/
install -m 0755 target/release/himmelblaud_tasks %{buildroot}/%{_sbindir}/
install -m 0644 README.md %{buildroot}/%{_datadir}/doc/himmelblau/README
install -m 0644 src/config/himmelblau.conf.example %{buildroot}/%{_datadir}/doc/himmelblau/
install -m 0644 man/man1/aad-tool.1 %{buildroot}/%{_mandir}/man1/
install -m 0644 man/man5/himmelblau.conf.5 %{buildroot}/%{_mandir}/man5/
install -m 0644 man/man8/himmelblaud.8 %{buildroot}/%{_mandir}/man8/
install -m 0644 man/man8/himmelblaud_tasks.8 %{buildroot}/%{_mandir}/man8/
install -m 0644 src/daemon/src/himmelblau-policies.tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/himmelblau-policies.conf
install -m 0644 src/daemon/src/himmelblaud.tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/himmelblaud.conf
%if 0%{?suse_version} >= 1600
install -D -d -m 0755 %{buildroot}/%{_selinux_pkgdir}/himmelblaud
install -D -d -m 0755 %{buildroot}/%{_selinux_docdir}
install -m 0644 src/selinux/src/himmelblaud.pp %{buildroot}/%{_selinux_pkgdir}/himmelblaud.pp
install -m 0644 src/selinux/src/himmelblaud.te %{buildroot}/%{_selinux_pkgdir}/himmelblaud/himmelblaud.te
install -m 0644 src/selinux/src/himmelblaud.fc %{buildroot}/%{_selinux_pkgdir}/himmelblaud/himmelblaud.fc
%endif
pushd %{buildroot}%{_sbindir}
ln -s himmelblaud rchimmelblaud
ln -s himmelblaud_tasks rchimmelblaud_tasks
ln -s broker rcbroker
popd

# SSHD Config
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
install -m 0644 platform/el/sshd_config %{buildroot}/%{_sysconfdir}/ssh/sshd_config.d/himmelblau.conf

# Single Sign On
strip --strip-unneeded target/release/linux-entra-sso
install -D -d -m 0755 %{buildroot}%{_libdir}/mozilla/native-messaging-hosts
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/firefox/policies
install -D -d -m 0755 %{buildroot}%{chrome_nm_dir}
install -D -d -m 0755 %{buildroot}%{chromium_nm_dir}
install -D -d -m 0755 %{buildroot}%{chrome_ext_dir}
install -D -d -m 0755 %{buildroot}%{chrome_policy_dir}
install -D -d -m 0755 %{buildroot}%{chromium_policy_dir}
install -D -d -m 0755 %{buildroot}%{_datadir}/applications/
%{!?_iconsdir:%global _iconsdir %{_datadir}/icons}
install -D -d -m 0755 %{buildroot}%{_iconsdir}/hicolor/256x256/apps
install -m 0755 src/o365/src/o365.sh %{buildroot}/%{_bindir}/o365
install -m 0755 src/o365/src/o365-multi.sh %{buildroot}/%{_bindir}/o365-multi
install -m 0755 src/o365/src/o365-url-handler.sh %{buildroot}/%{_bindir}/o365-url-handler
install -m 0644 src/o365/generated/*.desktop %{buildroot}/%{_datadir}/applications/
install -m 0644 src/o365/src/*.png %{buildroot}/%{_iconsdir}/hicolor/256x256/apps/
install -m 0755 target/release/linux-entra-sso %{buildroot}/%{_bindir}/linux-entra-sso
install -m 0644 src/sso/src/firefox/linux_entra_sso.json %{buildroot}/%{_libdir}/mozilla/native-messaging-hosts/
install -m 0644 src/sso/src/firefox/policies.json %{buildroot}/%{_sysconfdir}/firefox/policies/
install -m 0644 src/sso/src/chrome/linux_entra_sso.json %{buildroot}/%{chrome_nm_dir}/
install -m 0644 src/sso/src/chrome/linux_entra_sso.json %{buildroot}/%{chromium_nm_dir}/
install -m 0644 src/sso/src/chrome/extension.json %{buildroot}/%{chrome_ext_dir}/jlnfnnolkbjieggibinobhkjdfbpcohn.json
install -m 0644 src/sso/src/chrome/policies.json %{buildroot}/%{chrome_policy_dir}/himmelblau.json
install -m 0644 src/sso/src/chrome/policies.json %{buildroot}/%{chromium_policy_dir}/himmelblau.json
install -m 0644 platform/opensuse/com.microsoft.identity.broker1.service %{buildroot}/%{_datadir}/dbus-1/services/
install -m 0755 target/release/broker %{buildroot}/%{_sbindir}/

# QR Greeter
install -D -d -m 0755 %{buildroot}%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/extension.js %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/extension.js
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/metadata.json %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/metadata.json
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/stylesheet.css %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/stylesheet.css
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/msdag.png %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/msdag.png

%post -n libnss_himmelblau2
/sbin/ldconfig

# Ensure cache directory is created immediately after installation, ignoring failures
systemd-tmpfiles --create /usr/lib/tmpfiles.d/nss-himmelblau.conf 2>/dev/null || systemd-tmpfiles --create /usr/lib/x86_64-linux-gnu/tmpfiles.d/nss-himmelblau.conf 2>/dev/null || true

%postun -n libnss_himmelblau2 -p /sbin/ldconfig

%post
%service_add_post himmelblaud.service himmelblaud-tasks.service

# Ensure cache directory is created with correct permissions
systemd-tmpfiles --create /usr/lib/tmpfiles.d/himmelblau-policies.conf 2>/dev/null || true

# Ensure private data directory is created with correct permissions
systemd-tmpfiles --create /usr/lib/tmpfiles.d/himmelblaud.conf 2>/dev/null || true

%postun
%service_del_postun himmelblaud.service himmelblaud-tasks.service

%if 0%{?suse_version} >= 1600
%selinux_modules_uninstall himmelblaud
%endif

%pre
%service_add_pre himmelblaud.service himmelblaud-tasks.service

%preun
%service_del_preun himmelblaud.service himmelblaud-tasks.service

%posttrans
%if 0%{?suse_version} >= 1600
%selinux_modules_install %{_selinux_pkgdir}/himmelblaud.pp

if command -v selinuxenabled >/dev/null 2>&1 && selinuxenabled && command -v restorecon >/dev/null 2>&1; then
  restorecon -Fv /usr/sbin/himmelblaud /usr/sbin/himmelblaud_tasks 2>/dev/null || :

  [ -d /etc/himmelblau ]                && restorecon -RFv /etc/himmelblau || :
  [ -d /run/himmelblaud ]               && restorecon -RFv /run/himmelblaud || :
  [ -d /var/run/himmelblaud ]           && restorecon -RFv /var/run/himmelblaud || :
  [ -d /var/cache/private/himmelblaud ] && restorecon -RFv /var/cache/private/himmelblaud || :
  [ -d /var/cache/himmelblaud ]         && restorecon -RFv /var/cache/himmelblaud || :
  [ -d /var/cache/nss-himmelblau ]      && restorecon -RFv /var/cache/nss-himmelblau || :
  [ -d /var/lib/private/himmelblaud ]   && restorecon -RFv /var/lib/private/himmelblaud || :
  [ -d /var/lib/himmelblaud ]           && restorecon -RFv /var/lib/himmelblaud || :
fi
%endif

%post -n himmelblau-sso
if command -v update-desktop-database >/dev/null 2>&1; then update-desktop-database -q || true; fi
if [ -d /usr/share/icons/hicolor ] && command -v gtk-update-icon-cache >/dev/null 2>&1; then gtk-update-icon-cache -q /usr/share/icons/hicolor || true; fi

%postun -n himmelblau-sso
if command -v update-desktop-database >/dev/null 2>&1; then update-desktop-database -q || true; fi
if [ -d /usr/share/icons/hicolor ] && command -v gtk-update-icon-cache >/dev/null 2>&1; then gtk-update-icon-cache -q /usr/share/icons/hicolor || true; fi

%files
%dir %{_sysconfdir}/himmelblau
%dir %{_localstatedir}/cache/himmelblau-policies
%dir %{_unitdir}/display-manager.service.d
%dir %{_datadir}/doc/himmelblau
%config(noreplace) %{_sysconfdir}/himmelblau/himmelblau.conf
%{_unitdir}/display-manager.service.d/override.conf
%{_bindir}/aad-tool
%{_unitdir}/himmelblaud-tasks.service
%{_unitdir}/himmelblaud.service
%{_unitdir}/himmelblau-hsm-pin-init.service
%{_libexecdir}/himmelblau-init-hsm-pin
%{_sbindir}/himmelblaud
%{_sbindir}/himmelblaud_tasks
%{_datadir}/doc/himmelblau/README
%{_datadir}/doc/himmelblau/himmelblau.conf.example
%{_mandir}/man1/aad-tool.1*
%{_mandir}/man5/himmelblau.conf.5*
%{_mandir}/man8/himmelblaud.8*
%{_mandir}/man8/himmelblaud_tasks.8*
%{_tmpfilesdir}/himmelblau-policies.conf
%{_tmpfilesdir}/himmelblaud.conf
%if 0%{?suse_version} >= 1600
%dir %{_docdir}/himmelblau-selinux
%dir %{_selinux_docdir}
%dir %{_selinux_pkgdir}
%dir %{_selinux_pkgdir}/himmelblaud
%{_selinux_pkgdir}/himmelblaud.pp
%{_selinux_pkgdir}/himmelblaud/himmelblaud.te
%{_selinux_pkgdir}/himmelblaud/himmelblaud.fc
%endif
%{_sbindir}/rchimmelblaud
%{_sbindir}/rchimmelblaud_tasks

%files -n libnss_himmelblau2
%dir %{_tmpfilesdir}
%{_libdir}/libnss_himmelblau.so.2
%{_tmpfilesdir}/nss-himmelblau.conf
%ghost %attr(0755,root,root) /%{_localstatedir}/cache/nss-himmelblau

%files -n pam-himmelblau
%{_pam_moduledir}/pam_himmelblau.so
%dir /usr/lib/pam-config.d
/usr/lib/pam-config.d/himmelblau.conf
%if !0%{?suse_version}
%dir %{_datadir}/authselect
%dir %{_datadir}/authselect/vendor
%dir %{_datadir}/authselect/vendor/himmelblau
%{_datadir}/authselect/vendor/himmelblau/*
%endif

%files -n himmelblau-sshd-config
%config %{_sysconfdir}/ssh/sshd_config.d/himmelblau.conf
%if 0%{?sle_version} <= 150500
%dir %{_sysconfdir}/ssh/sshd_config.d
%endif

%files -n himmelblau-sso
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/native-messaging-hosts
%dir %{_sysconfdir}/firefox
%dir %{_sysconfdir}/firefox/policies
%dir /etc/chromium
%dir /etc/chromium/native-messaging-hosts
%dir /etc/chromium/policies
%dir /etc/chromium/policies/managed
%dir /etc/opt/chrome
%dir /etc/opt/chrome/native-messaging-hosts
%dir /etc/opt/chrome/policies
%dir /etc/opt/chrome/policies/managed
%dir /usr/share/google-chrome
%dir %{chrome_nm_dir}
%dir %{chromium_nm_dir}
%dir %attr(0555,root,root) %{chrome_policy_dir}
%dir %attr(0555,root,root) %{chromium_policy_dir}
%dir %{chrome_ext_dir}
%dir %{_iconsdir}/hicolor
%dir %{_iconsdir}/hicolor/256x256
%dir %{_iconsdir}/hicolor/256x256/apps
%{_bindir}/o365
%{_bindir}/o365-multi
%{_bindir}/o365-url-handler
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/256x256/apps/*.png
%{_bindir}/linux-entra-sso
%{_libdir}/mozilla/native-messaging-hosts/linux_entra_sso.json
%config %{_sysconfdir}/firefox/policies/policies.json
%{chrome_nm_dir}/linux_entra_sso.json
%{chromium_nm_dir}/linux_entra_sso.json
%{chrome_ext_dir}/jlnfnnolkbjieggibinobhkjdfbpcohn.json
%{chrome_policy_dir}/himmelblau.json
%{chromium_policy_dir}/himmelblau.json
%{_datadir}/dbus-1/services/com.microsoft.identity.broker1.service
%{_sbindir}/broker
%{_sbindir}/rcbroker

%files -n himmelblau-qr-greeter
%dir %{_datarootdir}/gnome-shell
%dir %{_datarootdir}/gnome-shell/extensions
%dir %{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/extension.js
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/metadata.json
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/stylesheet.css
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/msdag.png

%changelog
