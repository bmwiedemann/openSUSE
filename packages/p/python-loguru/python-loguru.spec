#
# spec file for package python-loguru
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-loguru
Version:        0.3.2
Release:        0
License:        MIT
Summary:        Python logging component with a simple interface
Url:            https://github.com/Delgan/loguru
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/l/loguru/loguru-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Recommends:     python-colorama
BuildArch:      noarch

%python_subpackages

%description
Python logging component providing a single object
which dispatches log messages to configured handlers.

%prep
%setup -q -n loguru-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
