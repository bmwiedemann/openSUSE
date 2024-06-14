#
# spec file for package python-abseil
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-abseil
Version:        2.1.0
Release:        0
Summary:        Abseil Python Common Libraries
License:        Apache-2.0
URL:            https://github.com/abseil/abseil-py
Source0:        https://github.com/abseil/abseil-py/archive/v%{version}.tar.gz#/abseil-py-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-absl-py = %{version}
Obsoletes:      python-absl-py < %{version}
BuildArch:      noarch
%python_subpackages

%description
This package is a collection of Python library code for building Python
applications. The code is collected from Google's own Python code base, and has
been extensively tested and used in production.
* Simple application startup
* Distributed commandline flags system
* Custom logging module with additional features
* Testing utilities

%prep
%setup -q -n abseil-py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python smoke_tests/sample_app.py --echo smoke 2>&1 |grep 'echo is smoke.'
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python smoke_tests/sample_test.py 2>&1 | grep 'msg_for_test'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/absl
%{python_sitelib}/absl_py-%{version}*-info

%changelog
