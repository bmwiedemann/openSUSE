#
# spec file for package python-py2pack
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


Name:           python-py2pack
Version:        0.9.1
Release:        0
Summary:        Script for generating distribution packages from Python packages on PyPI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/openSUSE/py2pack
Source:         https://files.pythonhosted.org/packages/source/p/py2pack/py2pack-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module backports.entry_points_selectable}
BuildRequires:  %{python_module build}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module metaextract}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module pypi-search}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomli if %python_base < 3.11}
BuildRequires:  %{python_module wheel}
# SECTION doc requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinxcontrib-programoutput
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-backports.entry_points_selectable
Requires:       python-build
Requires:       python-metaextract
Requires:       python-packaging
Requires:       python-platformdirs
Requires:       python-pypi-search
Requires:       python-requests
Requires:       python-setuptools
Requires:       (python-tomli if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This script allows to generate RPM spec or DEB dsc files from Python modules.
It allows to list Python modules or search for them on the Python Package Index
(PyPI). Conveniently, it can fetch tarballs and changelogs making it an
universal tool to package Python modules.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Development/Languages/Python
Provides:       %{python_module py2pack-doc = %{version}}

%description -n %{name}-doc
Documentation and help files for %{name}.

%prep
%setup -q -n py2pack-%{version}
# remove shebang
sed -i '1{/#!/d}' py2pack/__init__.py
chmod -x py2pack/__init__.py

%build
export PBR_VERSION=0.9.0

%pyproject_wheel

# build docs, cli.rst needs py2pack as executable
mkdir -p build/directbin/
cat <<EOF > build/directbin/py2pack
#!%{__python3}
import sys
import py2pack
sys.exit(py2pack.main())
EOF
chmod +x build/directbin/py2pack
export PATH="$PWD/build/directbin/:$PATH"
export PYTHONPATH=$PWD
sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/py2pack
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires network
donttest="test_list or test_newest_download_url or test_search or test_show or test_template"
%pytest -k "not ($donttest)"

%post
%python_install_alternative py2pack

%postun
%python_uninstall_alternative py2pack

%files %{python_files}
%python_alternative %{_bindir}/py2pack
%{python_sitelib}/py2pack-%{version}.dist-info
%{python_sitelib}/py2pack/

%files -n %{name}-doc
%license LICENSE
%doc doc/build/html/

%changelog
