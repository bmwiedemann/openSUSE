#
# spec file for package python-nose-cov
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without  test
Name:           python-nose-cov
Version:        1.6
Release:        0
Summary:        Nose plugin for coverage reporting
License:        MIT
Group:          Development/Languages/Python
URL:            http://bitbucket.org/memedough/nose-cov/overview
Source:         https://files.pythonhosted.org/packages/source/n/nose-cov/nose-cov-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cov-core >= 1.6
Requires:       python-nose >= 0.11.4
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module cov-core >= 1.6}
BuildRequires:  %{python_module nose >= 0.11.4}
%endif
%python_subpackages

%description
This plugin produces coverage reports.  It also supports coverage of subprocesses.

All features offered by the coverage package should be available, either through nose-cov or
through coverage's config file.

%prep
%setup -q -n nose-cov-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.txt
%{python_sitelib}/*

%changelog
