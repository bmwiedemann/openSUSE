#
# spec file for package gpa
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gpa
Version:        0.10.0
Release:        0
Summary:        GNU Privacy Assistant
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            http://www.gnupg.org/related_software/gpa/index.html
Source:         ftp://ftp.gnupg.org/gcrypt/gpa/%{name}-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/gpa/%{name}-%{version}.tar.bz2.sig
Source2:        gpa.keyring
Patch0:         gpa-0.10.0-reduce-gpgme-requirement.patch
BuildRequires:  gnupg
BuildRequires:  gpgme-devel >= 1.9.0
BuildRequires:  gtk2-devel >= 2.10.0
BuildRequires:  libassuan-devel >= 2.4.2
BuildRequires:  libgpg-error-devel >= 1.27
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang

%description
Gnu Privacy Assistant (GPA) is a graphical user interface for Gnu
Privacy Guard (GPG) for displaying keyrings, manipulating keys,
checking signatures, and signing, decrypting, and encrypting files.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure \
        --with-gnu-ld
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file -i %{name} Security
%find_lang %{name} %{?no_lang_C}

%check
make %{?_smp_mflags} check

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license COPYING
%doc NEWS TODO THANKS AUTHORS ChangeLog ChangeLog-2011
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/gpa
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gpa/
%{_datadir}/pixmaps/gpa.png

%files lang -f %{name}.lang

%changelog
