#
# spec file for package gpa
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           gpa
Version:        0.11.1
Release:        0
Summary:        GNU Privacy Assistant
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            https://www.gnupg.org/related_software/gpa/index.html
Source:         https://gnupg.org/ftp/gcrypt/gpa/%{name}-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/gpa/%{name}-%{version}.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
Source2:        gpa.keyring
BuildRequires:  gnupg
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error) >= 1.27
BuildRequires:  pkgconfig(gpgme) >= 1.9.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libassuan) >= 2.4.2
BuildRequires:  pkgconfig(zlib)

%description
Gnu Privacy Assistant (GPA) is a graphical user interface for Gnu
Privacy Guard (GPG) for displaying keyrings, manipulating keys,
checking signatures, and signing, decrypting, and encrypting files.

%lang_package

%prep
%autosetup -p1

%build
%configure \
        --with-gnu-ld \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%check
%make_build check

%files
%license COPYING
%doc NEWS TODO THANKS AUTHORS ChangeLog ChangeLog-2011
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/gpa
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gpa/

%files lang -f %{name}.lang
%license COPYING

%changelog
