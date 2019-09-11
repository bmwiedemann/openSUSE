#
# spec file for package cvsps
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           cvsps
BuildRequires:  cmake
BuildRequires:  zlib-devel
Summary:        A Program for Generating Patch Set Information from a CVS Repository
License:        GPL-2.0+
Group:          Development/Tools/Version Control
# DO NOT UPGRADE to 3.x before you make sure it works with git-cvsps [bnc#809800]
Version:        2.1
Release:        0
%define real_version 2.1
Source:         cvsps-%{real_version}.tar.bz2
Source1:        bk-cvs.mail
Source2:        cvsps-bk-cvs.mail
Source3:        fixes.tar.bz2
Source4:        CMakeLists.txt
Obsoletes:      cvsps2 <= %{version}
Provides:       cvsps2 = %{version}
Patch:          commitid.diff
Url:            http://www.cobite.com/cvsps/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CVSps is a program for generating 'patchset' information from a CVS
repository. In this case, a patchset is defined as a set of changes
made to a collection of files, all committed at the same time (using a
single 'cvs commit' command). This information is valuable for seeing
the big picture of the evolution of a CVS project. While CVS tracks
revision information, it is often difficult to see what changes were
'atomically' committed to the repository.



%prep
%setup -q -n cvsps-%{real_version}
tar xvfj %{SOURCE3}
for patch in $(cat fixes/series); do
    patch -p1 < fixes/$patch
done
cp %{SOURCE1} %{SOURCE2} %{SOURCE4} .
%patch -p1

%build
export CFLAGS="%{optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_VERBOSE_MAKEFILE=TRUE .
%{__make} %{?jobs:-j%jobs}

%install
%makeinstall 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGELOG COPYING
%doc bk-cvs.mail cvsps-bk-cvs.mail
%{_bindir}/cvsps
%{_mandir}/man*/*

%changelog
