#
# spec file for package cookiecutter
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017 LISA GmbH, Bingen, Germany.
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


%define skip_python2 1
Name:           cookiecutter
Version:        1.7.3
Release:        0
Summary:        A command-line utility that creates projects from project templates
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/audreyr/cookiecutter
Source:         https://files.pythonhosted.org/packages/source/c/cookiecutter/cookiecutter-%{version}.tar.gz
Source1:        ccext.py
BuildRequires:  %{python_module Jinja2 >= 2.7}
BuildRequires:  %{python_module binaryornot >= 0.2.0}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module future >= 0.15.2}
BuildRequires:  %{python_module jinja2-time >= 0.1.0}
BuildRequires:  %{python_module poyo >= 0.1.0}
BuildRequires:  %{python_module python-slugify}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module whichcraft >= 0.4.0}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       python-Jinja2 >= 2.7
Requires:       python-binaryornot >= 0.2.0
Requires:       python-click >= 7.0
Requires:       python-future >= 0.15.2
Requires:       python-jinja2-time >= 0.1.0
Requires:       python-poyo >= 0.1.0
Requires:       python-python-slugify
Requires:       python-requests >= 2.18.0
Requires:       python-whichcraft >= 0.4.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION Testing requirements
BuildRequires:  %{python_module chardet >= 2.0.0}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.18.0}
# /SECTION
# SECTION Documentation requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-recommonmark
# /SECTION
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       cookiecutter = %{version}-%{release}
Obsoletes:      cookiecutter < %{version}-%{release}
%endif
%python_subpackages

%package -n cookiecutter-doc
Summary:        Documentation files for %{name}
Group:          Documentation/HTML

%description
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

Project templates can be in any programming language or markup format.

%description -n cookiecutter-doc
A command-line utility that creates projects from cookiecutters (project
templates), e.g. creating a Python package project from a Python package
project template.

This package contains the documentation for cookiecutter.

%prep
%setup -q -n cookiecutter-%{version}
cp %{SOURCE1} docs
# Remove pytest addopts:
rm setup.cfg

%build
%python_build
pushd docs
make %{?_smp_mflags} html
rm _build/html/.buildinfo
popd

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/cookiecutter
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# the doc directive in the files section cannot deduplicate, so do it manually
mkdir -p %{buildroot}%{_docdir}/cookiecutter-doc
cp -r docs/_build/html %{buildroot}%{_docdir}/cookiecutter-doc/
%fdupes %{buildroot}%{_docdir}/cookiecutter-doc

%check
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
%pytest tests

%pre
# delete command if the old package was not update-alternatives controlled
[ -h %{_bindir}/cookiecutter ] || rm -f %{_bindir}/cookiecutter

%post
%python_install_alternative cookiecutter

%postun
%python_uninstall_alternative cookiecutter

%files %{python_files}
%license LICENSE
%python_alternative cookiecutter
%{python_sitelib}/cookiecutter
%{python_sitelib}/cookiecutter-%{version}*-info

%files -n cookiecutter-doc
%license LICENSE
%doc %{_docdir}/cookiecutter-doc

%changelog
