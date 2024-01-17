#
# spec file for package ctris
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ctris
Version:        0.42.1
Release:        0
Summary:        Console based Tetris clone
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/dominikhackl/ctris
#Git-Clone:     https://github.com/dominikhackl/ctris.git
Source:         https://github.com/dominikhackl/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
A colorized, small and flexible Tetris clone for the console.

%prep
%setup -q

%build
make CFLAGS="%{optflags} -fcommon" %{?_smp_mflags}

%install
%make_install BINDIR="%{buildroot}%{_bindir}"

%files
%license COPYING
%doc AUTHORS README TODO
%{_mandir}/man6/ctris.6%{?ext_man}
%{_bindir}/ctris

%changelog
