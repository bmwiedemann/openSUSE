#
# spec file for package python-tortilla
#
# Copyright (c) 2025 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-tortilla
Version:        0.5.0
Release:        0
Summary:        A library for creating wrappers around web APIs
License:        MIT
URL:            https://github.com/jcarbaugh/python-tortilla
Source:         https://github.com/tortilla/tortilla/archive/v%{version}.tar.gz#/tortilla-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module formats}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/tortilla
%{python_sitelib}/tortilla-%{version}.dist-info

%changelog
