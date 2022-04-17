#
# spec file for package python-cloud-sptheme
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-cloud-sptheme
Version:        1.10.1.post20200504175005
Release:        0
Summary:        Sphinx theme named 'Cloud', and some related extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://cloud-sptheme.readthedocs.io
Source:         https://files.pythonhosted.org/packages/source/c/cloud_sptheme/cloud_sptheme-%{version}.tar.gz
# PATCH-FIX-UPSTREAM sphinx-4-compat.patch -- https://foss.heptapod.net/doc-utils/cloud_sptheme/-/issues/45
Patch0:         sphinx-4-compat.patch
# PATCH-FIX-UPSTREAM 0002-patch-jinja-markup-deprecation.patch -- https://foss.heptapod.net/doc-utils/cloud_sptheme/-/issues/47 https://github.com/conda-forge/cloud_sptheme-feedstock/pull/12
Patch1:         https://raw.githubusercontent.com/melund/cloud_sptheme-feedstock/d09095170b329b4f6502479662b9114717a6a230/recipe/0002-patch-jinja-markup-deprecation.patch
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION docs
BuildRequires:  python3-Sphinx
BuildRequires:  python3-importlib-metadata >= 4.4
BuildRequires:  python3-pip
BuildRequires:  python3-sphinxcontrib-fulltoc
BuildRequires:  python3-wheel
# /SECTION
BuildArch:      noarch

%python_subpackages

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/HTML

%description
This package contains the Sphinx theme named "Cloud",
along with some related Sphinx extensions.

%description -n %{name}-doc
HTML documentation and examples for %name.

%prep
%setup -q -n cloud_sptheme-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build
PYTHONPATH=. python3 setup.py build_sphinx -E
rm build/sphinx/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/*
%doc CHANGES README
%license LICENSE

%files -n %{name}-doc
%doc build/sphinx/html/

%changelog
