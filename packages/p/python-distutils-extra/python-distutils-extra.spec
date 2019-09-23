#
# spec file for package python-distutils-extra
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-distutils-extra
Version:        2.38
Release:        0
Summary:        Distutils/Setuptools Adapter
License:        GPL-2.0-only
Group:          Development/Libraries/Python
Url:            https://launchpad.net/python-distutils-extra
Source:         http://launchpad.net/python-distutils-extra/trunk/%{version}/+download/python-distutils-extra-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package adds support for common build additions to distutils. This
includes the follwing:

  * gettext/i18n
  * documentation
  * program icons

%prep
%setup -q

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root)
%doc doc/*
%license LICENSE
%{python_sitelib}/*

%changelog
