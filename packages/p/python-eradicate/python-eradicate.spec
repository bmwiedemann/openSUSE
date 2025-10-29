#
# spec file for package python-eradicate
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


%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-eradicate
Version:        3.0.1
Release:        0
Summary:        Python utility for removing commented-out code
License:        MIT
URL:            https://github.com/myint/eradicate
Source:         https://files.pythonhosted.org/packages/source/e/eradicate/eradicate-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
With modern revision control available, there is no reason to save
commented-out code to your repository. "eradicate" helps cleans up
existing junk comments. It does this by detecting block comments that
contain valid Python syntax that are likely to be commented out code.
(It avoids false positives like the sentence "this is not good",
which is valid Python syntax, but is probably not code.)

%prep
%setup -q -n eradicate-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/eradicate

%pre
%python_libalternatives_reset_alternative eradicate

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/eradicate
%{python_sitelib}/eradicate.py
%pycache_only %{python_sitelib}/__pycache__/eradicate*.pyc
%{python_sitelib}/eradicate-%{version}.dist-info

%changelog
