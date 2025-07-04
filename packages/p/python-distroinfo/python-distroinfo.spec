#
# spec file for package python-distroinfo
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


Name:           python-distroinfo
Version:        0.6.3
Release:        0
Summary:        Parsing, validation and query functions for packaging metadata
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/softwarefactory-project/distroinfo
Source:         https://files.pythonhosted.org/packages/source/d/distroinfo/distroinfo-%{version}.tar.gz
BuildRequires:  %{python_module pbr >= 0.5.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-pbr >= 0.5.6
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Python module for parsing, validating and querying distribution/packaging
metadata stored in human readable and reviewable text/YAML files.

%prep
%setup -q -n distroinfo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not integration'

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%{python_sitelib}/distroinfo
%{python_sitelib}/distroinfo-%{version}.dist-info

%changelog
