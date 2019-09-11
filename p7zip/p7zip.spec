#
# spec file for package p7zip
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?suse_version} >= 1320 || 0%{?is_opensuse}
# Temporarily disable GUI build as it needs wxWidgets < 3.0 that is no longer
# available in TW
%bcond_with buildgui
%endif
Name:           p7zip
Version:        16.02
Release:        0
Summary:        7-zip file compression program
License:        LGPL-2.1-or-later
Group:          Productivity/Archiving/Compression
Url:            http://p7zip.sourceforge.net/
# Update note: RAR sources need to be removed from the package because of the incompatible licence
# Run the following commands after each package update to remove them
# export VERSION=16.02
# wget http://downloads.sourceforge.net/project/p7zip/p7zip/${VERSION}/p7zip_${VERSION}_src_all.tar.bz2
# tar xjvf p7zip_${VERSION}_src_all.tar.bz2
# rm -rf p7zip_${VERSION}/CPP/7zip/Compress/Rar*
# rm -rf p7zip_${VERSION}/DOC/unRarLicense.txt
# tar cjvf p7zip_${VERSION}_src_all-norar.tar.bz2 p7zip_${VERSION}
# rm -rf p7zip_${VERSION}_src_all.tar.bz2
Source:         p7zip_%{version}_src_all-norar.tar.bz2
# Debian gzip-like CLI wrapper for p7zip (the version shipped within the p7zip tarball is too old)
Source1:        https://anonscm.debian.org/cgit/users/robert/p7zip.git/plain/debian/scripts/p7zip
Source2:        https://anonscm.debian.org/cgit/users/robert/p7zip.git/plain/debian/p7zip.1
Patch1:         CVE-2016-9296.patch
# PATCH-FIX-SUSE bnc#1077978 kstreitova@suse.com -- adjust makefile not to use CPP/7zip/Compress/Rar* files
Patch2:         p7zip_16.02_norar.patch
# PATCH-FIX-UPSTREAM bnc#1077725 kstreitova@suse.com -- fix heap-based buffer overflow in a shrink decoder
Patch3:         p7zip-16.02-CVE-2017-17969.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
Suggests:       p7zip-full
%if %{with buildgui}
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  ninja
BuildRequires:  wxWidgets-devel < 3.0
%endif
%ifarch x86_64
BuildRequires:  yasm
%endif

%description
p7zip is a quick port of 7z.exe and 7za.exe (command line version of
7zip, see www.7-zip.org) for Unix. 7-Zip is a file archiver with
highest compression ratio. Since 4.10, p7zip (like 7-zip) supports
little-endian and big-endian machines.

This package provides:
  * %{_bindir}/7zr - a light stand-alone executable that supports only 7z/LZMA/BCJ/BCJ2 archives
  * %{_bindir}/p7zip - a gzip-like wrapper around 7zr

%package full
Summary:        7z and 7za archivers that handle more types of archives than 7zr
Group:          Productivity/Archiving/Compression
Requires:       %{name} = %{version}
Provides:       %{name}:%{_bindir}/7z
Provides:       %{name}:%{_bindir}/7za

%description full
p7zip is a quick port of 7z.exe and 7za.exe (command line version of
7zip, see www.7-zip.org) for Unix. 7-Zip is a file archiver with
highest compression ratio. Since 4.10, p7zip (like 7-zip) supports
little-endian and big-endian machines.

This package provides:
 * %{_bindir}/7z - uses plugins to handle many types of archives
 * %{_bindir}/7za - a stand-alone executable (handles less archive formats than 7z)

This package allows e.g. File Roller or Ark to create/extract 7z archives.

%if %{with buildgui}
%package gui
Summary:        GUI for 7-zip file compression program
Group:          Productivity/Archiving/Compression
Requires:       %{name} = %{version}
Requires:       %{name}-full = %{version}
Requires:       kf5-filesystem
Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

%description gui
p7zip is a quick port of 7z.exe and 7za.exe (command line version of
7zip, see www.7-zip.org) for Unix. 7-Zip is a file archiver with
highest compression ratio. Since 4.10, p7zip (like 7-zip) supports
little-endian and big-endian machines.
%endif

%package        doc
Summary:        HTML manual for 7-zip
Group:          Productivity/Archiving/Compression
Provides:       %{name}:%{_defaultdocdir}/%{name}/MANUAL
BuildArch:      noarch

%description    doc
This package contains the HTML documentation for 7-Zip.

%prep
%setup -q -n %{name}_%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1

%ifarch x86_64
cp makefile.linux_amd64_asm makefile.machine
%else
%ifarch ppc64 s390x
cp makefile.linux_amd64 makefile.machine
%else
cp makefile.linux_any_cpu_gcc_4.X makefile.machine
%endif
%endif

sed -i s,444,644,g install.sh
sed -i s,555,755,g install.sh
%if %{with buildgui}
chmod 755 CPP/7zip/CMAKE/generate.sh
rm GUI/kde4/p7zip_compress2.desktop
%endif

perl -pi -e 's/ -s / /' makefile.machine
perl -pi -e 's/(\$\(LOCAL_FLAGS\))/'"%{optflags} -fno-strict-aliasing"' \\\n\t$1/' makefile.machine

# move license files
mv DOC/License.txt DOC/copying.txt .

%build
%if %{with buildgui}
pushd CPP/7zip/CMAKE/
./generate.sh
popd
make %{?_smp_mflags} OPTFLAGS="%{optflags} -fno-strict-aliasing -Wl,-z,now -fPIC -pie" all3 7zG
%else
make %{?_smp_mflags} OPTFLAGS="%{optflags} -fno-strict-aliasing -Wl,-z,now -fPIC -pie" all3
%endif

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
./install.sh \
    %{_bindir} \
    %{_libdir}/%{name} \
    %{_mandir} \
    %{_defaultdocdir}/%{name} \
    %{buildroot}
%if %{with buildgui}
mkdir -p %{buildroot}%{_kf5_servicesdir}/ServiceMenus
for i in 16x16 32x32; do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$i/apps
done
install -m644 GUI/kde4/*.desktop %{buildroot}%{_kf5_servicesdir}/ServiceMenus
install -m644 GUI/p7zip_16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/p7zip.png
install -m644 GUI/p7zip_32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/p7zip.png
chmod 755 %{buildroot}%{_bindir}/p7zipForFilemanager
%endif

# Install p7zip wrapper and its manpage
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/p7zip
install -m644 %{SOURCE2} %{buildroot}%{_mandir}/man1/p7zip.1
# Remove a mention of the p7zip-rar package that we don't have
sed -i 's/RAR (if the non-free p7zip-rar package is installed)//g' %{buildroot}%{_mandir}/man1/p7zip.1

# remove superfluous DOC directory
mv %{buildroot}%{_defaultdocdir}/%{name}/DOC/* %{buildroot}%{_defaultdocdir}/%{name}
rmdir %{buildroot}%{_defaultdocdir}/%{name}/DOC/

%fdupes -s %{buildroot}

%check
%if ! 0%{?qemu_user_space_build}
make %{?_smp_mflags} test
make %{?_smp_mflags} test_7z
make %{?_smp_mflags} test_7zr
%endif

%if %{with buildgui}
%post gui
%desktop_database_post
%icon_theme_cache_post

%postun gui
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license copying.txt License.txt
%doc ChangeLog
%doc %{_defaultdocdir}/%{name}
%exclude %{_defaultdocdir}/%{name}/MANUAL
%{_bindir}/7zr
%{_bindir}/p7zip
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/7zr
%{_mandir}/man1/7zr.1%{?ext_man}
%{_mandir}/man1/p7zip.1%{?ext_man}

%files full
%{_bindir}/7z
%{_bindir}/7za
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/7z
%{_libdir}/%{name}/7za
%{_libdir}/%{name}/7z.so
%{_libdir}/%{name}/7zCon.sfx
%{_mandir}/man1/7z.1%{?ext_man}
%{_mandir}/man1/7za.1%{?ext_man}

%if %{with buildgui}
%files gui
%{_bindir}/7zG
%{_bindir}/p7zipForFilemanager
%{_libdir}/%{name}/7zG
%dir %{_libdir}/%{name}/Lang
%{_libdir}/%{name}/Lang/*.txt
%{_libdir}/%{name}/Lang/en.ttt
%{_datadir}/icons/hicolor/*/apps/p7zip.png
%dir %{_kf5_servicesdir}/ServiceMenus
%{_kf5_servicesdir}/ServiceMenus/*.desktop
%endif

%files doc
%doc %{_defaultdocdir}/%{name}/MANUAL

%changelog
