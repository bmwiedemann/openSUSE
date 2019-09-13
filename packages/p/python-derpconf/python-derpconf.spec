#
# spec file for package python-derpconf
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
Name:           python-derpconf
Version:        0.8.3
Release:        0
Summary:        Configuration file loader
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/globocom/derpconf
Source:         https://github.com/globocom/derpconf/archive/v%{version}.tar.gz#/derpconf-%{version}.tar.gz
BuildRequires:  %{python_module pyVows}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
derpconf abstracts loading configuration files for your app.

%prep
%setup -q -n derpconf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pyvows

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
