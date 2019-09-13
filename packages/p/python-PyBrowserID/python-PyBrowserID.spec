#
# spec file for package python-PyBrowserID
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 The openSUSE Project.
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
Name:           python-PyBrowserID
Version:        0.14.0
Release:        0
Summary:        Python library for the BrowserID Protocol
License:        MPL-2.0
Group:          Development/Languages/Python
Url:            https://github.com/mozilla/PyBrowserID
Source:         https://files.pythonhosted.org/packages/source/P/PyBrowserID/PyBrowserID-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module requests}
%endif
%python_subpackages

%description
This is a python client library for the BrowserID protocol that underlies
Mozilla Persona.

%prep
%setup -q -n PyBrowserID-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%doc CHANGES.txt README.rst
%{python_sitelib}/*

%changelog
