#
# spec file for package python-sunpy
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
%define         skip_python2 1
Name:           python-sunpy
Version:        1.0.6
Release:        0
Summary:        SunPy: Python for Solar Physics
License:        BSD-2-Clause AND BSD-3-Clause AND Apache-2.0 AND MIT
URL:            https://github.com/sunpy/sunpy
Source0:        https://files.pythonhosted.org/packages/source/s/sunpy/sunpy-%{version}.tar.gz
Source100:      python-sunpy-rpmlintrc
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module asdf}
BuildRequires:  %{python_module astropy >= 1.0.0}
BuildRequires:  %{python_module astropy-helpers >= 1.0.0}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module drms}
BuildRequires:  %{python_module matplotlib >= 1.1}
BuildRequires:  %{python_module numpy-devel > 1.7.1}
BuildRequires:  %{python_module pandas >= 0.12.0}
BuildRequires:  %{python_module parfive}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module scikit-image}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module suds-jurko}
BuildRequires:  fdupes
BuildRequires:  python-backports.functools_lru_cache
BuildRequires:  python-rpm-macros
Requires:       python-aioftp
Requires:       python-astropy >= 1.0.0
Requires:       python-matplotlib >= 1.1
Requires:       python-numpy > 1.7.1
Requires:       python-pandas >= 0.12.0
Requires:       python-parfive
Requires:       python-scipy
Recommends:     python-SQLAlchemy
Recommends:     python-asdf
Recommends:     python-beautifulsoup4
Recommends:     python-drms
Recommends:     python-glymur
Recommends:     python-requests
Recommends:     python-scikit-image
Recommends:     python-suds-jurko
Recommends:     python-wcsaxes >= 0.8
Recommends:     python-zeep
# SECTION test requirements
BuildRequires:  %{python_module aioftp}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zeep}
# /SECTION
%python_subpackages

%description
SunPy is a Python library for solar physics data analysis.

%prep
%setup -q -n sunpy-%{version}
chmod -x sunpy/data/test/cor1_20090615_000500_s4c1A.fts

%build
export CFLAGS="%{optflags}"
%python_exec setup.py build --offline

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE.rst licenses/*
%{python_sitearch}/sunpy
%{python_sitearch}/sunpy-%{version}-py*.egg-info

%changelog
