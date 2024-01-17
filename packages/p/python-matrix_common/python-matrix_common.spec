#
# spec file for package python-matrix_common
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


%define skip_python39 1
Name:           python-matrix_common
Version:        1.3.0
Release:        0
Summary:        Common utilities for Synapse, Sydent and Sygnal
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/matrix-python-common
Source:         https://github.com/matrix-org/matrix-python-common/archive/refs/tags/v%{version}.tar.gz#/matrix-python-common-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs
Provides:       python-matrix-common = %{version}-%{release}
BuildArch:      noarch
%python_subpackages

%description
Common utilities for Synapse, Sydent and Sygnal.

%prep
%setup -q -n matrix-python-common-%{version}

%build
export PYTHONPATH=$PWD
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/matrix_common-%{version}*-info
%{python_sitelib}/matrix_common

%changelog
