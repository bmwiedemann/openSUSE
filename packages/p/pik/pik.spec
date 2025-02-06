#
# spec file for package pik
#
# Copyright (c) 2024 mantarimay
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


%bcond_without test
Name:           pik
Version:        0.15.0
Release:        0
Summary:        Process Interactive Kill
License:        MIT
URL:            https://github.com/jacek-kurlit/pik
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Process Interactive Kill is a command line tool that helps to find and kill
process. It works like pkill command but search is interactive.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%if %{with test}
%check
%{cargo_test}
%endif

%files
%license LICEN*
%doc README*
%{_bindir}/%{name}

%changelog
