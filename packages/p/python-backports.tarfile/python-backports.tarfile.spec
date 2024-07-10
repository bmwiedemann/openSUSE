#
# spec file for package python-backports.tarfile
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


%{?sle15_python_module_pythons}
Name:           python-backports.tarfile
Version:        1.0.0
Release:        0
Summary:        Backport of CPython tarfile module
License:        MIT
URL:            https://github.com/jaraco/backports.tarfile
Source:         https://files.pythonhosted.org/packages/source/b/backports.tarfile/backports.tarfile-1.0.0.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-jaraco.packaging >= 9.3
Suggests:       python-rst.linker >= 1.9
BuildArch:      noarch
%python_subpackages

%description
Backport of CPython tarfile module

%prep
%autosetup -p1 -n backports.tarfile-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/backports
%{python_sitelib}/backports.tarfile-%{version}.dist-info

%changelog
