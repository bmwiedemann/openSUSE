#
# spec file for package grubby
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


Name:           grubby
Version:        8.40
Release:        0
Summary:        Command line tool for updating bootloader configs
License:        GPL-2.0-or-later
Group:          System/Base
Url:            https://github.com/rhinstaller/grubby.git
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  libblkid-devel
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
# for make test / getopt:
BuildRequires:  grub2
BuildRequires:  util-linux
%ifarch s390 s390x
Requires:       s390utils-base
%endif
%ifarch %{arm}
Requires:       uboot-tools
%endif

%description
grubby is a command line tool for updating and displaying information about 
the configuration files for the grub, lilo, elilo (ia64), yaboot (powerpc)  
and zipl (s390) boot loaders. It is primarily designed to be used from scripts
which install new kernels and need to find information about the current boot 
environment.

%prep
%setup -q

%build
make %{?_smp_mflags}

%ifnarch aarch64
%check
make test
%endif

%install
make install DESTDIR="%{buildroot}" mandir="%{_mandir}"
# Remove installkernel as it is provided with mkinitrd package
rm %{buildroot}/sbin/installkernel
rm %{buildroot}/%{_mandir}/man8/installkernel.8

%files
%defattr(-,root,root,-)
%doc COPYING
/sbin/new-kernel-pkg
/sbin/grubby
%{_mandir}/man8/*.8*

%changelog
