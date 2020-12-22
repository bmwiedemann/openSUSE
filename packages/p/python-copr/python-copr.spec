#
# spec file for package python-copr
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
Name:           python-copr
Version:        1.106
Release:        0
Summary:        Python client for copr service
License:        GPL-2.0+
URL:            https://pagure.io/copr/copr
Source:         https://files.pythonhosted.org/packages/source/c/copr/copr-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module marshmallow}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module munch}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module six}
# /SECTION
BuildRequires:  fdupes
Requires:       python-marshmallow
Requires:       python-munch
Requires:       python-requests
Requires:       python-requests-toolbelt
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Python client for copr service.

%prep
%setup -q -n copr-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
