#
# spec file for package bsdiff
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bsdiff
Version:        4.3
Release:        0
Summary:        Tools for binary file patches
License:        BSD-2-Clause
Group:          Productivity/File utilities
Url:            http://daemonology.net/bsdiff
Source:         http://daemonology.net/bsdiff/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE bsdiff-fix-makefile.patch sor.alexei@meowr.ru
Patch0:         %{name}-fix-makefile.patch
# PATCH-FIX-UPSTREAM bsdiff-fix-heap-vul.patch bsc#990660 -- Fix heap vulnerability in bspatch (CVE-2014-9862).
Patch1:         %{name}-fix-heap-vul.patch
BuildRequires:  libbz2-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
bsdiff and bspatch are tools for building and applying patches to
binary files. By using suffix sorting (specifically, Larsson and
Sadakane's qsufsort) and taking advantage of how executable files
change, bsdiff routinely produces binary patches 50-80%% smaller
than those produced by Xdelta, and 15%% smaller than those produced
by .RTPatch.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
head -n 25 %{name}.c > COPYING

%build
make %{?_smp_mflags} \
  CFLAGS="%{optflags}"

%install
%make_install \
  PREFIX=%{_prefix}

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/%{name}
%{_bindir}/bspatch
%{_mandir}/man1/*.1%{?ext_man}

%changelog
