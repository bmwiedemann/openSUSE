#
# spec file for package python-pyrrd
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define skip_python3 1
%define modname PyRRD
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyrrd
Version:        0.1.0
Release:        0
Summary:        An Object-Oriented Python Interface for RRD
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://code.google.com/p/pyrrd/
Source:         https://files.pythonhosted.org/packages/source/P/PyRRD/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-xml
Requires:       rrdtool
BuildArch:      noarch
%python_subpackages

%description
PyRRD is a pure-Python OO wrapper for the RRDTool (round-robin database tool).
The idea is to make RRDTool insanely easy to use and to be aesthetically
pleasing for Python programmers.

%package -n %{name}-docs
Summary:        Documentation files for %{name}
Group:          Documentation/Other

%description -n %{name}-docs
HTML Documentation and examples for %{name}.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc ChangeLog README TODO
%{python_sitelib}/pyrrd
%{python_sitelib}/PyRRD-*.egg-info

%files -n %{name}-docs
%doc examples docs

%changelog
