#
# spec file for package opmsg
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           opmsg
Version:        1.77s
Release:        0
Summary:        File encryption, sign and verify utility
License:        GPL-3.0+
Group:          Productivity/Security
Url:            https://github.com/stealth/opmsg
Source0:        https://github.com/stealth/opmsg/archive/rel-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
#BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
opmsg is a replacement for gpg which can encrypt/sign/verify your mails or
create/verify detached signatures of local files. Even though the opmsg
output looks similar, the concept is entirely different.

* Perfect Forward Secrecy (PFS) by means of ECDH or DH Kex.
* Native EC or RSA fallback if no (EC)DH keys left.
* Signing messages is mandatory.
* OTR-like deniable signatures if demanded.
* Support for 1:1 key bindings to auto-select source key per
  destination.
* Adds the possibility to (re-)route messages different from mail
  address to defeat meta data collection.
* Key format suitable for easy use with QR codes.
* Optional cross-domain ECDH Kex.

%prep
%setup -q -n %{name}-rel-%{version}

%build
pushd src
make %{?_smp_mflags} all contrib

%install
pushd src
mkdir -p %{buildroot}/%{_bindir}
install %{name} %{buildroot}/%{_bindir}/%{name}
install opmux %{buildroot}/%{_bindir}/opmux
install opcoin %{buildroot}/%{_bindir}/opcoin
#mkdir -p %{buildroot}/%{_mandir}/man1
#help2man ./%{name} --no-info --output %{buildroot}/%{_mandir}/man1/%{name}.1

%files
%doc README.md LICENSE sample.config GPL3
%{_bindir}/%{name}
%{_bindir}/opmux
%{_bindir}/opcoin
#%{_mandir}/man1/%{name}*

%changelog
