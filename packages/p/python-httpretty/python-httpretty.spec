#
# spec file for package python-httpretty
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
Name:           python-httpretty
Version:        0.9.6
Release:        0
Summary:        HTTP client mocking tool for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/gabrielfalcao/HTTPretty
Source:         https://files.pythonhosted.org/packages/source/h/httpretty/httpretty-%{version}.tar.gz
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module rednose}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sure}
BuildRequires:  %{python_module tornado}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This library allows mocking of HTTP protocol based
unit tests.
It is similar to Ruby's FakeWeb.

%prep
%setup -q -n httpretty-%{version}
# randomly is unknown option for our nose
sed -i -e '/with-randomly/d' setup.cfg

%build
%python_build

%check
%python_exec setup.py test

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/httpretty
%{python_sitelib}/httpretty*egg-info

%changelog
