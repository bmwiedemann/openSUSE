#
# spec file for package python-django-webpack-loader
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-django-webpack-loader
Version:        1.8.1
Release:        0
Summary:        Django plugin to transparently use webpack
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/owais/django-webpack-loader
Source:         https://github.com/owais/django-webpack-loader/archive/%{version}.tar.gz
BuildRequires:  %{python_module Django >= 1.10}
BuildRequires:  %{python_module django-jinja}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
# tests are not currently run; transition unittest2
#BuildRequires:  %%{python_module unittest2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.10
Recommends:     python-django-jinja
BuildArch:      noarch
%python_subpackages

%description
webpack can be used to generate static bundles without Django's
staticfiles or opaque wrappers.

%prep
%setup -q -n django-webpack-loader-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd tests
export DJANGO_SETTINGS_MODULE='app.settings'
# The tests are not working without nodejs webpack package
#%%pytest
popd

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitelib}/*

%changelog
