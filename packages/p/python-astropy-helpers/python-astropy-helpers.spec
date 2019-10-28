#
# spec file for package python-astropy-helpers
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
Name:           python-astropy-helpers
Version:        3.2.1
Release:        0
Summary:        Utilities for building and installing Astropy
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/astropy/astropy-helpers
Source:         https://files.pythonhosted.org/packages/source/a/astropy-helpers/astropy-helpers-%{version}.tar.gz
Source100:      python-astropy-helpers-rpmlintrc
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpydoc}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
Requires:       python-numpy
Requires:       python-numpydoc
BuildArch:      noarch
%python_subpackages

%description
This project provides a Python package, astropy_helpers, which includes
many build, installation, and documentation-related tools used by the Astropy
project, but packaged separately for use by other projects that wish to
leverage this work.  The motivation behind this package and details of its
implementation are in the accepted Astropy Proposal for Enhancement (APE) 4:
https://github.com/astropy/astropy-APEs/blob/master/APE4.rst

astropy_helpers includes a special "bootstrap" module called
ah_bootstrap.py which is intended to be used by a project's setup.py in
order to ensure that the astropy_helpers package is available for
build/installation.  This is similar to the ez_setup.py module that is
shipped with some projects to bootstrap setuptools.

%prep
%setup -q -n astropy-helpers-%{version}

%build
%python_build

%install
%python_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/astropy_helpers
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/astropy_helpers
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%license LICENSE.rst
%doc README.rst CHANGES.rst
%{python_sitelib}/*

%changelog
