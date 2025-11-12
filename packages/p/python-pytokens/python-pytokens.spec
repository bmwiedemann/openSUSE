#
# spec file for package python-pytokens
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}
Name:           python-pytokens
Version:        0.3.0
Release:        0
Summary:        A Fast, spec compliant Python 3.12+ tokenizer that runs on older Pythons
License:        MIT
URL:            https://github.com/tusharsadhwani/pytokens
Source:         https://files.pythonhosted.org/packages/source/p/pytokens/pytokens-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Fast, spec compliant Python 3.12+ tokenizer that runs on older Pythons.

%prep
%autosetup -p1 -n pytokens-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pytokens
%{python_sitelib}/pytokens-%{version}.dist-info

%changelog
