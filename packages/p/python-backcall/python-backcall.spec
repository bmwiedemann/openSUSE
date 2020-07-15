#
# spec file for package python-backcall
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
Name:           python-backcall
Version:        0.2.0
Release:        0
Summary:        Specifications for callback functions passed in to an API
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/takluyver/backcall
Source0:        https://files.pythonhosted.org/packages/source/b/backcall/backcall-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
#
%python_subpackages

%description
If code lets other people supply callback functions, it is important
to specify the function signature that is being expected, and to
check that functions support that. Adding extra parameters later
would break other peoples code unless one is careful.
backcall provides a way of specifying the callback signature using a
prototype function.

%prep
%setup -q -n backcall-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/backcall
%{python_sitelib}/backcall-%{version}-py*.egg-info

%changelog
