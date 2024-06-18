#
# spec file for package cdecl
#
# Copyright (c) 2024 SUSE LLC
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


Name:           cdecl
Version:        17.0.1
Release:        0
Summary:        C/C++ function declaration translator
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            https://github.com/paul-j-lucas/cdecl/

Source:         https://github.com/paul-j-lucas/cdecl/releases/download/cdecl-%version/cdecl-%version.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel

%description
Cdecl is a program which will turn English-like phrases such as
"declare foo as array 5 of pointer to function returning int" into C
declarations such as "int (*foo[5])()" and vice-versa. It handles
typecasts and C++ as well, and offers command line editing and
history.

%prep
%autosetup -p1

%build
%configure

%install
%make_install

%files
%_bindir/*
%_mandir/*/*
%_datadir/*sh*
%license COPYING

%changelog
