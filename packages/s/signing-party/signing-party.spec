#
# spec file for package signing-party
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           signing-party
Version:        2.10
Release:        0
Summary:        GPG Tools
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://wiki.debian.org/caff
Source:         http://ftp.debian.org/debian/pool/main/s/signing-party/signing-party_%{version}.orig.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE caff-manpage.patch [bnc#722626]
Patch1:         caff-manpage.patch
Requires:       %{_sbindir}/sendmail
Requires:       gpg
Requires:       perl
Requires:       perl-GnuPG-Interface
Requires:       perl-MIME-tools
Requires:       perl-MailTools
Requires:       perl-Net-IDN-Encode
Requires:       perl-Text-Template
Requires:       qprint
%if 0%{?suse_version} > 1320
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libmd-devel
BuildRequires:  libtool
%else
BuildArch:      noarch
%endif

%description
Signing Party is a collection for all kinds of pgp related things,
including signing scripts, party preparation scripts etc.

caff is a script that helps you in keysigning. It takes a list of
keyids on the command line, fetches them from a keyserver and calls
GnuPG so that you can sign it. It then mails each key to all its email
addresses - only including the one UID that we send to in each mail.

pgp-clean takes a list of keyids on the command line and outputs an
ascii-armored keyring on stdout for each key with all signatures
except self-signatures stripped. Its use is to reduce the size of keys
sent out after signing. (pgp-clean is a stripped-down caff version.)

gpg-key2ps will output a PostScript file which has your Key-ID, UIDs
and fingerprint nicely formatted for printing paper slips to take with
you to a signing-party.

Given one or more key-ids, gpg-mailkeys mails these keys to their
owners. You use this after you've signed them. By default, the mails
contain a standard text and your name and address as the From (as
determined by the sendmail command).

gpglist takes a keyid and creates a listing showing who signed your
user IDs.

gpgsigs was written to assist the user in signing keys during a
keysigning party. It takes as input a file containing keys in gpg
--list-keys format and prepends every line with a tag indicating if
the user has already signed that uid.

keylookup is a wrapper around gpg --search, allowing you to search for
keys on a keyserver. It presents the list of matching keys to the user
and allows her to select the keys for importing into the GnuPG
keyring.

%prep
%setup -q -n signing-party-%{version}
%patch1 -p1

%build
%if 0%{?suse_version} > 1320
pushd keyanalyze/pgpring
autoreconf -fiv
%configure
popd
%else
rm -rf keyanalyze
%endif

make %{?_smp_mflags} V=1 CFLAGS="%{optflags}"

%install

%if 0%{?suse_version} > 1320
pushd keyanalyze/pgpring
install -D -p -m 0755 pgpring   %{buildroot}%{_bindir}/signing-party-pgpring
install -D -p -m 0644 pgpring.1 %{buildroot}%{_mandir}/man1/signing-party-pgpring.1
popd
%endif

mkdir -p %{buildroot}
install -d d %{buildroot}%{_bindir}
install -m 755 caff/caff caff/pgp-clean caff/pgp-fixkey %{buildroot}%{_bindir}
install -m 755 gpglist/gpglist %{buildroot}%{_bindir}
install -m 755 gpg-key2ps/gpg-key2ps %{buildroot}%{_bindir}
install -m 755 gpglist/gpglist %{buildroot}%{_bindir}
install -m 755 gpg-mailkeys/gpg-mailkeys %{buildroot}%{_bindir}
install -m 755 gpgsigs/gpgsigs %{buildroot}%{_bindir}
install -m 755 keylookup/keylookup %{buildroot}%{_bindir}
install -m 755 keyart/keyart %{buildroot}%{_bindir}

install -d %{buildroot}%{_mandir}/man1
install -m 644 caff/caff.1 caff/pgp-clean.1 caff/pgp-fixkey.1 %{buildroot}%{_mandir}/man1
install -m 644 gpg-key2ps/gpg-key2ps.1 %{buildroot}%{_mandir}/man1
install -m 644 gpglist/gpglist.1 %{buildroot}%{_mandir}/man1
install -m 644 gpg-mailkeys/gpg-mailkeys.1 %{buildroot}%{_mandir}/man1
install -m 644 gpgsigs/gpgsigs.1 %{buildroot}%{_mandir}/man1
install -m 644 keylookup/keylookup.1 %{buildroot}%{_mandir}/man1
install -m 644 keyart/doc/keyart.1 %{buildroot}%{_mandir}/man1

%files
%doc caff/README caff/README.gpg-agent caff/README.many-keys caff/README.v3-keys caff/caffrc.sample
%doc gpgsigs/gpgsigs-lt2k5*.txt gpg-mailkeys/example.gpg-mailkeysrc
%doc keylookup/NEWS
%{_bindir}/caff
%{_bindir}/gpg-key2ps
%{_bindir}/gpg-mailkeys
%{_bindir}/gpglist
%{_bindir}/gpgsigs
%{_bindir}/keyart
%{_bindir}/keylookup
%{_bindir}/pgp-clean
%{_bindir}/pgp-fixkey
%if 0%{?suse_version} > 1320
%{_bindir}/signing-party-pgpring
%endif
%{_mandir}/man1/caff.1%{?ext_man}
%{_mandir}/man1/gpg-key2ps.1%{?ext_man}
%{_mandir}/man1/gpg-mailkeys.1%{?ext_man}
%{_mandir}/man1/gpglist.1%{?ext_man}
%{_mandir}/man1/gpgsigs.1%{?ext_man}
%{_mandir}/man1/keyart.1%{?ext_man}
%{_mandir}/man1/keylookup.1%{?ext_man}
%{_mandir}/man1/pgp-clean.1%{?ext_man}
%{_mandir}/man1/pgp-fixkey.1%{?ext_man}
%if 0%{?suse_version} > 1320
%{_mandir}/man1/signing-party-pgpring.1%{?ext_man}
%endif

%changelog
