#
# spec file for package python-traitlets
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-traitlets
Version:        4.3.2
Release:        0
Summary:        Traitlets Python config system
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://ipython.org
Source:         https://files.pythonhosted.org/packages/source/t/traitlets/traitlets-%{version}.tar.gz
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module ipython_genutils}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-enum34
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module pytest}
# Python 2 test requirements
BuildRequires:  python-mock
Requires:       python-decorator
Requires:       python-ipython_genutils
Requires:       python-six
%ifpython2
Requires:       python-enum34
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
A configuration system for Python applications.

%prep
%setup -q -n traitlets-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
pushd docs
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix} ../traitlets/tests
}

%files %{python_files}
%defattr(-,root,root,-)
%doc examples/
%{python_sitelib}/traitlets/
%{python_sitelib}/traitlets-%{version}-py*.egg-info

%changelog
