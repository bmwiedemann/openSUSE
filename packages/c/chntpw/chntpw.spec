#
# spec file for package chntpw
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

%define         dateversion 140201
Name:           chntpw
Version:        1.0
Release:        0
Summary:        Offline NT Password and Registry Editor
License:        GPL-2.0 and LGPL-2.1
Group:          System/Management
Url:            http://pogostick.net/~pnh/ntpasswd/
Source:         http://pogostick.net/~pnh/ntpasswd/chntpw-source-%{dateversion}.zip
# PATCH-FIX-UPSTREAM chntpw_1.0-1.diff.gz -- use all patches from debian, fixes build and runtime bugs
Patch0:         http://http.debian.net/debian/pool/main/c/chntpw/chntpw_%{version}-1.diff.gz
BuildRequires:  libgcrypt-devel
BuildRequires:  unzip

%description
A utility to reset the password of any user that has a valid local account on your Windows system.
Supports all Windows from NT3.5 to Win8.1, also 64 bit and also the Server versions (like 2003, 2008, 2012)
You do not need to know the old password to set a new one.
It works offline, that is, you have to shutdown your computer and boot off a CD or USB disk to do the password reset.
Will detect and offer to unlock locked or disabled out user accounts.
There is also a registry editor and other registry utilities that works under linux/unix, and can be used for other things than password editing. 

%prep
%setup -qn %{name}-%{dateversion}
%patch0 -p1
while read line; do
    [ "${line#\#}"x = "${line}x" ] && echo "Applying patch $line" && /usr/bin/patch --no-backup-if-mismatch -p1 --fuzz=0 < "debian/patches/$line"
done < debian/patches/series

%build
make %{?_smp_mflags} CFLAGS="-DUSELIBGCRYPT $(shell libgcrypt-config --cflags) -g -I. -Wall $(EXTRA_CFLAGS) %{optflags}" chntpw cpnt reged samusrgrp sampasswd

%install
install -Dm 755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 755 cpnt %{buildroot}%{_bindir}/
install -m 755 reged %{buildroot}%{_bindir}/
install -m 755 sampasswd %{buildroot}%{_bindir}/
install -m 755 samusrgrp %{buildroot}%{_bindir}/

install -Dm 644 debian/%{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%doc README.txt HISTORY.txt
%license COPYING.txt GPL.txt LGPL.txt
%{_bindir}/%{name}
%{_bindir}/cpnt
%{_bindir}/reged
%{_bindir}/samusrgrp
%{_bindir}/sampasswd
%{_mandir}/man8/%{name}.8%{ext_man}

%changelog

