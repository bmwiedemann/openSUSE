#
# spec file for package gpg2
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gpg2
Version:        2.5.3
Release:        0
Summary:        File encryption, decryption, signature creation and verification utility
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.gnupg.org
Source:         https://gnupg.org/ftp/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Source2:        https://gnupg.org/ftp/gcrypt/gnupg/gnupg-%{version}.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
Source3:        https://gnupg.org/signature_key.asc#/%{name}.keyring
Source4:        scdaemon.udev
Source5:        gpg2-systemd-user.tar.xz
Source99:       %{name}.changes
Patch1:         gnupg-gpg-agent-ulimit.patch
Patch2:         gnupg-2.0.9-langinfo.patch
Patch3:         gnupg-dont-fail-with-seahorse-agent.patch
Patch4:         gnupg-set_umask_before_open_outfile.patch
Patch5:         gnupg-detect_FIPS_mode.patch
Patch6:         gnupg-add_legacy_FIPS_mode_option.patch
Patch7:         gnupg-2.2.16-secmem.patch
Patch8:         gnupg-accept_subkeys_with_a_good_revocation_but_no_self-sig_during_import.patch
Patch9:         gnupg-add-test-cases-for-import-without-uid.patch
Patch10:        gnupg-allow-import-of-previously-known-keys-even-without-UIDs.patch
#PATCH-FIX-SUSE Allow 8192 bit RSA keys in keygen UI when large_rsa is set
Patch11:        gnupg-allow-large-rsa.patch
#PATCH-FIX-SUSE Revert the rfc4880bis features default of key generation
Patch12:        gnupg-revert-rfc4880bis.patch
#PATCH-FIX-OPENSUSE Do not pull revision info from GIT when autoconf is run
Patch13:        gnupg-nobetasuffix.patch
BuildRequires:  expect
BuildRequires:  fdupes
BuildRequires:  libassuan-devel >= 3.0.0
BuildRequires:  libgcrypt-devel >= 1.11.0
BuildRequires:  libgpg-error-devel >= 1.51
BuildRequires:  libksba-devel >= 1.6.3
BuildRequires:  makeinfo
BuildRequires:  npth-devel >= 1.2
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls) >= 3.2
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.27
BuildRequires:  pkgconfig(zlib)
Requires:       pinentry
Recommends:     dirmngr = %{version}
Provides:       gnupg = %{version}
Provides:       gpg = 1.4.9
Provides:       newpg
Obsoletes:      gpg < 1.4.9
%ifnarch loongarch64
BuildRequires:  ibmswtpm2
BuildRequires:  ibmtss-devel
%endif

%description
GnuPG is a hybrid-encryption software program; it uses a combination
of symmetric-key and public-key cryptography to encrypt/decrypt
messages and/or to sign and verify them.

gpg2 provides GPGSM, gpg-agent, and a keybox library.

%package -n dirmngr
Summary:        Keyserver, CRL, and OCSP access for GnuPG
Group:          Productivity/Networking/Security

%description -n dirmngr
Since version  2.1 of GnuPG, dirmngr takes care of accessing the OpenPGP
keyservers. As with previous versions it is also used as a server for managing
and downloading certificate
revocation lists (CRLs) for X.509 certificates, downloading X.509 certificates,
and providing access to OCSP providers.  Dirmngr is invoked internally by gpg,
gpgsm, or via the gpg-connect-agent tool.

%package tpm
Summary:        TPM2 support for GnuPG
Group:          Productivity/Networking/Security

%description tpm
Version 2.3 of GnuPG introduced support for converting GPG private
keys to TPM2 wrapped form.  This package enables that support.  The
keytotpm command will not function unless this package is installed.

%lang_package

%prep
%autosetup -p1 -a5 -n gnupg-%{version}

# In order to compensate for gnupg-add_legacy_FIPS_mode_option.patch
# to not have man pages and info files have the build date (boo#1047218)
touch -d 2018-05-04 doc/gpg.texi

%build
date=$(date -u +%%Y-%%m-%%dT%%H:%%M+0000 -r %{SOURCE99})
%configure \
    --docdir=%{_docdir}/%{name} \
    --disable-rpath \
    --enable-g13 \
    --enable-large-secmem \
    --with-gnu-ld \
    --with-default-trust-store-file=%{_sysconfdir}/ssl/ca-bundle.pem \
    --enable-build-timestamp=$date

%make_build

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/gnupg/

# install gpgconf.conf bnc#391347
install -m 644 doc/examples/gpgconf.conf %{buildroot}%{_sysconfdir}/gnupg
# delete to prevent fdupes from creating cross-partition hardlink
rm -rf %{buildroot}%{_docdir}/gpg2/examples/gpgconf.conf

# remove info dir
rm %{buildroot}%{_infodir}/dir

# compat symlinks
ln -sf gpg %{buildroot}%{_bindir}/gpg2
ln -sf gpgv %{buildroot}%{_bindir}/gpgv2
ln -sf gpg.1 %{buildroot}%{_mandir}/man1/gpg2.1
ln -sf gpgv.1 %{buildroot}%{_mandir}/man1/gpgv2.1
ln -sf gnupg.7 %{buildroot}%{_mandir}/man7/gnupg2.7

# install udev rules for scdaemon
install -Dm 0644 %{SOURCE4} %{buildroot}%{_udevrulesdir}/60-scdaemon.rules

# Move the systemd user units to the appropriate directory
install -d -m 755 %{buildroot}%{_userunitdir}
cp systemd-user/gpg-agent*.s* %{buildroot}%{_userunitdir}
cp systemd-user/dirmngr.s* %{buildroot}%{_userunitdir}
cp systemd-user/README.systemd %{buildroot}%{_docdir}/gpg2/

%find_lang gnupg2
%fdupes -s %{buildroot}

%check
%make_build check || :

%post
%udev_rules_update

%files lang -f gnupg2.lang

%files
%license COPYING*
%doc AUTHORS NEWS THANKS TODO ChangeLog
%{_infodir}/gnupg*
%dir %{_mandir}/manh/
%{_mandir}/*/[aghsw]*%{ext_man}
%doc %{_docdir}/%{name}
%{_bindir}/[gkw]*
%{_libexecdir}/[gks]*
%{_sbindir}/addgnupghome
%{_sbindir}/applygnupgdefaults
%{_sbindir}/g13-syshelp
%{_udevrulesdir}/60-scdaemon.rules
%{_datadir}/gnupg
%dir %{_sysconfdir}/gnupg
%config(noreplace) %{_sysconfdir}/gnupg/gpgconf.conf
%{_userunitdir}/gpg-agent*
%if 0%{?sle_version} >= 150500
%exclude %{_userunitdir}/dirmngr.*
%endif

%files -n dirmngr
%license COPYING*
%{_mandir}/*/dirmngr*%{ext_man}
%{_bindir}/dirmngr*
%{_libexecdir}/dirmngr_ldap
%{_userunitdir}/dirmngr.*

%ifnarch loongarch64
%files tpm
%license COPYING*
%{_libexecdir}/tpm2daemon*
%endif

%changelog
