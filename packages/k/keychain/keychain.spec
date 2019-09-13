#
# spec file for package keychain
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


Name:           keychain
Version:        2.8.5
Release:        0
Summary:        A Key Management Application for SSH2 RSA/DSA and GnuPG Keys
License:        GPL-2.0+
Group:          Productivity/Security
Url:            http://www.funtoo.org/Keychain
Source:         https://github.com/funtoo/keychain/archive/2.8.5.tar.gz#/%{name}-%{version}.tar.gz
Requires:       bash
Requires:       coreutils
Requires:       openssh
Requires:       sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version} == 0
BuildRequires:  gpg2
Requires:       gpg2
%else
BuildRequires:  gpg
Requires:       gpg
%endif

%description
Keychain is an extremely handy OpenSSH, commercial SSH2-compatible
RSA/DSA and GnuPG key management application. It acts as a front-end to
the agents, allowing you to easily have one long-running agent process
per system, rather than per login session. This dramatically reduces
the number of times you need to enter your pass phrase from once per
new login session to once every time your local machine is rebooted.

%prep
%setup -q

%build
# Nothing to build

%install
install -D -m0755 keychain "%{buildroot}/%{_bindir}/keychain"
install -D -m0644 keychain.1 "%{buildroot}/%{_mandir}/man1/keychain.1"

%files
%defattr(-,root,root)
%doc ChangeLog README.md COPYING.txt
%{_bindir}/keychain
%{_mandir}/man1/keychain.1%{ext_man}

%changelog
