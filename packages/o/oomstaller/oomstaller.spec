#
# spec file for package oomstaller
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           oomstaller
Version:        0.3.0
Release:        0
Summary:        A tool for suppressing swap thrashing at build time
License:        BSL-1.0
URL:            https://github.com/shibatch/oomstaller
Source:         https://github.com/shibatch/oomstaller/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler

%description
Oomstaller is a tool for suppressing swap thrashing at build time. It is
intended for use in build processes of large processes, using parallelism to
make use of available CPUs. It works by monitoring memory usage of each process
when performing a build, and suspends processes as necessary to prevent
swapping from occurring.

%prep
%autosetup -p1

%build
%make_build

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/*
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
