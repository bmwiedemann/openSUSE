#
# spec file for package python-pylama
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
Name:           python-pylama
Version:        7.7.1
Release:        0
Summary:        Code audit tool for python
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/klen/pylama
Source:         https://files.pythonhosted.org/packages/source/p/pylama/pylama-%{version}.tar.gz
# https://github.com/klen/pylama/issues/147
Source1:        https://raw.githubusercontent.com/klen/pylama/develop/dummy.py
BuildRequires:  %{python_module eradicate >= 0.2}
BuildRequires:  %{python_module mccabe >= 0.5.2}
BuildRequires:  %{python_module pycodestyle >= 2.3.1}
BuildRequires:  %{python_module pydocstyle >= 2.0.0}
BuildRequires:  %{python_module pyflakes >= 1.5.0}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module radon >= 1.4.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  mypy
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-mccabe >= 0.5.2
Recommends:     python-pycodestyle >= 2.3.1
Recommends:     python-pydocstyle >= 2.0.0
Recommends:     python-pyflakes >= 1.5.0
Recommends:     python-pylint
Recommends:     python-radon >= 1.4.2
BuildArch:      noarch
%python_subpackages

%description
Audit tool for Python and JavaScript. Pylama wraps these tools:
* PEP8
* PEP257
* PyFlakes
* Mccabe

%prep
%setup -q -n pylama-%{version}
cp %{SOURCE1} .

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pylama

%check
export LANG=en_US.UTF-8
%python_expand py.test-%{$python_bin_suffix} -v tests/

%post
%python_install_alternative pylama

%postun
%python_uninstall_alternative pylama

%files %{python_files}
%doc AUTHORS Changelog README.rst
%license LICENSE
%python_alternative %{_bindir}/pylama
%{python_sitelib}/*

%changelog
