#
# spec file for package gpg2
#
# Copyright (c) 2021 SUSE LLC
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
Version:        2.2.27
Release:        0
Summary:        File encryption, decryption, signature creation and verification utility
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.gnupg.org
Source:         ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Source2:        ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-%{version}.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
Source3:        %{name}.keyring
Source4:        scdaemon.udev
Source99:       %{name}.changes
Patch4:         gnupg-2.0.9-langinfo.patch
Patch5:         gnupg-2.2.8-files-are-digests.patch
Patch6:         gnupg-dont-fail-with-seahorse-agent.patch
Patch8:         gnupg-set_umask_before_open_outfile.patch
Patch9:         gnupg-detect_FIPS_mode.patch
Patch11:        gnupg-add_legacy_FIPS_mode_option.patch
Patch12:        gnupg-2.2.16-secmem.patch
Patch13:        gnupg-accept_subkeys_with_a_good_revocation_but_no_self-sig_during_import.patch
Patch14:        gnupg-add-test-cases-for-import-without-uid.patch
Patch15:        gnupg-allow-import-of-previously-known-keys-even-without-UIDs.patch
Patch1124847:   gnupg-gpg-agent-ulimit.patch
BuildRequires:  expect
BuildRequires:  fdupes
BuildRequires:  libassuan-devel >= 2.5.0
BuildRequires:  libgcrypt-devel >= 1.8.0
BuildRequires:  libgpg-error-devel >= 1.27
BuildRequires:  libksba-devel >= 1.3.5
BuildRequires:  makeinfo
BuildRequires:  npth-devel >= 1.2
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls) >= 3.0
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRequires:  pkgconfig(zlib)
# runtime dependency to support devel repository users - boo#955982
Requires:       libassuan0 >= 2.5.0
Requires:       libgcrypt20 >= 1.8.0
Requires:       libksba >= 1.3.5
Requires:       pinentry
Recommends:     dirmngr = %{version}
Provides:       gnupg = %{version}
Provides:       gpg = 1.4.9
Provides:       newpg
# special feature needed for OBS signd
Provides:       gpg2_signd_support
Obsoletes:      gpg < 1.4.9

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

%lang_package

%prep
%setup -q -n gnupg-%{version}
%patch1124847 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
touch -d 2018-05-04 doc/gpg.texi # to compensate for patch11 in order to not have man pages and info files have the build date (boo#1047218)

%build
date=$(date -u +%%Y-%%m-%%dT%%H:%%M+0000 -r %{SOURCE99})
%configure \
    --libexecdir=%{_libdir} \
    --docdir=%{_docdir}/%{name} \
    --with-agent-pgm=%{_bindir}/gpg-agent \
    --with-pinentry-pgm=%{_bindir}/pinentry \
    --with-dirmngr-pgm=%{_bindir}/dirmngr \
    --with-scdaemon-pgm=%{_bindir}/scdaemon \
    --enable-ldap \
    --enable-gpgsm=yes \
    --enable-gpg \
    --enable-gpgtar \
    --enable-g13 \
    --enable-large-secmem \
    --enable-wks-tools \
    --with-gnu-ld \
    --with-default-trust-store-file=%{_sysconfdir}/ssl/ca-bundle.pem \
    --enable-build-timestamp=$date \
    --enable-gpg-is-gpg2 \
    --enable-Werror

%make_build

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/gnupg/
# bnc#391347
install -m 644 doc/examples/gpgconf.conf %{buildroot}%{_sysconfdir}/gnupg
# delete to prevent fdupes from creating cross-partition hardlink
rm -rf %{buildroot}%{_docdir}/gpg2/examples/gpgconf.conf
rm %{buildroot}%{_infodir}/dir
# compat symlinks
ln -sf gpg2 %{buildroot}%{_bindir}/gpg
ln -sf gpgv2 %{buildroot}%{_bindir}/gpgv
ln -sf gpg2.1 %{buildroot}%{_mandir}/man1/gpg.1
ln -sf gpgv2.1 %{buildroot}%{_mandir}/man1/gpgv.1
# fix rpmlint invalid-lc-messages-dir:
rm -rf %{buildroot}/%{_datadir}/locale/en@{bold,}quot
# install scdaemon to %%{_bindir} (bnc#863645)
mv %{buildroot}%{_libdir}/scdaemon %{buildroot}%{_bindir}
mv %{buildroot}%{_libdir}/dirmngr_ldap %{buildroot}%{_bindir}
# install udev rules for scdaemon
install -Dm 0644 %{SOURCE4} %{buildroot}%{_udevrulesdir}/60-scdaemon.rules
# install legacy tools
install -m 755 tools/gpg-zip %{buildroot}/%{_bindir}
# install -m 755 tools/gpgsplit %%{buildroot}/%%{_bindir}

%find_lang gnupg2
%fdupes -s %{buildroot}

%check
# Run only localy, fails in OBS
#%%if ! 0%%{?qemu_user_space_build}
#make %%{?_smp_mflags} check
#%%endif

%post
%udev_rules_update

%files lang -f gnupg2.lang

%files
%{_infodir}/gnupg*
%exclude %{_mandir}/*/dirmngr*%{ext_man}
%{_mandir}/*/*%{ext_man}
%license COPYING*
%doc AUTHORS ChangeLog NEWS THANKS TODO doc/FAQ
%exclude %{_docdir}/%{name}/examples/systemd-user/dirmngr.*
%doc %{_docdir}/%{name}
%exclude %{_bindir}/dirmngr*
%{_bindir}/*
%{_libdir}/[^d]*
%{_sbindir}/addgnupghome
%{_sbindir}/applygnupgdefaults
%{_sbindir}/g13-syshelp
%{_udevrulesdir}/60-scdaemon.rules
%{_datadir}/gnupg
%dir %{_sysconfdir}/gnupg
%config(noreplace) %{_sysconfdir}/gnupg/gpgconf.conf

%files -n dirmngr
%license COPYING*
%{_mandir}/*/dirmngr*%{ext_man}
%{_docdir}/%{name}/examples/systemd-user/dirmngr.*
%{_bindir}/dirmngr*

%changelog
