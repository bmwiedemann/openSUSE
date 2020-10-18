#
# spec file for package openssh-askpass-gnome
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


%define _name openssh
Name:           openssh-askpass-gnome
Version:        8.3p1
Release:        0
Summary:        A GNOME-Based Passphrase Dialog for OpenSSH
License:        BSD-2-Clause
Group:          Productivity/Networking/SSH
URL:            http://www.openssh.com/
Source:         http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{_name}-%{version}.tar.gz
Source42:       http://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{_name}-%{version}.tar.gz.asc
Requires:       %{_name} = %{version}
Supplements:    packageand(openssh-clients:libgtk-3-0)
%if 0%{?suse_version} >= 1550
BuildRequires:  gtk3-devel
%else
BuildRequires:  gtk2-devel
%endif

%description
SSH (Secure Shell) is a program for logging into a remote machine and
for executing commands on a remote machine. This package contains a
GNOME-based passphrase dialog for OpenSSH.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
cd contrib
export CFLAGS="%{optflags}"
%if 0%{?suse_version} >= 1550
%make_build gnome-ssh-askpass3
%else
%make_build gnome-ssh-askpass2
%endif

%install
install -d -m 755 %{buildroot}%{_libexecdir}/ssh/
%if 0%{?suse_version} >= 1550
install contrib/gnome-ssh-askpass3 %{buildroot}%{_libexecdir}/ssh/gnome-ssh-askpass
%else
install contrib/gnome-ssh-askpass2 %{buildroot}%{_libexecdir}/ssh/gnome-ssh-askpass
%endif

%files
%dir %{_libexecdir}/ssh
%attr(0755,root,root) %{_libexecdir}/ssh/gnome-ssh-askpass

%changelog
