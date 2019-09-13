#
# spec file for package python-docker-pycreds
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-docker-pycreds
Version:        0.4.0
Release:        0
Summary:        Python bindings for the Docker credentials store API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/shin-/dockerpy-creds
Source:         https://files.pythonhosted.org/packages/source/d/docker-pycreds/docker-pycreds-%{version}.tar.gz
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Recommends:     docker-credential-secretservice
BuildArch:      noarch
%python_subpackages

%description
This package contains the Python bindings for the Docker credentials
store API.

%prep
%setup -q -n docker-pycreds-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/

%check
# Can't run tests as they are depending on crendentials store to exist already
#%%python_expand py.test-%{$python_bin_suffix} .

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
