#
# spec file for package python-atomicwrites
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%define psuffix -doc
%bcond_without doc
%else
%define psuffix %{nil}
%bcond_with doc
%endif
Name:           python-atomicwrites%{psuffix}
Version:        1.4.1
Release:        0
Summary:        Atomic file writes for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/untitaker/python-atomicwrites
Source:         https://files.pythonhosted.org/packages/source/a/atomicwrites/atomicwrites-%{version}.tar.gz
# PATCH-FIX-OPENSUSE sphinx8.patch -- daniel.garcia@suse.com
Patch0:         sphinx8.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with doc}
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module pytest}
BuildRequires:  python3-Sphinx
Provides:       %{python_module atomicwrites-doc = %{version}}
%endif
%python_subpackages

%description
Atomic file writes for python3.
Features that distinguish it from other similar libraries:

- Race-free assertion that the target file doesn't yet exist. This can be
  controlled with the 'overwrite' parameter.

- High-level API that wraps a very flexible class-based API.

%prep
%autosetup -p1 -n atomicwrites-%{version}
rm -rf atomicwrites.egg-info

%if %{with doc}
%package -n %{name}-doc
Summary:        Atomic file writes for Python (documentation)
Group:          Documentation/HTML

%description -n %{name}-doc
Atomic file writes for python3.
Features that distinguish it from other similar libraries:

- Race-free assertion that the target file doesn't yet exist. This can be
  controlled with the 'overwrite' parameter.

- High-level API that wraps a very flexible class-based API.

This package contains the documentation for both python2 and python3 versions
of python-atomicwrites
%endif

%build
%if %{without doc}
%python_build
%else
pushd docs
make html
rm _build/html/.buildinfo
popd
%endif

%install
%if %{without doc}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with doc}
%pytest
%endif

%if %{without doc}
%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%{python_sitelib}/atomicwrites*

%else

%files -n %{name}-doc
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%doc docs/_build/html
%endif

%changelog
