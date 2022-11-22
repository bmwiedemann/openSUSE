#
# spec file for package icmake
#
# Copyright (c) 2022 SUSE LLC
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
Version:        10.03.00
Release:        0
Summary:        A program maintenance (make) utility using a C-like grammar
License:        GPL-3.0-only
Group:          Development/Tools/Building
URL:            https://gitlab.com/fbb-git/icmake
Source:         %{URL}/-/archive/%{version}/icmake-%{version}.tar.bz2
Patch1:         prevent-double-slash.patch
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
%setup -q
%patch1 -p1

%build
export CXXFLAGS="%{optflags} -std=c++20"
echo "/* created during rpmbuild */" >  %{name}/INSTALL.im
echo "#define BINDIR      \"%{_bindir}\"" >>  %{name}/INSTALL.im
echo "#define SKELDIR     \"%{_datadir}/%{name}\"" >>  %{name}/INSTALL.im
echo "#define MANDIR      \"%{_mandir}\"" >>  %{name}/INSTALL.im
echo "#define LIBDIR      \"%{_libdir}/%{name}\"" >>  %{name}/INSTALL.im
echo "#define CONFDIR     \"%{_sysconfdir}/%{name}\"" >>  %{name}/INSTALL.im
echo "#define DOCDIR      \"%{_docdir}/%{name}\"" >>  %{name}/INSTALL.im
echo "#define DOCDOCDIR   \"%{_docdir}/%{name}\"" >>  %{name}/INSTALL.im
pushd %{name}
./icm_prepare   "/"
./icm_bootstrap ""
popd

%install
pushd %{name}
./icm_install all %{buildroot}
popd

%files
%doc %{name}/changelog
%doc %{_docdir}/%{name}/
%{_bindir}/icmake
%{_bindir}/icmbuild
%{_bindir}/icmstart
%{_mandir}/man1/icmake.1%{ext_man}
%{_mandir}/man1/icmbuild.1%{ext_man}
%{_mandir}/man1/icmstart.1%{ext_man}
%{_mandir}/man7/icmconf.7%{ext_man}
%{_mandir}/man7/icmstart.rc.7%{ext_man}
%{_mandir}/man7/icmscript.7%{ext_man}
%{_datadir}/icmake
%dir %{_libdir}/icmake
%{_libdir}/icmake/icm-comp
%{_libdir}/icmake/icm-exec
%{_libdir}/icmake/icm-pp
%{_libdir}/icmake/icm-dep
%{_libdir}/icmake/icmun
%{_libdir}/icmake/icmbuild
%{_libdir}/icmake/icmstart.bim
%dir %{_sysconfdir}/icmake
%config %{_sysconfdir}/icmake/icmstart.rc

%changelog
