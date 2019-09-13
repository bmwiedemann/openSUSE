#
# spec file for package python-fysom
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-fysom
Version:        2.1.5
Release:        0
Summary:        Python Finite State Machine
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mriehl/fysom
Source:         https://files.pythonhosted.org/packages/source/f/fysom/fysom-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A standalone Python micro-framework providing a finite state machine.

%prep
%setup -q -n fysom-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover test/ -v

%files %{python_files}
%doc CHANGELOG README
%license README
%{python_sitelib}/*

%changelog
