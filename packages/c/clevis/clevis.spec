#
# spec file for package clevis
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


%bcond_without pin_pkcs11
%bcond_without pin_tpm2
Name:           clevis
Version:        21
Release:        0
Summary:        A pluggable framework for automated decryption
License:        GPL-3.0-or-later
URL:            https://github.com/latchset/clevis
Source0:        https://github.com/latchset/clevis/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         cryptsetup-path.patch
Patch1:         0002-find-pcscd.patch
BuildRequires:  asciidoc
BuildRequires:  cryptsetup
BuildRequires:  curl
BuildRequires:  jq
BuildRequires:  keyutils
BuildRequires:  libpwquality-tools
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  socat
BuildRequires:  pkgconfig(audit) >= 2.7.8
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(jansson) >= 2.10
BuildRequires:  pkgconfig(jose) >= 8
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcryptsetup) >= 2.0.4
BuildRequires:  pkgconfig(luksmeta) >= 8
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udisks2)
Requires:       jose >= 8
#TPM2 pin
%if %{with pin_tpm2}
BuildRequires:  tpm2.0-tools >= 3.0.0
%endif
# pkcs11 pin
%if %{with pin_pkcs11}
BuildRequires:  pcsc-lite
BuildRequires:  pkgconfig(opensc-pkcs11)
%endif

%description
Clevis is a pluggable framework for automated decryption. It can be used to
provide automated decryption of data or even automated unlocking of LUKS
volumes.

%if %{with pin_pkcs11}
%package pin-pkcs11
Summary:        PKCS\#11 pin integration for Clevis
Requires:       %{name}-luks = %{version}
Requires:       opensc
Requires:       pcsc-lite

%description pin-pkcs11
Automatically unlocks LUKS block devices through a PKCS\#11 device.
%endif

%if %{with pin_tpm2}
%package pin-tpm2
Summary:        TPM2 pin integration for Clevis
Requires:       tpm2.0-tools >= 3.0.0

%description pin-tpm2
Provides support to encrypt a key in a Trusted Platform Module 2.0 (TPM2) chip. The key used for encryption is encrypted using the TPM2 chip, and is decrypted using TPM2 to allow clevis to decrypt the secret stored in the JWE.
Clevis store the public and private keys of the encrypted key in the JWE object, so those can be fetched on decryption to unseal the key encrypted using the TPM2.
%endif

%package pin-sss
Summary:        SSS pin integration for Clevis
Recommends:     %{name}-pin-pkcs11
Recommends:     %{name}-pin-tpm2

%description pin-sss
Support for the Shamir Secret Service algorithm as a way to mix pins together to provide sophisticated unlocking policies.

%package pin-tang
Summary:        Tang pin integration for Clevis
Requires:       curl

%description pin-tang
Support for Tang, a server implementation which provides cryptographic binding services without the need for an escrow.

%package luks
Summary:        LUKS integration for Clevis
Requires:       %{name} = %{version}
Requires:       cryptsetup
Requires:       libpwquality-tools
#Requires:       luksmeta >= 8

%description luks
LUKS integration for Clevis.

%package systemd
Summary:        Systemd integration for Clevis
Requires:       %{name}-luks = %{version}
Requires:       systemd

%description systemd
Automatically unlock LUKS devices in %{_sysconfdir}/crypttab with Clevis.

%package dracut
Summary:        Dracut integration for Clevis
Requires:       dracut

%description dracut
Automatically unlock LUKS devices in %{_sysconfdir}/crypttab with Clevis at early boot.

%package udisks2
Summary:        UDisks2 integration for Clevis
Requires:       %{name}-luks = %{version}

%description udisks2
Automatically unlock LUKS devices in UDisks2 with Clevis.

%package bash-completion
Summary:        Bash completion for Clevis
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash)

%description bash-completion
This package provides Bash completion for Clevis.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%pre systemd
%service_add_pre clevis-luks-askpass.path clevis-luks-askpass.service

%post systemd
%service_add_post clevis-luks-askpass.path clevis-luks-askpass.service

%preun systemd
%service_del_preun clevis-luks-askpass.path clevis-luks-askpass.service

%postun systemd
%service_del_postun clevis-luks-askpass.path clevis-luks-askpass.service

%post dracut
%{?regenerate_initrd_post}

%postun dracut
%{?regenerate_initrd_post}

%posttrans dracut
%{?regenerate_initrd_posttrans}

%if %{with pin_pkcs11}
%files pin-pkcs11
%license COPYING
%{_libexecdir}/clevis-luks-pkcs11-askpass
%{_libexecdir}/clevis-luks-pkcs11-askpin
%{_bindir}/clevis-decrypt-pkcs11
%{_bindir}/clevis-encrypt-pkcs11
%{_bindir}/clevis-pkcs11-common
%{_bindir}/clevis-pkcs11-afunix-socket-unlock
%{_mandir}/man1/clevis-encrypt-pkcs11.1%{?ext_man}
%endif

%files pin-tang
%license COPYING
%{_bindir}/clevis-decrypt-tang
%{_bindir}/clevis-encrypt-tang
%{_mandir}/man1/clevis-encrypt-tang.1%{?ext_man}

%if %{with pin_tpm2}
%files pin-tpm2
%license COPYING
%{_bindir}/clevis-decrypt-tpm2
%{_bindir}/clevis-encrypt-tpm2
%{_mandir}/man1/clevis-encrypt-tpm2.1%{?ext_man}
%endif

%files pin-sss
%license COPYING
%{_bindir}/clevis-decrypt-sss
%{_bindir}/clevis-encrypt-sss
%{_bindir}/clevis-decrypt-null
%{_bindir}/clevis-encrypt-null
%{_mandir}/man1/clevis-encrypt-sss.1%{?ext_man}

%files luks
%license COPYING
%{_bindir}/clevis-luks-*
%{_mandir}/man[17]/clevis-luks-*.[17]%{?ext_man}

%files systemd
%license COPYING
%{_libexecdir}/clevis-luks-askpass
%{_unitdir}/*

%files dracut
%license COPYING
%{_prefix}/lib/dracut/modules.d/**
%{_libexecdir}/clevis-luks-unlocker

%files udisks2
%license COPYING
%{_libexecdir}/clevis-luks-udisks2
%{_sysconfdir}/xdg/autostart/clevis-luks-udisks2.desktop

%files bash-completion
%license COPYING
%{_datadir}/bash-completion/completions/clevis

%files
%license COPYING
%{_bindir}/clevis
%{_bindir}/clevis-decrypt
%{_mandir}/man1/clevis.1%{?ext_man}
%{_mandir}/man1/clevis-decrypt.1%{?ext_man}

%changelog
