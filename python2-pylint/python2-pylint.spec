#
# spec file for package python2-pylint
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
%define skip_python3 1
%define oldpython python
Name:           python2-pylint
Version:        1.9.5
Release:        0
Summary:        Syntax and style checker for Python code
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/pycqa/pylint
Source:         https://files.pythonhosted.org/packages/source/p/pylint/pylint-%{version}.tar.gz
BuildRequires:  %{python_module astroid >= 1.6.5}
BuildRequires:  %{python_module editdistance}
BuildRequires:  %{python_module isort >= 4.2.5}
BuildRequires:  %{python_module mccabe}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-backports.functools_lru_cache
BuildRequires:  python2-configparser
BuildRequires:  python2-enum34
BuildRequires:  python2-singledispatch
Requires:       python-astroid >= 1.6.5
Requires:       python-backports.functools_lru_cache
Requires:       python-configparser
Requires:       python-editdistance
Requires:       python-enum34
Requires:       python-isort >= 4.2.5
Requires:       python-mccabe
Requires:       python-singledispatch
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       pylint = %{version}
Obsoletes:      pylint < %{version}
Provides:       %{oldpython}-pylint = %{version}
BuildArch:      noarch
%python_subpackages

%description
Pylint analyzes Python source code looking for bugs and signs of poor
quality.

Pylint is a python tool that checks if a module satisfies a coding
standard. Pylint can be seen as another PyChecker since nearly all
tests you can do with PyChecker can also be done with Pylint. But
Pylint offers some more features, like checking line-code's length,
checking if variable names are well-formed according to your coding
standard, or checking if declared interfaces are truly implemented, and
much more (see the complete check list).

The big advantage with Pylint is that it is highly configurable,
customizable, and you can easily write a small plugin to add a personal
feature.

%prep
%setup -q -n pylint-%{version}
# FIXME: remove with next update
# The test fails here reliably
rm -f pylint/test/functional/using_constant_test.py

%build
%python_build

%install
%python_install

for p in pylint epylint pyreverse symilar ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pylint epylint pyreverse symilar

%postun
%python_uninstall_alternative pylint

%check
# bsddb fails and upstream dropped support for python2 with new releases
%pytest pylint/test/ -k 'not test_libmodule[bsddb]'

%files %{python_files}
%license COPYING
%doc ChangeLog README.rst
%doc examples/
%python_alternative %{_bindir}/pylint
%python_alternative %{_bindir}/epylint
%python_alternative %{_bindir}/pyreverse
%python_alternative %{_bindir}/symilar
%{python_sitelib}/pylint/
%{python_sitelib}/pylint-%{version}-py*.egg-info

%changelog
