#
# spec file for package pam_ssh
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pam_ssh
Version:        2.3
Release:        0
Summary:        PAM Module for SSH Authentication
License:        BSD-3-Clause
Group:          Productivity/Networking/SSH
URL:            http://sourceforge.net/projects/pam-ssh/
Source:         http://sourceforge.net/projects/pam-ssh/files/pam_ssh/%{version}/%{name}-%{version}.tar.xz
Source1:        http://sourceforge.net/projects/pam-ssh/files/pam_ssh/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        baselibs.conf
Source3:        %{name}.keyring
BuildRequires:  libtool
BuildRequires:  openssh
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This module provides single sign-on behavior. The user types a
passphrase when logging in and is allowed in if it decrypts the user s
SSH private key. An ssh-agent is started and keys are added. For the
entire session, the user types no more passwords.

%prep
%setup -q

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fno-strict-aliasing -fcommon"
%configure --libdir=/%{_lib}
make %{?_smp_mflags}

%install
install -d 755 %{buildroot}/%{_lib}/security
install -m 755 .libs/pam_ssh.so %{buildroot}/%{_lib}/security
install -d 755 %{buildroot}%{_mandir}/man8
install -m 644 pam_ssh.8 %{buildroot}%{_mandir}/man8/

%files
%defattr(444,root,root,755)
%doc README TODO NEWS
%attr(555,root,root) /%{_lib}/security/pam_ssh.so
%attr(444,root,root) %{_mandir}/man*/*.*

%changelog
