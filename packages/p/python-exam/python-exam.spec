#
# spec file for package python-exam
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-exam
Version:        0.10.6
Release:        0
Summary:        Helpers for better testing
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/fluxx/exam
Source:         https://files.pythonhosted.org/packages/source/e/exam/exam-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Fluxx/exam/master/LICENSE
# https://github.com/Fluxx/exam/pull/50
Patch0:         remove_nose.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
%ifpython2
Requires:       python-mock
%endif
Recommends:     python-pep8
Recommends:     python-pyflakes
BuildArch:      noarch

%python_subpackages

%description
Exam is a Python toolkit for writing better tests. 
It aims to remove a lot of the boiler plate testing
code one often writes, while still following Python
conventions and adhering to the unit testing interface.

%prep
%setup -q -n exam-%{version}
%patch0 -p1
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -s tests/ -v
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
