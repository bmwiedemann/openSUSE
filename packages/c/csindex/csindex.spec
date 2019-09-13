#
# spec file for package csindex
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           csindex
Summary:        Utility for creating Czech or Slovak Sorted LaTeX Index Files
License:        MakeIndex
Group:          Productivity/Publishing/TeX/Utilities
Version:        19980713
Release:        0
Source:         %{name}-%{version}.tar.bz2
Source1:        COPYING
Url:            ftp://ftp.fi.muni.cz/pub/localization/csindex/
Patch:          %{name}-%{version}.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program creates Czech and Slovak sorted index files for LaTeX.
Usage: csindex -z il2 file.idx Creates file.ind - a sorted index file.
Uses the ISO 8859-2 encoding.

%prep
%setup
install -m 644 %{SOURCE1} .
%patch

%build
make CC="gcc $RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -c -m 0755 csindex $RPM_BUILD_ROOT/usr/bin

%files
%defattr(-,root,root,-)
%doc README COPYING
/usr/bin/csindex

%changelog
