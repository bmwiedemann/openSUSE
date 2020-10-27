#
# spec file for package python-py2pack
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
Name:           python-py2pack
Version:        0.8.5
Release:        0
Summary:        Script for generating distribution packages from Python packages on PyPI
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/openSUSE/py2pack
Source:         https://files.pythonhosted.org/packages/source/p/py2pack/py2pack-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module metaextract}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
# SECTION doc requirements
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinxcontrib-programoutput
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-metaextract
Requires:       python-pbr
Requires:       python-setuptools
Requires:       python-six
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

%build
%python_build
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/py2pack
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative py2pack

%postun
%python_uninstall_alternative py2pack

%files %{python_files}
%python_alternative %{_bindir}/py2pack
%{python_sitelib}/py2pack-%{version}-py*.egg-info
%{python_sitelib}/py2pack/

%files -n %{name}-doc
%license LICENSE
%doc AUTHORS
%doc doc/build/html/

%changelog
