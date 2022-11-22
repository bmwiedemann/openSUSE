#
# spec file for package python-django-appconf
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


%define skip_python2 1
%define skip_python36 1
Name:           python-django-appconf
Version:        1.0.4
Release:        0
Summary:        A Helper Class for Handling Configuration Defaults of Packaged Apps
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/django-compressor/django-appconf
Source:         https://github.com/django-compressor/django-appconf/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django
BuildArch:      noarch
%python_subpackages

%description
A helper class for handling configuration defaults of packaged Django apps
gracefully.

%prep
%setup -q -n django-appconf-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export DJANGO_SETTINGS_MODULE=tests.test_settings
%pytest tests/tests.py

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst docs
%{python_sitelib}/appconf
%{python_sitelib}/django_appconf-%{version}*-info

%changelog
