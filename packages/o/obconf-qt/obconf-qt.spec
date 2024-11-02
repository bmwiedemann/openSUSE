#
# spec file for package obconf-qt
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


Name:           obconf-qt
Version:        0.16.5
Release:        0
Summary:        OpenBox window manager configuration tool
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/obconf-qt
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets) >= 6.6.0
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     %{name}-lang
Conflicts:      obconf

%description
Configuration tool for the OpenBox Window Manager.
This tool is used by LXQt to configure OpenBox, since it is
used as the default WindowManager in LXQt.

%lang_package

%prep
%autosetup -p1

%build
%cmake_qt6
%qt6_build

%install
%qt6_install
install -dm 755 %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/obconf
ln -s %{_sysconfdir}/alternatives/obconf \
    %{buildroot}%{_bindir}/obconf

%find_lang %{name} --with-qt

%post
%{_sbindir}/update-alternatives --install \
    %{_bindir}/obconf \
    obconf \
    %{_bindir}/%{name} \
    40

%postun
if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove obconf \
        %{_bindir}/%{name}
fi

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_bindir}/obconf
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%ghost %{_sysconfdir}/alternatives/obconf

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%if 0%{?sle_version}
%{_datadir}/%{name}/translations/%{name}_???.qm
%endif

%changelog
