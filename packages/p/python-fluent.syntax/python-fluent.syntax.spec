#
# spec file for package python-fluent.syntax
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


Name:           python-fluent.syntax
Version:        0.19.0
Release:        0
Summary:        Localization library for expressive translations
License:        Apache-2.0
URL:            https://github.com/projectfluent/python-fluent
Source:         https://github.com/projectfluent/python-fluent/archive/refs/tags/fluent.syntax@%{version}.tar.gz#/fluent.syntax-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module typing-extensions >= 3.7}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-typing-extensions >= 3.7
Provides:       python-fluent = %{version}
Obsoletes:      python-fluent < %{version}
BuildArch:      noarch
%python_subpackages

%description
Localization library for expressive translations.

%prep
%autosetup -p1 -n python-fluent-fluent.syntax-%{version}

%build
pushd fluent.syntax
%pyproject_wheel
popd

%install
pushd fluent.syntax
%pyproject_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd fluent.syntax
%pytest
popd

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/fluent
%{python_sitelib}/fluent.syntax-%{version}.dist-info

%changelog
