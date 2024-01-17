#
# spec file for package ima-inspect
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ima-inspect
Version:        0.15
Release:        0
Summary:        Output IMA/EVM extended attributes in a human readable format
License:        LGPL-2.1-or-later
Group:          System/Base
URL:            https://github.com/mgerstner/ima-inspect
Source0:        https://github.com/mgerstner/ima-inspect/releases/download/v%{version}/ima-inspect-dist-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  ima-evm-utils-devel
BuildRequires:  tclap

%description
This is a small utility that supplements ima-evm-utils with a way to inspect
the security.ima and security.evm extended attributes in human readable
format.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root,-)
%{_bindir}/ima_inspect

%changelog
