#
# spec file for package python-derpconf
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


Name:           python-derpconf
Version:        0.8.4
Release:        0
Summary:        Configuration file loader
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/globocom/derpconf
Source:         https://github.com/globocom/derpconf/archive/refs/tags/%{version}.tar.gz
# https://github.com/globocom/derpconf/issues/26
Patch0:         python-derpconf-no-six.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyVows}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
derpconf abstracts loading configuration files for your app.

%prep
%autosetup -p1 -n derpconf-%{version}

%build
sed -i '1{/^#!/ d}' derpconf/*.py
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pyvows

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/derpconf*

%changelog
