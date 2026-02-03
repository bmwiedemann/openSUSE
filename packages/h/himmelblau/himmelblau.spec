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
Version:        2.3.3+git0.25e8b73
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
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-tools
%endif
ExclusiveArch:  %{rust_tier1_arches}
Requires:       make
Requires:       policycoreutils
Requires:       selinux-policy-devel
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
%if !(0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000)
export HIMMELBLAU_ALLOW_MISSING_SELINUX=1
%endif
%{cargo_build} --workspace --exclude himmelblau-fuzz
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
install -m 0644 src/config/krb5_himmelblau.conf %{buildroot}/%{_sysconfdir}/krb5.conf.d/
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
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
install -D -d -m 0755 %{buildroot}/%{_selinux_pkgdir}/himmelblaud
install -D -d -m 0755 %{buildroot}/%{_selinux_docdir}
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

handle_nsswitch_conf() {
  conf=$1
  sed -i '/^passwd:/ {/himmelblau/! s/$/ himmelblau/}' $conf
  sed -i '/^group:/ {/himmelblau/! s/$/ himmelblau/}' $conf
  sed -i '/^shadow:/ {/himmelblau/! s/$/ himmelblau/}' $conf
}

etc_nsswitch_conf="/etc/nsswitch.conf"
usr_etc_nsswitch_conf="/usr/etc/nsswitch.conf"
if [ -f $etc_nsswitch_conf ]; then
  handle_nsswitch_conf $etc_nsswitch_conf
elif [ -f $usr_etc_nsswitch_conf ]; then
  cp $usr_etc_nsswitch_conf $etc_nsswitch_conf
  handle_nsswitch_conf $etc_nsswitch_conf
fi

# Ensure cache directory is created immediately after installation, ignoring failures
systemd-tmpfiles --create /usr/lib/tmpfiles.d/nss-himmelblau.conf 2>/dev/null || systemd-tmpfiles --create /usr/lib/x86_64-linux-gnu/tmpfiles.d/nss-himmelblau.conf 2>/dev/null || true

%postun -n libnss_himmelblau2 -p /sbin/ldconfig

%post -n pam-himmelblau
# Only create a symlink if it doesn't already exist
if [ ! -e /lib64/security/pam_himmelblau.so ]; then
    mkdir -p /lib64/security
    ln -s /usr/lib64/security/pam_himmelblau.so /lib64/security/pam_himmelblau.so
fi

# 1) authselect first (if available)
if command -v authselect >/dev/null 2>&1; then
    feats="$(authselect current 2>/dev/null | awk '"'"'/Enabled features:/{f=1;next} f && /^-/{print $2}'"'"')"
    authselect select himmelblau $feats --force >/dev/null 2>&1 || :
    authselect apply-changes >/dev/null 2>&1 || :
fi

# Helper: validate/fix pam-config account line for pam_himmelblau
fix_pam_config_account_line() {
    local pc="/etc/pam.d/common-account-pc"
    local plain="/etc/pam.d/common-account"

    [ -f "$pc" ] || return 1

    # Detect the known-bad pam-config output:
    #   account required pam_himmelblau.so ignore_unknown_user
    if ! grep -Eq '^[[:space:]]*account[[:space:]]+required[[:space:]]+pam_himmelblau\.so([[:space:]]+|$).*ignore_unknown_user' "$pc"; then
        return 0
    fi

    # Ensure we have a self-managed common-account
    if [ ! -f "$plain" ]; then
        sed '/^[[:space:]]*#/d' "$pc" >"$plain" || return 1
        chmod --reference="$pc" "$plain" || :
    fi

    # Fix required -> sufficient in the self-managed file
    sed -i -E \
        's/^([[:space:]]*account[[:space:]]+)required([[:space:]]+pam_himmelblau\.so([[:space:]]+|$).*ignore_unknown_user)/\1sufficient\2/' \
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
# Only do this if pam-config wasn't used successfully.
if [ "$pam_config_ok" -ne 1 ]; then
    if command -v aad-tool >/dev/null 2>&1; then
        # Opt out of pam-config-managed common-*-pc so future pam-config runs
        # don’t overwrite the configuration we’re about to install.
        pamconfig_optout_self_managed_common >/dev/null 2>&1 || :

        aad-tool configure-pam --really >/dev/null 2>&1 || :
    fi
fi

%postun -n pam-himmelblau
# Only remove a symlink if it exists and is a symlink
if [ -L /lib64/security/pam_himmelblau.so ]; then
    rm -f /lib64/security/pam_himmelblau.so
fi

%preun -n pam-himmelblau
# $1 is set by RPM: 0=uninstall, 1=upgrade. If your packager doesn’t pass it, we default to 0.
if [ "${1:-0}" -ne 0 ]; then exit 0; fi   # don’t switch on upgrade
if command -v authselect >/dev/null 2>&1; then
    if authselect current 2>/dev/null | grep -qE "^Profile ID:\s+himmelblau$"; then
        if   [ -d /usr/share/authselect/default/local   ]; then base=local
        elif [ -d /usr/share/authselect/default/minimal ]; then base=minimal
        else base=sssd; fi
        feats="$(authselect current 2>/dev/null | awk '"'"'/Enabled features:/{f=1;next} f && /^-/{print $2}'"'"')"
        authselect select "$base" $feats --force >/dev/null 2>&1 || :
        authselect apply-changes >/dev/null 2>&1 || :
    fi
fi

%post
%service_add_post himmelblaud.service himmelblaud-tasks.service

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

# Ensure cache directory is created with correct permissions
systemd-tmpfiles --create /usr/lib/tmpfiles.d/himmelblau-policies.conf 2>/dev/null || true

# Ensure private data directory is created with correct permissions
systemd-tmpfiles --create /usr/lib/tmpfiles.d/himmelblaud.conf 2>/dev/null || true

# Remove old service files from /etc/systemd/system/ that were installed by v1.4.x
# These take precedence over the new files in /usr/lib/systemd/system/ and lack
# the LoadCredentialEncrypted directive needed for HSM pin handling.
for OLD_FILE in \
    "/etc/systemd/system/himmelblaud.service" \
    "/etc/systemd/system/himmelblaud-tasks.service" \
    "/etc/systemd/system/gdm3.service.d/override.conf"; do
    if [ -f "$OLD_FILE" ]; then
        echo "Removing old service file: $OLD_FILE"
        rm -f "$OLD_FILE"
    fi
done

# Reload systemd to pick up the new service files from /usr/lib/systemd/system/
if command -v systemctl >/dev/null 2>&1; then
    systemctl daemon-reload || true
fi

# Enable and start Himmelblau daemons if systemd is available
# On Live systems, skip service start - the HSM PIN will be generated at first boot
# via the himmelblau-hsm-pin-init.service oneshot when deployed to real hardware.
if command -v systemctl >/dev/null 2>&1; then
    if is_live_system; then
        echo "Live system detected - skipping service start (HSM PIN will be initialized at first boot)"
        # Only enable services so they start on first real boot
        systemctl enable himmelblaud.service himmelblaud-tasks.service 2>/dev/null || true
        # Enable HSM PIN init service separately (may not exist on older systemd)
        systemctl enable himmelblau-hsm-pin-init.service 2>/dev/null || true
    else
        echo "Enabling and starting Himmelblau services..."
        systemctl enable himmelblaud.service himmelblaud-tasks.service 2>/dev/null || true
        # Enable HSM PIN init service separately (may not exist on older systemd)
        systemctl enable himmelblau-hsm-pin-init.service 2>/dev/null || true
        systemctl restart himmelblaud.service himmelblaud-tasks.service 2>/dev/null || true
    fi
fi

%postun
%service_del_postun himmelblaud.service himmelblaud-tasks.service

if [ "$1" -eq 0 ]; then
  if command -v selinuxenabled >/dev/null 2>&1 && selinuxenabled; then
    semodule -r himmelblaud || :
  fi
fi

%pre
%service_add_pre himmelblaud.service himmelblaud-tasks.service

%preun
%service_del_preun himmelblaud.service himmelblaud-tasks.service

%posttrans
SELINUX_SRC_DIR="/usr/share/selinux/packages/himmelblaud"
SELINUX_MAKEFILE="/usr/share/selinux/devel/Makefile"

if command -v selinuxenabled >/dev/null 2>&1 && selinuxenabled; then
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
      if semodule -i himmelblaud.pp; then
        # Clean up compiled files (keep source for potential recompilation)
        rm -f himmelblaud.pp tmp/*.* 2>/dev/null || :
        rmdir tmp 2>/dev/null || :

        # Relabel installed binaries
        restorecon -Fv /usr/sbin/himmelblaud /usr/sbin/himmelblaud_tasks 2>/dev/null || :

        # Relabel existing dirs (may not exist on fresh install)
        [ -d /etc/himmelblau ]                && restorecon -RFv /etc/himmelblau || :
        [ -d /run/himmelblaud ]               && restorecon -RFv /run/himmelblaud || :
        [ -d /var/run/himmelblaud ]           && restorecon -RFv /var/run/himmelblaud || :
        [ -d /var/cache/private/himmelblaud ] && restorecon -RFv /var/cache/private/himmelblaud || :
        [ -d /var/cache/himmelblaud ]         && restorecon -RFv /var/cache/himmelblaud || :
        [ -d /var/cache/nss-himmelblau ]      && restorecon -RFv /var/cache/nss-himmelblau || :
        [ -d /var/lib/private/himmelblaud ]   && restorecon -RFv /var/lib/private/himmelblaud || :
        [ -d /var/lib/himmelblaud ]           && restorecon -RFv /var/lib/himmelblaud || :

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

%post -n himmelblau-sso
if command -v update-desktop-database >/dev/null 2>&1; then update-desktop-database -q || true; fi
if [ -d /usr/share/icons/hicolor ] && command -v gtk-update-icon-cache >/dev/null 2>&1; then gtk-update-icon-cache -q /usr/share/icons/hicolor || true; fi

%postun -n himmelblau-sso
if command -v update-desktop-database >/dev/null 2>&1; then update-desktop-database -q || true; fi
if [ -d /usr/share/icons/hicolor ] && command -v gtk-update-icon-cache >/dev/null 2>&1; then gtk-update-icon-cache -q /usr/share/icons/hicolor || true; fi

%post -n himmelblau-qr-greeter
if command -v machinectl >/dev/null 2>&1 && getent passwd gdm >/dev/null 2>&1; then
    echo "Enabling Himmelblau QR Greeter GNOME Shell extension for GDM user..."

    # Run the gsettings command inside a non-interactive gdm shell.
    machinectl --quiet shell gdm@ /bin/bash -lc \
        "gsettings set org.gnome.shell enabled-extensions \"['qr-greeter@himmelblau-idm.org']\"" \
        || echo 'Warning: unable to enable QR Greeter extension for gdm user' >&2
    echo "Himmelblau QR Greeter GNOME Shell extension enabled for GDM user. You must restart for the changes to take effect."
else
    echo 'Info: machinectl or gdm user not available; skipping automatic extension enable.' >&2
fi

%files
%dir %{_sysconfdir}/himmelblau
%dir %{_localstatedir}/cache/himmelblau-policies
%dir %{_unitdir}/display-manager.service.d
%dir %{_datadir}/doc/himmelblau
%config(noreplace) %{_sysconfdir}/himmelblau/himmelblau.conf
%config %{_sysconfdir}/krb5.conf.d/krb5_himmelblau.conf
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
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
%dir %{_docdir}/himmelblau-selinux
%dir %{_selinux_docdir}
%dir %{_selinux_pkgdir}
%dir %{_selinux_pkgdir}/himmelblaud
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
