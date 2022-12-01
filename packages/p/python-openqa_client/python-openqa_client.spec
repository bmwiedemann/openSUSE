#
# spec file for package python-openqa_client
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-openqa_client
Version:        4.2.1
Release:        0
Summary:        Python openQA client library
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/os-autoinst/openQA-python-client
Source:         https://github.com/os-autoinst/openQA-python-client/archive/refs/tags/%{version}.tar.gz#/python-openqa_client-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-requests
Requires:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
This is a client for the openQA API, based on requests.

%prep
%setup -q -n openQA-python-client-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitelib}/*
%pycache_only %{python_sitelib}/*/__pycache__/*

%changelog
