#
# spec file for package python-ndjson
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


Name:           python-ndjson
Version:        0.3.1
Release:        0
Summary:        JsonDecoder for ndjson
License:        GPL-3.0-or-later
URL:            https://github.com/rhgrant10/ndjson
Source:         https://files.pythonhosted.org/packages/source/n/ndjson/ndjson-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
JsonDecoder for ndjson

%prep
%autosetup -p1 -n ndjson-%{version}

sed -i -e '/^setup_requirements = \['pytest-runner', \]/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CONTRIBUTING.rst HISTORY.rst AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/ndjson
%{python_sitelib}/ndjson-%{version}*-info

%changelog
