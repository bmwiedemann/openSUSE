#
# spec file for package python-aspectlib
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
# Test requires network connection
%bcond_with     test
%define         oldpython python
Name:           python-aspectlib
Version:        1.4.2
Release:        0
License:        BSD-2-Clause
Summary:        Aspect-oriented programming
Url:            https://github.com/ionelmc/python-aspectlib
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/aspectlib/aspectlib-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
%if %{with test}
BuildRequires:  %{python_module fields}
BuildRequires:  %{python_module process-tests}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tornado}
BuildRequires:  python-mock
BuildRequires:  python-trollius
%endif
BuildRequires:  fdupes
Requires:       python-fields
Recommends:     python-tornado
%ifpython2
Requires:       %{oldpython}-trollius
%endif
BuildArch:      noarch

%python_subpackages

%description
Aspectlib is an aspect-oriented programming, monkey-patch and
decorators library. It is useful when changing behavior in
existing code is desired. It includes tools for debugging and
testing: simple mock/record and a complete capture/replay
framework.

%prep
%setup -q -n aspectlib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_expand py.test-%{$python_bin_suffix} -vv --ignore=src
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%{python_sitelib}/*

%changelog
