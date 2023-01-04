#
# spec file for package mawk
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2010 Guido Berhoerster.
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


%define _upver 1.3.4
%define _datever 20200120
Name:           mawk
Version:        %{_upver}.%{_datever}
Release:        0
Summary:        Implementation of New/POSIX AWK
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://invisible-island.net/mawk/mawk.html
Source0:        ftp://ftp.invisible-island.net/mawk/mawk-%{_upver}-%{_datever}.tgz
Source1:        ftp://ftp.invisible-island.net/mawk/mawk-%{_upver}-%{_datever}.tgz.asc
Source2:        %{name}.keyring
# PATCH-FIX-OPENSUSE -- bmwiedemann -- drop timestamp / for build-compare
Patch0:         reproducible.patch

%description
mawk is an interpreter for the AWK Programming Language. It implements the AWK
language as defined in Aho, Kernighan and Weinberger, The AWK  Programming
Language, Addison-Wesley Publishing, 1988. Furthermore, it conforms to the
POSIX 1003.2 (draft 11.3) definition of the AWK language and additionally
provides a small number of extensions.

%prep
%setup -q -n mawk-%{_upver}-%{_datever}
%patch0 -p1
chmod 755 examples/*

%build
# without --enable-warnings several functions will not be marked with gcc's
# noreturn attribute and produce warnings when $RPM_OPT_FLAGS contains -Wall
%configure \
  --enable-warnings
%make_build

%install
%make_install

%if 0%{?suse_version} < 1550
# compatibility symlink
install -d -m 755 %{buildroot}/bin
ln -s %{_bindir}/mawk %{buildroot}/bin/mawk
%endif

%check
%make_build check

%files
%license COPYING
%doc ACKNOWLEDGMENT CHANGES README examples/
%{_bindir}/mawk
%{_mandir}/man1/mawk.1%{?ext_man}
%if 0%{?suse_version} < 1550
/bin/mawk
%endif

%changelog
