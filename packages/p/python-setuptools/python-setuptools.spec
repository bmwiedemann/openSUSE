#
# spec file for package python-setuptools
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%bcond_without python2
Name:           python-setuptools%{psuffix}
Version:        44.0.0
Release:        0
Summary:        Enhancements to distutils for building and distributing Python packages
License:        MIT
URL:            https://github.com/pypa/setuptools
Source:         https://files.pythonhosted.org/packages/source/s/setuptools/setuptools-%{version}.zip
Source3:        testdata.tar.gz
Patch0:         sort-for-reproducibility.patch
Patch1:         importlib.patch
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module ordered-set}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pyparsing >= 2.0.2}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-appdirs
Requires:       python-base
Requires:       python-ordered-set
Requires:       python-packaging
Requires:       python-six
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# The dependency download feature may require SSL, which is in python3-base and python(2)
%ifpython2
Requires:       python
%endif
%if %{with test}
BuildRequires:  %{python_module Paver}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-fixture-config}
BuildRequires:  %{python_module pytest-virtualenv}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= %{version}}
BuildRequires:  %{python_module wheel}
%if %{with python2}
BuildRequires:  python-futures
%endif
%endif
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Recommends:     ca-certificates-mozilla
%endif
%ifpython2
Provides:       %{oldpython}-distribute = %{version}
Obsoletes:      %{oldpython}-distribute < %{version}
%endif
%python_subpackages

%description
setuptools is a collection of enhancements to the Python distutils that
allow you to build and distribute Python packages,
especially ones that have dependencies on other packages.

%prep
%setup -q -n setuptools-%{version}
tar -xzvf %{SOURCE3}
%patch0 -p1
%patch1 -p1
find . -type f -name "*.orig" -delete

# fix rpmlint spurious-executable-perm
chmod -x README.rst

# strip shebangs to fix rpmlint warnings
# "explain the sed":
# 1 = first line only
# s@...@...@ = same as s/.../.../ except with @ instead of /
# ^ = start; #!/ = shebang leading characters; .* = rest of line; $ = end
# replace with nothing
sed -r -i '1s@^#!/.*$@@' setuptools/command/easy_install.py

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

%build
%python_build

%install
%if !%{with test}
%python_install
%prepare_alternative easy_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# the 4 skipped test rely on the bundled packages but they are
# not available on virtualenv; this is expected behaviour
export LANG=en_US.UTF-8
# tests need imports local source dir
export PYTHONPATH=$(pwd)
%pytest -k 'not (test_clean_env_install or test_pip_upgrade_from_source or test_test_command_install_requirements or test_no_missing_dependencies)'
%endif

%if !%{with test}
%post
%python_install_alternative easy_install

%postun
%python_uninstall_alternative easy_install

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/easy_install
%{python_sitelib}/setuptools
%{python_sitelib}/setuptools-%{version}-py%{python_version}.egg-info
%{python_sitelib}/easy_install.py*
%pycache_only %{python_sitelib}/__pycache__/easy_install.*
%dir %{python_sitelib}/pkg_resources
%{python_sitelib}/pkg_resources/*
%endif

%changelog
