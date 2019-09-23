#
# spec file for package utox
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


%define realname uTox
Name:           utox
Version:        0.17.1
Release:        0
Summary:        The lightweight Tox client
License:        MIT
Group:          Productivity/Networking/Instant Messenger
URL:            https://utox.org/
Source:         https://github.com/uTox/uTox/releases/download/v%{version}/%{realname}-%{version}-full.tar.gz
Source1:        https://github.com/uTox/uTox/releases/download/v%{version}/%{realname}-%{version}-full.tar.gz.asc
Source2:        uTox.keyring
BuildRequires:  c-toxcore-devel
BuildRequires:  cmake >= 3.2
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  filter_audio-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libv4l-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)

%description
Lightweight Tox client.

%prep
%setup -q -n %{realname}

%build
%cmake \
      -DENABLE_ASAN=OFF \
      -DENABLE_TESTS=OFF \
      -DENABLE_AUTOUPDATE=OFF \
      -DENABLE_LTO=ON
%make_jobs V=1

%install
%cmake_install
%suse_update_desktop_file -r %{name} Network Telephony

%fdupes %{buildroot}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/icons/hicolor/14x14
%dir %{_datadir}/icons/hicolor/14x14/apps
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/*/apps/%{name}-*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
