#
# spec file for package python-radexreader
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


Name:           python-radexreader
Version:        1.3.0
Release:        0
Summary:        Reader for the RADEX RD1212 and ONE Geiger counters
License:        GPL-2.0-or-later
URL:            https://github.com/luigifab/python-radexreader
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pyusb}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyserial
Requires:       python-pyusb
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The RadexReader is an user-space driver for the RADEX RD1212 and
the RADEX ONE Geiger counters. It allow to read and clear stored
data via USB.

To avoid Access denied (insufficient permissions), don't forget
to unplug the device after installation.

%prep
%setup -q -n python-radexreader-%{version}
sed -i 's/radexreader-local /python3-radexreader-rpm /g' src/radexreader-cli.py
sed -i 's/\#\!\/usr\/bin\/python3/\#/g' src/radexreader/__init__.py

%build
cd src
%pyproject_wheel

%install
cd src
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -Dpm 755 radexreader-cli.py %{buildroot}%{_bindir}/radexreader
install -Dpm 644 ../data/radexreader.bash %{buildroot}%{_datadir}/bash-completion/completions/radexreader
install -Dpm 644 ../data/radexreader.1 %{buildroot}%{_mandir}/man1/radexreader.1
install -Dpm 644 ../data/radexreader.fr.1 %{buildroot}%{_mandir}/fr/man1/radexreader.1
%python_clone -a %{buildroot}%{_bindir}/radexreader
%python_clone -a %{buildroot}%{_datadir}/bash-completion/completions/radexreader
%python_clone -a %{buildroot}%{_mandir}/man1/radexreader.1
%python_clone -a %{buildroot}%{_mandir}/fr/man1/radexreader.1
%python_expand install -Dpm 644 ../scripts/debian/python3-radexreader.udev %{buildroot}%{_udevrulesdir}/60-python%{$python_bin_suffix}-radexreader.rules

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/radexreader
%{python_sitelib}/radexreader-%{version}.dist-info
%python_alternative %{_bindir}/radexreader
%python_alternative %{_datadir}/bash-completion/completions/radexreader
%python_alternative %{_mandir}/man1/radexreader.1%{?ext_man}
%python_alternative %{_mandir}/fr/man1/radexreader.1%{?ext_man}
%{_udevrulesdir}/60-python%{python_bin_suffix}-radexreader.rules

%post
%{python_install_alternative radexreader radexreader.1}

%postun
%{python_uninstall_alternative radexreader radexreader.1}

%changelog
