#
# spec file for package python-moretools
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
Name:           python-moretools
Version:        0.1.12
Release:        0
Summary:        MORE Overly Reusable Essentials for Python
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/zimmermanncode/moretools
Source:         https://files.pythonhosted.org/packages/source/m/moretools/moretools-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm >= 3.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zetup >= 0.2.60}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator >= 4.4.0
Requires:       python-six >= 1.12
Requires:       python-zetup >= 0.2.60
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module decorator >= 4.4.0}
BuildRequires:  %{python_module pytest >= 4.6.2}
BuildRequires:  %{python_module six >= 1.12}
# /SECTION
%python_subpackages

%description
Many more basic tools for python extending
itertools, functools, operator and collections

%prep
%setup -q -n moretools-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license COPYING COPYING.LESSER
%{python_sitelib}/moretools/
%{python_sitelib}/moretools-%{version}-py*.egg-info

%changelog
