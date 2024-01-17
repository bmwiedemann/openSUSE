#
# spec file for package pam_ssh
#
# Copyright (c) 2022 SUSE LLC
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
Source4:        pam_ssh.tmpfiles
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
%configure
make %{?_smp_mflags}

%install
install -d 755 %{buildroot}/%{_pam_moduledir}
install -m 755 .libs/pam_ssh.so %{buildroot}/%{_pam_moduledir}
install -d 755 %{buildroot}%{_mandir}/man8
install -m 644 pam_ssh.8 %{buildroot}%{_mandir}/man8/
install -Dm0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/%{name}.conf

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%files
%defattr(444,root,root,755)
%doc README TODO NEWS
%{_tmpfilesdir}/%{name}.conf
%attr(555,root,root) /%{_pam_moduledir}/pam_ssh.so
%attr(444,root,root) %{_mandir}/man*/*.*

%changelog
