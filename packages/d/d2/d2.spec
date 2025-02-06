#
# spec file for package d2
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


Name:           d2
Version:        0.6.9
Release:        0
Summary:        CLI tool and modern declarative language that turns text to diagrams
License:        Apache-2.0 AND MIT AND MPL-2.0 AND EPL-2.0 AND GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Text/Utilities
URL:            https://github.com/terrastruct/d2
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.23

%description
A modern declarative diagramming language that turns text to diagrams. Create
beautiful diagrams in minutes. Simple syntax. Endlessly customizable. D2 is the
fastest and easiest way to get a mental model from your head onto the screen,
then make edits with your team.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}

%changelog
