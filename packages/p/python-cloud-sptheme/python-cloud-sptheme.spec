#
# spec file for package python-cloud-sptheme
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
Name:           python-cloud-sptheme
Version:        1.10.1.post20200504175005
Release:        0
Summary:        Sphinx theme named 'Cloud', and some related extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://cloud-sptheme.readthedocs.io
Source:         https://files.pythonhosted.org/packages/source/c/cloud_sptheme/cloud_sptheme-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION docs
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinxcontrib-fulltoc
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

%build
%python_build
python3 setup.py build_sphinx -E
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
