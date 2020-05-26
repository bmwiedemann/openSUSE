#
# spec file for package python-pyroma
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pyroma
Version:        2.6
Release:        0
Summary:        Program to test a Python project's adherence to packaging guidelines
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/regebro/pyroma
Source:         https://files.pythonhosted.org/packages/source/p/pyroma/pyroma-%{version}.tar.gz
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments
Requires:       python-docutils
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Pyroma is a package that gives a rating of how well a Python project
complies with the best practices of the Python packaging ecosystem,
primarily PyPI, pip, Distribute, etc., as well as a list of issues
that could be improved.

It's written so that there are a library with methods to call from Python, as
well as a script, also called pyroma.

%prep
%setup -q -n pyroma-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyroma
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py test

%post
%python_install_alternative pyroma

%postun
%python_uninstall_alternative pyroma

%files %{python_files}
%license LICENSE.txt
%doc README.rst HISTORY.txt
%python_alternative %{_bindir}/pyroma
%{python_sitelib}/*

%changelog
