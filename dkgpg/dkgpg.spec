#
# spec file for package dkgpg
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


Name:           dkgpg
Version:        1.1.3
Release:        0
Summary:        Distributed Key Generation (DKG) and Threshold Cryptography for OpenPGP
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://www.nongnu.org/dkgpg/
Source:         https://download.savannah.gnu.org/releases/dkgpg/%{name}-%{version}.tar.gz
Source2:        https://download.savannah.gnu.org/releases/dkgpg/%{name}-%{version}.tar.gz.sig
Source3:        %{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel >= 4.2
BuildRequires:  libTMCG-devel >= 1.3.18
BuildRequires:  libbz2-devel
BuildRequires:  libgcrypt-devel >= 1.6
BuildRequires:  libgpg-error-devel >= 1.12
BuildRequires:  zlib-devel

%description
The Distributed Privacy Guard (DKGPG) implements Distributed Key
Generation (DKG) and Threshold Cryptography for OpenPGP. The
generated public keys are RFC4880 compatible and can be used by e.g.
GnuPG. The main purpose of this software is distributing power among
multiple parties, eliminating single points of failure, and
increasing the difficulty of side-channel attacks on private key
material.

DKGPG consists of a number of command-line programs. The current implementation
is in experimental state and should NOT be used in production environments.

A shared private key and a common public key (currently only
DSA/ElGamal) are generated. Further interactive protocols perform the
private operations like decryption and signing of files, provided
that a previously defined threshold of parties/devices take part in
the distributed computation. Due to the interactiveness of the
protocols, a lot of messages between participating parties have to be
exchanged in a secure way. GNUnet's mesh-routed CADET srvice is used
to establish private and broadcast channels for this message
exchange. A TCP/IP-based service is included as an alternative. It
may be combined with torsocks and NAT of a local hidden service.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%{_bindir}/dkg-*
%{_mandir}/man1/*%{ext_man}

%changelog
