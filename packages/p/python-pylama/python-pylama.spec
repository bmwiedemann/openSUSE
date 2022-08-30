#
# spec file for package python-pylama
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-pylama
Version:        8.4.1
Release:        0
Summary:        Code audit tool for python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/klen/pylama
Source:         https://github.com/klen/pylama/archive/refs/tags/%{version}.tar.gz#/pylama-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module mccabe      >= 0.7.0}
BuildRequires:  %{python_module pycodestyle >= 2.9.1}
BuildRequires:  %{python_module pydocstyle  >= 6.1.1}
BuildRequires:  %{python_module pyflakes    >= 2.5.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  mypy
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       python-mccabe      >= 0.7.0
Requires:       python-pycodestyle >= 2.9.1
Requires:       python-pydocstyle  >= 6.1.1
Requires:       python-pyflakes    >= 2.5.0
Suggests:       python-pylint
Suggests:       python-eradicate
Suggests:       python-radon
Suggests:       python-mypy
Suggests:       python-vulture
Recommends:     python-toml >= 0.10.2
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module eradicate >= 2}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pylint >= 2.11.1}
BuildRequires:  %{python_module radon >= 5.1.0}
BuildRequires:  %{python_module toml >= 0.10.2}
BuildRequires:  %{python_module vulture}
# /SECTION
BuildArch:      noarch
%python_subpackages

%description
Code audit tool for Python. Pylama wraps these tools:

- pycodestyle (formerly pep8) © 2012-2013, Florent Xicluna;
- pydocstyle (formerly pep257 by Vladimir Keleshev) © 2014, Amir Rachum;
- PyFlakes © 2005-2013, Kevin Watters;
- Mccabe © Ned Batchelder;
- Pylint © 2013, Logilab;
- Radon © Michele Lacchia
- eradicate © Steven Myint;
- Mypy © Jukka Lehtosalo and contributors;
- Vulture © Jendrik Seipp and contributors;

%prep
%autosetup -p1 -n pylama-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/pylama
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# pylama-quotes is on PyPI but has no active Website or repository for code maintenance
donttest="test_quotes"
%pytest -k "not ($donttest)"

%post
%python_install_alternative pylama

%postun
%python_uninstall_alternative pylama

%files %{python_files}
%doc Changelog README.rst
%license LICENSE
%python_alternative %{_bindir}/pylama
%{python_sitelib}/pylama
%{python_sitelib}/pylama-%{version}*-info

%changelog
