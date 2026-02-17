#
# spec file for package python-frozendict
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-frozendict
Version:        2.4.7
Release:        0
Summary:        An immutable dictionary
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Marco-Sulla/python-frozendict
Source:         https://files.pythonhosted.org/packages/source/f/frozendict/frozendict-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install

%check
%pytest_arch

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitearch}/frozendict-%{version}.dist-info
%{python_sitearch}/frozendict

%changelog
