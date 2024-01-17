#
# spec file for package python-vcver
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-vcver
Version:        0.2.12
Release:        0
Summary:        Provide package versions with version control data
License:        MIT
URL:            https://github.com/toumorokoshi/vcver-python
Source:         https://files.pythonhosted.org/packages/source/v/vcver/vcver-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/toumorokoshi/vcver-python/master/LICENSE
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging
BuildArch:      noarch
%python_subpackages

%description
Python module to provide package versions with version control data.

%prep
%setup -q -n vcver-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_happy_case wants to be run from git repo, which we obviously don't have
# test_child_directory_detected_as_git_repo same as the test_happy_case
%pytest -k 'not test_happy_case and not test_child_directory_detected_as_git_repo'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
