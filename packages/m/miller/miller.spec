#
# spec file for package miller
#
# Copyright (c) 2020 SUSE LLC
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
Version:        5.10.0
Release:        0
Summary:        Name-indexed data processing tool
# c/lib/netbsd_strptime.c is BSD-4-Clause
License:        BSD-2-Clause AND BSD-4-Clause
URL:            http://johnkerl.org/miller/doc
Source0:        https://github.com/johnkerl/miller/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  flex >= 2.5.35
BuildRequires:  libtool

%description
Miller (mlr) allows name-indexed data such as CSV and JSON files to be
processed with functions equivalent to sed, awk, cut, join, sort etc. It can
convert between formats, preserves headers when sorting or reversing, and
streams data where possible so its memory requirements stay small. It works
well with pipes and can feed "tail -f".

%prep
%setup -q
%ifarch %ix86
sed -e 's/-pg//' -i c/Makefile.am
%endif

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
install -Dm0644 docs/mlr.1 %{buildroot}/%{_mandir}/man1/mlr.1

%files
%license LICENSE.txt
%doc README.md c/draft-release-notes.md
%{_bindir}/mlr
%{_mandir}/man1/mlr.1%{ext_man}

%changelog
