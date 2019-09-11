#
# spec file for package delta
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           delta
Version:        2006.08.03
Release:        0
Summary:        Minimize files to interesting parts
License:        BSD-3-Clause
Group:          Development/Tools/Other
Url:            http://delta.tigris.org/
Source:         http://delta.tigris.org/files/documents/3103/33566/%{name}-%{version}.tar.gz
Patch0:         delta-documentation.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Delta assists you in minimizing "interesting" files subject to a test
of their interestingness. A common such situation is when attempting to
isolate a small failure-inducing substring of a large input that causes
your program to exhibit a bug. Please see
%{_docdir}/delta/www/using_delta.html for documentation.

%prep
%setup -q
%patch0
find . -type f -print0|xargs -0 chmod -x
chmod +x delta multidelta test1_multidelta/testit test1_multidelta/trivtest test0_delta/hello.test

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_prefix}/bin
install delta multidelta topformflat %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%%doc Readme www
%{_bindir}/delta
%{_bindir}/multidelta
%{_bindir}/topformflat

%changelog
