#
# spec file for package cgdb
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


Name:           cgdb
Version:        0.7.1
Release:        0
Summary:        Curses debugger
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://cgdb.github.io/
Source0:        https://cgdb.me/files/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  makeinfo
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
Requires:       gdb
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
CGDB is a curses (terminal-based) interface to the GNU Debugger (GDB). Its goal
is to be lightweight and responsive; not encumbered with unnecessary features.

The primary feature of CGDB is the constant presence of a source display,
updated as the program executes, to help keep you focused while debugging. The
interface is inspired by the classic Unix text editor, vi. Those familiar with
vi (or vim) should feel right at home using CGDB.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.txt
%{_infodir}/%{name}.info%{ext_info}
%{_datadir}/%{name}

%changelog
