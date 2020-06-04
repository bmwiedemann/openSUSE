#
# spec file for package python-portalocker
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-portalocker
Version:        1.7.0
Release:        0
Summary:        Locking library for Python
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/WoLpH/portalocker
Source:         https://github.com/WoLpH/portalocker/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest >= 3.4.0}
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Portalocker is a library to provide an API to file locking.

On Linux and Unix systems, the locks are advisory by default. By
specifying the `-o mand` option to the mount command, it is possible
to enable mandatory file locking on Linux. This is generally not
recommended however.

%prep
%setup -q -n portalocker-%{version}
# do not bother with benchmark and cov
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
