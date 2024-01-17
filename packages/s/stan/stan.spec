#
# spec file for package stan
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


Name:           stan
Version:        0.4.1
Release:        0
Summary:        Stream Analyzer
License:        BSD-4-Clause
Group:          System/Console
Url:            http://www.roqe.org/stan
Source:         %{name}-%{version}.tar.gz
Patch1:         %{name}-0.4_add-errno.diff
Patch2:         stan-0.4-optflags.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Stan is a small console application that works on all UNIX systems. It
is able to generate several types of statistical information about a
stream. A stream can be either standard input or given files. For
example, stan can be used to analyze encrypted data or to measure the
quality of a pseudo-random number generator, but there are probably
hundreds of other situations where stan comes in handy.

Stan supports three types of analysis: general statistics, pattern
statistics, and bit statistics. By choosing intelligent values for each
statistic, stan can give amazing results about a stream and is fun to
work with.

%prep
%setup -q
%patch1 -p1
%patch2

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/stan
%{_mandir}/man1/stan.1%{ext_man}

%changelog
