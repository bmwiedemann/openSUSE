#
# spec file for package python-slycot
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
Name:           python-slycot
Version:        0.3.5.0
Release:        0
Summary:        A wrapper for the SLICOT control and systems library
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/python-control/Slycot
Source:         https://files.pythonhosted.org/packages/source/s/slycot/slycot-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module scikit-build}
BuildRequires:  %{python_module setuptools}
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python2-configparser
Requires:       blas
Requires:       lapack
Requires:       python-numpy
%python_subpackages

%description
Slycot is a wrapper for the SLICOT control and systems library.

%prep
%setup -q -n slycot-%{version}

%build
export CFLAGS="%{optflags}"
%{python_expand # make sure the correct f2py flavor is executed
%{$python_build} --generator "Unix Makefiles" -- -DF2PY_EXECUTABLE=/usr/bin/f2py%{$python_bin_suffix}
}

%install
%python_expand %{$python_install} --install-lib %{$python_sitearch} --generator "Unix Makefiles"
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1 # make package build reproducible (boo#1047218)
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python runtests.py --coverage --no-build
}

%files %{python_files}
%doc README.rst CREDITS
%license COPYING
%{python_sitearch}/slycot
%{python_sitearch}/slycot-*-py*.egg-info

%changelog
