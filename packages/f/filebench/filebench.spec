#
# spec file for package filebench
#
# Copyright (c) 2023 SUSE LLC
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


Name:           filebench
Version:        1.4.9.1+git.20200220
Release:        0
Summary:        File system and storage benchmark
License:        CDDL-1.0
URL:            https://github.com/filebench/filebench/wiki
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.1
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool

%description
Filebench is a file system and storage benchmark that allows to generate a
large variety of workloads. Unlike typical benchmarks it is very flexible and
allows to minutely specify (any) applications' behaviour using extensive
Workload Model Language (WML). Filebench uses loadable workload personalities
to allow easy emulation of complex applications (e.g., mail, web, file, and
database servers). Filebench is quick to set up and easy to use compared to
deploying real applications. It is also a handy tool for micro-benchmarking.

%prep
%autosetup

%build
mkdir m4
autoreconf -fiv
%configure \
  --enable-static=no
%make_build

%install
%make_install
install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_mandir}/man1/%{name}.1
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
