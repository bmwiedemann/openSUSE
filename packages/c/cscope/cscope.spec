#
# spec file for package cscope
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cscope
Version:        15.8b
Release:        0
Summary:        Interactive Tool for Browsing C Source Code
License:        BSD-3-Clause
Group:          Development/Tools/Navigators
Url:            http://cscope.sourceforge.net/
Source:         http://sourceforge.net/projects/cscope/files/cscope/%{version}/%{name}-%{version}.tar.gz
Patch1:         cscope-null.patch
Patch2:         cscope-15.7-gcc-warnings.patch
Patch3:         cscope-15.7-vpath.patch
Patch4:         cscope-15.8a-fix-bashisms.patch
Patch5:         cscope-cleanup_on_sigterm.patch
Patch6:         cscope-egrep.out.patch
Patch7:         support-fun-as-params.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cscope is an interactive, screen-oriented tool that allows the user to
browse through C source code files for specified elements of code.

%prep
%setup -q
%patch1 -p1
%patch2
%patch3
%patch4 -p1
%patch5
%patch6 -p1
%patch7 -p1

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 src/cscope %{buildroot}%{_bindir}/cscope
install -m 644 doc/cscope.1 %{buildroot}%{_mandir}/man1/cscope.1
install -m 755 contrib/xcscope/cscope-indexer %{buildroot}%{_bindir}/cscope-indexer
pushd contrib
%make_install
popd

%files
%defattr(-,root,root)
%doc TODO COPYING ChangeLog AUTHORS README NEWS
%{_mandir}/man1/cscope.1%{ext_man}
%{_bindir}/cscope
%{_bindir}/ocs
%{_bindir}/cscope-indexer

%changelog
