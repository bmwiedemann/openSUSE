#
# spec file for package python-pylint
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without tests
Name:           python-pylint
Version:        2.15.10
Release:        0
Summary:        Syntax and style checker for Python code
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/pycqa/pylint
# Tests are no longer packaged in the PyPI sdist, use GitHub archive
Source:         https://github.com/PyCQA/pylint/archive/refs/tags/v%{version}.tar.gz#/pylint-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM gh#PyCQA/pylint#7367
Patch0:         pylint-pr7367-pythonpathtest.patch
BuildRequires:  %{python_module base >= 3.7.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dill >= 0.3.6
Requires:       python-platformdirs >= 2.2
Requires:       python-tomlkit >= 0.10.1
Requires:       (python-astroid >= 2.12.13 with python-astroid < 2.14.0~dev0)
Requires:       (python-isort >= 4.2.5 with python-isort < 6)
Requires:       (python-mccabe >= 0.6 with python-mccabe < 0.8)
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
%if 0%{?python_version_nodots} < 310
Requires:       python-typing-extensions >= 3.10
%endif
%if %{with tests}
# SECTION pylint deps
BuildRequires:  %{python_module astroid >= 2.12.13 with %python-astroid < 2.14.0~dev0}
BuildRequires:  %{python_module dill >= 0.3.6}
BuildRequires:  %{python_module isort >= 4.2.5 with %python-isort < 6}
BuildRequires:  %{python_module mccabe >= 0.6 with %python-mccabe < 0.8}
BuildRequires:  %{python_module platformdirs >= 2.2}
BuildRequires:  %{python_module tomli >= 1.1.0 if %python-base < 3.11}
BuildRequires:  %{python_module tomlkit >= 0.10.1}
# typing-extensions for python310 required for tests only, same as gh#PyCQA/astroid#1585
BuildRequires:  %{python_module typing-extensions >= 3.10}
# /SECTION
# SECTION test deps
BuildRequires:  %{python_module GitPython > 3}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%autosetup -p1 -n pylint-%{version}
sed -i '1{/^#!/ d}' pylint/__main__.py

%build
export LC_ALL="en_US.UTF-8"
%pyproject_wheel

%install
export LC_ALL="en_US.UTF-8"
%pyproject_install
for p in pylint epylint pyreverse symilar pylint-config ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with tests}
%check
export LC_ALL="en_US.UTF-8"
%pytest --benchmark-disable -k "not test_linter_with_unpickleable_plugins_is_pickleable"
%endif

%post
%python_install_alternative pylint epylint pyreverse symilar pylint-config

%postun
%python_uninstall_alternative pylint

%files %{python_files}
%license LICENSE
%doc README.rst
%doc examples/
%python_alternative %{_bindir}/pylint
%python_alternative %{_bindir}/pylint-config
%python_alternative %{_bindir}/epylint
%python_alternative %{_bindir}/pyreverse
%python_alternative %{_bindir}/symilar
%{python_sitelib}/pylint/
%{python_sitelib}/pylint-%{version}*-info

%changelog
