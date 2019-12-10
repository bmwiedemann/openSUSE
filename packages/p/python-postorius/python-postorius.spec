#
# spec file for package python-postorius
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
%define skip_python2 1
Name:           python-postorius
Version:        1.3.0
Release:        0
Summary:        A web user interface for GNU Mailman
License:        GPL-3.0-only
URL:            https://gitlab.com/mailman/postorius
Source:         https://files.pythonhosted.org/packages/source/p/postorius/postorius-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-django-mailman3 >= 1.2.0
Requires:       python-mailmanclient >= 3.2.3
Requires:       python-readme_renderer
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module cmarkgfm}
BuildRequires:  %{python_module django-mailman3 >= 1.2.0}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module mailmanclient >= 3.2.3}
BuildRequires:  %{python_module mailman}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module readme_renderer}
BuildRequires:  %{python_module vcrpy}
# /SECTION
%python_subpackages

%description
A web user interface for GNU Mailman

%prep
%setup -q -n postorius-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd example_project
export PYTHONPATH='../src'
%pytest ..
popd

%files %{python_files}
%doc README.rst example_project
%license COPYING
%{python_sitelib}/*

%changelog
