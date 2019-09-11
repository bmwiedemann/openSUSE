#
# spec file for package enigmail
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        2.1.2
Release:        0
Summary:        OpenPGP addon for Thunderbird and SeaMonkey
License:        MPL-2.0
Group:          Productivity/Networking/Email/Clients
URL:            https://www.enigmail.net/
# git clone git://git.code.sf.net/p/enigmail/source enigmail
Source0:        https://www.enigmail.net/download/source/%{name}-%{version}.tar.gz
Source1:        https://www.enigmail.net/download/source/%{name}-%{version}.tar.gz.asc
# https://www.enigmail.net/documentation/pgp-key.php
Source2:        enigmail.keyring
BuildRequires:  perl >= 5
BuildRequires:  python >= 2.7
BuildRequires:  unzip
BuildRequires:  zip
Requires:       gpg2 >= 2.0.7
Requires:       pinentry-gui

%description
This package contains the Enigmail OpenPGP Addon for Thunderbird and SeaMonkey.

%prep
%setup -q -n enigmail

%build
# FIXME: you should use the %%configure macro
./configure \
	CFLAGS="%{optflags}"
# parallel build not supported
make # %{?_smp_mflags}

%install
# Thunderbird location
_enig_dir=%{buildroot}%{_libdir}/mozilla/extensions/\{3550f703-e582-4d05-9a08-453d09bdfdc6\}/\{847b3a00-7ab1-11d4-8f02-006008948af5\}
mkdir -p $_enig_dir
(cd $_enig_dir; unzip $RPM_BUILD_DIR/enigmail/build/enigmail-*.xpi)
#rm $_enig_dir/*.xpi
# SeaMonkey location
mkdir -p %{buildroot}%{_libdir}/mozilla/extensions/\{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a\}
(cd %{buildroot}%{_libdir}/mozilla/extensions/\{92650c4d-4b8e-4d2a-b7eb-24ecf4f6b63a\}; \
  ln -s ../\{3550f703-e582-4d05-9a08-453d09bdfdc6\}/\{847b3a00-7ab1-11d4-8f02-006008948af5\} )

mkdir -p %{buildroot}%{_datadir}/appdata/
install -m644 public/thunderbird-enigmail.metainfo.xml %{buildroot}%{_datadir}/appdata/enigmail.appdata.xml

%files
%license LICENSE
%{_libdir}/mozilla/
%dir %{_datadir}/appdata
%{_datadir}/appdata/enigmail.appdata.xml

%changelog
