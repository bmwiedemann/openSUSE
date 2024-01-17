#
# spec file for package meson-tools
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


Name:           meson-tools
Version:        0.1
Release:        0
Url:            https://github.com/afaerber/meson-tools
Summary:        Utilities for Amlogic SoCs
License:        GPL-2.0+ AND MIT
Group:          System/Boot
Source0:        https://github.com/afaerber/meson-tools/archive/v%{version}.tar.gz#/meson-tools-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libopenssl-devel
BuildRequires:  pkg-config

%description
Utilities for working with Amlogic "Meson" SoCs

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="$(pkg-config --cflags openssl) %{optflags}" \
                    LDFLAGS="$(pkg-config --libs   openssl)"

%install
install -D -m 755 amlbootsig %{buildroot}%{_bindir}/amlbootsig
install -D -m 755 unamlbootsig %{buildroot}%{_bindir}/unamlbootsig
install -D -m 755 amlinfo %{buildroot}%{_bindir}/amlinfo

%files
%defattr(-,root,root)
%doc COPYING README.md
%{_bindir}/amlbootsig
%{_bindir}/unamlbootsig
%{_bindir}/amlinfo

%changelog

