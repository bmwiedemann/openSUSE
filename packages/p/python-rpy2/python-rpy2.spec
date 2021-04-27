#
# spec file for package python-rpy2
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python36 1
Name:           python-rpy2
Version:        3.4.4
Release:        0
Summary:        A Python interface to the R Programming Language
License:        GPL-2.0-or-later
URL:            https://bitbucket.org/rpy2/rpy2
Source:         https://files.pythonhosted.org/packages/source/r/rpy2/rpy2-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.13.1}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  R-base >= 3.2
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  texinfo
BuildRequires:  texlive-latex
Requires:       R-base >= 2.12
Requires:       python-cffi >= 1.13.1
Requires:       python-numpy
Requires:       readline
BuildArch:      noarch
%python_subpackages

%description
RPy is a Python interface to the R Programming Language. It can
manage all kinds of R objects and can execute arbitrary R functions
(including the graphic functions). All errors from the R language are
converted to Python exceptions. Any module installed for the R system
can be used from Python.

This code is inspired by RSPython from the Omegahat project.

%prep
%setup -q -n rpy2-%{version}
sed -i 's/\r$//' README.md

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Test files have been removed
# %%check
# mkdir -p tester
# pushd tester
# %%{python_expand export PYTHONPATH=%%{buildroot}%%{$python_sitearch}
# $python -B -m rpy2.tests
# }
# popd

%files %{python_files}
%doc AUTHORS NEWS README.md
%license gpl-2.0.txt
%{python_sitelib}/rpy2/
%{python_sitelib}/rpy2-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/_rinterface*.py*
%{python_sitelib}/_rinterface*.py*

%changelog
