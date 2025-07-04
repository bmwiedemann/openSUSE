#
# spec file for package python-pygerrit2
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


Name:           python-pygerrit2
Version:        2.0.15
Release:        0
Summary:        Client library for interacting with Gerrit code review
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dpursehouse/pygerrit2
Source:         https://files.pythonhosted.org/packages/source/p/pygerrit2/pygerrit2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pbr >= 0.8.0
Requires:       python-requests >= 2.20.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pbr >= 0.8.0}
BuildRequires:  %{python_module requests >= 2.20.0}
# /SECTION
%python_subpackages

%description
Client library for interacting with Gerrit code review rest api

Pygerrit2 provides a simple interface for clients to interact with
Gerrit code review via its rest api.

See also: https://gerritcodereview.com/

%prep
%setup -q -n pygerrit2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/dpursehouse/pygerrit2/issues/247
sed -i 's:from mock:from unittest.mock:' unittests.py
%python_exec unittests.py

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{python_sitelib}/pygerrit2
%{python_sitelib}/pygerrit2-%{version}*-info

%changelog
