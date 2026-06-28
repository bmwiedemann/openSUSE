#
# spec file for package python-moreorless
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-moreorless
Version:        0.6.0
Release:        0
Summary:        Python diff wrapper
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thatch/moreorless/
Source:         https://files.pythonhosted.org/packages/source/m/moreorless/moreorless-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 65}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest >= 8}
# /SECTION
%python_subpackages

%description
Python diff wrapper.

%prep
%setup -q -n moreorless-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/moreorless
%{python_sitelib}/moreorless-%{version}.dist-info

%changelog
