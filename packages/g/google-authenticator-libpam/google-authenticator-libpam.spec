#
# spec file for package google-authenticator-libpam
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


Name:           google-authenticator-libpam
Version:        1.10
Release:        0
Summary:        Google Authenticator PAM module
License:        Apache-2.0
Group:          Productivity/Security
URL:            https://github.com/google/google-authenticator-libpam
Source:         %{name}-%{version}.tar.xz
Source99:       baselibs.conf
Patch0:         a0b6cf1f022f987d21d3d9c597e9f7f9759968ba.patch
Patch1:         2a1f725e83d3ffc11d229543c4c2980dffd637b9.patch
Patch2:         75151df21a19e7182c09ae0118379fae890bdf5b.patch
Patch3:         267cbfa31bc17805c4850afd39788d97a7b5374c.patch
Patch4:         6313ae4c2b475e1b73fd272434089cfc4631e14d.patch
Patch5:         665012cf90acadac882db4738b21b7246965ee2a.patch
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  pam-devel
# libqrencode.so.[234] are dynamically loaded if present in order to show a QR code
# As the library is not linked, it can't be auto-detected. And as it's not mandatory,
# we recommend it only
Recommends:     (libqrencode4 or libqrencode3 or libqrencode2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       pam-google-authenticator = %{version}
Obsoletes:      pam-google-authenticator < %{version}

%description
Integrate GOOGLE Authenticator into your login process for full 2FA.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
./bootstrap.sh
%configure \
    --docdir=%{_docdir}/%{name} \
    --libdir=$(dirname %{_pam_moduledir})
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print

%check
make test

%files
%defattr(-,root,root)
%doc CONTRIBUTING.md README.md totp.html FILEFORMAT
%license LICENSE
%{_pam_moduledir}/pam_google_authenticator.so
%{_bindir}/google-authenticator
%{_mandir}/man1/google-authenticator.1%{?ext_man}
%{_mandir}/man8/pam_google_authenticator.8%{?ext_man}

%changelog
