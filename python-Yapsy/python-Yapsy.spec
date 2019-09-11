#
# spec file for package python-Yapsy
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
Name:           python-Yapsy
Version:        1.12.2
Release:        0
Summary:        Yet another plugin system
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://yapsy.sourceforge.net
Source:         https://files.pythonhosted.org/packages/source/Y/Yapsy/Yapsy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION docs
BuildRequires:  python-Sphinx
# /SECTION
Provides:       python-yapsy
Suggests:       %{name}-doc
BuildArch:      noarch

%{python_subpackages}

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML

%description
Yapsy is a small library implementing the core mechanisms needed to
build a plugin system into a wider application.

The main purpose is to depend only on Python's standard libraries (at
least version 2.3) and to implement only the basic functionalities
needed to detect, load and keep track of several plugins.

%description -n %{name}-doc
HTML documentation files for %{name}.

%prep
%setup -q -n Yapsy-%{version}

%build
%{python_build}
find yapsy/ -name "*.py" -exec sed -i -e  '/^#!\s\?\/usr\/bin\/\(env\s\)\?python$/d' {} ';'
pushd doc
make html
#rm _build/html/.buildinfo
popd

%install
%{python_install}
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
%{python_exec setup.py test}

%files %{python_files}
%{python_sitelib}/*
%doc CHANGELOG.txt README.txt
%license LICENSE.txt

%files -n %{name}-doc
%doc doc/_build/html
%doc artwork

%changelog
