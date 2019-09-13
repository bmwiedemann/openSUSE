#
# spec file for package rtags
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           rtags
Version:        2.22+git.20190304.c4dea899
Release:        0
Summary:        Clang based source code indexer
License:        GPL-3.0-or-later
Group:          Development/Tools/Navigators
Url:            https://github.com/Andersbakken/rtags
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  emacs-nox
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  llvm-clang-devel
BuildRequires:  llvm-devel
BuildRequires:  ncurses-devel

%description
Rtags is Clang based source file indexer supporting C/C++/Objective-C(++) code.

%define _sitedir %{_datadir}/emacs/site-lisp
%define _scriptdir %{_datadir}/rtags/

%prep
%setup -q

%build
export CFLAGS="%{optflags} -Wno-unused-parameter"
export CXXFLAGS="%{optflags} -Wno-unused-parameter"
%cmake \
       -DCURSES_CURSES_LIBRARY:FILEPATH="%{_libdir}/libncurses.so"

make %{?_smp_mflags}

%install
%cmake_install
mkdir -p %{buildroot}%{_sitedir} %{buildroot}%{_scriptdir}
install -m 0755 -t %{buildroot}%{_scriptdir} bin/*.sh
chmod 0755 %{buildroot}%{_bindir}/gcc-rtags-wrapper.sh

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man7/rc.7.gz
%{_mandir}/man7/rdm.7.gz
%{_sitedir}/rtags
%{_scriptdir}
%doc LICENSE.txt README.org

%changelog
