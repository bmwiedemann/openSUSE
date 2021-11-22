#
# spec file for package python-magicalimport
#
# Copyright (c) 2021 SUSE LLC
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
%define skip_python2 1
Name:           python-magicalimport
Version:        0.9.1
Release:        0
Summary:        Importing Python modules by physical file path
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/podhmo/magicalimport
Source:         https://github.com/podhmo/magicalimport/archive/%{version}.tar.gz#/magicalimport-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Importing Python modules by physical file path.

%prep
%setup -q -n magicalimport-%{version}

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/examples
 %fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.rst examples/
%license LICENSE
%{python_sitelib}/magicalimport*

%changelog
