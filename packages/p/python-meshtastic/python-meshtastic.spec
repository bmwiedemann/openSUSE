#
# spec file for package python-meshtastic
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


Name:           python-meshtastic
Version:        2.5.11
Release:        0
Summary:        A Python client for use with Meshtastic devices
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/meshtastic/python
Source:         https://files.pythonhosted.org/packages/source/m/meshtastic/meshtastic-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 6.0.1
Requires:       python-bleak >= 0.22.3
Requires:       python-packaging
Requires:       python-protobuf >= 4.21.12
Requires:       python-pypubsub >= 4.0.3
Requires:       python-pyserial >= 3.5
Requires:       python-requests >= 2.31.0
Requires:       python-tabulate >= 0.9.0
Requires(post): alts
Requires(postun): alts
Recommends:     python-dbus-fast
BuildArch:      noarch
%python_subpackages

%description
A Python client for use with Meshtastic devices. This small library (and example application) provides an easy API for sending and receiving messages over mesh radios. It also provides access to any of the operations/data available in the device user interface or the Android application. Events are delivered using a publish-subscribe model, and you can subscribe to only the message types you are interested in.

%prep
%setup -q -n meshtastic-%{version}

# Remove hidden file
rm -v meshtastic/.gitignore

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/mesh-analysis
%python_clone -a %{buildroot}%{_bindir}/mesh-tunnel
%python_clone -a %{buildroot}%{_bindir}/meshtastic

%post
%python_install_alternative mesh-analysis
%python_install_alternative mesh-tunnel
%python_install_alternative meshtastic

%postun
%python_uninstall_alternative mesh-analysis
%python_uninstall_alternative mesh-tunnel
%python_uninstall_alternative meshtastic

%files %{python_files}
%license LICENSES/GPL-3.0-only.txt
%doc README.md
%python_alternative %{_bindir}/mesh-analysis
%python_alternative %{_bindir}/mesh-tunnel
%python_alternative %{_bindir}/meshtastic
%{python_sitelib}/meshtastic
%{python_sitelib}/meshtastic-%{version}*-info

%changelog
