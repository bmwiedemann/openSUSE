#
# spec file for package par
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


Name:           par
Version:        1.1
Release:        0
Summary:        Parity Archive File Generator
License:        GPL-2.0-or-later
URL:            https://parchive.sourceforge.net/
Source:         https://sourceforge.net/projects/parchive/files/par/%{version}/par-v%{version}.tar.gz/download#/par-v%{version}.tar.gz
Patch0:         %{name}.diff
BuildRequires:  gcc
BuildRequires:  make

%description
Parchive creates extra parity data over several volumes. These can be
used to restore the complete archive after some data loss or
corruption.

%prep
%autosetup -p0 -n %{name}-cmdline

%build
%make_build

%install
%make_install

%files
%doc README AUTHORS NEWS
%license COPYING
%{_bindir}/par

%changelog
