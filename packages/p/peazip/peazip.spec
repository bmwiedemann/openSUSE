#
# spec file for package peazip
#
# Copyright (c) 2020 SUSE LLC
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
%define         _helpver 7.4.0
Name:           peazip
Version:        7.4.0
Release:        0
Summary:        Graphical file archiver
License:        LGPL-3.0-only
URL:            http://www.peazip.org
Source0:        https://sourceforge.net/projects/peazip/files/%{version}/peazip-%{version}.src.zip
Source1:        altconf.txt
Source2:        https://sourceforge.net/projects/peazip/files/%{_helpver}/peazip_help.pdf#/peazip_help-%{_helpver}.pdf
Patch0:         peazip-desktop.patch
# PATCH-FIX-UPSTREAM: https://sourceforge.net/p/peazip/tickets/492/
Patch1:         peazip-fix_aarch64.patch
# PATCH-FIX-OPENSUSE peazip-build_PIE.patch -- aloisio@gmx.com
Patch2:         peazip-build_PIE.patch
# PATCH-FIX-OPENSUSE peazip-help_path.patch set correct path for the pdf guide -- aloisio@gmx.com
Patch3:         peazip-help_path.patch
# PATCH-FEATURE-OPENSUSE peazip-debuginfo.patch
Patch4:         peazip-debuginfo.patch
BuildRequires:  arc
BuildRequires:  brotli
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  fpc
BuildRequires:  fpc-src
BuildRequires:  kf5-filesystem
BuildRequires:  lazarus
BuildRequires:  unzip
BuildRequires:  upx
BuildRequires:  zpaq
BuildRequires:  zstd
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150200
BuildRequires:  p7zip-full
Requires:       p7zip-full
%else
BuildRequires:  p7zip
Requires:       p7zip
%endif
Requires:       upx
%if 0%{?suse_version} < 1500
BuildRequires:  update-desktop-files
%endif
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

%package kf5
Summary:        KF5 servicemenu for peazip
Requires:       peazip
%if 0%{?suse_version} < 1500
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%endif
BuildArch:      noarch

%description kf5
PeaZip is a file and archive manager GUI for many formats.
This subpackage contains the KF5 integration.

%prep
%autosetup -p1 -n %{name}-%{version}.src
chmod +w res/lang
dos2unix readme
cp %{SOURCE2} peazip_help.pdf

%build
lazbuild \
	--lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=gtk2 \
        --max-process-count=1 \
	-B project_pea.lpi project_peach.lpi

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_peazipinstalldir}
cp -r res %{buildroot}%{_peazipinstalldir}
cp %{SOURCE1} %{buildroot}%{_peazipinstalldir}/res

mkdir -p %{buildroot}%{_peazipinstalldir}/res/7z
mkdir -p %{buildroot}%{_peazipinstalldir}/res/upx
ln -s %{_bindir}/7z  %{buildroot}%{_peazipinstalldir}/res/7z/7z
ln -s %{_bindir}/upx  %{buildroot}%{_peazipinstalldir}/res/upx/upx

mkdir -p %{buildroot}%{_peazipinstalldir}/res/arc
mkdir -p %{buildroot}%{_peazipinstalldir}/res/brotli
mkdir -p %{buildroot}%{_peazipinstalldir}/res/zpaq
mkdir -p %{buildroot}%{_peazipinstalldir}/res/zstd
ln -s %{_bindir}/arc  %{buildroot}%{_peazipinstalldir}/res/arc/arc
ln -s %{_bindir}/brotli  %{buildroot}%{_peazipinstalldir}/res/brotli/brotli
ln -s %{_bindir}/zpaq  %{buildroot}%{_peazipinstalldir}/res/zpaq/zpaq
ln -s %{_bindir}/zstd  %{buildroot}%{_peazipinstalldir}/res/zstd/zstd

install -m755 peazip %{buildroot}%{_peazipinstalldir}
ln -s %{_peazipinstalldir}/peazip %{buildroot}%{_bindir}/peazip
install -m755 pea %{buildroot}%{_peazipinstalldir}/res
ln -s %{_peazipinstalldir}/res/pea %{buildroot}%{_bindir}/pea

install -D -m644 FreeDesktop_integration/peazip.desktop %{buildroot}%{_datadir}/applications/peazip.desktop
install -D -m644 FreeDesktop_integration/peazip.png %{buildroot}%{_datadir}/pixmaps/peazip.png

pushd FreeDesktop_integration/kde4-dolphin/usr/share/kde4/services/ServiceMenus
mkdir -p %{buildroot}%{_kf5_servicesdir}/ServiceMenus
install -m644 *.desktop %{buildroot}%{_kf5_servicesdir}/ServiceMenus
popd

%fdupes %{buildroot}/%{_prefix}

%if 0%{?suse_version} < 1500
%post kf5
%desktop_database_post

%postun kf5
%desktop_database_postun
%endif

%files
%license copying.txt
%doc readme  peazip_help.pdf
%{_bindir}/pea
%{_bindir}/peazip
%{_peazipinstalldir}
%{_datadir}/applications/peazip.desktop
%{_datadir}/pixmaps/peazip.png

%files kf5
%dir %{_kf5_servicesdir}/ServiceMenus
%{_kf5_servicesdir}/ServiceMenus/*.desktop

%changelog
