#
# spec file for package python-pip
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pip%{psuffix}
Version:        20.2.3
Release:        0
Summary:        A Python package management system
License:        MIT
URL:            http://www.pip-installer.org
# The PyPI archive lacks the tests
Source:         https://github.com/pypa/pip/archive/%{version}.tar.gz#/pip-%{version}-gh.tar.gz
# Wheel used for testing, no need to update regularly beyond the minimum version specified in 
# tools/requirements/tests-common_wheels.txt
Source1:        https://files.pythonhosted.org/packages/py3/s/setuptools/setuptools-45.1.0-py3-none-any.whl
# PATCH-FIX-OPENSUSE pip-shipped-requests-cabundle.patch -- adapted patch from python-certifi package
Patch0:         pip-shipped-requests-cabundle.patch
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       ca-certificates
Requires:       coreutils
Requires:       python-setuptools
Requires:       python-xml
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     ca-certificates-mozilla
BuildArch:      noarch
%if %{with test}
# Test requirements:
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module csv23}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scripttest}
BuildRequires:  %{python_module virtualenv >= 1.10}
BuildRequires:  %{python_module wheel}
BuildRequires:  ca-certificates
BuildRequires:  git
BuildRequires:  subversion
%endif
%python_subpackages

%description
Pip is a replacement for easy_install. It uses mostly the same techniques for
finding packages, so packages that were made easy_installable should be
pip-installable as well.

%prep
%setup -q -n pip-%{version}
# Unbundling is not advised by upstream. See src/pip/_vendor/README.rst
# Exception: Use our own cabundle. Adapted patch from python-certifi package
%patch0 -p1
rm src/pip/_vendor/certifi/cacert.pem

%if %{with test}
mkdir -p tests/data/common_wheels
cp %{SOURCE1} tests/data/common_wheels/
%endif
# remove shebangs verbosely (if only sed would offer a verbose mode...)
for f in $(find src -name \*.py -exec grep -l '^#!%{_bindir}/env' {} \;); do
    sed -i 's|^#!%{_bindir}/env .*$||g' $f
done

%build
%python_build

%if ! %{with test}
%install
%python_install
%prepare_alternative pip
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export PYTHONPATH=$(pwd)/build/lib
# no network on OBS
donttest="test_network or test_remote_reqs_parse"
# incompatible virtualenv version
donttest+=" or test_build_env_allow_only_one_install"
donttest+=" or test_build_env_isolation"
donttest+=" or test_build_env_requirements_check"
donttest+=" or test_build_env_overlay_prefix_has_priority"
donttest+=" or test_should_cache_git_sha"
# incompatible virtualenv version and no coverage wheel in common_wheels
donttest+=" or test_from_link_vcs_with_source_dir_obtains_commit_id"
donttest+=" or test_from_link_vcs_without_source_dir"
%pytest -k "not ($donttest)" tests/unit
%endif

%pre
# Since /usr/bin/pip became ghosted to be used with update-alternatives, we have to get rid
# of the old binary resulting from the non-update-alternatives-ified package:
[ -h %{_bindir}/pip ] || rm -f %{_bindir}/pip

%post
# can't use `python_install_alternative` because it's pipX.Y, not pip-X.Y
PRIO=$(echo %{python_version} | tr -d .)
%install_alternative pip %{_bindir}/pip%{python_version} $PRIO

%postun
%uninstall_alternative pip %{_bindir}/pip%{python_version}

%if ! %{with test}
%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt NEWS.rst README.rst
%python3_only %{_bindir}/pip
%{_bindir}/pip%{python_version}
%python2_only %{_bindir}/pip2
%python3_only %{_bindir}/pip3
%ghost %{_sysconfdir}/alternatives/pip
%{python_sitelib}/pip-%{version}-py%{python_version}.egg-info
%{python_sitelib}/pip
%endif

%changelog
