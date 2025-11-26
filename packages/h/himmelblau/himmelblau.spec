#
# spec file for package himmelblau
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        2.0.4+git.2.5d26a19
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
BuildRequires:  dbus-1-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libclang13
BuildRequires:  libdhash-devel
BuildRequires:  libopenssl-3-devel
BuildRequires:  libunistring-devel
BuildRequires:  pam-devel
BuildRequires:  patchelf
BuildRequires:  pcre2-devel
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
BuildRequires:  selinux-policy-devel
%endif
BuildRequires:  sqlite3-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tpm2-0-tss-devel
ExclusiveArch:  %{rust_tier1_arches}
Recommends:     cron
Recommends:     krb5
Recommends:     libnss_himmelblau2
Recommends:     pam-himmelblau
Requires:       system-user-tss
Provides:       aad-cli
Provides:       aad-common
Provides:       authd
Provides:       authd-msentraid
Suggests:       himmelblau-sso
Requires:       man
Requires:       system-user-tss

%description
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n pam-himmelblau
Summary:        Azure Entra Id authentication PAM module
Requires:       %{name} = %{version}
Provides:       libpam-aad
Suggests:       himmelblau-qr-greeter
Recommends:     authselect
Recommends:     (oddjob-mkhomedir if authselect)

%description -n pam-himmelblau
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n libnss_himmelblau2
Summary:        Azure Entra Id authentication NSS module
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires:       %{name}
Provides:       libnss-aad
Provides:       nss-himmelblau

%description -n libnss_himmelblau2
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n himmelblau-sshd-config
Summary:        Azure Entra Id SSHD Configuration
Requires:       %{name} = %{version}
Supplements:    (pam-himmelblau and openssh-server)
Requires:       openssh-server
BuildRequires:  openssh-server
BuildArch:      noarch

%description -n himmelblau-sshd-config
Himmelblau is an interoperability suite for Microsoft Azure Entra Id,
which allows users to sign into a Linux machine using Azure
Entra Id credentials.

%package -n himmelblau-sso
Summary:        Azure Entra Id Browser SSO
Requires:       %{name} = %{version}
Supplements:    (MozillaFirefox and himmelblau)
Supplements:    (chromium and himmelblau)
Supplements:    (google-chrome-stable and himmelblau)
Supplements:    (microsoft-edge-stable and himmelblau)
Provides:       linux-entra-sso
# This is a hint, enabling users to call `zypper in intune-portal`, and receive
# the expected himmelblau+intune+sso capabilities.
Provides:       intune-portal
# This is necessary to prevent users from installing Himmelblau SSO along side
# Microsoft's Broker, as these will conflict.
Provides:       microsoft-identity-broker

%description -n himmelblau-sso
Himmelblau SSO provides Azure Entra Id browser single sign-on via
Firefox, Chromium, Google Chrome, and Microsoft Edge (where installed),
using native messaging and managed browser policies.

%package -n himmelblau-qr-greeter
Summary:        Azure Entra Id DAG URL QR code GNOME Shell extension
Requires:       gnome-shell >= 45
Supplements:    (pam-himmelblau and gnome-shell)
BuildArch:      noarch

%description -n himmelblau-qr-greeter
GNOME Shell extension that adds a QR code to authentication prompts
when a MS DAG URL is detected.

%postun -n libnss_himmelblau2 -p /sbin/ldconfig

%prep
%autosetup -a1

%build
make rpm-servicefiles
%if !(0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000)
export HIMMELBLAU_ALLOW_MISSING_SELINUX=1
%endif
%{cargo_build} --workspace --exclude himmelblau-fuzz

%check
%if !(0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000)
export HIMMELBLAU_ALLOW_MISSING_SELINUX=1
%endif
%{cargo_test} --workspace --exclude himmelblau-fuzz

%install
# NSS
cp target/release/libnss_%{name}.so target/release/libnss_%{name}.so.2
install -D -d -m 0755 %{buildroot}/%{_libdir}
strip --strip-unneeded target/release/libnss_himmelblau.so.2
patchelf --set-soname libnss_himmelblau.so.2 target/release/libnss_himmelblau.so.2
install -m 0755 target/release/libnss_%{name}.so.2 %{buildroot}/%{_libdir}
install -Dm 0644 src/nss/src/nss-himmelblau.tmpfiles.conf %{buildroot}/%{_tmpfilesdir}/nss-himmelblau.conf

# PAM
install -D -d -m 0755 %{buildroot}/%{_pam_moduledir}
strip --strip-unneeded target/release/libpam_himmelblau.so
install -m 0755 target/release/libpam_%{name}.so %{buildroot}/%{_pam_moduledir}/pam_%{name}.so
install -D -d -m 0755 %{buildroot}%{_datadir}/authselect/vendor/himmelblau
install -m 644 platform/el/authselect/* %{buildroot}%{_datadir}/authselect/vendor/himmelblau/

# Daemons, etc
install -D -d -m 0755 %{buildroot}/%{_sysconfdir}/himmelblau
cp src/config/himmelblau.conf.example %{buildroot}/%{_sysconfdir}/himmelblau/himmelblau.conf
install -D -d -m 0755 %{buildroot}%{_sbindir}
strip --strip-unneeded target/release/himmelblaud
strip --strip-unneeded target/release/himmelblaud_tasks
strip --strip-unneeded target/release/broker
install -m 0755 target/release/himmelblaud %{buildroot}/%{_sbindir}
install -m 0755 target/release/himmelblaud_tasks %{buildroot}/%{_sbindir}
install -m 0755 target/release/broker %{buildroot}/%{_sbindir}
pushd %{buildroot}%{_sbindir}
ln -s himmelblaud rchimmelblaud
ln -s himmelblaud_tasks rchimmelblaud_tasks
ln -s broker rcbroker
popd
install -D -d -m 0755 %{buildroot}%{_bindir}
strip --strip-unneeded target/release/aad-tool
install -m 0755 target/release/aad-tool %{buildroot}/%{_bindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 platform/opensuse/himmelblaud.service %{buildroot}%{_unitdir}/himmelblaud.service
install -m 0644 platform/opensuse/himmelblaud-tasks.service %{buildroot}%{_unitdir}/himmelblaud-tasks.service
install -D -d -m 0755 %{buildroot}%{_datarootdir}/dbus-1/services
install -m 0644 platform/opensuse/com.microsoft.identity.broker1.service %{buildroot}%{_datarootdir}/dbus-1/services/
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/ssh/sshd_config.d
install -m 0644 platform/el/sshd_config %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/himmelblau.conf
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/krb5.conf.d
install -m 0644 src/config/krb5_himmelblau.conf %{buildroot}%{_sysconfdir}/krb5.conf.d/krb5_himmelblau.conf
install -d -m 0600 %{buildroot}%{_localstatedir}/cache/himmelblau-policies
install -Dm 0644 src/config/gdm3_service_override.conf %{buildroot}%{_unitdir}/display-manager.service.d/override.conf
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
install -Dm 0644 target/release/himmelblaud.pp %{buildroot}%{_selinux_pkgdir}/himmelblaud.pp
install -Dm 0644 src/selinux/src/himmelblaud.te %{buildroot}%{_selinux_docdir}/himmelblaud.te
install -Dm 0644 src/selinux/src/himmelblaud.fc %{buildroot}%{_selinux_docdir}/himmelblaud.fc
%endif

# Single Sign On
strip --strip-unneeded target/release/linux-entra-sso
install -m 0755 target/release/linux-entra-sso %{buildroot}/%{_bindir}/linux-entra-sso
install -D -d -m 0755 %{buildroot}%{_libdir}/mozilla/native-messaging-hosts
install -m 0644 src/sso/src/firefox/linux_entra_sso.json %{buildroot}%{_libdir}/mozilla/native-messaging-hosts/
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/firefox/policies
install -m 0644 src/sso/src/firefox/policies.json %{buildroot}%{_sysconfdir}/firefox/policies/
install -D -d -m0755 %{buildroot}%{chrome_nm_dir}
install -D -d -m0755 %{buildroot}%{chromium_nm_dir}
install -D -d -m0755 %{buildroot}%{chrome_ext_dir}
install -D -d -m0755 %{buildroot}%{chrome_policy_dir}
install -D -d -m0755 %{buildroot}%{chromium_policy_dir}
install -m 0644 src/sso/src/chrome/linux_entra_sso.json %{buildroot}%{chrome_nm_dir}
install -m 0644 src/sso/src/chrome/linux_entra_sso.json %{buildroot}%{chromium_nm_dir}
install -m 0644 src/sso/src/chrome/extension.json %{buildroot}%{chrome_ext_dir}/jlnfnnolkbjieggibinobhkjdfbpcohn.json
install -m 0644 src/sso/src/chrome/policies.json %{buildroot}%{chrome_policy_dir}/himmelblau.json
install -m 0644 src/sso/src/chrome/policies.json %{buildroot}%{chromium_policy_dir}/himmelblau.json
install -m 0755 src/o365/src/o365.sh %{buildroot}/%{_bindir}/o365
install -m 0755 src/o365/src/o365-multi.sh %{buildroot}/%{_bindir}/o365-multi
install -m 0755 src/o365/src/o365-url-handler.sh %{buildroot}/%{_bindir}/o365-url-handler
install -D -d -m 0755 %{buildroot}%{_datadir}/applications/
install -m 0644 src/o365/generated/*.desktop %{buildroot}%{_datadir}/applications/
%{!?_iconsdir:%global _iconsdir %{_datadir}/icons}
install -D -d -m 0755 %{buildroot}%{_iconsdir}/hicolor/256x256/apps/
install -m 0644 src/o365/src/*.png %{buildroot}%{_iconsdir}/hicolor/256x256/apps/

# Man pages
install -D -d -m 0755 %{buildroot}%{_mandir}/man1
install -D -d -m 0755 %{buildroot}%{_mandir}/man5
install -D -d -m 0755 %{buildroot}%{_mandir}/man8
install -m 0644 man/man1/aad-tool.1 %{buildroot}%{_mandir}/man1/
install -m 0644 man/man5/himmelblau.conf.5 %{buildroot}%{_mandir}/man5/
install -m 0644 man/man8/himmelblaud.8 %{buildroot}%{_mandir}/man8/
install -m 0644 man/man8/himmelblaud_tasks.8 %{buildroot}%{_mandir}/man8/

# QR Greeter
install -D -d -m 0755 %{buildroot}%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org
install -m 0644 src/qr-greeter/src/qr-greeter@himmelblau-idm.org/extension.js %{buildroot}%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/
install -m 0644 src/qr-greeter/src/qr-greeter@himmelblau-idm.org/metadata.json %{buildroot}%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/
install -m 0644 src/qr-greeter/src/qr-greeter@himmelblau-idm.org/stylesheet.css %{buildroot}%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/
install -m 0644 src/qr-greeter/src/msdag.png %{buildroot}%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/

%pre
%service_add_pre himmelblaud.service himmelblaud-tasks.service

%post
gen_pin_hex() {
    if command -v openssl >/dev/null 2>&1; then
        openssl rand -hex 24 | tr -d '\n'
    else
        head -c 24 /dev/urandom | od -An -t x1 | tr -d ' \n'
    fi
}

if command -v systemd-creds >/dev/null 2>&1; then
    # Migrate the hsm-pin to a TPM bound cred (where a TPM is available)
    LEGACY=/var/lib/private/himmelblaud/hsm-pin
    CRED=/var/lib/private/himmelblaud/hsm-pin.enc

    if [ ! -f $CRED ]; then
        # Generate a new PIN if one doesn't exist, otherwise use the existing one
        if [ ! -f $LEGACY ]; then
            HSM_PIN=$(gen_pin_hex)
        else
            echo "Migrating existing HSM-PIN to encrypted credential"
            HSM_PIN=$(cat $LEGACY)
        fi

        # Encrypt the PIN
        install -d -m 755 /var/lib/private/himmelblaud
        printf '%s' "$HSM_PIN" | systemd-creds encrypt --name=hsm-pin --with-key=auto --tpm2-device=auto - "$CRED" && (rm -f $LEGACY || true)
    fi
fi

if command -v selinuxenabled >/dev/null 2>&1 && selinuxenabled; then
  if semodule -i /usr/share/selinux/packages/himmelblaud.pp; then
    semanage fcontext -a -t himmelblau_var_cache_t '/var/cache/himmelblaud'
    #restorecon -v -h /var/cache/himmelblaud
    TARGET="$(readlink -f /var/cache/himmelblaud)"
    semanage fcontext -a -t himmelblau_var_cache_t "${TARGET}(/.*)?"
    #restorecon -Rv "${TARGET}"

    # Relabel installed binaries (fc covers /usr/bin and /usr/sbin) /usr/sbin/himmelblaud /usr/sbin/himmelblaud_tasks
    restorecon -Fv /usr/sbin/himmelblaud /usr/sbin/himmelblaud_tasks || :

    # Relabel existing dirs only (DynamicUser will create cache dirs on first start)
    [ -d /etc/himmelblau ]                && restorecon -RFv /etc/himmelblau || :
    [ -d /run/himmelblaud ]               && restorecon -RFv /run/himmelblaud || :
    [ -d /var/cache/private/himmelblaud ] && restorecon -RFv /var/cache/private/himmelblaud || :
    [ -d /var/cache/himmelblaud ]         && restorecon -RFv /var/cache/himmelblaud || :
    [ -d /var/cache/nss-himmelblau ]      && restorecon -RFv /var/cache/nss-himmelblau || :

    # /var/lib/himmelblaud is a systemd DynamicUser symlink to /var/lib/private/himmelblaud
    semanage fcontext -a -t himmelblau_var_lib_t '/var/lib/himmelblaud'
    #restorecon -v -h /var/lib/himmelblaud
    LIBTARGET="$(readlink -f /var/lib/himmelblaud || true)"
    [ -n "$LIBTARGET" ] && semanage fcontext -a -t himmelblau_var_lib_t "${LIBTARGET}(/.*)?"
    # If the private dir already exists (e.g. after a previous run), relabel it
    [ -d "$LIBTARGET" ] && restorecon -RFv "$LIBTARGET" || :
  fi
fi

%service_add_post himmelblaud.service himmelblaud-tasks.service

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

%post -n pam-himmelblau
if command -v authselect >/dev/null 2>&1; then
    feats="$(authselect current 2>/dev/null | awk '"'"'/Enabled features:/{f=1;next} f && /^-/{print $2}'"'"')"
    authselect select himmelblau $feats --force >/dev/null 2>&1 || :
    authselect apply-changes >/dev/null 2>&1 || :
fi

%preun
%service_del_preun himmelblaud.service himmelblaud-tasks.service

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

%postun
if [ "$1" -eq 0 ]; then
  if command -v selinuxenabled >/dev/null 2>&1 && selinuxenabled; then
    semodule -r himmelblaud || :
  fi
fi
%service_del_postun himmelblaud.service himmelblaud-tasks.service

%files
%dir %{_sysconfdir}/himmelblau
%dir %{_localstatedir}/cache/himmelblau-policies
%config(noreplace) %{_sysconfdir}/himmelblau/himmelblau.conf
%config %{_sysconfdir}/krb5.conf.d/krb5_himmelblau.conf
%dir %{_unitdir}/display-manager.service.d
%config %{_unitdir}/display-manager.service.d/override.conf
%{_sbindir}/himmelblaud
%{_sbindir}/rchimmelblaud
%{_sbindir}/himmelblaud_tasks
%{_sbindir}/rchimmelblaud_tasks
%{_bindir}/aad-tool
%{_unitdir}/himmelblaud.service
%{_unitdir}/himmelblaud-tasks.service
%{_mandir}/man1/aad-tool.1*
%{_mandir}/man5/himmelblau.conf.5*
%{_mandir}/man8/himmelblaud.8*
%{_mandir}/man8/himmelblaud_tasks.8*
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 160000
%{_selinux_pkgdir}/himmelblaud.pp
%dir %{_docdir}/himmelblau-selinux
%dir %{_selinux_docdir}
%{_selinux_docdir}/himmelblaud.te
%{_selinux_docdir}/himmelblaud.fc
%endif

%files -n libnss_himmelblau2
%{_libdir}/libnss_%{name}.so.*
%dir %{_tmpfilesdir}
%{_tmpfilesdir}/nss-himmelblau.conf
%ghost %attr(0755,root,root) /var/cache/nss-himmelblau

%files -n pam-himmelblau
%{_pam_moduledir}/pam_%{name}.so
%dir %{_datadir}/authselect
%dir %{_datadir}/authselect/vendor
%dir %{_datadir}/authselect/vendor/himmelblau
%{_datadir}/authselect/vendor/himmelblau/*

%files -n himmelblau-sshd-config
# openssh-server doesn't own /etc/ssh/sshd_config.d before 15.5
%if 0%{?sle_version} <= 150500
%dir %{_sysconfdir}/ssh/sshd_config.d
%endif
%config %{_sysconfdir}/ssh/sshd_config.d/himmelblau.conf

%files -n himmelblau-sso
%{_bindir}/linux-entra-sso
%dir %{_libdir}/mozilla
%dir %{_libdir}/mozilla/native-messaging-hosts
%{_libdir}/mozilla/native-messaging-hosts/linux_entra_sso.json
%dir %{_sysconfdir}/firefox
%dir %{_sysconfdir}/firefox/policies
%config %{_sysconfdir}/firefox/policies/policies.json
%{_sbindir}/broker
%{_sbindir}/rcbroker
%{_datarootdir}/dbus-1/services/com.microsoft.identity.broker1.service
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
%config %{chrome_nm_dir}/linux_entra_sso.json
%config %{chromium_nm_dir}/linux_entra_sso.json
%config %{chrome_ext_dir}/jlnfnnolkbjieggibinobhkjdfbpcohn.json
%config %{chrome_policy_dir}/himmelblau.json
%config %{chromium_policy_dir}/himmelblau.json
%{_bindir}/o365
%{_bindir}/o365-multi
%{_bindir}/o365-url-handler
%{_datadir}/applications/*.desktop
%dir %{_iconsdir}/hicolor
%dir %{_iconsdir}/hicolor/256x256
%dir %{_iconsdir}/hicolor/256x256/apps
%{_iconsdir}/hicolor/256x256/apps/*.png

%files -n himmelblau-qr-greeter
%dir %{_datarootdir}/gnome-shell
%dir %{_datarootdir}/gnome-shell/extensions
%dir %{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org
%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/extension.js
%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/metadata.json
%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/stylesheet.css
%{_datarootdir}/gnome-shell/extensions/qr-greeter@himmelblau-idm.org/msdag.png

%changelog
