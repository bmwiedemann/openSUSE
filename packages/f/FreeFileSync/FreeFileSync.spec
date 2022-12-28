#
# spec file for package FreeFileSync
#
# Copyright (c) 2022 SUSE LLC
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


Name:           FreeFileSync
Version:        11.29
Release:        0
Summary:        Backup software to synchronize files and folders
License:        GPL-3.0-or-later
Group:          Productivity/Networking/System
URL:            https://www.freefilesync.org/
Source0:        %{name}_%{version}_Source.zip
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        RealTimeSync.desktop
Source4:        RealTimeSync.png
Patch0:         FreeFileSync-build.patch
Patch1:         FreeFileSync-resources.patch
Patch2:         FreeFileSync-icon-loader.patch
Patch3:         FreeFileSync-disable-in-app-updates.patch
Patch4:         FreeFileSync-openssl-1.1.1.patch
BuildRequires:  boost-devel >= 1.54
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libssh2-devel
BuildRequires:  libstdc++6 >= 10.0.0
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-3_2-devel >= 3.1.4

%description
FreeFileSync is a software that helps synchronizing files
and folders. It runs backup jobs while having visual
feedback along the way.

%package -n     RealtimeSync
Summary:        Backup software to synchronize files and folders
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}

%description -n RealtimeSync
RealtimeSync executes a command each time it detects changes
in one of the monitored directories, or when a directory becomes
available (e.g. insertion of a USB drive).
This command will usually trigger a FreeFileSync batch job.

%prep
%autosetup -p1 -c %{name}-%{version}
sed -i 's/\r$//' License.txt
mkdir FreeFileSync/Build/Bin

%build
export TMPDIR=/tmp # necessary since 11.0
export CXXFLAGS="%{optflags}"
export CC="gcc"
export CXX="g++"

%make_build -C %{name}/Source exeName=FreeFileSync
%make_build -C %{name}/Source/RealTimeSync exeName=RealTimeSync

%install
# FreeFileSync
pushd %{name}/Build
mkdir -p %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} Bin/%{name}

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -rT  Resources %{buildroot}%{_datadir}/%{name}

find "%{buildroot}%{_datadir}/%{name}" -type f -print0 | xargs -0 chmod 644
#%%make_install

# RealTimeSync
mkdir -p %{buildroot}%{_bindir}
install -t %{buildroot}%{_bindir} Bin/RealTimeSync
#%%make_install
popd

# desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -p %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/
install -p %{SOURCE4} %{buildroot}%{_datadir}/pixmaps/
%suse_update_desktop_file -i %{name}
%suse_update_desktop_file -i RealTimeSync

%filetriggerin -- %{_datadir}/applications
%{_bindir}/update-desktop-database --quiet %{_datadir}/applications || true

%filetriggerpostun -- %{_datadir}/applications
%{_bindir}/update-desktop-database --quiet %{_datadir}/applications || true

%files
%license License.txt
%doc Changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/*
%dir %{_datadir}/%{name}

%files -n RealtimeSync
%license License.txt
%doc Changelog.txt
%{_bindir}/RealTimeSync
%{_datadir}/applications/RealTimeSync.desktop
%{_datadir}/pixmaps/RealTimeSync.png

%changelog
