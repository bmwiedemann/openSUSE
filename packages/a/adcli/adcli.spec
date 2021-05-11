#
# spec file for package adcli
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


%define filehash 30880d967e79cee789194435e70fbf30
%define sighash 1075c948917caa32464c15ec9b6c5caf
Name:           adcli
Version:        0.9.1
Release:        0
Summary:        Tool for performing actions on an Active Directory domain
License:        LGPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://gitlab.freedesktop.org/realmd/adcli
Source0:        https://gitlab.freedesktop.org/sbose/adcli/uploads/%{filehash}/%{name}-%{version}.tar.gz
Source2:        https://gitlab.freedesktop.org/sbose/adcli/uploads/%{sighash}/%{name}-%{version}.tar.gz.sig
# https://keys.openpgp.org/vks/v1/by-fingerprint/4A21C23848CDC107F487939849236C40EE9D57EB
Source3:        %{name}.keyring
BuildRequires:  libxslt-tools
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(mit-krb5)

%description
A command line tool that can perform actions in an Active Directory domain.
Among other things it can be used to join a computer to a domain.

%package doc
Summary:        Documentation for adcli
Group:          Documentation/Other
BuildArch:      noarch

%description doc
A command line tool that can perform actions in an Active Directory domain.
Among other things it can be used to join a computer to a domain.

This package contains the documentation for adcli.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-silent-rules \
	--enable-strict
%make_build

%install
%make_install
# Remove zero-length file.
rm %{buildroot}/%{_datadir}/doc/%{name}/adcli-docs.proc

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_sbindir}/%{name}
%{_mandir}/man8/adcli.8%{?ext_man}

%files doc
%license COPYING
%doc %{_datadir}/doc/%{name}

%changelog
