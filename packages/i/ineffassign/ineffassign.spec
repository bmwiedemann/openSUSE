#
# spec file for package ineffassign
#
# Copyright (c) 2021 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           ineffassign
Version:        0.0.0+git20210225.2e10b26
Release:        0
Summary:        Tool to detect ineffectual assignments in Go code
License:        MIT
URL:            https://github.com/gordonklaus/ineffassign
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  golang(API) >= 1.14

%description
This tool misses some cases because does not consider any type information in
its analysis. (For example, assignments to struct fields are never marked as
ineffectual.) It should, however, never give any false positives.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -buildmode=pie ;

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%defattr(-,root,root)
%doc README.md
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%{_bindir}/%{name}

%changelog
