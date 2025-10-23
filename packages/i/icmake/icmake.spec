#
# spec file for package icmake
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           icmake
Version:        13.00.01
Release:        0
Summary:        A program maintenance (make) utility using a C-like grammar
License:        GPL-3.0-only
Group:          Development/Tools/Building
URL:            https://gitlab.com/fbb-git/icmake
Source:         %{URL}/-/archive/%{version}/icmake-%{version}.tar.bz2
Patch:          fix-lib-path-for-builds-file.patch
# FIXED-UPSTREAM
Patch:          fix-spch-process.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libbobcat-light-devel-static

%description
Icmake allows the programmer to use a program language (closely
resembling the well-known C-programming language) to define the
actions involved in (complex) program maintenance. For this, icmake
offers various special operators as well as a set of support functions
that have proven to be useful in program maintenance.

%prep
%autosetup -p1

%build
export CXXFLAGS="%{optflags} -std=c++2b -g"
export ICMAKE_CPPSTD="${CXXFLAGS}"
_bindir=%{_bindir}
_datadir=%{_datadir}
_mandir=%{_mandir}
_libdir=%{_libdir}
_sysdir=%{_sysconfdir}
_docdir=%{_docdir}
{
    echo "/* created during rpmbuild */"
    echo "#define BINDIR      \"${_bindir:1}\""
    echo "#define SKELDIR     \"${_datadir:1}/%{name}\""
    echo "#define MANDIR      \"${_mandir:1}\""
    echo "#define LIBDIR      \"${_libdir:1}/%{name}\""
    echo "#define CONFDIR     \"${_sysdir:1}/%{name}\""
    echo "#define DOCDIR      \"${_docdir:1}/%{name}\""
} > %{name}/INSTALL.im
pushd %{name}
./prepare "/"
./buildlib "/"
./build all
popd

%install
pushd %{name}
./install strip all %{buildroot}
popd

%files
%doc %{name}/changelog
%doc %{_docdir}/%{name}/
%{_bindir}/icmake
%{_bindir}/icmbuild
%{_bindir}/icmodmap
%{_bindir}/icmstart
%{_mandir}/man1/icmake.1%{ext_man}
%{_mandir}/man1/icmbuild.1%{ext_man}
%{_mandir}/man1/icmodmap.1%{ext_man}
%{_mandir}/man1/icmstart.1%{ext_man}
%{_mandir}/man7/icmconf.7%{ext_man}
%{_mandir}/man7/icmstart.rc.7%{ext_man}
%{_mandir}/man7/icmscript.7%{ext_man}
%{_datadir}/icmake
%dir %{_libdir}/icmake
%{_libdir}/icmake/icm-comp
%{_libdir}/icmake/icm-dep
%{_libdir}/icmake/icm-exec
%{_libdir}/icmake/icm-multicomp
%{_libdir}/icmake/icm-pp
%{_libdir}/icmake/icm-spch
%{_libdir}/icmake/icm-un
%{_libdir}/icmake/icmbuild
%{_libdir}/icmake/icmstart.bim
%dir %{_sysconfdir}/icmake
%config %{_sysconfdir}/icmake/icmstart.rc

%changelog
