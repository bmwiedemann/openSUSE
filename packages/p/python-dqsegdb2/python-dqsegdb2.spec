#
# spec file for package python-dqsegdb2
#
# Copyright (c) 2025 SUSE LLC
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


# PYTHON2 NOT SUPPORTED FOR DEPENDENCY python-gwdatafind - TESTS FAIL
%define skip_python2 1

%global modname dqsegdb2
Name:           python-dqsegdb2
Version:        1.2.1
Release:        0
Summary:        Simplified python interface to the DQSEGDB API
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/duncanmmacleod/dqsegdb2
Source:         https://files.pythonhosted.org/packages/source/d/dqsegdb2/dqsegdb2-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-igwn-auth-utils
Requires:       python-ligo-segments
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module igwn-auth-utils}
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
# /SECTION
%python_subpackages

%description
DQSEGDB2 is a simplified Python implementation of the DQSEGDB API
as defined in LIGO-T1300625, providing a query interface for GET
requests to DQSEGDB.

%prep
%setup -q -n dqsegdb2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_query requires network
%pytest -k 'not test_query'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}.dist-info/

%changelog
