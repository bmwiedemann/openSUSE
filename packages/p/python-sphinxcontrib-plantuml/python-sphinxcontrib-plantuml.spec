#
# spec file for package python-sphinxcontrib-plantuml
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
Name:           python-sphinxcontrib-plantuml
Version:        0.17.1
Release:        0
Summary:        Sphinx API for Web Apps
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/sphinx-contrib/plantuml/
Source:         https://github.com/sphinx-contrib/plantuml/archive/%{version}.tar.gz#/sphinxcontrib-plantuml-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx-latex}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  ghostscript
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-epstopdf
BuildRequires:  tox
Requires:       plantuml
Requires:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
Once you enable this extension, a very simple string like this:

    "Alice -> Bob: Hi!"

will create a nice UML schema. WIth PlantUML, you can specify things like height, width, scale, caption and so on. For details, please see PlantUML documentation at: http://plantuml.sourceforge.net/.

%prep
%setup -q -n plantuml-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH="." nosetests-%{$python_bin_suffix} -w tests

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib/
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib/plantuml.*
%{python_sitelib}/sphinxcontrib_plantuml-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_plantuml-%{version}-py*.*-info

%changelog
