#
# spec file for package gqlplus
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gqlplus
Version:        1.15
Release:        0
Summary:        A drop-in replacement for sqlplus, an Oracle SQL client
License:        GPL-2.0-only
URL:            https://gqlplus.sourceforge.net/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel

%description
GQLPlus is a drop-in replacement for sqlplus, an Oracle SQL client, for
UNIX and UNIX-like platforms. The difference between GQLPlus and sqlplus is
command-line editing and history, plus table-name and column-name
completion.

%prep
%autosetup

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc ChangeLog README
%{_bindir}/gqlplus

%changelog
