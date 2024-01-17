#
# spec file for package aespipe
#
# Copyright (c) 2022 SUSE LLC
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


Name:           aespipe
Version:        2.4f
Release:        0
Summary:        AES Encrypting/Decrypting Pipe
License:        GPL-2.0-only
URL:            https://loop-aes.sourceforge.net/
Source0:        https://loop-aes.sourceforge.net/aespipe/%{name}-v%{version}.tar.bz2#/%{name}-%{version}.tar.bz2
Source1:        https://loop-aes.sourceforge.net/aespipe/%{name}-v%{version}.tar.bz2.sign#/%{name}-%{version}.tar.bz2.sign
Source2:        %{name}.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gpg2
Requires:       gpg2

%description
aespipe program is AES encrypting or decrypting pipe. It reads from standard
input and writes to standard output. It can be used to create and restore
encrypted tar or cpio archives. It can be used to encrypt and decrypt loop-AES
compatible encrypted disk images.

%prep
%setup -q -n %{name}-v%{version}
patch  < aes-GPL.diff

%build
autoreconf -fiv
%configure \
CFLAGS="$CFLAGS -fno-strict-aliasing" \
LDFLAGS="$LDFLAGS -fno-strict-aliasing" \
%ifarch %{ix86}
  --enable-asm=x86   --enable-padlock --enable-intelaes \
%endif
%ifarch amd64 x86_64 ia32e em64t
  --enable-asm=amd64 --enable-padlock --enable-intelaes \
%endif
  --disable-silent-rules
%make_build

%check
%make_build tests

%install
%make_install
install -D -p -m 0755 bz2aespipe \
  %{buildroot}%{_bindir}/bz2aespipe

%files
%doc ChangeLog README
%{_bindir}/aespipe
%{_bindir}/bz2aespipe
%{_mandir}/man1/aespipe.1%{?ext_man}

%changelog
