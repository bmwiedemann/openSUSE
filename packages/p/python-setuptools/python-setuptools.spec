#
# spec file for package python-setuptools
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


%global flavor @BUILD_FLAVOR@%{nil}
%if 0%{?suse_version} >= 1550
%if "%{flavor}" == "primary"
# this one is goes into Ring0:  Bootstrap for primary python stack
%define pprefix %{primary_python}
%define pythons %{primary_python}
%define psuffix %{nil}
%endif
%if "%{flavor}" == ""
# The rest is in Ring1
%define pprefix python
%{expand:%%define skip_%{primary_python} 1}
%define psuffix %{nil}
%endif
%else
# backport and option d projects for 15.X having one or more python in the buildset don't need the Ring split for bootstrap
%if "%{flavor}" == "primary"
%define python_module() invalid-multibuild-flavor-for-15.X
ExclusiveArch:  do-not-build
%else
%define pprefix python
%endif
%endif
%if "%{flavor}" == "test"
%define psuffix -test
%define pprefix python
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif

# in order to avoid rewriting for subpackage generator
%define mypython python
%{?sle15_python_module_pythons}
Name:           %{pprefix}-setuptools%{psuffix}
Version:        75.6.0
Release:        0
Summary:        Download, build, install, upgrade, and uninstall Python packages
License:        Apache-2.0 AND MIT AND BSD-2-Clause AND Python-2.0
URL:            https://github.com/pypa/setuptools
Source:         https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
Patch0:         sort-for-reproducibility.patch
# Bootstrap: Don't BuildRequire pip here!
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-rpm-packaging
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module filelock >= 3.4.0}
BuildRequires:  %{python_module ini2toml-lite >= 0.14}
BuildRequires:  %{python_module jaraco.develop >= 7.21}
BuildRequires:  %{python_module jaraco.envs >= 2.2}
BuildRequires:  %{python_module jaraco.packaging >= 9.3}
BuildRequires:  %{python_module jaraco.path >= 3.2.0}
BuildRequires:  %{python_module jaraco.test >= 5.5}
BuildRequires:  %{python_module packaging >= 24.2}
BuildRequires:  %{python_module pip >= 19.1}
BuildRequires:  %{python_module pytest >= 6}
BuildRequires:  %{python_module pytest-home >= 0.5}
BuildRequires:  %{python_module pytest-subprocess}
BuildRequires:  %{python_module pytest-timeout}
# BuildRequires:  %%{python_module pytest-xdist >= 3}
BuildRequires:  %{python_module setuptools = %{version}}
BuildRequires:  %{python_module setuptools-wheel = %{version}}
BuildRequires:  %{python_module tomli-w >= 1.0.0}
BuildRequires:  %{python_module virtualenv >= 13.0.0}
%endif
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Recommends:     ca-certificates-mozilla
%endif
%if "%{flavor}" == "primary"
Provides:       %{mypython}3-setuptools = %{version}-%{release}
%endif
%python_subpackages

%description
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages,
especially ones that have dependencies on other packages.

%package wheel
Summary:        The setuptools wheel for custom tests and install requirements
Requires:       %mypython(abi) = %python_version
%if "%{flavor}" == "primary"
Provides:       %{mypython}3-setuptools-wheel = %{version}-%{release}
%endif

%description wheel
This packages provides the setuptools wheel as separate file for cases where
the wheel needs to be used directly in test or install setups

%prep
%autosetup -p1 -n setuptools-%{version}

# Remove bundled exes
rm -f setuptools/*.exe

%build
%if %{without test}
%{python_expand # bootstrap with built-in pip
$python -m venv build/env
build/env/bin/python -m ensurepip
export PYTHONPATH=build/env/lib/python%{$python_bin_suffix}/site-packages
%{$python_pyproject_wheel}
}
%endif

%install
%if %{without test}
%{python_expand # use pip bootstrapped above
export PYTHONPATH=build/env/lib/python%{$python_bin_suffix}/site-packages
%{$python_pyproject_install}
%fdupes %{buildroot}%{$python_sitelib}
install -D -m 0644 -t %{buildroot}%{$python_sitelib}/../wheels dist/*.whl
}
%endif

%check
%if %{with test}
%{python_expand # just use the last one from the expansion, they're all the same
mkdir -p dist/
cp %{$python_sitelib}/../wheels/setuptools-%{version}-py3-none-any.whl $PWD/dist/
}
export PRE_BUILT_SETUPTOOLS_WHEEL=$PWD/dist/setuptools-%{version}-py3-none-any.whl
export LANG=en_US.UTF-8
export PIP_FIND_LINKS=$PWD/dist
# tests need imports from local source dir
export PYTHONPATH=$(pwd)
# no online comparisons in obs
donttest="(test_apply_pyproject_equivalent_to_setupcfg and https)"
# test_pbr_integration tries to install pbr from network using pip
donttest+=" or test_pbr_integration"
# looks for .exe files that we do not ship
donttest+=" or test_wheel_includes_cli_scripts"
# ignores environment variables
donttest+=" or test_setup_requires_with_distutils_command_dep"
donttest+=" or test_setup_requires_with_transitive_extra_dependency"
# skip tests that require network access
donttest+=" or uses_network"
%pytest -rfE -k "not ($donttest)"
%endif

%if %{without test}
%files %{python_files}
%if !%{with wheel}
%license LICENSE
%doc NEWS.rst README.rst
%{python_sitelib}/setuptools
%{python_sitelib}/setuptools-%{version}.dist-info
%dir %{python_sitelib}/pkg_resources
%{python_sitelib}/pkg_resources/*
%{python_sitelib}/_distutils_hack
%{python_sitelib}/distutils-precedence.pth
%endif

%files %{python_files wheel}
%dir %{python_sitelib}/../wheels
%{python_sitelib}/../wheels/*
%endif

%changelog
