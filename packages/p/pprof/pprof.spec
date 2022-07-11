#
# spec file for package pprof
#
# Copyright (c) 2022 SUSE LLC
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


Name:           pprof
Version:        0.0.0+git20220520.d04f242
Release:        0
Summary:        CLI tool for visualization and analysis of profiling data
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://github.com/google/pprof
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.14

%description
pprof reads a collection of profiling samples in profile.proto format and generates reports to visualize and help analyze the data.
It can generate both text and graphical reports (through the use of the dot visualization package).

%prep
%autosetup -a1

%build
go build

%install
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md CONTRIBUTORS CONTRIBUTING.md AUTHORS
%license LICENSE
%{_bindir}/%{name}

%changelog
