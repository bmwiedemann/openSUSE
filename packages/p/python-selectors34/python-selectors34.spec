#
# spec file for package python-selectors34
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
%if %python3_version_nodots >= 34
%define         skip_python3 1
%endif
Name:           python-selectors34
Version:        1.2
Release:        0
Summary:        Backport of the selectors module from Python 3.4
License:        Python-2.0
Group:          Development/Languages/Python
Url:            https://github.com/berkerpeksag/selectors34
Source:         https://files.pythonhosted.org/packages/source/s/selectors34/selectors34-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  python-mock
# /SECTION
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
Selectors3* is a backport of the selectors module from Python 3.4. The
selectors module written by Charles-François Natali. This port is based on
Victor Stinner's ``trollius/selectors.py`` port.

%prep
%setup -q -n selectors34-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix} tests/
}

%files %{python_files}
%defattr(-,root,root,-)
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
