#
# spec file for package python-jinja2-time
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
%bcond_without test
Name:           python-jinja2-time
Version:        0.2.0
Release:        0
Summary:        Jinja2 Extension for Dates and Times
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hackebrot/jinja2-time
Source:         https://files.pythonhosted.org/packages/source/j/jinja2-time/jinja2-time-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-arrow
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module arrow}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
A Jinja2 extension providing support for dates and times.

%prep
%setup -q -n jinja2-time-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix}
}
%endif

%files %{python_files}
%license LICENSE
%doc HISTORY.rst README.rst
%{python_sitelib}/*

%changelog
