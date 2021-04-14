#
# spec file for package python-gwdatafind
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

# PYTHON2 NOT SUPPORTED - TESTS FAIL
%define skip_python2 1

Name:           python-gwdatafind
Version:        1.0.4
Release:        0
License:        GPL-3.0
Summary:        Client library for the LIGO Data Replicator (LDR) service
Url:            https://gwdatafind.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/g/gwdatafind/gwdatafind-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module ligo-segments}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module pytest >= 2.8.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-ligo-segments
Requires:       python-pyOpenSSL
Requires:       python-six
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives

%python_subpackages

%description
The client library for the LIGO Data Replicator (LDR) service.

The DataFind service allows users to query for the location of
Gravitational-Wave Frame (GWF) files containing data from the current
gravitational-wave detectors

%prep
%setup -q -n gwdatafind-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/gw_data_find

%check
%pytest

%post
%python_install_alternative gw_data_find

%postun
%python_uninstall_alternative gw_data_find

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/gw_data_find
%{python_sitelib}/*

%changelog
