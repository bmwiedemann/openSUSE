#
# spec file for package python-PyBrowserID
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-PyBrowserID
Version:        0.14.0
Release:        0
Summary:        Python library for the BrowserID Protocol
License:        MPL-2.0
URL:            https://github.com/mozilla/PyBrowserID
Source:         https://files.pythonhosted.org/packages/source/P/PyBrowserID/PyBrowserID-%{version}.tar.gz
# https://github.com/mozilla/PyBrowserID/issues/42
Patch0:         python-PyBrowserID-unittest-mock.patch
# PATCH-FIX-UPSTREAM (not submitted because the project is archive and doesn't accept pull requests)
Patch1:         0001-Remove-the-use-of-the-deprecated-assertEquals-functi.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
BuildArch:      noarch
# SECTION test requirements
%if %{suse_version} < 1550
BuildRequires:  %{python_module mock}
%endif
BuildRequires:  %{python_module requests}
# /SECTION
%python_subpackages

%description
This is a python client library for the BrowserID protocol that underlies
Mozilla Persona.

%prep
%autosetup -p1 -n PyBrowserID-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc CHANGES.txt README.rst
%{python_sitelib}/browserid
%{python_sitelib}/[Pp]y[Bb]rowser[Ii][Dd]-%{version}*-info

%changelog
