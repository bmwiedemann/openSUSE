#
# spec file for package python-EditorConfig
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
Name:           python-EditorConfig
Version:        0.12.2
Release:        0
Summary:        File Locator and Interpreter for Python
License:        Python-2.0 AND BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://editorconfig.org
Source0:        https://files.pythonhosted.org/packages/source/E/EditorConfig/EditorConfig-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
EditorConfig Python Core provides the same functionality as the
EditorConfig C Core. EditorConfig Python core can be used as a
command line program or as an importable library.

%prep
%setup -q -n EditorConfig-%{version}

%build
%python_build

%install
%python_install
# remove executable that is already supplied by the editorconfig package
rm -rf %{buildroot}%{_bindir}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.* COPYING
%doc README.rst
%{python_sitelib}/editorconfig
%{python_sitelib}/EditorConfig-%{version}-py%{py_ver}.egg-info

%changelog
