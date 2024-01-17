#
# spec file for package kbuild
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


%define _svnrev 3427
Name:           kbuild
Version:        0.1.9998svn%{_svnrev}
Release:        0
Summary:        Framework for writing simple makefiles for complex tasks
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://svn.netlabs.org/kbuild
Source0:        %{name}-%{version}.tar.bz2
Patch0:         kbuild-man.diff
Patch2:         kbuild-dummy_noreturn.diff
Patch5:         kbuild-pthread.diff
Patch6:         kbuild-timestamps.diff
Patch7:         kbuild-armv7l.diff
Patch8:         kbuild-wrong-memset.patch
Patch9:         ppc64le.patch
Patch10:        aarch64.patch
Patch13:        glob-lstat.patch
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  libacl-devel
BuildRequires:  makeinfo
BuildRequires:  readline-devel

%description
The goals of the kBuild framework:

 - Similar behavior across all supported platforms
 - Flexibility, don't create unnecessary restrictions preventing ad-hoc
   solutions
 - Makefiles can be simple to write and maintain
 - One configuration file for a subtree automatically included
 - Target configuration templates as the primary mechanism for makefile
   simplification
 - Tools and SDKs for helping out the templates with flexibility
 - Non-recursive makefile method by using sub-makefiles

%prep
%setup -q
%patch0
%patch2
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch13 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
cat > SvnInfo.kmk << EOF
KBUILD_SVN_REV := %{_svnrev}
KBUILD_SVN_URL := http://svn.netlabs.org/repos/kbuild/trunk
EOF
kBuild/env.sh --full make -f bootstrap.gmk SRCDIR=`pwd`
kBuild/env.sh kmk rebuild PATH_INS=`pwd`
pod2man -c 'kBuild for SUSE Linux' -r kBuild-%{version} kmk.pod > kmk.1

%install
kBuild/env.sh kmk NIX_INSTALL_DIR=%{_prefix} BUILD_TYPE=release PATH_INS=%{buildroot} LDFLAGS=-Wl,--as-needed install
install -m 644 -D kmk.1 %{buildroot}/%{_mandir}/man1/kmk.1
#remove execute flag, if occurs
chmod a-x %{buildroot}/%{_datadir}/kBuild/*/*kmk
rm -r %{buildroot}%{_datadir}/doc/kBuild-0.1.9998

%files
%license COPYING
%license kBuild/doc/COPYING-FDL-1.3
%doc ChangeLog
%doc kBuild/doc/QuickReference-kmk.*
%{_bindir}/*
%{_mandir}/man1/kmk.1%{?ext_man}
%{_datadir}/kBuild

%changelog
