#
# spec file for package deheader
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           deheader
Version:        1.11
Release:        0
Summary:        Find and optionally remove unneeded includes in C or C++ sourcefiles
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/deheader/
Source:         http://www.catb.org/~esr/deheader/%{name}-%{version}.tar.gz
BuildRequires:  xmlto
BuildRequires:  python-rpm-macros
BuildArch: noarch

%description
deheader analyzes C and C++ files to determine which header inclusions can be
removed while still allowing them to compile. This may result in substantial
improvements in compilation time, especially on large C++ projects; it also
sometimes exposes dependencies and cohesions of which developers were unaware.

%prep
%autosetup -p1

%build
%make_build

%install
%make_build install \
	DESTDIR=%{buildroot} \
	prefix=%{_prefix} \
	%{nil}
%python3_fix_shebang

%files
%license COPYING
%doc NEWS.adoc README
%{_bindir}/deheader
%{_mandir}/man1/deheader.1%{?ext_man}

%changelog
