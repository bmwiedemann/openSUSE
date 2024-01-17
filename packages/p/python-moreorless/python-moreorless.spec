#
# spec file for package python-moreorless
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
%define skip_python2 1
Name:           python-moreorless
Version:        0.4.0
Release:        0
Summary:        Python diff wrapper
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thatch/moreorless/
Source:         https://files.pythonhosted.org/packages/source/m/moreorless/moreorless-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  (python3-dataclasses if python3-base < 3.7)
BuildRequires:  (python36-dataclasses if python36-base)
Requires:       python-click
Requires:       python-volatile
%if 0%{?python_version_nodots} < 37
Requires:       python-dataclasses
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module volatile}
# /SECTION
%python_subpackages

%description
Python diff wrapper.

%prep
%setup -q -n moreorless-%{version}
sed -i '/parameterized/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest moreorless/tests/[a-z]*.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
