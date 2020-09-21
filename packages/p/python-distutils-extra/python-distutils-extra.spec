#
# spec file for package python-distutils-extra
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
Name:           python-distutils-extra
Version:        2.39
Release:        0
Summary:        Distutils/Setuptools Adapter
License:        GPL-2.0-only
Group:          Development/Libraries/Python
Url:            https://launchpad.net/python-distutils-extra
Source:         http://launchpad.net/python-distutils-extra/trunk/%{version}/+download/python-distutils-extra-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
This package adds support for common build additions to distutils.
This includes the following:

  * gettext/i18n
  * documentation
  * program icons

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc doc/*
%license LICENSE
%{python_sitelib}/*

%changelog
