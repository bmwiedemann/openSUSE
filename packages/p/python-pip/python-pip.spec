#
# spec file for package python-pip
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
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

# in order to avoid rewriting for subpackage generator
%define mypython python
%{?sle15_python_module_pythons}
Name:           python-pip%{psuffix}
Version:        24.0
Release:        0
Summary:        A Python package management system
License:        MIT
URL:            https://pip.pypa.io
# The PyPI archive lacks the tests
Source:         https://github.com/pypa/pip/archive/%{version}.tar.gz#/pip-%{version}-gh.tar.gz
# PATCH-FIX-OPENSUSE pip-shipped-requests-cabundle.patch -- adapted patch from python-certifi package
Patch0:         pip-shipped-requests-cabundle.patch
# PATCH-FIX-UPSTREAM distutils-reproducible-compile.patch gh#python/cpython#8057 mcepl@suse.com
# To get reproducible builds, byte_compile() of distutils.util now sorts filenames.
Patch1:         distutils-reproducible-compile.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools >= 40.8.0}
# The rpm python-wheel build is bootstrap friendly since 0.42
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       ca-certificates
Requires:       coreutils
Recommends:     ca-certificates-mozilla
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%if %{with test}
# Test requirements:
BuildRequires:  %{python_module pip = %{version}}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module installer}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scripttest}
BuildRequires:  %{python_module setuptools-wheel}
BuildRequires:  %{python_module virtualenv >= 1.10}
BuildRequires:  ca-certificates
BuildRequires:  git-core
%endif
%python_subpackages

%description
Pip is a replacement for easy_install. It uses mostly the same techniques for
finding packages, so packages that were made easy_installable should be
pip-installable as well.

%package wheel
Summary:        The pip wheel for custom tests and install requirements
Requires:       %mypython(abi) = %python_version

%description wheel
This packages provides the pip wheel as separate file for cases where
the wheel needs to be used directly in test or install setups

%prep
# Unbundling is not advised by upstream. See src/pip/_vendor/README.rst
# Exception: Use our own cabundle. Adapted patch from python-certifi package
%autosetup -p1 -n pip-%{version}

rm src/pip/_vendor/certifi/cacert.pem

%if %{with test}
mkdir -p tests/data/common_wheels
%python_expand cp %{$python_sitelib}/../wheels/setuptools*.whl tests/data/common_wheels/
%endif
# remove shebangs verbosely (if only sed would offer a verbose mode...)
for f in $(find src -name \*.py -exec grep -l '^#!%{_bindir}/env' {} \;); do
    sed -i 's|^#!%{_bindir}/env .*$||g' $f
done

# Remove windows executable binaries
# bsc#1212015
rm -v src/pip/_vendor/distlib/*.exe
sed -i '/\.exe/d' setup.py

%build
%if !%{with test}
%{python_expand # bootstrap with built-in pip
$python -m venv build/env
build/env/bin/python -m ensurepip
export PYTHONPATH=build/env/lib/python%{$python_bin_suffix}/site-packages
%{$python_pyproject_wheel}
}
%endif

%install
%if !%{with test}
%{python_expand # use pip bootstrapped above
export PYTHONPATH=build/env/lib/python%{$python_bin_suffix}/site-packages
%{$python_pyproject_install}
install -D -m 0644 -t %{buildroot}%{$python_sitelib}/../wheels dist/*.whl
%fdupes %{buildroot}%{$python_sitelib}
}

%{python_expand # Fix shebang path for "pip3.XX" binaries
sed -i "1s|#\!.*python.*|#\!/usr/bin/$python|" %{buildroot}%{_bindir}/pip%{$python_bin_suffix}
}

%python_clone -a %{buildroot}%{_bindir}/pip
%python_clone -a %{buildroot}%{_bindir}/pip3
%python_expand %fdupes %{buildroot}%{_bindir}
%endif

%if %{with test}
%check
%pytest -m "not network" tests/unit
%endif

%pre
# Since /usr/bin/pip became ghosted to be used with update-alternatives, we have to get rid
# of the old binary resulting from the non-update-alternatives-ified package:
[ -h %{_bindir}/pip ] || rm -f %{_bindir}/pip
[ -h %{_bindir}/pip3 ] || rm -f %{_bindir}/pip3
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pip

%post
# keep the alternative groups separate. Users could decide to let pip and pip3 point to
# different flavors
%python_install_alternative pip
%python_install_alternative pip3

%postun
%python_uninstall_alternative pip
%python_uninstall_alternative pip3

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt NEWS.rst README.rst
%python_alternative %{_bindir}/pip
%python_alternative %{_bindir}/pip3
%{_bindir}/pip%{python_bin_suffix}
%{python_sitelib}/pip-%{version}.dist-info
%{python_sitelib}/pip

%files %{python_files wheel}
%dir %{python_sitelib}/../wheels
%{python_sitelib}/../wheels/*
%endif

%changelog
