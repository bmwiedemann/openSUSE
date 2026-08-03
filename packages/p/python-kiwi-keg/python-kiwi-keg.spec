#
# spec file for package python-kiwi-keg
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2022 SUSE Software Solutions Germany GmbH, Nuernberg, Germany.
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

%define upstream_name keg

Name:           python-kiwi-keg
Version:        2.2.1
Release:        0
URL:            https://github.com/SUSE-Enceladus/keg
Summary:        KEG - Image Composition Tool
Group:          Development/Tools/Building
License:        GPL-3.0-or-later
Source0:        %{upstream_name}-%{version}.tar.gz
BuildRequires:  %{pythons}-Jinja2
BuildRequires:  %{pythons}-Sphinx
BuildRequires:  %{pythons}-pip
BuildRequires:  %{pythons}-setuptools
BuildRequires:  %{pythons}-sphinx_rtd_theme
BuildRequires:  %{pythons}-wheel
BuildRequires:  fdupes
BuildRequires:  make
BuildRequires:  python-rpm-macros
Obsoletes:      python3-kiwi-keg < %{version}
Obsoletes:      python310-kiwi-keg < %{version}
Obsoletes:      python311-kiwi-keg < %{version}
Obsoletes:      python312-kiwi-keg < %{version}
Obsoletes:      python313-kiwi-keg < %{version}
BuildArch:      noarch
Requires:       %{pythons}-Jinja2
Requires:       %{pythons}-PyYAML
Requires:       %{pythons}-docopt
Requires:       %{pythons}-kiwi >= 9.21.21
Requires:       %{pythons}-schema

%description
KEG is an image composition tool for KIWI image descriptions

%package -n obs-service-compose_kiwi_description
Summary:        An OBS service: generate KIWI description using KEG
Requires:       %{name} = %{version}
Requires:       git

%description -n obs-service-compose_kiwi_description
This is a source service for openSUSE Build Service.

The source service produces a KIWI image description through KEG from one or
more given git repositories that contain keg-recipes source tree. It supports
auto-generation of change log files from commit history.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%pyproject_wheel
make -C doc man

%install
%pyproject_install
make buildroot=%{buildroot}/ docdir=%{_defaultdocdir}/ install
%fdupes %{buildroot}%{$python_sitelib}

%check

%files
%{_bindir}/%{upstream_name}
%{_bindir}/generate_recipes_changelog
%{_bindir}/update_kiwi_description
%{python_sitelib}/kiwi_keg*
%license LICENSE
%doc README.rst
%{_mandir}/man1/%{upstream_name}.1%{?ext_man}
%{_mandir}/man1/generate_recipes_changelog.1%{?ext_man}

# OBS service
%files -n obs-service-compose_kiwi_description
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/*

%changelog
