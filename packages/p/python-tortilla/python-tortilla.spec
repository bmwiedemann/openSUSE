#
# spec file for package python-kismet-rest
#
# Copyright (c) 2016-2020, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-tortilla
Version:        0.5.0
Release:        0
Summary:        A library for creating wrappers around web APIs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jcarbaugh/python-tortilla
Source:         https://github.com/tortilla/tortilla/archive/v%{version}.tar.gz#/tortilla-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module formats}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
Requires:       python-colorama
Requires:       python-formats
Requires:       python-httpretty
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Wrapping web APIs made easy.
A tiny library for creating wrappers around web APIs.

%prep
%setup -q -n tortilla-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/tortilla*

%changelog
