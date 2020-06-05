#
# spec file for package python-appdirs
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
Name:           python-appdirs
Version:        1.4.4
Release:        0
Summary:        A small Python module for determining platform-specific dirs
License:        MIT
URL:            https://github.com/ActiveState/appdirs
Source:         https://files.pythonhosted.org/packages/source/a/appdirs/appdirs-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
``appdirs`` will
help you choose an appropriate:

- user data dir (``user_data_dir``)
- user cache dir (``user_cache_dir``)
- site data dir (``site_data_dir``)
- user log dir (``user_log_dir``)

%prep
%setup -q -n appdirs-%{version}

# strip shebang
sed -r -i '1s/^#!.*$//' appdirs.py

%build
%python_build

%install
%python_install
# fix up egg-info because distutils is bad and should feel bad
%{python_expand rm %{buildroot}%{$python_sitelib}/*.egg-info
cp -r appdirs.egg-info \
    %{buildroot}%{$python_sitelib}/appdirs-%{version}-py%{$python_version}.egg-info
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec -munittest discover -v

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%pycache_only %{python_sitelib}/__pycache__/*
%{python_sitelib}/appdirs.py*
%{python_sitelib}/appdirs-%{version}-py%{python_version}.egg-info

%changelog
