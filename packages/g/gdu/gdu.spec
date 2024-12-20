#
# spec file for package gdu
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gdu
Version:        5.29.0
Release:        0
Summary:        Fast disk usage analyzer with console interface
License:        MIT
URL:            https://github.com/dundee/gdu
Source:         https://github.com/dundee/gdu/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zstd
BuildRequires:  gzip
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.20

%description
Fast disk usage analyzer with console interface. Gdu is intended
primarily for SSD disks where it can fully utilize parallel
processing. HDDs work as well, but the performance gain is not so
huge.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build ./cmd/%{name}

# compress upstream provided man page
gzip %{name}.1

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m0755 -s %{name} %{buildroot}%{_bindir}/%{name}
install -D -m0644 %{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
