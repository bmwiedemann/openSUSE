#
# spec file for package miller
#
# Copyright (c) 2022 SUSE LLC
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


Name:           miller
Version:        6.6.0+git20230101.7495a8845
Release:        0
Summary:        Name-indexed data processing tool
# c/lib/netbsd_strptime.c is BSD-4-Clause
License:        BSD-2-Clause AND BSD-4-Clause
Group:          Productivity/Text/Utilities
URL:            http://johnkerl.org/miller/doc
Source0:        https://github.com/johnkerl/miller/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Patch0:         buildmode-pie.diff
#BuildRequires:  golang
BuildRequires:  golang-packaging
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
# Switched to a golang build sometime after 5.10.3
#BuildRequires:  automake
#BuildRequires:  flex >= 2.5.35
#BuildRequires:  libtool

%description
Miller (mlr) allows name-indexed data such as CSV and JSON files to be
processed with functions equivalent to sed, awk, cut, join, sort etc. It can
convert between formats, preserves headers when sorting or reversing, and
streams data where possible so its memory requirements stay small. It works
well with pipes and can feed "tail -f".

%prep
%setup -q -a 1
%if "%{_arch}" != "ppc64"
%patch0
%endif
# Not sure if this is still required
#%%ifarch %%ix86
#sed -e 's/-pg//' -i c/Makefile.am
#%%endif

%build
%make_build

%install
%make_install PREFIX=%{_prefix}
# Add provided example.csv
cp -v %{_builddir}/%{name}-%{version}/docs/src/example.csv %{_builddir}/%{name}-%{version}

%files
%license LICENSE.txt
%doc README.md example.csv
%{_bindir}/mlr
%{_mandir}/man1/mlr.1%{ext_man}

%changelog
