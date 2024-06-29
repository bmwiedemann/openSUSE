#
# spec file for package python-whitenoise
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-whitenoise
Version:        6.7.0
Release:        0
Summary:        Static file serving for WSGI applications
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/evansd/whitenoise
Source:         https://github.com/evansd/whitenoise/archive/%{version}.tar.gz#/whitenoise-%{version}.tar.gz
BuildRequires:  %{python_module Brotli >= 1.0.0}
BuildRequires:  %{python_module Django >= 2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-Brotli >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
Static file serving for WSGI applications.

%prep
%setup -q -n whitenoise-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
PYTHONPATH=$PWD
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/whitenoise
%{python_sitelib}/whitenoise-%{version}.dist-info

%changelog
