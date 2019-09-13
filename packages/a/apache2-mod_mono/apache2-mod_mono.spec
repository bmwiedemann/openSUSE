#
# spec file for package apache2-mod_mono
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


Name:           apache2-mod_mono
%define apxs /usr/sbin/apxs2
%define apache2_sysconfdir %(%{apxs} -q SYSCONFDIR)/conf.d
Obsoletes:      mod_mono < 2.10
%define modname mod_mono
%define apache2_libexecdir %(%{apxs} -q LIBEXECDIR)
%define apache_mmn        %(MMN=$(%{apxs} -q LIBEXECDIR)_MMN; test -x $MMN && $MMN)
Url:            http://www.mono-project.com/
Version:        3.12
Release:        0
Summary:        Run ASP.NET Pages on Unix with Apache and Mono
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
Source:         http://download.mono-project.com/sources/mod_mono/mod_mono-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       mod_mono = %{version}-%{release}
# This must be manually entered according to xsp's protocol version
Requires:       xsp >= 3.0.11
BuildRequires:  apache2-devel
BuildRequires:  libtool
BuildRequires:  mono-devel
BuildRequires:  pkg-config
Requires:       %{apache_mmn}
Requires:       apache2
BuildRequires:  libapr-util1-devel

%description
mod_mono is a module that interfaces Apache with Mono and allows
running ASP.NET pages on Unix and Unix-like systems. To load the module
into Apache, run the command "a2enmod mono" as root.



%prep
%setup -q -n %{modname}-%{version}

%build
%configure %_with_remove_display --disable-quiet-build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT APXS_SYSCONFDIR="%{apache2_sysconfdir}"

%files
%defattr(-,root,root)
%{apache2_libexecdir}/*
%config %{apache2_sysconfdir}/*
%{_mandir}/man8/mod_mono.8*

%changelog
