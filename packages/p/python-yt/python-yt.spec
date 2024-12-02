#
# spec file for package python-yt
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
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

# avoid "lto1: internal compiler error" during build
%global _lto_cflags %{nil}

%{?sle15_python_module_pythons}
Name:           python-yt%{psuffix}
Version:        4.4.0
Release:        0
Summary:        An analysis and visualization toolkit for volumetric data
License:        BSD-3-Clause
URL:            https://github.com/yt-project/yt
Source0:        https://files.pythonhosted.org/packages/source/y/yt/yt-%{version}.tar.gz
Source100:      python-yt-rpmlintrc
# PATCH-FIX-OPENSUSE yt-ignore-pytestdepr.patch code@bnavigator.de -- ignore a pytest deprecation warning. Upstream is still working on the nose ot pytest transition
Patch1:         yt-ignore-pytestdepr.patch
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  python-rpm-macros
%if !%{with test}
BuildRequires:  %{python_module Cython > 3 with %python-Cython < 3.1}
BuildRequires:  %{python_module ewah-bool-utils-devel >= 1.0.2}
BuildRequires:  %{python_module numpy-devel >= 1.25}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%endif
Requires:       python-Pillow >= 8
Requires:       python-cmyt >= 1.1.2
Requires:       python-ewah-bool-utils >= 1.0.2
Requires:       python-ipywidgets >= 8.0.0
Requires:       python-matplotlib >= 3.5
Requires:       python-more-itertools >= 8.4
Requires:       python-numpy >= 1.19.3
Requires:       python-packaging >= 20.9
Requires:       python-tomli-w >= 0.4.0
Requires:       python-tqdm >= 3.4.0
Requires:       python-unyt >= 2.9.2
Requires:       (python-tomli >= 1.2.3 if python-base < 3.11)
Requires:       (python-typing-extensions >= 4.4.0 if python-base < 3.12)
Requires(post): update-alternatives
Requires(postun): update-alternatives
%if %{with test}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sympy}
BuildRequires:  %{python_module yt = %{version}}
# More optional modules for tests: scipy, pandas, h5py, xarray, glue, astropy, miniball, firefly, ...
%endif
%python_subpackages

%description
YT is an python package for analyzing and visualizing volumetric
data.  YT supports structured, variable-resolution meshes,
unstructured meshes, and discrete or sampled data such as particles.

%prep
%autosetup -p1 -n yt-%{version}
sed -i -e '/^#!\//, 1d' yt/utilities/lodgeit.py

%build
%if !%{with test}
export CFLAGS="%{optflags} -freport-bug"
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/yt
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
mv yt yt.src
# incompatible API attributes
donttest="test_default_species_fields or test_stream_species"
%{python_expand # need to use the compiled modules in the current directory because of skips defined in pyproject.toml
cp -r %{$python_sitearch}/yt yt
$python -m pytest yt -k "not ($donttest)"
rm -r yt
}
%endif

%post
%python_install_alternative yt

%postun
%python_uninstall_alternative yt

%if !%{with test}
%files %{python_files}
%doc README.md
%license COPYING.txt
%python_alternative %{_bindir}/yt
%{python_sitearch}/yt
%{python_sitearch}/yt-%{version}.dist-info
%endif

%changelog
