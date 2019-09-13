#
# spec file for package filebench
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


Name:           filebench
Version:        1.4.9.1
Release:        0
Summary:        File system and storage benchmark
License:        CDDL-1.0
Group:          System/Benchmark
Url:            https://github.com/filebench/filebench/wiki
Source0:        https://github.com/filebench/filebench/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.1
Patch0:         make-dofile-global.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex

%description
Filebench is a file system and storage benchmark that allows to generate a
large variety of workloads. Unlike typical benchmarks it is very flexible and
allows to minutely specify (any) applications' behaviour using extensive
Workload Model Language (WML). Filebench uses loadable workload personalities
to allow easy emulation of complex applications (e.g., mail, web, file, and
database servers). Filebench is quick to set up and easy to use compared to
deploying real applications. It is also a handy tool for micro-benchmarking.

%prep
%setup -q
%patch0

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING LICENSE NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
