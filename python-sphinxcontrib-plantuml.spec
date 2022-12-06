#
# spec file for package python-sphinxcontrib-plantuml
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


%define skip_python2 1
%{?!python_module:%define python_module() python3-%{**}}

Name:           python-sphinxcontrib-plantuml
Version:        0.24.1
Release:        0
Summary:        Sphinx API for Web Apps
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-contrib/plantuml/
Source:         https://github.com/sphinx-contrib/plantuml/archive/%{version}.tar.gz#/sphinxcontrib-plantuml-%{version}.tar.gz
Patch0:         py3-for-tests.patch
BuildRequires:  %{python_module Sphinx >= 2}
BuildRequires:  %{python_module Sphinx-latex}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ghostscript
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-epstopdf
BuildRequires:  tox
Requires:       plantuml
Requires:       python-Sphinx >= 2
BuildArch:      noarch
%python_subpackages

%description
Once you enable this extension, a very simple string like this:

    "Alice -> Bob: Hi!"

will create a nice UML schema. WIth PlantUML, you can specify things like height, width, scale, caption and so on. For details, please see PlantUML documentation at: http://plantuml.sourceforge.net/.

%prep
%setup -q -n plantuml-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# upstream knows: https://github.com/sphinx-contrib/plantuml/commit/e1b3f7e709eae0e95c70564a7e42279db08c8447
# s/class="figure"/class="figure align-default"/ in test_functional.py
%pytest -k 'not test_buildhtml_name'

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib/
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib/plantuml.*
%{python_sitelib}/sphinxcontrib_plantuml-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_plantuml-%{version}-py*.*-info

%changelog
