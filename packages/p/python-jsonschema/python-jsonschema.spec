#
# spec file for package python-jsonschema
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
%bcond_without python2
Name:           python-jsonschema
# Please, do not update to the current version, it breaks numerous other
# packages, because of unstable API.
Version:        2.6.0
Release:        0
Summary:        An implementation of JSON-Schema validation for Python
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/Julian/jsonschema
Source:         https://files.pythonhosted.org/packages/source/j/jsonschema/jsonschema-%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcversioner >= 2.16.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python2-functools32
%endif
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-functools32
%endif
%python_subpackages

%description
jsonschema is an implementation of JSON Schema (currently in Draft 3)
for Python (supporting 2.6+ including Python 3).

%prep
%setup -q -n jsonschema-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

# Prepare for update-alternatives usage
%python_clone -a %{buildroot}%{_bindir}/jsonschema

%check
%python_exec -m unittest jsonschema.tests.test_jsonschema_test_suite

%post
%python_install_alternative jsonschema

%preun
%python_uninstall_alternative jsonschema

%files %{python_files}
%license COPYING
%doc README.rst
%python_alternative %{_bindir}/jsonschema
%{python_sitelib}/*

%changelog
