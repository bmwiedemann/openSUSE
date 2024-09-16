#
# spec file for package cosmic-player
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


%define         appname com.system76.CosmicPlayer
Name:           cosmic-player
Version:        0.1.0+git20240702.52b9439
Release:        0
Summary:        COSMIC media player
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-player
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Patch0:         ffmpeg-next.patch
Patch1:         ffmpeg-7.patch
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -N -a1
%patch -P0 -p1
%if 0%{?suse_version} >= 1600
%patch -P1 -p1
%endif

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install
%suse_update_desktop_file %{appname}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop

%changelog
