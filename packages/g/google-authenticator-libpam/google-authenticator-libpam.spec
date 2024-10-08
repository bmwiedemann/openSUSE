#
# spec file for package google-authenticator-libpam
#
# Copyright (c) 2024 SUSE LLC
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
