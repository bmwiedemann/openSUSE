#
# spec file for package python-sphinx-qt-documentation
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


%define skip_python2 1
Name:           python-sphinx-qt-documentation
Version:        0.4.1
Release:        0
Summary:        Sphinx Qt documentation
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://pypi.org/project/sphinx-qt-documentation/
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-qt-documentation/sphinx_qt_documentation-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
This is plugin to add cross-link to qt documentation for python code created with PyQt5/6 or PySide2/6.

%prep
%setup -q -n sphinx_qt_documentation-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/sphinx_qt_documentation
%{python_sitelib}/sphinx_qt_documentation-%{version}*-info

%changelog
