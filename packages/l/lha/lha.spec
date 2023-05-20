#
# spec file for package lha
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


Name:           lha
Version:        1.14.1~git.20230329
Release:        0
Summary:        Pack Program
License:        SUSE-Public-Domain
URL:            http://lha.sourceforge.jp/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
# Conflict with another lha implementation:
Conflicts:      lhasa

%description
Lha is a packer comparable to ZIP (PKZIP), ZOO, and others. It has been
included for compatibility reasons only. Use GZIP for general archiving
purposes, because it is the standard for Linux.

%prep
%autosetup

%build
autoreconf -fiv
%configure\
  --enable-multibyte-filename=utf8\
  --with-additional-suffixes=lha
%make_build

%install
%make_install

%check
%make_build check

%files
%{_bindir}/lha
%{_mandir}/man1/lha.1%{?ext_man}

%changelog
