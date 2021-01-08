#
# spec file for package python-pygments-pytest
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pygments-pytest
Version:        2.2.0
Release:        0
Summary:        A pygments lexer for pytest output
License:        MIT
URL:            https://github.com/asottile/pygments-pytest
Source:         https://github.com/asottile/pygments-pytest/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pygments-ansi-color >= 0.0.3}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest >= 4.0.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygments
Requires:       python-pytest >= 4.0.1
BuildArch:      noarch
%python_subpackages

%description
This library provides a pygments lexer called "pytest".

%prep
%setup -q -n pygments-pytest-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
