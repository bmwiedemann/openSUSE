#
# spec file for package python-casttube
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-casttube
Version:        0.2.1
Release:        0
Summary:        YouTube chromecast api
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ur1katz/casttube
Source:         https://files.pythonhosted.org/packages/source/c/casttube/casttube-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-requests
%python_subpackages

%description
casttube provides a way to interact with the Youtube Chromecast api.

%prep
%setup -q -n casttube-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
rm -v %{buildroot}%{_prefix}/LICENSE

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/casttube
%{python_sitelib}/casttube-%{version}*-info

%changelog
