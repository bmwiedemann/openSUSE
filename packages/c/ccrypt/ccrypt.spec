#
# spec file for package ccrypt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ccrypt
Version:        1.11
Release:        0
Summary:        Crypt and Decrypt Files and Streams with AES
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            http://ccrypt.sourceforge.net/
Source0:        http://ccrypt.sourceforge.net/download/%{version}/ccrypt-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  emacs-nox
BuildRequires:  libgcrypt-devel
Recommends:     %{name}-lang

%description
ccrypt is a utility for encrypting and decrypting files and streams.
It was designed as a replacement for the standard unix crypt utility,
which is notorious for using a very weak encryption algorithm.

ccrypt is based on the Rijndael cipher, which is the U.S. government's
chosen candidate for the Advanced Encryption Standard (AES, see
http://www.nist.gov/aes). This cipher is believed to provide very strong
security.

%package emacs
Summary:        Integration for %{name} with emacs
Group:          Productivity/Security
Requires:       %{name} = %{version}
Requires:       emacs
Supplements:    packageand(emacs:%{name})

%description emacs
ccrypt is a utility for encrypting and decrypting files and streams.
It was designed as a replacement for the standard unix crypt utility,
which is notorious for using a very weak encryption algorithm.

ccrypt is based on the Rijndael cipher, which is the U.S. government's
chosen candidate for the Advanced Encryption Standard (AES, see
http://www.nist.gov/aes). This cipher is believed to provide very strong
security.

This package contains integration with emacs

%lang_package

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install htmldir="%{_docdir}/%{name}"
%find_lang ccrypt

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%{_bindir}/ccrypt
%{_bindir}/ccguess
%{_bindir}/ccat
%{_bindir}/ccencrypt
%{_bindir}/ccdecrypt
%{_mandir}/man1/ccrypt.1%{?ext_man}
%{_mandir}/man1/ccguess.1%{?ext_man}
%{_mandir}/man1/ccat.1%{?ext_man}
%{_mandir}/man1/ccencrypt.1%{?ext_man}
%{_mandir}/man1/ccdecrypt.1%{?ext_man}

%files emacs
%{_datadir}/emacs/site-lisp/ps-ccrypt.el
%{_datadir}/emacs/site-lisp/ps-ccrypt.elc

%files lang -f %{name}.lang

%changelog
