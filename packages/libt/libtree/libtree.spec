#
# spec file for package libtree
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           libtree
Version:        3.1.1
Release:        0
Summary:        Ldd as a tree
License:        MIT
URL:            https://github.com/haampie/libtree
Source:         https://github.com/haampie/libtree/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Libtree is tool that turns ldd into a tree, and explains how shared libraries
are found or why they cannot be located.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install PREFIX=%{_prefix}

%check
%ifarch x86_64
%make_build check
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%changelog
