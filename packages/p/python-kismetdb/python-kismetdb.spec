#
# spec file for package python-kismetdb
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
%define binaries kismet_log_devices_to_filebeat_json kismet_log_to_pcap kismet_log_to_csv kismet_log_devices_to_json kismet_log_to_kml
Name:           python-kismetdb
Version:        2019.05.05
Release:        0
Summary:        A python wrapper for the Kismet database
License:        GPL-2.0-only
URL:            https://github.com/kismetwireless/python-kismet-db
Source:         https://github.com/kismetwireless/python-kismet-db/archive/%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
Requires:       python-simplekml
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Kismet database wrapper.

%prep
%setup -q -n python-kismet-db-%{version}

%build
%python_build

%install
%python_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are disabled for now since those need a docker environment for testing
#%%pytest

%post
for b in %{binaries}; do
  %python_install_alternative $b
done

%postun
for b in %{binaries}; do
  %python_uninstall_alternative $b
done

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%python_alternative %{_bindir}/kismet_log_to_kml
%python_alternative %{_bindir}/kismet_log_devices_to_json
%python_alternative %{_bindir}/kismet_log_to_csv
%python_alternative %{_bindir}/kismet_log_to_pcap
%python_alternative %{_bindir}/kismet_log_devices_to_filebeat_json
%{python_sitelib}/*

%changelog
