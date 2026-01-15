#
# spec file for package python-eval_type_backport
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


Name:           python-eval-type-backport
Version:        0.3.1
Release:        0
Summary:        `typing._eval_type` for older Python versions
License:        MIT
URL:            https://github.com/alexmojaki/eval_type_backport
Source:         https://files.pythonhosted.org/packages/source/e/eval_type_backport/eval_type_backport-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
Like `typing._eval_type`, but lets older Python versions use newer typing features.

%prep
%autosetup -p1 -n eval_type_backport-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/eval_type_backport
%{python_sitelib}/eval_type_backport-%{version}.dist-info

%changelog
