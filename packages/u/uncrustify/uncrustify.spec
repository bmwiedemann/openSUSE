#
# spec file for package uncrustify
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           uncrustify
Version:        0.81.0
Release:        0
Summary:        Source Code Beautifier for C, C++, C#, ObjectiveC, D
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++
URL:            https://github.com/uncrustify/uncrustify
Source:         https://github.com/%{name}/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
Source Code Beautifier for C, C++, C#, ObjectiveC, D, Java, Pawn and VALA.

Features:
  * Ident code, aligning on parens, assignments, etc.
  * Align on '=' and variable definitions.
  * Align structure initializers.
  * Align #define stuff.
  * Align backslash-newline stuff.
  * Reformat comments (a little bit).
  * Fix inter-character spacing.
  * Add or remove parens on return statements.
  * Add or remove braces on single-statement if/do/while/for statements.
  * Supports embedded SQL 'EXEC SQL' stuff.
  * Highly configurable - 454 configurable options as of version 0.60.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%define build_args %{nil}
%if 0%{?suse_version} < 1600
%define build_args -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}
%endif
%cmake %{build_args}

%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_docdir}/uncrustify

%files
%doc AUTHORS ChangeLog README.md documentation/* etc
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
