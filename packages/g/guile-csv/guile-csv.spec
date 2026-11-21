#
# spec file for package guile-csv
#
# Copyright (c) 2026 SUSE LLC
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


Name:           guile-csv
Version:        0.0.5
Release:        0
Summary:        CSV reader for GNU Guile
# Legal-Review-Notice: csv/csv.scm headers say LGPL-3.0-or-later while COPYING carries GPL-3.0 and pkg-list.scm GPL-3.0-or-later; dual tag covers the shipped sources.
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/NalaGinrut/guile-csv
Source0:        https://github.com/NalaGinrut/guile-csv/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  guile
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(guile-3.0)
Requires:       guile

%description
Guile-csv is a CSV reader for GNU Guile. It provides a reader
parametrised by delimiter, conversion of CSV data to SXML, and writing
SXML back out as CSV.

%prep
%autosetup

%build
guild compile -L . -o csv/csv.go csv/csv.scm

%install
GUILE_VER=$(guile -c '(display (effective-version))')
mkdir -p %{buildroot}%{_datadir}/guile/site/$GUILE_VER/csv
mkdir -p %{buildroot}%{_libdir}/guile/$GUILE_VER/site-ccache/csv
install -m 644 csv/csv.scm %{buildroot}%{_datadir}/guile/site/$GUILE_VER/csv/csv.scm
install -m 644 csv/csv.go %{buildroot}%{_libdir}/guile/$GUILE_VER/site-ccache/csv/csv.go

%files
%license COPYING
%doc AUTHORS README README.md
%dir %{_datadir}/guile/site/*
%{_datadir}/guile/site/*/csv*
%dir %{_libdir}/guile/*/site-ccache
%{_libdir}/guile/*/site-ccache/csv*

%changelog
