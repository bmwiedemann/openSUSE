#
# spec file for package openssh-askpass-gnome
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


%define _name openssh
Name:           openssh-askpass-gnome
Version:        10.2p1
%define wrongly_named_version 10.2p1
Release:        0
Summary:        A GNOME-Based Passphrase Dialog for OpenSSH
License:        BSD-2-Clause
Group:          Productivity/Networking/SSH
URL:            https://www.openssh.com/
Source0:        https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{_name}-%{wrongly_named_version}.tar.gz
Source1:        https://ftp.openbsd.org/pub/OpenBSD/OpenSSH/portable/%{_name}-%{wrongly_named_version}.tar.gz.asc
Requires:       %{_name}-clients = %{version}
Supplements:    packageand(openssh-clients:gcr)
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(gcr-4)
%else
BuildRequires:  gtk2-devel
%endif

%description
SSH (Secure Shell) is a program for logging into a remote machine and
for executing commands on a remote machine. This package contains a
GNOME-based passphrase dialog for OpenSSH.

%prep
%autosetup -p1 -n %{_name}-%{wrongly_named_version}

%build
cd contrib
export CFLAGS="%{optflags}"
%if 0%{?suse_version} >= 1550
%make_build gnome-ssh-askpass4
%else
%make_build gnome-ssh-askpass2
%endif

%install
install -d -m 755 %{buildroot}%{_libexecdir}/ssh/
%if 0%{?suse_version} >= 1550
install contrib/gnome-ssh-askpass4 %{buildroot}%{_libexecdir}/ssh/gnome-ssh-askpass
%else
install contrib/gnome-ssh-askpass2 %{buildroot}%{_libexecdir}/ssh/gnome-ssh-askpass
%endif

%files
%dir %{_libexecdir}/ssh
%attr(0755,root,root) %{_libexecdir}/ssh/gnome-ssh-askpass

%changelog
