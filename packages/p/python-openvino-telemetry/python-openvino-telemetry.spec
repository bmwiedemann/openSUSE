#
# spec file for package python-openvino-telemetry
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


# Consistent with openvino
%define pythons python3
%define modname openvino_telemetry
Name:           python-openvino-telemetry
Version:        2025.0.0
Release:        0
Summary:        Module for use with openVINO toolkit to send usage statistics with user consent
License:        Apache-2.0
URL:            https://github.com/openvinotoolkit/telemetry
Source:         https://files.pythonhosted.org/packages/source/o/openvino-telemetry/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
OpenVINO Telemetry is a package for sending statistics with user's consent,
used in combination with other OpenVINO packages.

%prep
%autosetup -p1 -n %{modname}-%{version}
sed -Ei "s/\r$//" README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/opt_in_out
%{python_expand sed -i "1{\@/usr/bin/env python@d}" %{buildroot}%{$python_sitelib}/%{modname}/opt_in_out.py
%fdupes %{buildroot}%{$python_sitelib}
}

#%%check
# No tests

%post
%python_install_alternative opt_in_out

%postun
%python_uninstall_alternative opt_in_out

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/opt_in_out
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*-info/

%changelog
