#
# spec file for package progress
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           progress
Version:        0.14
Release:        0
Summary:        Coreutils Viewer
License:        GPL-3.0-or-later
Group:          System/Console
URL:            https://github.com/Xfennec/progress
Source0:        https://github.com/Xfennec/progress/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         progress-fix_ncurses_without_pkgconfig.patch
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
Provides:       cv = %{version}
Obsoletes:      cv < %{version}

%description
This tool can be described as a Tiny Dirty Linux Only* C command that looks for coreutils basic
commands (cp, mv, dd, tar, gzip/gunzip, cat, ...) currently running on your system and displays
the percentage of copied data.

It can now also display an estimated throughput (using -w flag).

%prep
%setup -q
%patch1

%build
make %{?_smp_mflags} CFLAGS="-g -Wall -D_FILE_OFFSET_BITS=64 %{optflags}"

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
