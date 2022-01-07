#
# spec file for package python-django-dj-inmemorystorage
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
%define skip_python36 1
Name:           python-django-dj-inmemorystorage
Version:        2.1.0
Release:        0
Summary:        A non-persistent in-memory data storage backend for Django
License:        BSD-3-Clause
URL:            https://github.com/waveaccounting/dj-inmemorystorage
Source:         https://files.pythonhosted.org/packages/source/d/dj-inmemorystorage/dj-inmemorystorage-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
An in-memory data storage backend for Django.

Compatible with Django's storage API.

%prep
%setup -q -n dj-inmemorystorage-%{version}

%build
# We need unicode locale to overcome python issue with non-ascii character in
# LICENSE file
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
export DJANGO_SETTINGS_MODULE=inmemorystorage.test_settings
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
