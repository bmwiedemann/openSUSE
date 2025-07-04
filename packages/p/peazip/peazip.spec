#
# spec file for package peazip
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


%define         _peazipinstalldir %{_libdir}/peazip

Name:           peazip
Version:        10.5.0
Release:        0
Summary:        Graphical file archiver
License:        LGPL-3.0-only
Group:          Productivity/Archiving/Compression
URL:            https://peazip.github.io/
Source0:        https://github.com/peazip/PeaZip/releases/download/%{version}/peazip-%{version}.src.zip
Source1:        altconf.txt
Source2:        https://github.com/peazip/PeaZip/releases/download/%{version}/peazip_help.pdf
Patch0:         peazip-desktop.patch
# PATCH-FIX-OPENSUSE peazip-build_PIE.patch -- aloisio@gmx.com
Patch1:         peazip-build_PIE.patch
# PATCH-FIX-OPENSUSE peazip-help_path.patch set correct path for the pdf guide -- aloisio@gmx.com
Patch2:         peazip-help_path.patch
# PATCH-FEATURE-OPENSUSE peazip-debuginfo.patch
Patch3:         peazip-debuginfo.patch
BuildRequires:  arc
BuildRequires:  brotli
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  kf5-filesystem
BuildRequires:  lazarus-ide
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  lazarus-tools
BuildRequires:  libX11-devel
BuildRequires:  unzip
BuildRequires:  upx
BuildRequires:  zpaq
BuildRequires:  zstd
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150100
BuildRequires:  p7zip-full
Requires:       p7zip-full
%else
BuildRequires:  p7zip
Requires:       p7zip
%endif
Requires:       upx
Suggests:       arc
Suggests:       brotli
Suggests:       zpaq
Suggests:       zstd

%description
PeaZip is a file and archive manager GUI for many formats.

Create: 7Z, ARC, BZ2, GZ, *PAQ, PEA, QUAD/BALZ, TAR, UPX, WIM, XZ, ZIP files

Extract 150+ archive types: ACE, ARJ, CAB, DMG, ISO, LHA, RAR, UDF, ZIPX and more

It can extract, create and convert multiple archives at once,
create self-extracting archives, split/join files, supports strong encryption with two-factor authentication,
has an encrypted password manager, secure deletion, can find duplicate files, calculate hashes, and
export job definition as a script.

%if 0%{?suse_version} < 1690
%package kf5
Summary:        KF5 servicemenu for peazip
Group:          Productivity/Archiving/Compression
Requires:       peazip
BuildArch:      noarch

%description kf5
PeaZip is a file and archive manager GUI for many formats.
This subpackage contains the KF5 integration.
%else

%package kf6
Summary:        KF6 servicemenu for peazip
Group:          Productivity/Archiving/Compression
Requires:       peazip
BuildArch:      noarch

%description kf6
PeaZip is a file and archive manager GUI for many formats.
This subpackage contains the KF6 integration.
%endif

%prep
%autosetup -p1 -n %{name}-%{version}.src
chmod +w res/share/lang
dos2unix readme.txt
mv res/share/copying/copying.txt .
cp %{SOURCE2} peazip_help.pdf

%build
cd dev
lazbuild --add-package metadarkstyle/metadarkstyle.lpk
# Add additional packages to vanilla Lazarus
lazbuild \
	--lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=qt6 \
  --max-process-count=1 \
	-B --add-package metadarkstyle/metadarkstyle.lpk
# Build Peazip
lazbuild \
	--lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=qt6 \
  --max-process-count=1 \
	-B project_pea.lpi project_peach.lpi

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_peazipinstalldir}
cp -r res %{buildroot}%{_peazipinstalldir}
cp %{SOURCE1} %{buildroot}%{_peazipinstalldir}/res

mkdir -p %{buildroot}%{_peazipinstalldir}/res/bin/7z
mkdir -p %{buildroot}%{_peazipinstalldir}/res/bin/upx
ln -s %{_bindir}/7z  %{buildroot}%{_peazipinstalldir}/res/bin/7z/7z
ln -s %{_bindir}/upx  %{buildroot}%{_peazipinstalldir}/res/bin/upx/upx

mkdir -p %{buildroot}%{_peazipinstalldir}/res/bin/arc
mkdir -p %{buildroot}%{_peazipinstalldir}/res/bin/brotli
mkdir -p %{buildroot}%{_peazipinstalldir}/res/bin/zpaq
mkdir -p %{buildroot}%{_peazipinstalldir}/res/bin/zstd
ln -s %{_bindir}/arc  %{buildroot}%{_peazipinstalldir}/res/bin/arc/arc
ln -s %{_bindir}/brotli  %{buildroot}%{_peazipinstalldir}/res/bin/brotli/brotli
ln -s %{_bindir}/zpaq  %{buildroot}%{_peazipinstalldir}/res/bin/zpaq/zpaq
ln -s %{_bindir}/zstd  %{buildroot}%{_peazipinstalldir}/res/bin/zstd/zstd

install -m755 dev/peazip %{buildroot}%{_peazipinstalldir}
ln -s %{_peazipinstalldir}/peazip %{buildroot}%{_bindir}/peazip
install -m755 dev/pea %{buildroot}%{_peazipinstalldir}/res
ln -s %{_peazipinstalldir}/res/pea %{buildroot}%{_bindir}/pea

mkdir -p  %{buildroot}%{_datadir}/applications/
cp %{buildroot}%{_peazipinstalldir}/res/share/batch/freedesktop_integration/peazip.desktop %{buildroot}%{_datadir}/applications/
rm %{buildroot}%{_peazipinstalldir}/res/share/batch/freedesktop_integration/peazip.desktop
# Remove duplicate comment line
sed -i '/Comment=PeaZip/d' %{buildroot}%{_datadir}/applications/peazip.desktop
# Set correct category
sed -i 's/Categories=Qt;KDE;Utility;System;Archiving;/Categories=Qt;KDE;Utility;Archiving;/' %{buildroot}%{_datadir}/applications/peazip.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{buildroot}%{_peazipinstalldir}/res/share/batch/freedesktop_integration/peazip.png %{buildroot}%{_datadir}/pixmaps/
rm %{buildroot}%{_peazipinstalldir}/res/share/batch/freedesktop_integration/peazip.png

chmod +x %{buildroot}%{_peazipinstalldir}/res/share/batch/freedesktop_integration/Nautilus-scripts/PeaZip/*
%if 0%{?suse_version} < 1690
pushd %{buildroot}%{_peazipinstalldir}/res/share/batch/freedesktop_integration/KDE-servicemenus/KDE5-dolphin/
mkdir -p %{buildroot}%{_kf5_servicesdir}/ServiceMenus
install -m644 *.desktop %{buildroot}%{_kf5_servicesdir}/ServiceMenus
%else
pushd %{buildroot}%{_peazipinstalldir}/res/share/batch/freedesktop_integration/KDE-servicemenus/KDE6-dolphin/
mkdir -p %{buildroot}%{_datadir}/kio/servicemenus
install -m644 *.desktop %{buildroot}%{_datadir}/kio/servicemenus/
%endif
popd
# Remove hard linked png
rm %{buildroot}%{_peazipinstalldir}/res/share/icons/peazip.png

find %{buildroot} -type f -size 0 -delete

%fdupes %{buildroot}/%{_prefix}

%files
%license copying.txt
%doc readme.txt peazip_help.pdf
%{_bindir}/pea
%{_bindir}/peazip
%{_peazipinstalldir}
%{_datadir}/applications/peazip.desktop
%{_datadir}/pixmaps/peazip.png

%if 0%{?suse_version} < 1690
%files kf5
%dir %{_kf5_servicesdir}/ServiceMenus
%{_kf5_servicesdir}/ServiceMenus/*.desktop
%else

%files kf6
%dir %{_datadir}/kio
%dir %{_datadir}/kio/servicemenus
%{_datadir}/kio/servicemenus/*.desktop
%endif

%changelog
