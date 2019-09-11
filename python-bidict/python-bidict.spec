#
# spec file for package python-bidict
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
Name:           python-bidict
Version:        0.18.0
Release:        0
Summary:        Bidirectional map implementation for Python
License:        MPL-2.0
Group:          Development/Languages/Python
Url:            https://github.com/jab/bidict
Source:         https://files.pythonhosted.org/packages/source/b/bidict/bidict-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 3.6.1}
BuildRequires:  %{python_module pytest >= 3.0.7}
BuildRequires:  %{python_module pytest-benchmark >= 3.1.0a1}
BuildRequires:  %{python_module sortedcollections >= 0.4.2}
BuildRequires:  %{python_module sortedcontainers >= 1.5.5}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Bidirectional map implementation and related functionality.

%prep
%setup -q -n bidict-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
%python_install
export LANG=en_US.UTF-8
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_expand py.test-%{$python_bin_suffix}

%files %{python_files}
%doc CHANGELOG.rst README.rst docs/*.rst
%license LICENSE
%{python_sitelib}/*

%changelog
