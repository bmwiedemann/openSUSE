#
# spec file for package python-selection
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-selection
Version:        0.0.21
Release:        0
Summary:        API to extract content from HTML & XML documents
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lorien/selection
Source:         https://files.pythonhosted.org/packages/source/s/selection/selection-%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
BuildArch:      noarch
%python_subpackages

%description
API to extract content from HTML & XML documents

%prep
%setup -q -n selection-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/selection
%{python_sitelib}/selection-%{version}*-info

%changelog
