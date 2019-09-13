#
# spec file for package python-pylint
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-pylint
Version:        2.3.1
Release:        0
Summary:        Syntax and style checker for Python code
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/pycqa/pylint
Source:         https://files.pythonhosted.org/packages/source/p/pylint/pylint-%{version}.tar.gz
BuildRequires:  %{python_module astroid >= 2.2.0}
BuildRequires:  %{python_module editdistance}
BuildRequires:  %{python_module isort >= 4.2.5}
BuildRequires:  %{python_module mccabe >= 0.6}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module typed-ast}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astroid >= 2.2.0
Requires:       python-editdistance
Requires:       python-isort >= 4.2.5
Requires:       python-mccabe >= 0.6
Requires:       python-six
Requires:       python-typed-ast
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# test is checking that "tkinter.tix" is deprecated
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-tk
%endif
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

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/pylint/test/
for p in pylint epylint pyreverse symilar ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pylint epylint pyreverse symilar

%postun
%python_uninstall_alternative pylint

%check
export PYTHONDONTWRITEBYTECODE=1
%pytest pylint/test

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
