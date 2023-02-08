#
# spec file for package udica
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


Name:           udica
Version:        0.2.6
Release:        0
Summary:        A tool for generating SELinux security policies for containers
License:        GPL-3.0-or-later
URL:            https://github.com/containers/udica
Source0:        https://github.com/containers/udica/archive/v%{version}.tar.gz
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# container-selinux provides policy templates
Requires:       container-selinux >= 2.168.0-2
Requires:       python3
Requires:       python3-selinux
Requires:       python3-semanage
Requires:       python3-setuptools
BuildArch:      noarch

%description
Tool for generating SELinux security profiles for containers based on
inspection of container JSON file.

%prep
%autosetup -p 1

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed --root=%{buildroot}

install --directory %{buildroot}%{_mandir}/man8
install -m 0644 udica/man/man8/udica.8 %{buildroot}%{_mandir}/man8/udica.8

%files
%{_mandir}/man8/udica.8%{?ext_man}
%{_bindir}/udica
%dir %{_datadir}/udica
%dir %{_datadir}/udica/ansible
%{_datadir}/udica/ansible/*

%license LICENSE
%{python3_sitelib}/udica/
%{python3_sitelib}/udica-*.egg-info

%changelog
