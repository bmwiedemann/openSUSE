#
# spec file for package python-gwdatafind
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-gwdatafind
Version:        2.1.0
Release:        0
License:        GPL-3.0-only
Summary:        Client library for the LIGO Data Replicator (LDR) service
URL:            https://gwdatafind.readthedocs.io/
Source:         https://files.pythonhosted.org/packages/source/g/gwdatafind/gwdatafind-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module igwn-auth-utils}
BuildRequires:  %{python_module igwn-segments}
BuildRequires:  %{python_module pytest >= 3.9.3}
BuildRequires:  %{python_module requests-mock}
# /SECTION
BuildRequires:  fdupes
Requires:       python-igwn-auth-utils
Requires:       python-igwn-segments
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
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/gw_data_find

%check
%pytest -k 'not (test_find_urls or test_find_frame_urls or test_postprocess_cache_gaps)'

%post
%python_install_alternative gw_data_find

%postun
%python_uninstall_alternative gw_data_find

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/gw_data_find
%{python_sitelib}/gwdatafind
%{python_sitelib}/gwdatafind-%{version}.dist-info

%changelog
