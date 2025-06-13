#
# spec file for package python-yamldoc
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


Name:           python-yamldoc
Version:        0.3.0
Release:        0
Summary:        A module to determine file mimetypes
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/smathot/python-yamldoc
Source:         https://files.pythonhosted.org/packages/source/p/python-yamldoc/python-yamldoc-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
BuildArch:      noarch
%python_subpackages

%description
This module is a layer on top of the standard Python mimetypes module and
python-magic. Python-magic only works with local files to which you need to
have access, while mimetypes only uses the filename to determine its
filetype.

%prep
%setup -q -n python-yamldoc-%{version}
sed -i '1{/^#!/d}' yamldoc/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/yamldoc
%{python_sitelib}/python[-_]yamldoc-%{version}*-info

%changelog
