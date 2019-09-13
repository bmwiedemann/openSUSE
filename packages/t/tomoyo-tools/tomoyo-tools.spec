#
# spec file for package tomoyo-tools
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define downloadver 2.5.0-20140601
Name:           tomoyo-tools
Version:        2.5.0.20140601
Release:        0
Summary:        Userspace tools for TOMOYO Linux 2.4.x
License:        GPL-2.0
Group:          Development/Tools/Other
Url:            http://sourceforge.jp/projects/tomoyo/
Source0:        http://osdn.dl.sourceforge.jp/tomoyo/53357/tomoyo-tools-%{downloadver}.tar.gz
Source1:        http://osdn.dl.sourceforge.jp/tomoyo/53357/tomoyo-tools-%{downloadver}.tar.gz.asc
# http://i-love.sakura.ne.jp/kumaneko-key
Source2:        %name.keyring
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains userspace tools for administrating TOMOYO Linux 2.4.
Please see http://tomoyo.sourceforge.jp/2.4/ for documentation.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags} USRLIBDIR=%{_libdir} CFLAGS="-Wall %{optflags}"

%install
make INSTALLDIR=%{buildroot} USRLIBDIR=%{_libdir} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc COPYING.tomoyo README.tomoyo
%attr(700,root,root) /sbin/tomoyo-init
%{_libdir}/lib*.so*
%dir %{_libdir}/tomoyo
%{_libdir}/tomoyo/*
%{_sbindir}/*
%{_mandir}/man8/*

%changelog
