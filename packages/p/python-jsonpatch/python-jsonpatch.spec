#
# spec file for package python-jsonpatch
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-jsonpatch
Version:        1.33
Release:        0
Summary:        Python - JSON-Patches
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/stefankoegl/python-json-patch
Source:         https://files.pythonhosted.org/packages/source/j/jsonpatch/jsonpatch-%{version}.tar.gz
BuildRequires:  %{python_module jsonpointer >= 1.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-jsonpointer >= 1.9
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(preun): update-alternatives
%endif
%python_subpackages

%description
Python module to apply JSON-Patches (according to RFC 6902).

%prep
%setup -q -n jsonpatch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Prepare for update-alternatives usage
%python_clone -a %{buildroot}%{_bindir}/jsonpatch
rm %{buildroot}%{_bindir}/jsondiff

%check
%pyunittest -v tests

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative jsonpatch

%post
%python_install_alternative jsonpatch

%postun
%python_uninstall_alternative jsonpatch

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%python_alternative %{_bindir}/jsonpatch
%{python_sitelib}/jsonpatch*
%pycache_only %{python_sitelib}/__pycache__/jsonpatch*.pyc

%changelog
