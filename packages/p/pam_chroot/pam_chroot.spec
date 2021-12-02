#
# spec file for package pam_chroot
#
# Copyright (c) 2021 SUSE LLC
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


%define _buildshell /bin/bash

Name:           pam_chroot
URL:            http://sourceforge.net/projects/pam-chroot/
BuildRequires:  pam-devel
Requires:       pam
Provides:       pam-modules:/etc/security/chroot.conf
Version:        0.9.2
Release:        0
Summary:        Linux-PAM Module that Allows a User to Be Chrooted
License:        GPL-2.0-or-later
Group:          System/Libraries
Source0:        pam_chroot-0.9.2.tar.bz2
Source1:        baselibs.conf
Source50:       dlopen.sh
Patch1:         pam_chroot-0.9.2.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policies without
having to recompile programs that do authentication.

pam_chroot is a Linux-PAM module that allows a user to be chrooted in
auth, account, or session.



Authors:
--------
    Matthew Kirkwood (weejock@ferret.lmh.ox.ac.uk)
    Ed Schmollinger (schmolli@frozencrow.org)

%prep
%setup  
%patch1
cp options README

%build
EXTRA_CFLAGS=""
%ifnarch ia64
    EXTRA_CFLAGS="$EXTRA_CFLAGS -Wa,--noexecstack"
%endif
make CFLAGS="$RPM_OPT_FLAGS $EXTRA_CFLAGS -fPIC -DHAVE_SHADOW -DLINUX_PAM"

%install
mkdir -p %{buildroot}%{_pam_moduledir}
make DESTDIR=%{buildroot} install
[[ X"%{_pam_moduledir}" =~ X/lib.*/security/* ]] || mv %{buildroot}/lib/security/* %{buildroot}%{_pam_moduledir}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root,755)
%doc CREDITS LICENSE README TROUBLESHOOTING 
%attr(644,root,root) %config(noreplace) /etc/security/chroot.conf
%attr(755,root,root) /%{_pam_moduledir}/pam_*.so

%changelog
