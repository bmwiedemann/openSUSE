#
# spec file for package xortool
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


%define pythons python3
Name:           xortool
Version:        1.0.0
Release:        0
Summary:        A tool to analyze multi-byte xor cipher
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/hellman/xortool
Source:         https://github.com/hellman/xortool/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       %{python_module docopt}
BuildArch:      noarch

%description
A tool to do some xor analysis:
 * Guess the key length (based on count of equal chars).
 * Guess the key (base on knowledge of most frequent char).

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install

%files
%doc README.md
%{_bindir}/%{name}*
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*

%changelog
