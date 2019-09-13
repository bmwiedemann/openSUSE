#
# spec file for package silo
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           silo
Version:        1.4.14+git20
Release:        0
Summary:        Bootloader for SPARC systems
License:        GPL-2.0+
Group:          System/Boot

#Git-Clone:	git://git.kernel.org/pub/scm/linux/kernel/git/davem/silo
#Git-Web:	http://git.kernel.org/?p=linux/kernel/git/davem/silo.git;a=summary
Source:         silo-%version.tar.xz
ExclusiveArch:  sparc sparcv8 sparcv9 sparcv9v
BuildRequires:  elftoaout
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SILO, the Sparc Improved boot LOader, is a booting loader program
that runs from the PROM of SPARC (32-bit) and UltraSPARC (64-bit)
based systems.

%prep
%setup -qn silo

%build
# Also with stupid makefile so we cannot re-set CFLAGS.
make %{?_smp_mflags}

%install
rm -Rf "%buildroot"
mkdir "%buildroot"
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_sysconfdir/silo.conf"

%post
echo "You probably want to run /sbin/silo now."

%files
%defattr(-,root,root)
/boot/*
/sbin/*
%_bindir/*
%_sbindir/*
%doc %_mandir/*/*
%doc etc/silo.conf
%doc COPYING

%changelog
