#
# spec file for package python-requests-mock
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
Name:           python-requests-mock
Version:        1.8.0
Release:        0
Summary:        Module to mock out responses from the requests package
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/jamielennox/requests-mock
Source:         https://files.pythonhosted.org/packages/source/r/requests-mock/requests-mock-%{version}.tar.gz
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module purl}
BuildRequires:  %{python_module purl}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.3}
BuildRequires:  %{python_module rpm-macros}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
Requires:       python-requests >= 2.3
Requires:       python-six
BuildArch:      noarch
%ifpython3
BuildRequires:  python3-dbm
Requires:       python3-dbm
%endif
%python_subpackages

%description
requests-mock provides a building block to stub out the HTTP requests portions of your testing code.
You should checkout the docs for more information.

%prep
%setup -q -n requests-mock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/pytest

mv .testr.conf .testr.conf.orig
%{python_expand # first line can't be empty
rm -rf .testrepository
sed 's/python/$python/' .testr.conf.orig >| .testr.conf
testr init
testr run --parallel
}

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst ChangeLog
%{python_sitelib}/*

%changelog
