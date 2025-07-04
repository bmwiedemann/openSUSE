#
# spec file for package python-simplebayes
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


Name:           python-simplebayes
Version:        1.5.8
Release:        0
Summary:        A memory-based, optional-persistence naïve bayesian text classifier
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hickeroar/simplebayes
Source:         https://files.pythonhosted.org/packages/source/s/simplebayes/simplebayes-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
A memory-based, optional-persistence naïve bayesian text classifier
heavily inspired by the python "redisbayes" module.

%python_subpackages

%prep
%setup -q -n simplebayes-%{version}

%build
export LANG=C.UTF-8
%pyproject_wheel

%install
export LANG=C.UTF-8
%pyproject_install

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/simplebayes
%{python_sitelib}/simplebayes-%{version}*-info

%changelog
