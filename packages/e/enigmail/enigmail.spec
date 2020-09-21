#
# spec file for package enigmail
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014 Wolfgang Rosenauer <wr@rosenauer.org>
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


Name:           enigmail
Version:        2.1.8
Release:        0
Summary:        OpenPGP addon for Mozilla Thunderbird
License:        MPL-2.0
URL:            https://www.enigmail.net/
# git clone git://git.code.sf.net/p/enigmail/source enigmail
Source0:        https://www.enigmail.net/download/source/%{name}-%{version}.tar.gz
Source1:        https://www.enigmail.net/download/source/%{name}-%{version}.tar.gz.asc
# https://www.enigmail.net/documentation/pgp-key.php
Source2:        enigmail.keyring
BuildRequires:  fdupes
BuildRequires:  perl >= 5
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  zip
Requires:       gpg2 >= 2.0.7
Requires:       pinentry-gui

%description
This package contains the Enigmail OpenPGP Addon for Mozilla Thunderbird.

%prep
%setup -q -n enigmail

%build
%configure
make # %{?_smp_mflags}

%install
# Thunderbird location
_enig_dir=%{buildroot}%{_libdir}/mozilla/extensions/\{3550f703-e582-4d05-9a08-453d09bdfdc6\}/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
mkdir -p $_enig_dir
(cd $_enig_dir; unzip $RPM_BUILD_DIR/enigmail/build-tb/enigmail-*.xpi)
#rm $_enig_dir/*.xpi
%fdupes %{buildroot}

mkdir -p %{buildroot}%{_datadir}/appdata/
install -m644 public/thunderbird-enigmail.metainfo.xml %{buildroot}%{_datadir}/appdata/enigmail.appdata.xml

%files
%license LICENSE
%{_libdir}/mozilla/
%dir %{_datadir}/appdata
%{_datadir}/appdata/enigmail.appdata.xml

%changelog
