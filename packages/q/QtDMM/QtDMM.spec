#
# spec file for package QtDMM
#
# Copyright (c) 2024 SUSE LLC
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


Name:           QtDMM
Version:        0.9.8
Release:        0
Summary:        DMM Readout Software Including a Configurable Recorder
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/tuxmaster/QtDMM
Source:         https://github.com/tuxmaster/QtDMM/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM QtDMM-0.9.2-newmodels.patch
Patch0:         QtDMM-0.9.2-newmodels.patch
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.5
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
QtDMM is a DMM readout software including a configurable recorder. The
recorder features manual start, scheduled start (at a given time), and
triggered automatic start when given thresholds are reached.
Additionally, you can start an external application when given
thresholds are reached.

Although initially written for Metex (and compatible, like VOLTCRAFT)
multimeter, which use a 14-byte protocol, several more protocols have
been added. For more information about the currently supported DMMs,
refer to the preset table.

%prep
%autosetup -p1

# called lrelease in openSUSE
sed -i 's/lrelease-qt5/lrelease/' src/src.pro
sed -i 's/-fuse-ld=gold//' src/src.pro

%build
%qmake5
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install bin/qtdmm %{buildroot}%{_bindir}/qtdmm
install -Dm 644 qtdmm.1 %{buildroot}%{_mandir}/man1/qtdmm.1
install -Dm 644 qtdmm.png %{buildroot}%{_datadir}/pixmaps/qtdmm.png
install -Dm 644 QtDMM.desktop %{buildroot}%{_datadir}/applications/QtDMM.desktop
%suse_update_desktop_file -G "DMM Readout Software" -r %{name} "Education;Engineering"

%files
%license LICENSE
%doc CHANGELOG README
%{_bindir}/qtdmm
%{_mandir}/man1/qtdmm.1%{?ext_man}
%{_datadir}/pixmaps/qtdmm.png
%{_datadir}/applications/QtDMM.desktop

%changelog
