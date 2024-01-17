#
# spec file for package jtc
#
# Copyright (c) 2020 SUSE LLC
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


%define tag_name LatestBuild
Name:           jtc
Version:        1.76d
Release:        0
Summary:        JSON processing utility
License:        MIT
URL:            https://github.com/ldn-softdev/jtc
Source0:        %{URL}/archive/%{tag_name}.tar.gz#/%{name}-%{version}.tar.gz
# Full C++14 support added with version 5
BuildRequires:  gcc-c++ >= 5

%description
jtc stand for: JSON transformational chains (used to be JSON test console).

jtc offers a powerful way to select one or multiple elements from a source JSON
and apply various actions on the selected elements at once (wrap selected
elements into a new JSON, filter in/out, sort elements, update elements, insert
new elements, remove, copy, move, compare, transform, swap around and many other
operations).

%prep
%autosetup -n %{name}-%{tag_name}

%build
g++ -std=gnu++14 %{build_cxxflags} -pthread -lpthread %{name}.cpp -o %{name}

%install
install -Dpm 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md
%doc "User Guide.md"
%doc "Walk-path tutorial.md"

%changelog
