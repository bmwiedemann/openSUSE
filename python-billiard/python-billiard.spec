#
# spec file for package python-billiard
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-billiard
Version:        3.6.0.0
Release:        0
Summary:        Python multiprocessing fork
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/celery/billiard
Source:         https://files.pythonhosted.org/packages/source/b/billiard/billiard-%{version}.tar.gz
BuildRequires:  %{python_module case >= 1.3.1}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-devel
# Documentation requirements
BuildRequires:  python3-Sphinx >= 0.5
Suggests:       %{name}-doc = %{version}
%ifpython3
BuildArch:      noarch
%endif

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Development/Languages/Python
Provides:       %{python_module billiard-doc = %{version}}
BuildArch:      noarch
%python_subpackages

%description
billiard is a fork of the Python 2.7 multiprocessing package. The
multiprocessing package itself is a renamed and updated version of
R. Oudkerk's pyprocessing package. This standalone variant is
compatible with Python 2.4 and 2.5, and will draw its
fixes/improvements from python-trunk.

%description -n %{name}-doc
Documentation and help files for %{name}.

%prep
%setup -q -n billiard-%{version}

%build
%python_build
pushd Doc
sphinx-build -b html . html
rm -r html/.buildinfo html/.doctrees
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%python3_only %{python_sitelib}/*
%python2_only %{python_sitearch}/*

%files -n %{name}-doc
%doc Doc/html

%changelog
