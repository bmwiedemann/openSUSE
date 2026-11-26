#
# spec file for package python-confuse
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-confuse
Version:        2.3.1
Release:        0
Summary:        Painless YAML configuration
License:        MIT
URL:            https://github.com/beetbox/confuse
Source:         https://github.com/beetbox/confuse/archive/refs/tags/v%{version}.tar.gz#/confuse-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
# the test suite imports pytest (pytest.raises) in most modules
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
# upstream pyproject.toml asks for typing_extensions only for python_version < 3.13
Requires:       (python-typing_extensions >= 4.4 if python-base < 3.13)
BuildArch:      noarch
%python_subpackages

%description
Confuse is a configuration library for Python that reads YAML files. It handles
defaults, overrides, type checking, command-line and environment variable
integration, and standard OS-specific configuration locations.

%prep
%setup -q -n confuse-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# upstream tests are written for pytest (pytest.raises with match=)
%pytest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/confuse-%{version}*-info/
%{python_sitelib}/confuse/

%changelog
