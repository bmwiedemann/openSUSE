#
# spec file for package python-openqa_client
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-openqa_client
Version:        1.3.0
Release:        0
Summary:        Python openQA client library
License:        GPL-2.0+
Group:          Development/Languages/Python
Url:            https://github.com/os-autoinst/openQA-python-client
Source:         %{name}-%{version}.tar.xz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This is a client for the openQA API, based on requests.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitelib}/*
%pycache_only %{python_sitelib}/*/__pycache__/*

%changelog
