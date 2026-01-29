#
# spec file for package python-gcemetadata
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


%if 0%{?suse_version} >= 1600
%define pythons %{primary_python}
%else
%{?sle15_python_module_pythons}
%endif
%global _sitelibdir %{%{pythons}_sitelib}

%define upstream_name gcemetadata
Name:           python-gcemetadata
Version:        1.1.0
Release:        0
Summary:        Python module for collecting instance metadata from GCE
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/SUSE/Enceladus
Source0:        %{upstream_name}-%{version}.tar.bz2
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      python3-gcemetadata < %{version}
Obsoletes:      python310-gcemetadata < %{version}
Obsoletes:      python311-gcemetadata < %{version}
Obsoletes:      python312-gcemetadata < %{version}
Obsoletes:      python313-gcemetadata < %{version}
BuildArch:      noarch

%description
A module for collecting instance metadata from Google Compute Engine.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/gcemetadata.1 %{buildroot}/%{_mandir}/man1
%fdupes %{buildroot}%{_sitelibdir}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{upstream_name}
%{_sitelibdir}/%{upstream_name}
%{_sitelibdir}/%{upstream_name}-%{version}*-info
%{_mandir}/man1/%{upstream_name}.1%{?ext_man}

%changelog
