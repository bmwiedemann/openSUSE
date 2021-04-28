#
# spec file for package apache2-mod_mono
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


%define modname mod_mono
Name:           apache2-mod_mono
Version:        3.13
Release:        0
Summary:        Run ASP.NET Pages on Unix with Apache and Mono
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://www.mono-project.com/docs/web/mod_mono/
Source:         http://download.mono-project.com/sources/%{modname}/%{name}-%{version}.tar.gz
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  libapr-util1-devel
BuildRequires:  libtool
BuildRequires:  mono-devel
BuildRequires:  pkgconfig
Requires:       %{apache_mmn}
Requires:       apache2
# This must be manually entered according to xsp's protocol version
Requires:       xsp >= 3.0.11
Obsoletes:      mod_mono < 2.10
Provides:       mod_mono = %{version}-%{release}

%description
mod_mono is a module that interfaces Apache with Mono and allows
running ASP.NET pages on Unix and Unix-like systems. To load the module
into Apache, run the command "a2enmod mono" as root.

%prep
%setup -q -n %{modname}-%{version}

%build
%configure %{_with_remove_display} --disable-quiet-build
%make_build

%install
make install DESTDIR=%{buildroot} APXS_SYSCONFDIR="%{apache_sysconfdir}"

%files
%license COPYING
%{apache_libexecdir}/*
%config %{apache_sysconfdir}/*
%{_mandir}/man8/mod_mono.8%{?ext_man}

%changelog
