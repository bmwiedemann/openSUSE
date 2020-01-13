#
# spec file for package python-efilter
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
Name:           python-efilter
Version:        1.6.0
Release:        0
Summary:        EFILTER query language
License:        Apache-2.0
URL:            https://github.com/rekall-innovations/efilter
Source0:        https://github.com/rekall-innovations/efilter/archive/v%{version}.tar.gz
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-future
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-six >= 1.4.0
BuildArch:      noarch
%python_subpackages

%description
EFILTER is a general-purpose destructuring and search language implemented in Python, and suitable for integration with any Python project that requires a search function for some of its data.

%prep
%setup -q -n efilter-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc AUTHORS.txt README.md
%{python_sitelib}/efilter*
%{python_sitelib}/rekall_efilter*
%exclude %{python_sitelib}/sample_projects

%changelog
