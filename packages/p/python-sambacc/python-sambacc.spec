#
# spec file
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


%global bname sambacc

Name:           python-%{bname}
Version:        v0.2+git.56.9d8b892
Release:        0
Summary:        Samba Container Configurator
License:        GPL-3.0-or-later
URL:            https://github.com/samba-in-kubernetes/sambacc
Source:         %{bname}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python3-pyxattr
Requires:       samba-python3

%python_subpackages

%description
A Python library intended to act as a bridge between a container
environment and Samba servers and utilities. It aims to consolidate, coordinate and
automate all of the low level steps of setting up smbd, users, groups, and other
supporting components.

%package -n %{bname}
Summary:        %{summary}
Requires:       python3-%{bname}

%description -n %{bname}
A set of CLI tools intended to act as a bridge between a container
environment and Samba servers and utilities. It aims to consolidate, coordinate and
automate all of the low level steps of setting up smbd, users, groups, and other
supporting components.

%prep
%autosetup -n %{bname}-%{version}

%generate_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/%{bname}-*.dist-info
%python_expand find %{buildroot}%{$python_sitelib} -name *.pyc -delete
sed -i 's;python%{python_version};python3;g' %{buildroot}/%{_bindir}/samba-container
sed -i 's;python%{python_version};python3;g' %{buildroot}/%{_bindir}/samba-dc-container

%files %{python_files}
%{python_sitelib}/%{bname}

%files -n %{bname}
%doc README.*
%{_bindir}/samba-container
%{_bindir}/samba-dc-container
%{_datadir}/%{bname}

%changelog
