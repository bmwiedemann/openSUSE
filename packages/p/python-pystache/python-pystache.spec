#
# spec file for package python-pystache
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


%{?sle15_python_module_pythons}
Name:           python-pystache
Version:        0.6.7
Release:        0
Summary:        Mustache for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/defunkt/pystache
Source:         https://files.pythonhosted.org/packages/source/p/pystache/pystache-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%description
Pystache is a Python implementation of Mustache. Mustache is a
framework-agnostic, logic-free templating system inspired by
ctemplate and etc. Like ctemplate, Mustache "emphasises separating
logic from presentation: it is impossible to embed application
logic in this template language."

The mustache(5) man page provides a good introduction to Mustache's
syntax. For a more complete (and more current) description of
Mustache's behaviour, see the official Mustache spec:
https://github.com/mustache/spec.

%python_subpackages

%prep
%setup -q -n pystache-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pystache
%python_clone -a %{buildroot}%{_bindir}/pystache-test
%{python_expand %fdupes %{buildroot}%$python_sitelib/}

%check
%pytest

%post
%{python_install_alternative pystache pystache-test}

%postun
%{python_uninstall_alternative pystache pystache-test}

%files %{python_files}
%license LICENSE
%doc HISTORY.md README.rst TODO.rst
%python_alternative %{_bindir}/pystache
%python_alternative %{_bindir}/pystache-test
%{python_sitelib}/pystache/
%{python_sitelib}/pystache-%{version}.dist-info

%changelog
