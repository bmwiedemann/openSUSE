#
# spec file for package python-vcversioner
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


%{?sle15_python_module_pythons}
Name:           python-vcversioner
Version:        2.16.0.0
Release:        0
Summary:        setup.py extension for deriving versions from SCM tags
License:        ISC
URL:            https://github.com/habnabit/vcversioner
Source0:        https://files.pythonhosted.org/packages/source/v/vcversioner/vcversioner-%{version}.tar.gz
# https://github.com/habnabit/vcversioner/issues/13
Source1:        https://raw.githubusercontent.com/habnabit/vcversioner/%{version}/COPYING
# https://github.com/habnabit/vcversioner/issues/13
Source2:        https://raw.githubusercontent.com/habnabit/vcversioner/%{version}/test_vcversioner.py
Source9:        %{name}-rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
A setup.py file can be written with no version information
specified, and vcversioner will find a recent, properly-formatted
VCS tag and extract a version from it.

%prep
%setup -q -n vcversioner-%{version}
cp %{SOURCE1} %{SOURCE2} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/vcversioner.py
%pycache_only %{python_sitelib}/__pycache__/vcversioner.*.pyc
%{python_sitelib}/vcversioner-%{version}.dist-info

%changelog
