#
# spec file for package python-javaproperties
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


Name:           python-javaproperties
Version:        0.8.1
Release:        0
Summary:        Read & Write Java Properties Files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jwodder/javaproperties
Source:         https://files.pythonhosted.org/packages/source/j/javaproperties/javaproperties-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-mock >= 2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Read & write Java .properties files.

%prep
%autosetup -p1 -n javaproperties-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i -e '/--cov/d' -e '/--no-cov/d' -e '/--flakes/d' -e '/--doctest-modules/d' tox.ini
export LC_ALL='en_US.UTF-8'
export TZ=EST5EDT,M3.2.0,M11.1.0
%pytest test

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/javaproperties*

%changelog
