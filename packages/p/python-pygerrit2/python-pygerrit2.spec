#
# spec file for package python-pygerrit2
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
Name:           python-pygerrit2
Version:        2.0.9
Release:        0
Summary:        Client library for interacting with Gerrit code review
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dpursehouse/pygerrit2
Source:         https://files.pythonhosted.org/packages/source/p/pygerrit2/pygerrit2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pbr >= 0.8.0
Requires:       python-requests >= 2.10.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec unittests.py

%files %{python_files}
%license LICENSE
%doc AUTHORS ChangeLog README.md
%{python_sitelib}/*

%changelog
