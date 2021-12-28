#
# spec file
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%bcond_with wheel
%else
%if "%{flavor}" == "wheel"
%define psuffix -wheel
%bcond_without wheel
%else
%define psuffix %{nil}
%bcond_with test
%bcond_with wheel
%endif
%endif
# in order to avoid rewriting for subpackage generator
%define mypython python
Name:           python-setuptools%{psuffix}
Version:        57.4.0
Release:        0
Summary:        Download, build, install, upgrade, and uninstall Python packages
License:        MIT
URL:            https://github.com/pypa/setuptools
Source:         https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
Patch0:         sort-for-reproducibility.patch
# PATCH-FIX-OPENSUSE remove_mock.patch mcepl@suse.com
Patch1:         remove_mock.patch
# PATCH-FIX-OPENSUSE remove-more-itertools-dependency-cycle.patch alarrosa@suse.com
Patch2:         remove-more-itertools-dependency-cycle.patch
BuildRequires:  %{python_module appdirs >= 1.4.3}
BuildRequires:  %{python_module ordered-set >= 3.1.1}
BuildRequires:  %{python_module packaging >= 20.4}
BuildRequires:  %{python_module pyparsing >= 2.2.1}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs >= 1.4.3
Requires:       python-base >= 3.6
Requires:       python-ordered-set >= 3.1.1
Requires:       python-packaging >= 20.4
Requires:       python-pyparsing >= 2.2.1
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Paver}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module jaraco.envs}
BuildRequires:  %{python_module jaraco.path >= 3.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-fixture-config}
BuildRequires:  %{python_module pytest-virtualenv}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= %{version}}
BuildRequires:  %{python_module virtualenv >= 13.0.0}
BuildRequires:  %{python_module wheel}
%endif
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Recommends:     ca-certificates-mozilla
%endif
%if %{with wheel}
BuildRequires:  %{python_module wheel}
%endif
%if !%{with test} && !%{with wheel}
# work around boo#1186870
Provides:       %{mypython}%{python_version}dist(setuptools) = %{version}
Provides:       %{mypython}%{python_version}dist(pkg_resources) = %{version}
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       %{mypython}3dist(pkg_resources) = %{version}
Provides:       %{mypython}3dist(setuptools) = %{version}
%endif
%endif
%python_subpackages

%description
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages,
especially ones that have dependencies on other packages.

%prep
%autosetup -p1 -n setuptools-%{version}

# strip shebangs to fix rpmlint warnings
# "explain the sed":
# 1 = first line only
# s@...@...@ = same as s/.../.../ except with @ instead of /
# ^ = start; #!/ = shebang leading characters; .* = rest of line; $ = end
# replace with nothing
sed -r -i '1s@^#!/.*$@@' pkg_resources/_vendor/appdirs.py

%if ! %{with wheel}
# replace the bundled stuff
find ./ -type f -name \*.py -exec sed -i \
  -e 's:from setuptools\.extern\.:from :g' \
  -e 's:from pkg_resources\.extern\.:from :g' \
  -e 's:pkg_resources\.extern\.::g' \
  -e 's:setuptools\.extern\.::g' \
  {} \;
find ./ -type f -name \*.py -exec sed -i \
  -e 's:from setuptools\.extern ::g' \
  -e 's:from pkg_resources\.extern ::g' \
  {} \;
find ./ -type f -name \*.py -exec sed -i  \
  -e 's:from .extern ::g' \
  {} \;
%endif

%build
%if ! %{with wheel}
%python_build
%else
%python_exec setup.py bdist_wheel --universal
%endif

%install
%if !%{with test} && !%{with wheel}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with wheel}
%python_expand install -D -m 0644 -t %{buildroot}%{$python_sitelib}/../wheels dist/*.whl
%endif

%check
%if %{with test}
# the 4 skipped test rely on the bundled packages but they are
# not available on virtualenv; this is expected behaviour
donttest="test_clean_env_install or test_pip_upgrade_from_source or test_test_command_install_requirements or test_no_missing_dependencies"
# these 3 tests try to download the wheel wheel from PyPI
donttest="$donttest or (test_distutils_adoption and (distutils_stdlib or distutils_local))"
export LANG=en_US.UTF-8
# tests need imports local source dir
export PYTHONPATH=$(pwd)
%pytest -rfE -n auto -k "not ($donttest)"
%endif

%if !%{with test}
%files %{python_files}
%if !%{with wheel}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/setuptools
%{python_sitelib}/setuptools-%{version}-py%{python_version}.egg-info
%dir %{python_sitelib}/pkg_resources
%{python_sitelib}/pkg_resources/*
%{python_sitelib}/_distutils_hack
%{python_sitelib}/distutils-precedence.pth
%endif

%if %{with wheel}
%dir %{python_sitelib}/../wheels
%{python_sitelib}/../wheels/*
%endif
%endif

%changelog
