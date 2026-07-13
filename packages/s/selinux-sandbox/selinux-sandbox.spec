#
# spec file for package selinux-sandbox
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


Name:           selinux-sandbox
Version:        3.11
Release:        0
Summary:        SELinux sandbox helper
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/SELinuxProject/selinux/wiki
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        selinux-sandbox.keyring
Source3:        SANDBOX-README.md
# PATCH-FEATURE-OPENSUSE sandbox_seunshare_move_usr_bin.patch bsc#1268256
Patch1:         sandbox_seunshare_move_usr_bin.patch
# PATCH-FEATURE-NOT-SUBMITTED sandbox-fix-cleanup.patch https://bugzilla.redhat.com/show_bug.cgi?id=2481569
Patch10:        sandbox-fix-cleanup.patch
BuildRequires:  libcap-ng-devel
BuildRequires:  libselinux-devel
Requires:       selinux-policy-sandbox
Requires(pre):  permissions
Requires(post): %fillup_prereq
Recommends:     (xwayland or xorg-x11-server-extra)
Suggests:       xwayland
Provides:       policycoreutils-sandbox = %{version}
Obsoletes:      policycoreutils-sandbox < %{version}

%description
Run an application within a tightly confined SELinux domain. The default
sandbox domain only allows applications the ability to read and write stdin,
stdout and any other file descriptors handed to it.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
%make_build LIBDIR="%{_libdir}"

%install
# we are forcing seunshare into /usr/bin because bsc#1268256
%make_install SBINDIR="%{_bindir}"
mkdir %{buildroot}%{_fillupdir}/
mv %{buildroot}%{_sysconfdir}/sysconfig/sandbox %{buildroot}%{_fillupdir}/sysconfig.sandbox
cp -a %{SOURCE3} .
%find_lang selinux-sandbox

%post
%{fillup_only -n sandbox}
%set_permissions %{_bindir}/seunshare

%verifyscript
%verify_permissions -e %{_bindir}/seunshare

%files
%doc SANDBOX-README.md
%attr(755,root,root) %{_bindir}/seunshare
%{_bindir}/sandbox
%{_mandir}/man5/sandbox.5%{?ext_man}
%{_mandir}/man8/sandbox.8%{?ext_man}
%{_mandir}/man8/seunshare.8%{?ext_man}
%{_datadir}/sandbox/sandboxX.sh
%{_datadir}/sandbox/start
%{_fillupdir}/sysconfig.sandbox
%dir %{_datadir}/sandbox

%files lang -f %{name}.lang
%{_datadir}/locale/*/LC_MESSAGES/selinux-sandbox.mo

%changelog
