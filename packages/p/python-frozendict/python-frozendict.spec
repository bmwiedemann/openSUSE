#
# spec file for package python-frozendict
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
# as of 2.3.5: if you want to enable 3.11 you would need to disable the C extension test for 3.11 otherwise the build will fails in %check
%define skip_python311 1
# Do not enable multibuild unless seriously necessary, it in
# combination with arch is a right mess!
Name:           python-frozendict
Version:        2.3.5
Release:        0
Summary:        An immutable dictionary
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Marco-Sulla/python-frozendict
Source:         https://files.pythonhosted.org/packages/source/f/frozendict/frozendict-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
frozendict is an immutable wrapper around dictionaries that implements the
complete mapping interface. It can be used as a drop-in replacement for
dictionaries where immutability is desired.

%prep
%setup -q -n frozendict-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/frozendict-%{version}-py*.egg-info/
%{python_sitearch}/frozendict

%changelog
