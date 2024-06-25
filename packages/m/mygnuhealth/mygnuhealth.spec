#
# spec file for package mygnuhealth
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020-2024 Dr. Axel Braun
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


%define modname MyGNUHealth
%define majorver 2

%if %{?suse_version} > 1500
# only the primary one for TW
%define pythons python3
%define mypython python3
%define mypython_sitelib %{python3_sitelib}
%else
# needs Python 3.9+
%{?sle15_python_module_pythons}
# use the one define in sle15_python_module_pythons
%define mypython %pythons
%define mypython_sitelib %{expand:%%%{mypython}_sitelib}
%endif

Name:           mygnuhealth
Version:        %{majorver}.2.0
Release:        0
Summary:        The personal health record for the GNU Health system
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            http://health.gnu.org/
## Source:         https://files.pythonhosted.org/packages/source/m/%{name}/%{name}-%{version}.tar.gz  
Source:         https://ftp.gnu.org/gnu/health/mygnuhealth/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/health/mygnuhealth/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=health&download=1#/%{name}.keyring
Patch0:         remove-obsolete-deps.patch
# SECTION build
BuildRequires:  fdupes
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module pip}
BuildRequires:  update-desktop-files
BuildRequires:  python-rpm-macros
# /SECTION
# SECTION test requirements
# there are no tests, but at least check that all the runtime requirements are available on build time
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module Kivy}
BuildRequires:  %{python_module pygal}
BuildRequires:  %{python_module tinydb}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module CairoSVG}
Requires:       %{mypython}-dateutil
Requires:       %{mypython}-bcrypt
Requires:       %{mypython}-Kivy
Requires:       %{mypython}-pygal
Requires:       %{mypython}-tinydb
Requires:       %{mypython}-requests
Requires:       %{mypython}-CairoSVG
# /SECTION
## BuildArch:      noarch
# singlespec rewriter for exactly one python (see above)


%description
The Personal Health Information Management System for Desktop and Mobile Devices
for the GNU Health ecosystem

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# remove shebang
%python_expand sed -i '1{/env python/d}' %{buildroot}%{python_sitelib}/mygnuhealth/*.py

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications org.gnuhealth.mygnuhealth.desktop
%suse_update_desktop_file org.gnuhealth.mygnuhealth

%python_expand %fdupes %{buildroot}%{python_sitelib}

%post
#clean qml cache to avoid issues
rm -rf /home/*/.cache/mygnuhealth

%postun
#clean qml cache - housekeeping
rm -rf /home/*/.cache/mygnuhealth

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/org.gnuhealth.mygnuhealth.desktop
%license COPYRIGHT LICENSE
%{mypython_sitelib}/mygnuhealth
%{mypython_sitelib}/mygnuhealth-%{version}.dist-info

%changelog
