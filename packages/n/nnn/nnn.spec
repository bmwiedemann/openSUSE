#
# spec file for package nnn
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


Name:           nnn
Version:        3.2
Release:        0
Summary:        Terminal based file browser
License:        BSD-2-Clause
Group:          Productivity/File utilities
URL:            https://github.com/jarun/nnn#nnn
Source0:        https://github.com/jarun/nnn/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
%if 0%{?leap_version} == 420300
BuildRequires:  ncurses-devel
%else
BuildRequires:  pkgconfig(ncursesw)
%endif
Recommends:     sshfs

%description
nnn is a fork of noice, a terminal file browser with keyboard
shortcuts for navigation, opening files and running tasks. There is
no config file and MIME associations are hard-coded.

%prep 
%setup -q 

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md CHANGELOG
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
