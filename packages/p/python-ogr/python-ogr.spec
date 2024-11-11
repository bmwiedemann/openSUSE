#
# spec file for package python-ogr
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-ogr
Version:        0.50.2
Release:        0
Summary:        One API for multiple git forges
License:        MIT
URL:            https://github.com/packit-service/ogr
Source:         https://files.pythonhosted.org/packages/source/o/ogr/ogr-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Deprecated
Requires:       python-GitPython
Requires:       python-PyGithub
Requires:       python-PyYAML
Requires:       python-cryptography
Requires:       python-python-gitlab
Requires:       python-requests
Requires:       python-urllib3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Deprecated}
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module PyGithub}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module flexmock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-gitlab}
BuildRequires:  %{python_module requre}
# /SECTION
%python_subpackages

%description
One API for multiple git forges.

%prep
%autosetup -p1 -n ogr-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/ogr
%{python_sitelib}/ogr-%{version}.dist-info

%changelog
