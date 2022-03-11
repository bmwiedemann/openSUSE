#
# spec file for package mygnuhealth
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2020-2021 Dr. Axel Braun
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
%define majorver 1

#boo#1181905
%global __requires_exclude qmlimport\\((BloodPressure|FedLogin|GHBio|GHBol|GHPsycho|Glucose|LocalAccountManager|MoodEnergy|NetworkSettings|Osat|ProfileSettings|Weight|PoL|GHLifestyle|GHPhysicalActivity|GHNutrition|GHSleep|GHAbout)

Name:           mygnuhealth
Version:        %{majorver}.0.5
Release:        0
Summary:        The personal health record for the GNU Health system
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            http://health.gnu.org/
Source:         https://ftp.gnu.org/gnu/health/mygnuhealth/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/health/mygnuhealth/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/project/memberlist-gpgkeys.php?group=health&download=1#/%{name}.keyring
Patch0:         shebang.diff
Patch1:         doc_path.diff
BuildRequires:  fdupes
BuildRequires:  python3-bcrypt
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pyside2 >= 5.15
BuildRequires:  python3-setuptools
BuildRequires:  python3-tinydb
BuildRequires:  update-desktop-files
Requires:       kirigami2
Requires:       python3-bcrypt
Requires:       python3-matplotlib
Requires:       python3-pyside2 >= 5.15
Requires:       python3-requests
Requires:       python3-tinydb

%description
The Personal Health Information Management System for Desktop and Mobile Devices
for the GNU Health ecosystem

%package -n %{name}-doc
Summary:        Documentation files for MyGNUHealth
Group:          Productivity/Office/Management
BuildArch:      noarch

%description -n %{name}-doc
This package includes the documentation for MyGNUHealth Personal Health
Information Management System for Desktop and Mobile Devices

%prep
%setup -q
%autopatch -p1

%build
%python3_build

%install
%python3_install --prefix=%{_prefix} --root=%{buildroot}

# menu-entry
desktop-file-install --dir %{buildroot}%{_datadir}/applications org.kde.mygnuhealth.desktop
%suse_update_desktop_file org.kde.mygnuhealth

#documentation in the MyGNUHealth-doc package is sufficient
rm -rf %{buildroot}%{_docdir}/*

%python_expand %fdupes %{buildroot}%{python3_sitelib}

%post
#clean qml cache to avoid issues
rm -rf /home/*/.cache/mygnuhealth

%postun
#clean qml cache - housekeeping
rm -rf /home/*/.cache/mygnuhealth

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/org.kde.mygnuhealth.desktop
%{_datadir}/icons/*
%{_datadir}/metainfo/*
%license COPYRIGHT LICENSE
%{python3_sitelib}/*

%files -n %{name}-doc
%doc README.rst doc/*

%changelog
