#
# spec file for package python-retrying
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
Name:           python-retrying
Version:        1.3.4
Release:        0
Summary:        Retrying library for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/rholder/retrying
Source:         https://files.pythonhosted.org/packages/source/r/retrying/retrying-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.7.0
BuildArch:      noarch
%python_subpackages

%description
Retrying is a general-purpose retrying library, written in Python, to
simplify the task of adding retry behavior to just about anything.

%prep
%setup -q -n retrying-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python_sitelib}/*

%changelog
