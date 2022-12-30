#
# spec file for package python-fqdn
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


Name:           python-fqdn
Version:        1.5.1
Release:        0
Summary:        RFC-compliant FQDN validation and manipulation for Python
License:        MPL-2.0
URL:            https://github.com/ypcrts/fqdn
Source:         https://github.com/ypcrts/fqdn/archive/refs/tags/v%{version}.tar.gz#/fqdn-%{version}-gh.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module cached-property if %python-base < 3.8}
BuildRequires:  fdupes
%if %python_version_nodots < 38
Requires:       python-cached-property >= 1.3.0
%endif
BuildArch:      noarch
%python_subpackages

%description
This package validates Fully Qualified Domain Names (FQDNs) conforming to the
Internet Engineering Task Force specification . The design intent is to
validate that a string would be traditionally acceptable as a public Internet
hostname to RFC-conforming software, which is a strict subset of the logic in
modern web browsers like Mozilla Firefox and Chromium that determines whether
make a DNS lookup. Configuration options can relax constraints so that short
hostnames without periods or others with underscores will be valid. These
relaxations are closer to how modern web browsers work.


%prep
%setup -q -n fqdn-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/fqdn
%{python_sitelib}/fqdn-%{version}.dist-info

%changelog

