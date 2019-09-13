#
# spec file for package plasma5-applet-suse-prime
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:			plasma5-applet-suse-prime
Version:		1.1
Release:		0
Summary:		Plasma 5 applet for controlling SUSE Prime
License:		Unlicense
Group:			System/GUI/KDE
URL:			https://github.com/Appadeia/plasma5-applet-suse-prime
Source0:		%{name}-%{version}.tar.gz
BuildRequires:	extra-cmake-modules
BuildRequires:	cmake(KF5Plasma)
Requires:		libqt5-qdbus
Requires:		kdialog
Supplements:	(plasma5-workspace and suse-prime)
BuildArch:		noarch

%description
A Plasma 5 applet for controlling SUSE Prime.

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%files
%license LICENSE
%doc README.md

%dir %{_kf5_plasmadir}/plasmoids

%{_kf5_plasmadir}/plasmoids/org.kde.plasma.prime/
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.prime.desktop
%{_kf5_appstreamdir}/org.kde.plasma.prime.appdata.xml


%changelog
