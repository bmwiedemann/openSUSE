#
# spec file for package python-jsonpatch
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
Name:           python-jsonpatch
Version:        1.23
Release:        0
Summary:        Python - JSON-Patches
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/stefankoegl/python-json-patch
Source:         https://files.pythonhosted.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
BuildRequires:  %{python_module jsonpointer >= 1.9}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-jsonpointer >= 1.9
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python module to apply JSON-Patches (according to RFC 6902).

%prep
%setup -q -n jsonpatch-%{version}

%build
%python_build

%install
%python_install

# Prepare for update-alternatives usage
%python_clone -a %{buildroot}%{_bindir}/jsonpatch
rm %{buildroot}%{_bindir}/jsondiff

%check
%python_exec tests.py

%post
%python_install_alternative jsonpatch

%preun
%python_uninstall_alternative jsonpatch

%files %{python_files}
%license COPYING
%doc AUTHORS README.md
%python_alternative %{_bindir}/jsonpatch
%{python_sitelib}/*

%changelog
