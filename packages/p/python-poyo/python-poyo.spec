#
# spec file for package python-poyo
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
%bcond_without test
Name:           python-poyo
Version:        0.5.0
Release:        0
Summary:        YAML Parser for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hackebrot/poyo
Source:         https://files.pythonhosted.org/packages/source/p/poyo/poyo-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
A YAML Parser for Python.

Please note that Poyo supports only a chosen subset of the YAML format.

It can only read but not write and is not compatible with JSON.

Poyo does not allow deserialization of arbitrary Python objects. Supported
types are str, bool, int, float, NoneType as well as dict and list values.

%prep
%setup -q -n poyo-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix}
}
%endif

%files %{python_files}
%license LICENSE
%doc CHANGES.md COMMUNITY.md CONTRIBUTING.md README.md
%{python_sitelib}/*

%changelog
