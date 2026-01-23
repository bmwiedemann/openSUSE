#
# spec file for package add
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           add
Version:        20250914
Release:        0
Summary:        Fixed-point calculator that operates as a full-screen editor
License:        MIT
URL:            https://invisible-island.net/add/add.html
Source:         https://invisible-island.net/archives/add/add-%{version}.tgz
Source2:        https://invisible-island.net/archives/add/add-%{version}.tgz.asc
# https://invisible-island.net/public/public.html
# https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc
Source3:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncursesw)

%description
add is a fixed-point calculator that operates as a full-screen editor. It is
designed for use as a checkbook or expense-account balancing tool.

add maintains a running result for each operation. You may scroll to any
position in the expression list and modify the list. Enter data by typing
numbers (with optional decimal point), separated by operators.

An output transcript may be saved and reloaded for further editing.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc CHANGES README MANIFEST
%{_bindir}/add
%{_mandir}/man1/add.1%{?ext_man}
/usr/share/add.hlp

%changelog
