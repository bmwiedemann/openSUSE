#
# spec file for package python-pycdio
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pycdio
Version:        2.1.1
Release:        0
Summary:        Python Bindings for the CDIO Library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/pycdio/
Source:         https://files.pythonhosted.org/packages/source/p/pycdio/pycdio-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libcdio-devel >= 2.0.0
BuildRequires:  python-rpm-macros
BuildRequires:  swig
%python_subpackages

%description
pycdio is a Python interface to the CD Input and Control library (libcdio).

The pycdio (and libcdio) libraries encapsulate CD-ROM reading and control.
Python programs wishing to be oblivious of the OS- and device-dependent
properties of a CD-ROM can use this library.

%prep
%setup -q -n pycdio-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license COPYING
%doc ChangeLog README.rst THANKS
%{python_sitearch}/*cdio.py
%{python_sitearch}/_pycdio.cpython*
%{python_sitearch}/*iso9660.py
%{python_sitearch}/_pyiso9660.cpython*
%{python_sitearch}/pycdio-%{version}*-info
%pycache_only %{python_sitearch}/__pycache__/*cdio*
%pycache_only %{python_sitearch}/__pycache__/*iso9660*

%changelog
