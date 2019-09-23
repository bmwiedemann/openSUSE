#
# spec file for package python-pytest-travis-fold
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pytest-travis-fold
Version:        1.3.0
Release:        0
Summary:        Pytest plugin to fold captured output sections in Travis CI build log
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/abusalimov/pytest-travis-fold
Source:         https://github.com/abusalimov/pytest-travis-fold/archive/v1.3.0.tar.gz#/pytest-travis-fold-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.6.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 2.6.0}
BuildRequires:  %{python_module pytest-runner}
# /SECTION
%python_subpackages

%description
Pytest plugin that folds captured output sections in Travis CI build log.

In addition, pytest-travis-fold recognizes presence of the pytest-cov plugin
and folds coverage reports accordingly.

%prep
%setup -q -n pytest-travis-fold-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_travis_fixture_registered wrongly compares in new releases
#   upstream has no commits since 2014, just skip it
%pytest -k 'not test_travis_fixture_registered'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
