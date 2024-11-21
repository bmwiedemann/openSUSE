#
# spec file for package python-traits
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


# cycle with pyface
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-traits%{psuffix}
Version:        6.4.3
Release:        0
Summary:        Explicitly typed attributes for Python
# Images have different licenses. For image license breakdown check
# image_LICENSE.txt file. Except enthought/traits/ui/editors_gen.py
# which is GPLv2+ all remaining source or image files are in BSD
# 3-clause license. Confirmed from upstream.
License:        BSD-3-Clause AND EPL-1.0 AND LGPL-2.1-only
URL:            https://github.com/enthought/traits
Source:         https://github.com/enthought/traits/archive/%{version}.tar.gz#/traits-%{version}.tar.gz
Patch1:         https://github.com/enthought/traits/commit/a20f2154b2c79eb8550ea9228d1a4415ff51b72a.patch#/py313-ctraits.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module pyface}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
%endif
# /SECTION
Recommends:     python-traitsui >= 7.0.0

%python_subpackages

%description
The traits package developed by Enthought provides a special type definition
called a trait. Although they can be used as normal Python object attributes,
traits also have several additional characteristics:

 * Initialization: A trait can be assigned a default value.
 * Validation: A trait attribute's type can be explicitly declared.
 * Delegation: The value of a trait attribute can be contained either
   in another object.
 * Notification: Setting the value of a trait attribute can trigger
   notification of other parts of the program.
 * Visualization: User interfaces that permit the interactive
   modification of a trait's value can be automatically constructed
   using the trait's definition.

Part of the Enthought Tool Suite (ETS).

%prep
%autosetup -p1 -n traits-%{version}
%fdupes examples/

%build
%if %{without test}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build
%endif

%install
%if %{without test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%check
%if %{with test}
%{python_expand mkdir tester_%{$python_bin_suffix}
pushd tester_%{$python_bin_suffix}
export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -m unittest discover -v traits
popd
}
%endif

%if %{without test}
%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGES.rst README.rst
%doc examples/
%license LICENSE.txt image_LICENSE*.txt
%{python_sitearch}/traits/
%{python_sitearch}/traits-%{version}-py*.egg-info
%endif

%changelog
