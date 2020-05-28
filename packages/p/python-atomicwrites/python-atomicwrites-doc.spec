#
# spec file for package python-atomicwrites-doc
#
# Copyright (c) 2020 SUSE LLC
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


# This package allows us to test the package without a dependency loop with python-pytest
# Please do not delete it

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-atomicwrites-doc
Version:        1.4.0
Release:        0
Summary:        Documentation for the Python atomic write support
License:        MIT
Group:          Documentation/HTML
URL:            https://github.com/untitaker/python-atomicwrites
Source:         https://files.pythonhosted.org/packages/source/a/atomicwrites/atomicwrites-%{version}.tar.gz
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Provides:       %{python_module atomicwrites-doc = %{version}}
BuildArch:      noarch

%description
Atomic file writes for python.
Features that distinguish it from other similar libraries:

- Race-free assertion that the target file doesn't yet exist. This can be
  controlled with the 'overwrite' parameter.

- high-level API that wraps a very flexible class-based API.

This package contains the documentation for both python2 and python3 versions
of python-atomicwrites

%prep
%setup -q -n atomicwrites-%{version}

%build
pushd docs
make html
rm _build/html/.buildinfo
popd

%install
# not needed

%check
%{python_expand rm -rf tests/__pycache__
export PYTHONDONTWRITEBYTECODE=1
py.test-%{$python_bin_suffix}
}

%files
%defattr(-,root,root,-)
%doc docs/_build/html
%doc README.rst
%license LICENSE

%changelog
