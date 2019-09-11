#
# spec file for package python-gogs_client
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
%{!?license: %global license %doc}
%bcond_without test
Name:           python-gogs_client
Version:        1.0.6
Release:        0
Summary:        A python library for interacting with a gogs server
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/unfoldingWord-dev/python-gogs-client
Source:         https://files.pythonhosted.org/packages/source/g/gogs_client/gogs_client-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Requires:       python-future
Requires:       python-requests
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
%endif
Provides:       python-gogs-client
%python_subpackages

%description
This is a Python client to Gogs servers.

Documentation for the module can be found at http://pythonhosted.org/gogs-client/

%prep
%setup -q -n gogs_client-%{version}

%build
%python_build

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
