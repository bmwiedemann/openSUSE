#
# spec file for package python-jsonpointer
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-jsonpointer
Version:        3.0.0
Release:        0
Summary:        Module to identify specific nodes in a JSON document
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/stefankoegl/python-json-pointer
Source:         https://files.pythonhosted.org/packages/source/j/jsonpointer/jsonpointer-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(preun): update-alternatives
%endif
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

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jsonpointer

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
