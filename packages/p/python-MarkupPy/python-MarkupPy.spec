#
# spec file for package python-MarkupPy
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-MarkupPy
Version:        1.14
Release:        0
License:        SUSE-Public-Domain
Summary:        An HTML/XML generator
Url:            https://github.com/tylerbakke/MarkupPy
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/M/MarkupPy/MarkupPy-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
This is MarkupPy - a Python module that for generating HTML/XML
for Python programs.

%prep
%setup -q -n MarkupPy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license %{python_sitelib}/MarkupPy/markup.py
%{python_sitelib}/MarkupPy/
%{python_sitelib}/MarkupPy-%{version}-py*.egg-info

%changelog
