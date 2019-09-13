#
# spec file for package python-flup
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-flup
Version:        1.0.3.dev20161029
Release:        0
Url:            http://www.saddi.com/software/flup/
Summary:        Random assortment of WSGI servers
License:        BSD-2-Clause
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/flup/flup-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Documentation build requirements:
BuildRequires:  python3-Sphinx
BuildArch:      noarch

%python_subpackages

%description
A random collection of WSGI modules for Python

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module flup-doc = %{version}}

%description -n %{name}-doc
This package contains HTML documentation for %{name}.

%prep
%setup -q -n flup-%{version}

%build
%python_build
python3 setup.py build_sphinx && rm docs/build/html/.buildinfo

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%files -n %{name}-doc
%defattr(-,root,root)
%doc docs/build/html/

%changelog
