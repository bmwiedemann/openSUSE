#
# spec file for package python-jsmin
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


%global skip_python2 1
Name:           python-jsmin
Version:        3.0.1
Release:        0
Summary:        JavaScript minifier
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tikitu/jsmin/
Source:         https://files.pythonhosted.org/packages/source/j/jsmin/jsmin-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
JavaScript minifier.

%prep
%setup -q -n jsmin-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v jsmin/

%files %{python_files}
%doc CHANGELOG.txt README.rst
%license LICENSE.txt
%{python_sitelib}/jsmin
%{python_sitelib}/jsmin-%{version}*-info

%changelog
