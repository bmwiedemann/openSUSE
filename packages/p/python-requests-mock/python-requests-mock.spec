#
# spec file for package python-requests-mock
#
# Copyright (c) 2023 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-requests-mock
Version:        1.11.0
Release:        0
Summary:        Module to mock out responses from the requests package
License:        Apache-2.0
URL:            https://github.com/jamielennox/requests-mock
Source:         https://files.pythonhosted.org/packages/source/r/requests-mock/requests-mock-%{version}.tar.gz
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module purl}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.3}
BuildRequires:  %{python_module requests-futures}
BuildRequires:  %{python_module six}
BuildRequires:  python-rpm-macros
%if 0%{suse_version} >= 1550 || (0%{?suse_version} == 1500 && 0%{?sle_version} >= 154000)
BuildRequires:  %{python_module dbm}
%else
BuildRequires:  python3-dbm
%endif
BuildRequires:  fdupes
Requires:       python-requests >= 2.3
Requires:       python-six
Requires:       python-urllib3 < 2
BuildArch:      noarch
Requires:       python-dbm
%python_subpackages

%description
requests-mock provides a building block to stub out the HTTP requests portions of your testing code.
You should checkout the docs for more information.

%prep
%autosetup -p1 -n requests-mock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst ChangeLog
%{python_sitelib}/requests_mock*

%changelog
