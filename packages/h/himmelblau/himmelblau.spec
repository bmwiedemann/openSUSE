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
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
%define _selinux_sharedir   /usr/share/selinux
%define _selinux_pkgdir     %{_selinux_sharedir}/packages
%define _selinux_docdir     %{_docdir}/himmelblau-selinux/selinux
%endif

Name:           himmelblau
Version:        4.0.8+git0.a969c748
Release:        0
Summary:        Interoperability suite for Microsoft Azure Entra Id
License:        GPL-3.0-or-later
URL:            https://github.com/himmelblau-idm/himmelblau
Group:          Productivity/Networking/Security
Source:         %{name}-%{version}.tar.bz2
Source1:        vendor.tar.zst
Source2:        cargo_config
Source3:        nsswitch-himmelblau.conf
Source6:        himmelblau-rpmlintrc
BuildRequires:  binutils
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  patchelf
BuildRequires:  systemd-rpm-macros
%if 0%{?suse_version}
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  nodejs-default
%else
BuildRequires:  nodejs
%endif
BuildRequires:  ca-certificates
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
BuildRequires:  nsswitch-config
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkg-config
BuildRequires:  policycoreutils
BuildRequires:  policycoreutils-devel
BuildRequires:  python3
BuildRequires:  rpm-build
BuildRequires:  sqlite3-devel
BuildRequires:  systemd-mini
BuildRequires:  tpm2-0-tss-devel
BuildRequires:  wget
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-tools
%endif
ExclusiveArch:  %{rust_tier1_arches}
Requires:       make
Requires:       man
Requires:       policycoreutils
Requires:       systemd >= 235
Provides:       aad-cli
Provides:       aad-common
Provides:       authd
Provides:       authd-msentraid
Recommends:     cron
Recommends:     himmelblau-apparmor
Recommends:     himmelblau-selinux
Recommends:     krb5
Recommends:     libnss_himmelblau2
Recommends:     pam-himmelblau
Recommends:     (system-user-tss or tpm2-tss)
Recommends:     (tpm2-tools or tpm2.0-tools)
Suggests:       himmelblau-sso
Suggests:       himmelblau-orchestrator

%description
Himmelblau is an interoperability suite for Microsoft Azure Entra Id
and Intune, which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
%package -n himmelblau-selinux
Summary:        SELinux policy for Himmelblau
Requires:       %{name} = %{version}
Requires:       make
Requires:       policycoreutils
Requires:       selinux-policy-devel
BuildArch:      noarch

%description -n himmelblau-selinux
SELinux policy module sources for Himmelblau, an interoperability suite
for Microsoft Azure Entra Id and Intune. The policy module is compiled
and loaded on the host when the package is installed.
%endif

%package -n pam-himmelblau
Summary:        Azure Entra Id authentication PAM module
Requires:       %{name} = %{version}
Provides:       libpam-aad
Recommends:     authselect
Recommends:     (oddjob-mkhomedir if authselect)
Suggests:       himmelblau-qr-greeter
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
Requires(post): nsswitch-config
Requires(postun): nsswitch-config
Provides:       libnss-aad
Provides:       nss-himmelblau

%description -n libnss_himmelblau2
Himmelblau is an interoperability suite for Microsoft Azure Entra Id
and Intune, which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n himmelblau-sshd-config
Summary:        Azure Entra Id SSHD Configuration
Requires:       %{name} = %{version}
Requires:       openssh-server
Supplements:    (pam-himmelblau and openssh-server)
BuildRequires:  openssh-server
BuildArch:      noarch

%description -n himmelblau-sshd-config
Himmelblau is an interoperability suite for Microsoft Azure Entra Id
and Intune, which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n himmelblau-broker
Summary:        Azure Entra Id Browser broker service
Requires:       %{name} = %{version}
Provides:       microsoft-identity-broker

%description -n himmelblau-broker
Himmelblau Broker provides Azure Entra Id browser broker service functionality.
It enables communication between the browser and the authentication backend,
enabling single sign-on and other authentication features.

%package -n himmelblau-sso
Summary:        Azure Entra Id Browser SSO
Requires:       %{name} = %{version}
Requires:       himmelblau-broker
Provides:       intune-portal
Provides:       linux-entra-sso
Recommends:     curl
Recommends:     himmelblau-sso-policies
Recommends:     jq
Recommends:     libfuse2
Supplements:    (MozillaFirefox and himmelblau)
Supplements:    (chromium and himmelblau)
Supplements:    (google-chrome-stable and himmelblau)
Supplements:    (microsoft-edge-stable and himmelblau)

%description -n himmelblau-sso
Himmelblau SSO provides Azure Entra Id browser single sign-on via
Firefox, Chromium, Google Chrome, and Microsoft Edge (where installed),
using native messaging and managed browser policies. It also provides
web apps for common Office 365 applications (Teams, Outlook, etc).

%package -n himmelblau-sso-policies
Summary:        Browser policy files for Himmelblau SSO
Recommends:     himmelblau-sso
Recommends:     jq
BuildArch:      noarch

%description -n himmelblau-sso-policies
Browser policy configuration files for Himmelblau SSO. This package
installs policy files that automatically configure Chrome/Chromium and
Firefox to install the required browser extension for SSO functionality.

Install this package if you want automatic browser policy configuration.
If you prefer to manage browser policies manually, you can skip this
package and configure the extension installation yourself.

%package -n himmelblau-qr-greeter
Summary:        Azure Entra Id DAG URL QR code GNOME Shell extension
Requires:       gnome-shell
Requires:       himmelblau
Recommends:     dconf
BuildArch:      noarch

%description -n himmelblau-qr-greeter
GNOME Shell extension that adds a QR code to authentication prompts
when a MS DAG URL is detected.

%prep
%autosetup -a1

%build
make rpm-servicefiles
%if !(0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000)
export HIMMELBLAU_ALLOW_MISSING_SELINUX=1
%endif
%{cargo_build} --workspace --exclude himmelblau-fuzz
scripts/i18n-compile --profile release
%if !0%{?suse_version}
make authselect
%endif

%check
%if !(0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000)
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
install -D -d -m 0755 %{buildroot}/%{_datadir}/nsswitch.conf.d
install -m 0644 %{SOURCE3} %{buildroot}/%{_datadir}/nsswitch.conf.d/50-himmelblau.conf

# PAM
install -D -d -m 0755 %{buildroot}/%{_pam_moduledir}
install -D -d -m 0755 %{buildroot}/usr/lib/pam-config.d
strip --strip-unneeded target/release/libpam_himmelblau.so
install -m 0755 target/release/libpam_himmelblau.so %{buildroot}/%{_pam_moduledir}/pam_himmelblau.so
install -m 0644 platform/opensuse/pam-config %{buildroot}/usr/lib/pam-config.d/himmelblau.conf
install -m 0644 platform/opensuse/pam-config-unseal %{buildroot}/usr/lib/pam-config.d/himmelblau-unseal.conf
%if !0%{?suse_version}
install -D -d -m 0755 %{buildroot}/%{_datadir}/authselect/vendor/himmelblau/
install -m 0755 platform/el/authselect/* %{buildroot}/%{_datadir}/authselect/vendor/himmelblau/
%endif

# Himmelblau
install -D -d -m 0755 %{buildroot}%{_sbindir}
install -D -d -m 0755 %{buildroot}%{_bindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -D -d -m 0755 %{buildroot}%{_userunitdir}
install -D -d -m 0755 %{buildroot}%{_prefix}/lib/himmelblau
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/krb5.conf.d
install -D -d -m 0755 %{buildroot}/%{_unitdir}/display-manager.service.d/
install -D -d -m 0755 %{buildroot}%{_datadir}/doc/himmelblau/
install -D -d -m 0755 %{buildroot}%{_datadir}/doc/himmelblau-sso-policies/
install -D -d -m 0755 %{buildroot}/%{_tmpfilesdir}/
install -D -d -m 0755 %{buildroot}%{_mandir}/man1
install -D -d -m 0755 %{buildroot}%{_mandir}/man5
install -D -d -m 0755 %{buildroot}%{_mandir}/man8
install -D -d -m 0755 %{buildroot}%{_libexecdir}
strip --strip-unneeded target/release/himmelblaud
strip --strip-unneeded target/release/himmelblaud_tasks
strip --strip-unneeded target/release/aad-tool
install -m 0644 target/config/himmelblau.conf.example %{buildroot}/%{_prefix}/lib/himmelblau/himmelblau.conf
install -m 0644 src/config/gdm3_service_override.conf %{buildroot}/%{_unitdir}/display-manager.service.d/override.conf
install -m 0755 target/release/aad-tool %{buildroot}/%{_bindir}/
install -m 0644 platform/opensuse/himmelblaud-tasks.service %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblaud.service %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblaud.socket %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblaud-tasks.socket %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblaud-broker.socket %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblau-hsm-pin-init.service %{buildroot}/%{_unitdir}/
install -m 0644 platform/opensuse/himmelblau-compliance-check.service %{buildroot}/%{_userunitdir}/
install -m 0644 platform/opensuse/himmelblau-compliance-check.timer %{buildroot}/%{_userunitdir}/
install -m 0755 src/daemon/scripts/himmelblau-init-hsm-pin %{buildroot}/%{_libexecdir}/
install -m 0755 target/release/himmelblaud %{buildroot}/%{_sbindir}/
install -m 0755 target/release/himmelblaud_tasks %{buildroot}/%{_sbindir}/
install -m 0644 README.md %{buildroot}/%{_datadir}/doc/himmelblau/README
install -m 0644 target/config/himmelblau.conf.example %{buildroot}/%{_datadir}/doc/himmelblau/
install -m 0644 man/man1/aad-tool.1 %{buildroot}/%{_mandir}/man1/
install -m 0644 man/man5/himmelblau.conf.5 %{buildroot}/%{_mandir}/man5/
install -m 0644 man/man8/himmelblaud.8 %{buildroot}/%{_mandir}/man8/
install -m 0644 man/man8/himmelblaud_tasks.8 %{buildroot}/%{_mandir}/man8/
install -m 0644 src/daemon/src/himmelblau-policies.tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/himmelblau-policies.conf
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
install -D -d -m 0755 %{buildroot}/%{_selinux_pkgdir}/himmelblaud
install -D -d -m 0755 %{buildroot}/%{_selinux_docdir}
install -m 0644 src/selinux/src/himmelblaud.te %{buildroot}/%{_selinux_pkgdir}/himmelblaud/himmelblaud.te
install -m 0644 src/selinux/src/himmelblaud.fc %{buildroot}/%{_selinux_pkgdir}/himmelblaud/himmelblaud.fc
install -m 0644 src/selinux/src/himmelblaud.if %{buildroot}/%{_selinux_pkgdir}/himmelblaud/himmelblaud.if
%endif
pushd %{buildroot}%{_sbindir}
ln -s himmelblaud rchimmelblaud
ln -s himmelblaud_tasks rchimmelblaud_tasks
popd

install -d %{buildroot}%{_datadir}/locale
cp -a target/release/locale/. %{buildroot}%{_datadir}/locale/
find %{buildroot}%{_datadir}/locale -type f -exec chmod 0644 {} +

# Aliases for bare language codes that have no catalog of their own
install -D -m 0644 target/release/locale/pt_BR/LC_MESSAGES/himmelblau.mo   %{buildroot}%{_datadir}/locale/pt/LC_MESSAGES/himmelblau.mo
install -D -m 0644 target/release/locale/sr@latin/LC_MESSAGES/himmelblau.mo   %{buildroot}%{_datadir}/locale/sr/LC_MESSAGES/himmelblau.mo
%if 0%{?suse_version}
%fdupes %{buildroot}%{_datadir}/locale
%endif

%find_lang himmelblau

# SSHD Config
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
install -m 0644 platform/el/sshd_config %{buildroot}/%{_sysconfdir}/ssh/sshd_config.d/30-himmelblau.conf

# Broker
install -D -d -m 0755 %{buildroot}%{_datarootdir}/dbus-1/services
strip --strip-unneeded target/release/broker
install -m 0755 target/release/broker %{buildroot}/%{_sbindir}/himmelblau_broker
install -m 0644 src/broker/platform/com.microsoft.identity.broker1.service %{buildroot}/%{_datadir}/dbus-1/services/
install -m 0644 src/broker/platform/himmelblau-broker.service %{buildroot}/%{_userunitdir}/
pushd %{buildroot}%{_sbindir}
ln -s himmelblau_broker rchimmelblau_broker
popd

# Single Sign On
strip --strip-unneeded target/release/linux-entra-sso
install -D -d -m 0755 %{buildroot}%{_libdir}/mozilla/native-messaging-hosts
install -D -d -m 0755 %{buildroot}%{chrome_nm_dir}
install -D -d -m 0755 %{buildroot}%{chromium_nm_dir}
install -D -d -m 0755 %{buildroot}%{chrome_ext_dir}
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
install -m 0644 src/sso/src/chrome/linux_entra_sso.json %{buildroot}/%{chrome_nm_dir}/
install -m 0644 src/sso/src/chrome/linux_entra_sso.json %{buildroot}/%{chromium_nm_dir}/
install -m 0644 src/sso/src/chrome/extension.json %{buildroot}/%{chrome_ext_dir}/jlnfnnolkbjieggibinobhkjdfbpcohn.json
# The dependency generator does not resolve the interpreter of "env" scripts
sed -i '1s|^#!/usr/bin/env bash$|#!/bin/bash|' %{buildroot}%{_bindir}/o365 %{buildroot}%{_bindir}/o365-multi %{buildroot}%{_bindir}/o365-url-handler

# SSO Policies
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/firefox/policies
install -D -d -m 0755 %{buildroot}%{chrome_policy_dir}
install -D -d -m 0755 %{buildroot}%{chromium_policy_dir}
install -m 0644 src/sso-policies/src/chrome/policies.json %{buildroot}/%{chrome_policy_dir}/himmelblau.json
install -m 0644 src/sso-policies/src/chrome/policies.json %{buildroot}/%{chromium_policy_dir}/himmelblau.json
install -m 0644 src/sso-policies/src/firefox/policies.json %{buildroot}/%{_datadir}/doc/himmelblau-sso-policies/firefox-policies.json.example
install -m 0644 src/sso-policies/src/thunderbird/policies.json %{buildroot}/%{_datadir}/doc/himmelblau-sso-policies/thunderbird-policies.json.example

# QR Greeter
install -D -d -m 0755 %{buildroot}%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/extension.js %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/extension.js
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/qrcodegen.js %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/qrcodegen.js
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/qrselection.js %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/qrselection.js
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/metadata.json %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/metadata.json
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/stylesheet.css %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/stylesheet.css
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/security-key.svg %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/security-key.svg
install -m 0644 target/release/qr-greeter-build/qr-greeter@himmelblau-idm.org/security-key-touch.svg %{buildroot}/%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/security-key-touch.svg

%post -n libnss_himmelblau2
/sbin/ldconfig

handle_nsswitch_conf() {
  conf=$1
  sed -i '/^passwd:/ {/himmelblau/! s/$/ himmelblau/}' $conf
  sed -i '/^group:/ {/himmelblau/! s/$/ himmelblau/}' $conf
  sed -i '/^shadow:/ {/himmelblau/! s/$/ himmelblau/}' $conf
  sed -i '/^initgroups:/ {/himmelblau/! s/$/ himmelblau/}' $conf
}

etc_nsswitch_conf="/etc/nsswitch.conf"
usr_etc_nsswitch_conf="/usr/etc/nsswitch.conf"
nsswitch_snippet="/usr/share/nsswitch.conf.d/50-himmelblau.conf"

# Where the package ships a nsswitch.conf snippet (the nsswitch-config targets),
# nsswitch-config merges it into /etc/nsswitch.conf. That only works if the file
# is missing or was generated by nsswitch-config: an admin managed file is left
# untouched and the result is written to /etc/nsswitch.conf.rpmnew.
use_nsswitch_config() {
  [ -f "$nsswitch_snippet" ] || return 1
  command -v nsswitch-config >/dev/null 2>&1 || return 1
  [ ! -e "$etc_nsswitch_conf" ] || nsswitch-config --is_generated >/dev/null 2>&1
}

configured=0
if use_nsswitch_config && nsswitch-config >/dev/null 2>&1; then
  configured=1
fi

if [ "$configured" -eq 0 ]; then
  if [ -f $etc_nsswitch_conf ]; then
    handle_nsswitch_conf $etc_nsswitch_conf
  elif [ -f $usr_etc_nsswitch_conf ]; then
    cp $usr_etc_nsswitch_conf $etc_nsswitch_conf
    handle_nsswitch_conf $etc_nsswitch_conf
  fi
fi

# Ensure cache directory is created immediately after installation, ignoring failures
systemd-tmpfiles --create /usr/lib/tmpfiles.d/nss-himmelblau.conf 2>/dev/null || systemd-tmpfiles --create /usr/lib/x86_64-linux-gnu/tmpfiles.d/nss-himmelblau.conf 2>/dev/null || true

%postun -n libnss_himmelblau2
/sbin/ldconfig

# Regenerate nsswitch.conf without the snippet of this package
if [ "${1:-1}" = "0" ] && command -v nsswitch-config >/dev/null 2>&1 &&
   [ -e /etc/nsswitch.conf ] && nsswitch-config --is_generated >/dev/null 2>&1; then
    nsswitch-config >/dev/null 2>&1 || :
fi

%post -n pam-himmelblau
# Only create a symlink if it doesn't already exist
if [ ! -e /lib64/security/pam_himmelblau.so ]; then
    mkdir -p /lib64/security
    ln -s /usr/lib64/security/pam_himmelblau.so /lib64/security/pam_himmelblau.so
fi

# Skip PAM configuration on upgrade ($1 >= 2) so admin customizations to
# /etc/pam.d/*, authselect profiles, or pam-config state aren't reset by
# a package update. Only the initial install wires PAM up.
if [ "${1:-1}" -le 1 ]; then

# 1) authselect first (if available)
authselect_ok=0
if command -v authselect >/dev/null 2>&1; then
    feats="$(authselect current 2>/dev/null | awk '/Enabled features:/{f=1;next} f && /^-/{print $2}')"
    if authselect select himmelblau $feats --force >/dev/null 2>&1; then
        if authselect apply-changes >/dev/null 2>&1; then
            authselect_ok=1
        fi
    fi
fi

# Helper: validate/fix pam-config account line for pam_himmelblau
fix_pam_config_account_line() {
    local pc="/etc/pam.d/common-account-pc"
    local plain="/etc/pam.d/common-account"

    [ -f "$pc" ] || return 1

    # Detect legacy/simple pam-config output:
    #   account required|sufficient pam_himmelblau.so ignore_unknown_user
    if ! grep -Eq '^[[:space:]]*account[[:space:]]+(required|sufficient)[[:space:]]+pam_himmelblau\.so([[:space:]]+|$).*ignore_unknown_user' "$pc"; then
        return 0
    fi

    # Ensure we have a self-managed common-account
    if [ ! -f "$plain" ]; then
        sed '/^[[:space:]]*#/d' "$pc" >"$plain" || return 1
        chmod --reference="$pc" "$plain" || :
    fi

    # Make explicit himmelblau account denials terminal while preserving
    # PAM_IGNORE fall-through for local users.
    sed -i -E \
        's#^([[:space:]]*account[[:space:]]+)(required|sufficient)([[:space:]]+pam_himmelblau\.so([[:space:]]+|$).*ignore_unknown_user)#\1[success=ok auth_err=die default=ignore]\3#' \
        "$plain" || return 1

    return 0
}

# 2) pam-config second (if available)
pam_config_ok=0
if command -v pam-config >/dev/null 2>&1; then
    # Attempt to add himmelblau via pam-config. Older pam-config may not recognize --himmelblau at all.
    if pam-config --add --himmelblau >/dev/null 2>&1; then
        pam_config_ok=1

        # Validate/fix the known-bad older behavior (account required)
        fix_pam_config_account_line >/dev/null 2>&1 || :
    fi
fi

pamconfig_optout_self_managed_common() {
    # Convert pam-config-generated common-*-pc into self-managed common-*
    # per pam-config’s own header instructions.
    local i pc plain

    for i in account auth password session; do
        pc="/etc/pam.d/common-${i}-pc"
        plain="/etc/pam.d/common-${i}"

        [ -f "$pc" ] || continue

        # Only create/refresh common-* if it doesn't exist yet.
        # (If it already exists, assume admin/system is already self-managed.)
        if [ ! -f "$plain" ]; then
            # Strip comment lines (pam-config’s suggestion)
            sed '/^[[:space:]]*#/d' "$pc" >"$plain" || return 1
            chmod --reference="$pc" "$plain" 2>/dev/null || :
        fi
    done

    return 0
}

# 3) Final fallback: aad-tool configure-pam --really
# Only do this if neither authselect nor pam-config was used successfully.
if [ "$authselect_ok" -ne 1 ] && [ "$pam_config_ok" -ne 1 ]; then
    if command -v aad-tool >/dev/null 2>&1; then
        # Opt out of pam-config-managed common-*-pc so future pam-config runs
        # don’t overwrite the configuration we’re about to install.
        pamconfig_optout_self_managed_common >/dev/null 2>&1 || :
        aad-tool configure-pam --really >/dev/null 2>&1 || :
    fi
fi

fi  # end upgrade guard

# If GDM is present, ensure keyring consumes the auth token so the keyring unlocks
# like a normal password login.
GDM_PAM="/etc/pam.d/gdm-password"
if [ -f "$GDM_PAM" ]; then
    # If the keyring auth line exists without use_authtok, add it.
    if grep -Eq '^[[:space:]]*auth[[:space:]]+optional[[:space:]]+pam_gnome_keyring\.so' "$GDM_PAM" && \
       ! grep -Eq '^[[:space:]]*auth[[:space:]]+optional[[:space:]]+pam_gnome_keyring\.so.*\buse_authtok\b' "$GDM_PAM"; then
        sed -i -E '/^[[:space:]]*auth[[:space:]]+optional[[:space:]]+pam_gnome_keyring\.so/ {/use_authtok/! s/$/ use_authtok/;}' "$GDM_PAM" || :
    fi
fi

%postun -n pam-himmelblau
if [ "${1:-1}" = "0" ]; then
    # Only remove a symlink if it exists and is a symlink
    if [ -L /lib64/security/pam_himmelblau.so ]; then
        rm -f /lib64/security/pam_himmelblau.so
    fi

    SYSTEMD_USER_OVERRIDE="/etc/pam.d/systemd-user"
    SYSTEMD_USER_MARKER="# Managed by pam-himmelblau: systemd-user NSS account workaround"
    if [ -f "$SYSTEMD_USER_OVERRIDE" ] && grep -qxF "$SYSTEMD_USER_MARKER" "$SYSTEMD_USER_OVERRIDE"; then
        rm -f "$SYSTEMD_USER_OVERRIDE"
    fi
fi

%preun -n pam-himmelblau
# $1 is set by RPM: 0=uninstall, 1=upgrade. If your packager doesn’t pass it, we default to 0.
if [ "${1:-0}" -ne 0 ]; then exit 0; fi   # don’t switch on upgrade
if command -v authselect >/dev/null 2>&1; then
    if authselect current 2>/dev/null | grep -qE "^Profile ID:\s+himmelblau$"; then
        if   [ -d /usr/share/authselect/default/local   ]; then base=local
        elif [ -d /usr/share/authselect/default/minimal ]; then base=minimal
        else base=sssd; fi
        feats="$(authselect current 2>/dev/null | awk '/Enabled features:/{f=1;next} f && /^-/{print $2}')"
        authselect select "$base" $feats --force >/dev/null 2>&1 || :
        authselect apply-changes >/dev/null 2>&1 || :
    fi
fi

%post
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
        *" debian "* | *" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

# Detect if running on a Live system where service start should be skipped
is_live_system() {
    # Check common Live system indicators
    grep -q 'boot=live' /proc/cmdline 2>/dev/null && return 0
    grep -q 'rd.live' /proc/cmdline 2>/dev/null && return 0
    [ -d /run/live ] && return 0
    [ -f /.live-installer ] && return 0
    # Check if running in a container (dracut/systemd-nspawn)
    systemd-detect-virt -c -q 2>/dev/null && return 0
    return 1
}

# Determine if SELinux policy for himmelblaud is loaded.
# Returns success if SELinux is disabled or the policy is already loaded.
selinux_policy_loaded() {
    if ! command -v selinuxenabled >/dev/null 2>&1; then
        return 0
    fi

    if ! selinuxenabled; then
        return 0
    fi

    # If the policy sources are not installed, don't block service start.
    if [ ! -d /usr/share/selinux/packages/himmelblaud ]; then
        return 0
    fi

    if ! command -v semodule >/dev/null 2>&1; then
        return 1
    fi

    semodule -l 2>/dev/null | awk '{print $1}' | grep -qx himmelblaud
}

# Ensure cache directory is created with correct permissions
systemd-tmpfiles --create /usr/lib/tmpfiles.d/himmelblau-policies.conf 2>/dev/null || true

if is_debian_family; then
    if [ "$1" != "configure" ]; then
        exit 0
    fi

    # The following line should be removed in trixie or trixie+1
    deb-systemd-helper unmask himmelblaud.service himmelblaud-tasks.service himmelblau-hsm-pin-init.service >/dev/null || true

    # was-enabled defaults to true, so new installations run enable.
    if deb-systemd-helper --quiet was-enabled himmelblaud.service himmelblaud-tasks.service himmelblau-hsm-pin-init.service; then
        # Enables the unit on first installation, creates new
        # symlinks on upgrades if the unit file has changed.
        deb-systemd-helper enable himmelblaud.service himmelblaud-tasks.service himmelblau-hsm-pin-init.service >/dev/null || true
    else
        # Update the statefile to add new symlinks (if any), which need to be
        # cleaned up on purge. Also remove old symlinks.
        deb-systemd-helper update-state himmelblaud.service himmelblaud-tasks.service himmelblau-hsm-pin-init.service >/dev/null || true
    fi

    if [ -z "$DPKG_ROOT" ] && [ -d /run/systemd/system ]; then
        if is_live_system; then
            echo "Live system detected - skipping service start (HSM PIN will be initialized at first boot)"
        else
            deb-systemd-invoke daemon-reload --system >/dev/null || true
            if ! selinux_policy_loaded; then
                echo "SELinux enabled but himmelblaud policy not loaded yet; deferring service start"
            else
                deb-systemd-invoke restart himmelblaud.service himmelblaud-tasks.service >/dev/null || true
            fi
        fi
    fi

    # was-enabled defaults to true, so new installations run enable.
    if deb-systemd-helper --user --quiet was-enabled himmelblau-compliance-check.timer; then
        # Globally enable user timer for compliance checks (does not start existing sessions).
        deb-systemd-helper --user enable himmelblau-compliance-check.timer >/dev/null || true
    else
        # Update the statefile to add new symlinks (if any), which need to be
        # cleaned up on purge. Also remove old symlinks.
        deb-systemd-helper --user update-state himmelblau-compliance-check.timer >/dev/null || true
    fi
else
    # Presets the units; the restart on upgrade is done in the postun scriptlet.
    %systemd_post himmelblaud.service himmelblaud.socket himmelblaud-tasks.service himmelblaud-tasks.socket himmelblaud-broker.socket himmelblau-hsm-pin-init.service
    %systemd_user_post himmelblau-compliance-check.timer

    # The preset above never starts anything, so start the daemons on a fresh install.
    if [ "$1" -eq 1 ] && [ -d /run/systemd/system ]; then
        if is_live_system; then
            echo "Live system detected - skipping service start (HSM PIN will be initialized at first boot)"
        elif ! selinux_policy_loaded; then
            echo "SELinux enabled but himmelblaud policy not loaded yet; deferring service start"
        else
            systemctl start himmelblaud.service himmelblaud-tasks.service >/dev/null 2>&1 || true
        fi
    fi
fi

echo "Support Himmelblau: Financial support helps keep cloud identity for Linux open."
echo "Learn more: https://himmelblau-idm.org/donations/"

%postun
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
            *" debian "*|*" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

# Detect if running on a Live system where service start should be skipped
is_live_system() {
    # Check common Live system indicators
    grep -q 'boot=live' /proc/cmdline 2>/dev/null && return 0
    grep -q 'rd.live' /proc/cmdline 2>/dev/null && return 0
    [ -d /run/live ] && return 0
    [ -f /.live-installer ] && return 0
    # Check if running in a container (dracut/systemd-nspawn)
    systemd-detect-virt -c -q 2>/dev/null && return 0
    return 1
}

# Determine if SELinux policy for himmelblaud is loaded.
# Returns success if SELinux is disabled or the policy is already loaded.
selinux_policy_loaded() {
    if ! command -v selinuxenabled >/dev/null 2>&1; then
        return 0
    fi

    if ! selinuxenabled; then
        return 0
    fi

    # If the policy sources are not installed, don't block service start.
    if [ ! -d /usr/share/selinux/packages/himmelblaud ]; then
        return 0
    fi

    if ! command -v semodule >/dev/null 2>&1; then
        return 1
    fi

    semodule -l 2>/dev/null | awk '{print $1}' | grep -qx himmelblaud
}

# On full uninstall (purge on Debian, $1=0 on RPM): remove all runtime data,
# caches, and AccountsService entries for Entra users so GDM stops listing them.
_is_full_remove=0
if is_debian_family; then
    if [ "${1:-}" = "purge" ]; then _is_full_remove=1; fi
else
    if [ "${1:-1}" = "0" ]; then _is_full_remove=1; fi
fi

if is_debian_family; then
    if [ -d /run/systemd/system ] && [ -z "$DPKG_ROOT" ] && [ "$1" = remove ]; then
        deb-systemd-invoke daemon-reload --system >/dev/null || true
    fi

    if [ "$_is_full_remove" = "1" ] && [ -z "$DPKG_ROOT" ]; then
        deb-systemd-helper purge himmelblaud.service himmelblaud-tasks.service himmelblau-hsm-pin-init.service >/dev/null || true
        deb-systemd-helper --user purge himmelblau-compliance-check.timer >/dev/null || true
    fi
else
    # Restarting on upgrade is done here (not in the post scriptlet) to avoid a double restart.
    if is_live_system; then
        echo "Live system detected - skipping service restart"
        %systemd_postun himmelblaud.service himmelblaud.socket himmelblaud-tasks.service himmelblaud-tasks.socket himmelblaud-broker.socket himmelblau-hsm-pin-init.service
    elif ! selinux_policy_loaded; then
        echo "SELinux enabled but himmelblaud policy not loaded yet; skipping service restart"
        %systemd_postun himmelblaud.service himmelblaud.socket himmelblaud-tasks.service himmelblaud-tasks.socket himmelblaud-broker.socket himmelblau-hsm-pin-init.service
    else
        %systemd_postun_with_restart himmelblaud.service himmelblaud.socket himmelblaud-tasks.service himmelblaud-tasks.socket himmelblaud-broker.socket himmelblau-hsm-pin-init.service
    fi
fi

if [ "$_is_full_remove" = "1" ]; then
    rm -rf /var/cache/himmelblaud/
    rm -rf /var/cache/nss-himmelblau/
    rm -rf /var/cache/himmelblau-policies/
    rm -rf /var/lib/himmelblaud
    rm -rf /var/lib/private/himmelblaud/

    # Remove AccountsService entries for Entra users (UPN contains @)
    # so GDM stops showing them on the login screen.
    if [ -d /var/lib/AccountsService/users ]; then
        find /var/lib/AccountsService/users -maxdepth 1 -type f -name '*@*' -delete || true
    fi
fi

%pre
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
            *" debian "*|*" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

if ! is_debian_family; then
    %systemd_pre himmelblaud.service himmelblaud.socket himmelblaud-tasks.service himmelblaud-tasks.socket himmelblaud-broker.socket himmelblau-hsm-pin-init.service
fi

# Remove old service files from /etc/systemd/system/ that were installed by v1.4.x
# These take precedence over the new files in /usr/lib/systemd/system/ and lack
# the LoadCredentialEncrypted directive needed for HSM pin handling.
# In order to avoid removing user overrides, check against the hashes of known old
# files shipped by the package.
for OLD_FILE in \
    "/etc/systemd/system/himmelblaud.service" \
    "/etc/systemd/system/himmelblaud-tasks.service" \
    "/etc/systemd/system/gdm3.service.d/override.conf"; do
    if [ -f "$OLD_FILE" ]; then
        hash="$(md5sum "$OLD_FILE" 2>/dev/null | awk '{print $1}')"
        for KNOWN_HASH in \
            "e3b66fe76769d64610a353adf3dbc595" \
            "7b0f82a49b6be1c285de8549e611ab66" \
            "ed238618354f885a2b0c697278ea33e8" \
            "65b026cc5d5f0f4d600184b6190b8cb3" \
            "a40d5ca8aedba32f9399acc7e5fdd03d" \
            "7473a7bee9c4ebde099a658522f21203" \
            "5e0b319ec558849d4cd08e2d5eaf90e3" \
            "60ad28a9039e527aa709137fe1f3db00" \
            "95c442df9bd7c7d94d94292cdda14513" \
            "73b676e55c6979c601b6c2d93257410f" \
            "85ab21f2ac8b5c4b60451fa6540771db" \
            "15501a8e5db36b92eac8a965d544bae8" \
            "73fa66e462ff429076107e346d5ddbe8" \
            "f794aaa11243213f8de06f1416f16682" \
            "bde93199f6dc7b28d5e4e1d67504601b" \
            "d7e2800688c23d570230296e17b0e6c2" \
            "db8132b5813a3413b4647529cf7ea8f3" \
            "8cffb12270663febb99c61e5d013926f" \
            "ca442221291feb739fb0b078e036f6c9" \
            "b18d0e9861fc161aa3a4c093f140bdf1" \
            "337e41fad21375f4ee614caf3b07a2de" \
            ; do
            if [ "$hash" = "$KNOWN_HASH" ]; then
                echo "Removing old service file: $OLD_FILE"
                rm -f "$OLD_FILE"
            fi
        done
    fi
done

%preun
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
            *" debian "*|*" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

if is_debian_family; then
    if [ -d /run/systemd/system ]; then
        if [ -z "$DPKG_ROOT" ] && [ "$1" = remove ]; then
            deb-systemd-invoke stop himmelblaud.service himmelblaud-tasks.service himmelblau-hsm-pin-init.service >/dev/null || true
        fi
    fi

    # Globally disable user timer on package removal (not during upgrades)
    if [ "$1" = remove ] || [ "$1" = purge ]; then
        deb-systemd-helper --user disable himmelblau-compliance-check.timer >/dev/null || true
    fi
else
    %systemd_preun himmelblaud.service himmelblaud.socket himmelblaud-tasks.service himmelblaud-tasks.socket himmelblaud-broker.socket himmelblau-hsm-pin-init.service
    %systemd_user_preun himmelblau-compliance-check.timer
fi

%posttrans
config_file="/etc/himmelblau/himmelblau.conf"
saved_config="${config_file}.rpmsave"

# RPM creates .rpmsave after the post scriptlet when an owned config is removed during an
# upgrade, so recover the previous local configuration at transaction end.
if [ -f "$saved_config" ] && [ ! -e "$config_file" ] && [ ! -L "$config_file" ]; then
    echo "Restoring Himmelblau configuration from $saved_config"
    if ! mv -- "$saved_config" "$config_file"; then
        echo "Failed to restore Himmelblau configuration from $saved_config" >&2
        exit 1
    fi

    if command -v systemctl >/dev/null 2>&1; then
        systemctl try-restart himmelblaud.service himmelblaud-tasks.service 2>/dev/null || true
    fi
fi

%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
%posttrans -n himmelblau-selinux
# Detect if running on a Live system where service start should be skipped
is_live_system() {
  # Check common Live system indicators
  grep -q 'boot=live' /proc/cmdline 2>/dev/null && return 0
  grep -q 'rd.live' /proc/cmdline 2>/dev/null && return 0
  [ -d /run/live ] && return 0
  [ -f /.live-installer ] && return 0
  # Check if running in a container (dracut/systemd-nspawn)
  systemd-detect-virt -c -q 2>/dev/null && return 0
  return 1
}

SELINUX_SRC_DIR="/usr/share/selinux/packages/himmelblaud"
SELINUX_MAKEFILE="/usr/share/selinux/devel/Makefile"
SELINUX_POLICYTYPE="targeted"

if [ -e /etc/selinux/config ]; then
  . /etc/selinux/config
fi

selinux_configured() {
  [ "${SELINUX:-}" = "disabled" ] && return 1
  [ -n "${SELINUXTYPE:-}" ] && [ "$SELINUXTYPE" != "$SELINUX_POLICYTYPE" ] && return 1
  command -v selinuxenabled >/dev/null 2>&1 && selinuxenabled && return 0
  [ -e /etc/selinux/config ] && [ "${SELINUXTYPE:-}" = "$SELINUX_POLICYTYPE" ]
}

if selinux_configured; then
  # Check if SELinux development tools are available
  if [ ! -f "$SELINUX_MAKEFILE" ]; then
    echo "Warning: SELinux development Makefile not found at $SELINUX_MAKEFILE"
    echo "Please install selinux-policy-devel and re-run this script"
    exit 0
  fi

  # Compile the policy module from source
  if [ -d "$SELINUX_SRC_DIR" ]; then
    echo "Compiling SELinux policy module..."
    cd "$SELINUX_SRC_DIR"
    if make -f "$SELINUX_MAKEFILE" himmelblaud.pp; then
      echo "Installing SELinux policy module..."
      if semodule -s "$SELINUX_POLICYTYPE" -i himmelblaud.pp; then
        # Clean up compiled files (keep source for potential recompilation)
        rm -f himmelblaud.pp tmp/*.* 2>/dev/null || :
        rmdir tmp 2>/dev/null || :

        # Relabel installed binaries
        restorecon -Fv /usr/sbin/himmelblaud /usr/sbin/himmelblaud_tasks 2>/dev/null || :

        # Relabel existing dirs (may not exist on fresh install)
        [ -d /usr/lib/himmelblau ]            && restorecon -RFv /usr/lib/himmelblau || :
        [ -d /etc/himmelblau ]                && restorecon -RFv /etc/himmelblau || :
        [ -d /run/himmelblaud ]               && restorecon -RFv /run/himmelblaud || :
        [ -d /var/run/himmelblaud ]           && restorecon -RFv /var/run/himmelblaud || :
        [ -d /var/cache/private/himmelblaud ] && restorecon -RFv /var/cache/private/himmelblaud || :
        [ -d /var/cache/himmelblaud ]         && restorecon -RFv /var/cache/himmelblaud || :
        [ -d /var/cache/nss-himmelblau ]      && restorecon -RFv /var/cache/nss-himmelblau || :
        [ -d /var/cache/himmelblau-policies ] && restorecon -RFv /var/cache/himmelblau-policies || :
        [ -d /var/lib/private/himmelblaud ]   && restorecon -RFv /var/lib/private/himmelblaud || :
        [ -d /var/lib/himmelblaud ]           && restorecon -RFv /var/lib/himmelblaud || :

        # Restart daemons now that the policy is loaded (if present)
        if [ -z "$DPKG_ROOT" ] && [ -d /run/systemd/system ] && ! is_live_system; then
          systemctl daemon-reload >/dev/null 2>&1 || :
          systemctl restart himmelblaud.service himmelblaud-tasks.service >/dev/null 2>&1 || :
        fi

        echo "SELinux policy module installed successfully"
      else
        echo "Warning: Failed to install SELinux policy module"
      fi
    else
      echo "Warning: Failed to compile SELinux policy module"
    fi
  else
    echo "Warning: SELinux source directory not found at $SELINUX_SRC_DIR"
  fi
fi

%postun -n himmelblau-selinux
if [ "$1" -eq 0 ]; then
  if command -v selinuxenabled >/dev/null 2>&1 && selinuxenabled; then
    semodule -r himmelblaud || :
  fi
fi
%endif

%post -n himmelblau-sshd-config
# Comment out the `KbdInteractiveAuthentication no` line if present
CONF="/etc/ssh/sshd_config"
if [ -f "$CONF" ]; then
    sed -i 's/^KbdInteractiveAuthentication[[:space:]]\+no/#KbdInteractiveAuthentication no/' "$CONF"
fi

# Restart sshd if systemd is available, to make the config change take effect
if command -v systemctl >/dev/null 2>&1; then
    echo "Restarting sshd service..."
    systemctl restart ssh 2>/dev/null || systemctl restart sshd 2>/dev/null || true
fi

%post -n himmelblau-broker
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
            *" debian "*|*" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

if is_debian_family; then
    if [ "$1" != "configure" ]; then
        exit 0
    fi

    if [ -z "$DPKG_ROOT" ] && [ -d /run/systemd/system ]; then
        deb-systemd-invoke daemon-reload --user >/dev/null || true
        deb-systemd-invoke restart --user himmelblau-broker.service >/dev/null || true
    fi
else
    # Reload and restart of user managers is handled by the systemd file
    # triggers at the end of the transaction.
    %systemd_user_post himmelblau-broker.service
fi

%postun -n himmelblau-broker
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
            *" debian "*|*" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

if is_debian_family; then
    if [ -d /run/systemd/system ]; then
        if [ -z "$DPKG_ROOT" ] && [ "$1" = remove ]; then
            deb-systemd-invoke daemon-reload --user >/dev/null || true
        fi
    fi
else
    # Restarting on upgrade is done here (not in the post scriptlet) to avoid a double restart.
    %systemd_user_postun_with_restart himmelblau-broker.service
fi

%pre -n himmelblau-broker
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
            *" debian "*|*" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

if ! is_debian_family; then
    %systemd_user_pre himmelblau-broker.service
fi

%preun -n himmelblau-broker
is_debian_family() {
    (
        for f in /etc/os-release /usr/lib/os-release; do
            if [ -r "$f" ]; then
                . "$f"
                break
            fi
        done
        case " ${ID:-} ${ID_LIKE:-} " in
            *" debian "*|*" ubuntu "*) exit 0 ;;
        esac
        exit 1
    )
}

if is_debian_family; then
    if [ -d /run/systemd/system ]; then
        if [ -z "$DPKG_ROOT" ] && [ "$1" = remove ]; then
            deb-systemd-invoke stop --user himmelblau-broker.service >/dev/null || true
        fi
    fi
else
    %systemd_user_preun himmelblau-broker.service
fi

%post -n himmelblau-sso
if command -v update-desktop-database >/dev/null 2>&1; then update-desktop-database -q || true; fi
if [ -d /usr/share/icons/hicolor ] && command -v gtk-update-icon-cache >/dev/null 2>&1; then gtk-update-icon-cache -q /usr/share/icons/hicolor || true; fi

%postun -n himmelblau-sso
if command -v update-desktop-database >/dev/null 2>&1; then update-desktop-database -q || true; fi
if [ -d /usr/share/icons/hicolor ] && command -v gtk-update-icon-cache >/dev/null 2>&1; then gtk-update-icon-cache -q /usr/share/icons/hicolor || true; fi

%post -n himmelblau-sso-policies
# Himmelblau SSO policies postinst script
# Merges Firefox/Thunderbird extension configuration into existing policies without overwriting
# (Chrome/Chromium use separate policy files per application, so no merging needed)

FIREFOX_EXTENSION_URL="https://github.com/siemens/linux-entra-sso/releases/download/v1.9.1/linux_entra_sso-1.9.1.xpi"
THUNDERBIRD_EXTENSION_URL="https://github.com/siemens/linux-entra-sso/releases/download/v1.9.1/linux_entra_sso-1.9.1.thunderbird.xpi"

# Function to merge a Mozilla extension into policies.json
merge_mozilla_policy() {
    POLICY_FILE="$1"
    EXTENSION_URL="$2"
    APP_NAME="$3"
    EXTENSION_PATTERN="$4"
    POLICY_DIR=$(dirname "$POLICY_FILE")

    # Ensure directory exists
    mkdir -p "$POLICY_DIR"

    if [ -f "$POLICY_FILE" ]; then
        # Check if jq is available for proper JSON merging
        if command -v jq >/dev/null 2>&1; then
            # Check if the extension URL is already present and no old managed URL remains
            if jq -e --arg url "$EXTENSION_URL" --arg pattern "$EXTENSION_PATTERN" '
                (.policies.Extensions.Install[]? | select(. == $url)) and
                ([.policies.Extensions.Install[]? | select(type == "string" and test($pattern) and . != $url)] | length == 0)
            ' "$POLICY_FILE" >/dev/null 2>&1; then
                echo "$APP_NAME SSO extension already configured in $POLICY_FILE"
                return 0
            fi

            # Replace old managed SSO extension URLs with the current one.
            TEMP_FILE=$(mktemp)
            jq --arg url "$EXTENSION_URL" --arg pattern "$EXTENSION_PATTERN" '
                .policies.Extensions.Install = (
                    ([.policies.Extensions.Install[]? | select((type == "string" and test($pattern)) | not)] + [$url])
                    | unique
                )
            ' "$POLICY_FILE" > "$TEMP_FILE" && mv "$TEMP_FILE" "$POLICY_FILE"
            echo "Merged $APP_NAME SSO extension into $POLICY_FILE"
        else
            # Without jq, check if our extension is already there
            if grep -Fq "$EXTENSION_URL" "$POLICY_FILE" 2>/dev/null; then
                echo "$APP_NAME SSO extension already configured in $POLICY_FILE"
                return 0
            fi
            echo "Warning: jq not found. Cannot safely merge into existing $POLICY_FILE"
            echo "Please manually replace old linux_entra_sso URLs in policies.Extensions.Install with:"
            echo "  $EXTENSION_URL"
        fi
    else
        # Create new policy file
        cat > "$POLICY_FILE" << EOF
{
  "policies": {
    "Extensions": {
      "Install": [
        "$EXTENSION_URL"
      ]
    }
  }
}
EOF
        echo "Created $APP_NAME SSO policy at $POLICY_FILE"
    fi
}

# Merge Firefox and Thunderbird policies
merge_mozilla_policy "/etc/firefox/policies/policies.json" "$FIREFOX_EXTENSION_URL" "Firefox" "linux_entra_sso-[0-9][0-9.]*\\.xpi$"
merge_mozilla_policy "/etc/thunderbird/policies/policies.json" "$THUNDERBIRD_EXTENSION_URL" "Thunderbird" "linux_entra_sso-[0-9][0-9.]*\\.thunderbird\\.xpi$"
# Betterbird is a Thunderbird fork; it does not read /etc/thunderbird/policies.
merge_mozilla_policy "/etc/betterbird/policies/policies.json" "$THUNDERBIRD_EXTENSION_URL" "Betterbird" "linux_entra_sso-[0-9][0-9.]*\\.thunderbird\\.xpi$"
if [ -d /opt/betterbird ]; then
    merge_mozilla_policy "/opt/betterbird/distribution/policies.json" "$THUNDERBIRD_EXTENSION_URL" "Betterbird" "linux_entra_sso-[0-9][0-9.]*\\.thunderbird\\.xpi$"
fi

echo "Himmelblau SSO Mozilla policy configuration complete"

%postun -n himmelblau-sso-policies
# Himmelblau SSO policies postrm script
# Removes Firefox/Thunderbird extension configuration that was merged during install
# (Chrome/Chromium policy files are handled by package manager directly)

FIREFOX_EXTENSION_URL="https://github.com/siemens/linux-entra-sso/releases/download/v1.9.1/linux_entra_sso-1.9.1.xpi"
THUNDERBIRD_EXTENSION_URL="https://github.com/siemens/linux-entra-sso/releases/download/v1.9.1/linux_entra_sso-1.9.1.thunderbird.xpi"

# Function to remove a Mozilla extension from policies.json
remove_mozilla_policy() {
    POLICY_FILE="$1"
    EXTENSION_URL="$2"

    if [ -f "$POLICY_FILE" ]; then
        if command -v jq >/dev/null 2>&1; then
            # Remove the extension URL from the Install array
            TEMP_FILE=$(mktemp)
            jq --arg url "$EXTENSION_URL" '
                if .policies.Extensions.Install then
                    .policies.Extensions.Install = [.policies.Extensions.Install[] | select(. != $url)]
                else
                    .
                end
            ' "$POLICY_FILE" > "$TEMP_FILE" && mv "$TEMP_FILE" "$POLICY_FILE"
            echo "Removed Mozilla SSO extension from $POLICY_FILE"

            # If the Install array is now empty, clean up the structure
            if jq -e '.policies.Extensions.Install == []' "$POLICY_FILE" >/dev/null 2>&1; then
                jq 'del(.policies.Extensions.Install)' "$POLICY_FILE" > "$TEMP_FILE" && mv "$TEMP_FILE" "$POLICY_FILE"
            fi
            # If Extensions is now empty, clean it up
            if jq -e '.policies.Extensions == {}' "$POLICY_FILE" >/dev/null 2>&1; then
                jq 'del(.policies.Extensions)' "$POLICY_FILE" > "$TEMP_FILE" && mv "$TEMP_FILE" "$POLICY_FILE"
            fi
            # If policies is now empty, remove the file
            if jq -e '.policies == {}' "$POLICY_FILE" >/dev/null 2>&1; then
                rm -f "$POLICY_FILE"
                echo "Removed empty policy file $POLICY_FILE"
            fi
        else
            echo "Warning: jq not found. Cannot safely remove SSO extension from $POLICY_FILE"
            echo "Please manually remove the extension URL from policies.Extensions.Install:"
            echo "  $EXTENSION_URL"
        fi
    fi
}

# Only run on Debian purge/remove or RPM erase ($1=0)
case "$1" in
    remove|purge|0)
        # Remove Firefox and Thunderbird policies
        remove_mozilla_policy "/etc/firefox/policies/policies.json" "$FIREFOX_EXTENSION_URL"
        remove_mozilla_policy "/etc/thunderbird/policies/policies.json" "$THUNDERBIRD_EXTENSION_URL"
        remove_mozilla_policy "/etc/betterbird/policies/policies.json" "$THUNDERBIRD_EXTENSION_URL"
        remove_mozilla_policy "/opt/betterbird/distribution/policies.json" "$THUNDERBIRD_EXTENSION_URL"

        echo "Himmelblau SSO Mozilla policy configuration removed"
        ;;
esac

%post -n himmelblau-qr-greeter
if command -v dconf >/dev/null 2>&1; then
    # Enable extension for GDM user (login screen)
    if getent passwd Debian-gdm >/dev/null 2>&1; then
        echo "Enabling Himmelblau QR Greeter GNOME Shell extension for Debian GDM greeter..."

        if [ -x /usr/share/gdm/generate-config ]; then
            mkdir -p /usr/share/gdm/dconf

            cat > /usr/share/gdm/dconf/01-himmelblau-qr-greeter << 'EOF'
[org/gnome/shell]
enabled-extensions=['qr-greeter@himmelblau-idm.org']
EOF
            echo "Created /usr/share/gdm/dconf/01-himmelblau-qr-greeter"

            if /usr/share/gdm/generate-config; then
                echo "Regenerated Debian GDM greeter dconf defaults."
            else
                echo 'Warning: Debian GDM greeter dconf generation failed' >&2
            fi
        else
            echo 'Info: Debian-gdm user is available but /usr/share/gdm/generate-config is not executable; skipping Debian GDM extension enable.' >&2
        fi
    elif getent passwd gdm >/dev/null 2>&1; then
        echo "Enabling Himmelblau QR Greeter GNOME Shell extension for GDM user..."

        # Create /etc/dconf/profile/gdm if it doesn't exist
        if [ ! -f /etc/dconf/profile/gdm ]; then
            mkdir -p /etc/dconf/profile
            cat > /etc/dconf/profile/gdm << 'EOF'
user-db:user
system-db:gdm
file-db:/usr/share/gdm/greeter-dconf-defaults
EOF
            echo "Created /etc/dconf/profile/gdm"
        fi

        # Create dconf database directory if it doesn't exist
        mkdir -p /etc/dconf/db/gdm.d

        # Create the extension enablement configuration
        cat > /etc/dconf/db/gdm.d/01-himmelblau-qr-greeter << 'EOF'
[org/gnome/shell]
enabled-extensions=['qr-greeter@himmelblau-idm.org']
EOF
        echo "Created /etc/dconf/db/gdm.d/01-himmelblau-qr-greeter"
    else
        echo 'Info: neither Debian-gdm nor gdm user is available; skipping GDM extension enable.' >&2
    fi

    # Enable extension for regular users (lockscreen)
    echo "Enabling Himmelblau QR Greeter GNOME Shell extension for regular users..."

    # Create /etc/dconf/profile/user if it doesn't exist
    if [ ! -f /etc/dconf/profile/user ]; then
        mkdir -p /etc/dconf/profile
        cat > /etc/dconf/profile/user << 'EOF'
user-db:user
system-db:local
EOF
        echo "Created /etc/dconf/profile/user"
    fi

    # Create dconf database directory if it doesn't exist
    mkdir -p /etc/dconf/db/local.d

    # Create the extension enablement configuration for regular users
    cat > /etc/dconf/db/local.d/01-himmelblau-qr-greeter << 'EOF'
[org/gnome/shell]
enabled-extensions=['qr-greeter@himmelblau-idm.org']
EOF
    echo "Created /etc/dconf/db/local.d/01-himmelblau-qr-greeter"

    # Update dconf database
    if dconf update; then
        echo "Himmelblau QR Greeter GNOME Shell extension enabled for all users. You must restart GDM or log out and log in for the changes to take effect."
    else
        echo 'Warning: dconf update failed' >&2
    fi
else
    echo 'Info: dconf not available; skipping automatic extension enable.' >&2
fi

%postun -n himmelblau-qr-greeter
case "${1:-}" in
    remove|purge|0)
        rm -f /usr/share/gdm/dconf/01-himmelblau-qr-greeter
        rm -f /etc/dconf/db/gdm.d/01-himmelblau-qr-greeter
        rm -f /etc/dconf/db/local.d/01-himmelblau-qr-greeter

        if [ -x /usr/share/gdm/generate-config ]; then
            if /usr/share/gdm/generate-config; then
                echo "Regenerated Debian GDM greeter dconf defaults."
            else
                echo 'Warning: Debian GDM greeter dconf generation failed' >&2
            fi
        fi

        if command -v dconf >/dev/null 2>&1; then
            if dconf update; then
                echo "Himmelblau QR Greeter GNOME Shell extension dconf settings removed."
            else
                echo 'Warning: dconf update failed' >&2
            fi
        fi
        ;;
esac

%files -f himmelblau.lang
%dir %{_prefix}/lib/himmelblau
%dir %ghost %dir %attr(0600,root,root) %{_localstatedir}/cache/himmelblau-policies
%dir %{_unitdir}/display-manager.service.d
%dir %{_datadir}/doc/himmelblau
%{_prefix}/lib/himmelblau/himmelblau.conf
%{_unitdir}/display-manager.service.d/override.conf
%{_bindir}/aad-tool
%{_unitdir}/himmelblaud-tasks.service
%{_unitdir}/himmelblaud.service
%{_unitdir}/himmelblaud.socket
%{_unitdir}/himmelblaud-tasks.socket
%{_unitdir}/himmelblaud-broker.socket
%{_unitdir}/himmelblau-hsm-pin-init.service
%{_userunitdir}/himmelblau-compliance-check.service
%{_userunitdir}/himmelblau-compliance-check.timer
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
%{_sbindir}/rchimmelblaud
%{_sbindir}/rchimmelblaud_tasks

%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
%files -n himmelblau-selinux
%dir %{_docdir}/himmelblau-selinux
%dir %{_selinux_docdir}
%dir %{_selinux_pkgdir}
%dir %{_selinux_pkgdir}/himmelblaud
%{_selinux_pkgdir}/himmelblaud/himmelblaud.te
%{_selinux_pkgdir}/himmelblaud/himmelblaud.fc
%{_selinux_pkgdir}/himmelblaud/himmelblaud.if
%endif

%files -n libnss_himmelblau2
%dir %{_tmpfilesdir}
%{_libdir}/libnss_himmelblau.so.2
%{_tmpfilesdir}/nss-himmelblau.conf
%{_datadir}/nsswitch.conf.d/50-himmelblau.conf
%ghost %dir %attr(0755,root,root) /var/cache/nss-himmelblau

%files -n pam-himmelblau
%dir /usr/lib/pam-config.d
%{_pam_moduledir}/pam_himmelblau.so
/usr/lib/pam-config.d/himmelblau.conf
/usr/lib/pam-config.d/himmelblau-unseal.conf
%if !0%{?suse_version}
%dir %{_datadir}/authselect
%dir %{_datadir}/authselect/vendor
%dir %{_datadir}/authselect/vendor/himmelblau
%{_datadir}/authselect/vendor/himmelblau/*
%endif

%files -n himmelblau-sshd-config
%config %{_sysconfdir}/ssh/sshd_config.d/30-himmelblau.conf
%if 0%{?sle_version} <= 150500
%dir %{_sysconfdir}/ssh/sshd_config.d
%endif

%files -n himmelblau-broker
%{_sbindir}/himmelblau_broker
%{_datadir}/dbus-1/services/com.microsoft.identity.broker1.service
%{_userunitdir}/himmelblau-broker.service
%{_sbindir}/rchimmelblau_broker

%files -n himmelblau-sso
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/native-messaging-hosts
%dir /etc/chromium
%dir /usr/share/google-chrome
%dir %{chrome_nm_dir}
%dir %{chromium_nm_dir}
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
%config %{chrome_nm_dir}/linux_entra_sso.json
%config %{chromium_nm_dir}/linux_entra_sso.json
%{chrome_ext_dir}/jlnfnnolkbjieggibinobhkjdfbpcohn.json

%files -n himmelblau-sso-policies
%dir /etc/firefox
%dir /etc/firefox/policies
%dir /etc/chromium/policies
%dir /etc/opt/chrome
%dir /etc/opt/chrome/policies
%dir %attr(0555,root,root) %{chrome_policy_dir}
%dir %attr(0555,root,root) %{chromium_policy_dir}
%dir %{_datadir}/doc/himmelblau-sso-policies
%config %{chrome_policy_dir}/himmelblau.json
%config %{chromium_policy_dir}/himmelblau.json
%{_datadir}/doc/himmelblau-sso-policies/firefox-policies.json.example
%{_datadir}/doc/himmelblau-sso-policies/thunderbird-policies.json.example

%files -n himmelblau-qr-greeter
%dir %{_datarootdir}/gnome-shell
%dir %{_datarootdir}/gnome-shell/extensions
%dir %{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/extension.js
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/qrcodegen.js
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/qrselection.js
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/metadata.json
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/stylesheet.css
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/security-key.svg
%{_datadir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/security-key-touch.svg

%changelog
