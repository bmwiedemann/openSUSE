#
# spec file for package ytree
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


Name:           ytree
Version:        2.09
Release:        0
Summary:        A filemanager similar to XTree
License:        GPL-2.0-only
Group:          Productivity/File utilities
URL:            https://www.han.de/~werner/ytree.html
Source:         https://www.han.de/~werner/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel

%description
ytree is a (curses-based) file manager similar to DOS XTree.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build

%install
install -D -m0644 ytree.1 %{buildroot}/%{_mandir}/man1/ytree.1
install -D -m0755 ytree %{buildroot}/%{_bindir}/ytree

%files
%license COPYING
%doc CHANGES README THANKS
%doc ytree.conf
%{_bindir}/ytree
%{_mandir}/man1/ytree.1%{?ext_man}

%changelog
