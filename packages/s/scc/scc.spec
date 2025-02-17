#
# spec file for package scc
#
# Copyright (c) 2025 SUSE LLC
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


%define shortname sccount

Name:           scc
Version:        3.5.0
Release:        0
Summary:        CLI tool to report lines of code and other metrics
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/boyter/scc
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.24

%description
A tool similar to cloc, sloccount and tokei. For counting physical the lines of
code, blank lines, comment lines, and physical lines of source code in many
programming languages.

Binary name is sccount to avoid conflict with the Steam game controller driver.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build -o %{shortname}

%check
# execute the binary as a basic check
./%{shortname} --help

%install
install -D -m 0755 %{shortname} "%{buildroot}/%{_bindir}/%{shortname}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{shortname}

%changelog
