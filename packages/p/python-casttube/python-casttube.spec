#
# spec file for package python-casttube
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
Name:           python-casttube
Version:        0.2.0
Release:        0
Summary:        YouTube chromecast api
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/ur1katz/casttube
Source:         https://files.pythonhosted.org/packages/source/c/casttube/casttube-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/ur1katz/casttube/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
casttube provides a way to interact with the Youtube Chromecast api.

%prep
%setup -q -n casttube-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
