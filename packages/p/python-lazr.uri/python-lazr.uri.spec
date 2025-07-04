#
# spec file for package python-lazr.uri
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


Name:           python-lazr.uri
Version:        1.0.6
Release:        0
Summary:        Code for parsing and dealing with URI
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://launchpad.net/lazr.uri
Source:         https://files.pythonhosted.org/packages/source/l/lazr.uri/lazr.uri-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The lazr.uri package includes code for parsing and dealing with URIs.

%prep
%setup -q -n lazr.uri-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING.txt
%doc README.rst
%dir %{python_sitelib}/lazr
%{python_sitelib}/lazr/uri
%{python_sitelib}/lazr[._]uri-%{version}*-info
%{python_sitelib}/lazr[._]uri-%{version}*nspkg.pth

%changelog
