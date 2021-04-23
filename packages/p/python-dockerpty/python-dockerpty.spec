#
# spec file for package python-dockerpty
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname dockerpty
Name:           python-dockerpty
Version:        0.4.1
Release:        0
Summary:        Docker API Client
License:        Apache-2.0
Group:          System/Management
URL:            https://pypi.python.org/pypi/dockerpty
Source0:        https://github.com/d11wtq/dockerpty/archive/v%{version}.tar.gz
BuildRequires:  %{python_module expects}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2
Requires:       python-docker
Requires:       python-six >= 1.3.0
%ifpython2
Requires:       python2
%endif
BuildArch:      noarch
%python_subpackages

%description
Provides the functionality needed to operate the pseudo-tty (PTY) allocated to
a docker container, using the Python client.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand py.test-%{$python_bin_suffix} -v tests/

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*

%changelog
