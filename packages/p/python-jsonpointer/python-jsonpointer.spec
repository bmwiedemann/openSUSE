#
# spec file for package python-jsonpointer
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
Name:           python-jsonpointer
Version:        2.0
Release:        0
Summary:        Module to identify specific nodes in a JSON document
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/stefankoegl/python-json-pointer
Source:         https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A module to identify specific nodes in a JSON document (according to draft 08).

%prep
%setup -q -n jsonpointer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/jsonpointer

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests.py

%post
%python_install_alternative jsonpointer

%preun
%python_uninstall_alternative jsonpointer

%files %{python_files}
%doc README.md
%license LICENSE.txt
%python_alternative %{_bindir}/jsonpointer
%{python_sitelib}/*

%changelog
