#
# spec file for package python-sklearn-crfsuite
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


%define pyname sklearn-crfsuite
%define pyname_ sklearn_crfsuite
%{?sle15_python_module_pythons}
Name:           python-%{pyname}
Version:        0.5.0
Release:        0
Summary:        CRFsuite wrapper which provides interface simlar to scikit-learn
License:        MIT
URL:            https://github.com/TeamHG-Memex/%{pyname}
Source:         https://files.pythonhosted.org/packages/source/s/%{pyname_}/%{pyname_}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# We can't use python_module here, because the name contains python, so do it manually
Requires:       %{python_flavor}-python-crfsuite
Requires:       python-scikit-learn
Requires:       python-tabulate
Requires:       python-tqdm
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-crfsuite}
BuildRequires:  %{python_module sklearn}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module tqdm}
# /SECTION
%python_subpackages

%description
sklearn-crfsuite is a thin CRFsuite (python-crfsuite) wrapper which provides interface simlar
to scikit-learn. sklearn_crfsuite.CRF is a scikit-learn compatible estimator: you can use e.g.
scikit-learn model selection utilities (cross-validation, hyperparameter optimization) with it,
or save/load CRF models using joblib.

%prep
%autosetup -n %{pyname_}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/%{pyname_}
%{python_sitelib}/%{pyname_}-%{version}.dist-info

%changelog
