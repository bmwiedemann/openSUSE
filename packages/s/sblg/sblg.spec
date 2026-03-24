#
# spec file for package sblg
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           sblg
Version:        0.6.1
Release:        0
Summary:        Static blog utility
License:        ISC
URL:            https://kristaps.bsd.lv/sblg/
Source:         https://github.com/kristapsdz/sblg/archive/refs/tags/VERSION_0_6_1.tar.gz
BuildRequires:  gcc
BuildRequires:  libexpat-devel
BuildRequires:  make

%description
sblg is a utility for creating static blogs. It merges articles into templates, generating static HTML files, Atom feeds, and JSON files. It's built for use with make-style build environments.

%package doc
Summary:        Static blog utility
BuildArch:      noarch

%description doc
Examples and documentation for sblg.

%prep
%autosetup -p1 -n sblg-VERSION_0_6_1

%build
# doesn't use autotools
./configure PREFIX=%{_prefix} MANDIR=%{_mandir} SHAREDIR=%{_docdir} LDFLAGS="${LDFLAGS}"
%make_build

%install
%make_install

%check
%make_build regress

%files
%license LICENSE.md
%{_bindir}/sblg
%{_mandir}/man1/sblg.1%{?ext_man}

%files doc
%license LICENSE.md
%{_docdir}/sblg/

%changelog
