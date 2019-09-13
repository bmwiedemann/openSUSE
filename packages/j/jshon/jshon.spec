#
# spec file for package jshon
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015, Martin Hauke <mardnh@gmx.de>
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


Name:           jshon
Version:        20131105
Release:        0
Summary:        A JSON parser for the shell
License:        MIT
Group:          Productivity/Text/Utilities
URL:            http://kmkeen.com/jshon
#Git-Clone:     https://github.com/keenerd/jshon.git
Source:         https://github.com/keenerd/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         jshon-fix-install-permissions.diff
Patch1:         0001-check-for-a-error-on-file-open-with-F-option.patch
Patch2:         0001-Fix-Makefile-typo.patch
Patch3:         0001-Fix-null-termination-in-read_stream.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(jansson)

%description
Jshon parses, reads and creates JSON. It is usable from within the
shell and can replace adhoc parsers made from grep/sed/awk as well as
one-line parsers made from perl/python.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%{_bindir}/jshon
%{_mandir}/man1/jshon.1%{?ext_man}

%changelog
