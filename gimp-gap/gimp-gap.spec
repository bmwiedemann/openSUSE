#
# spec file for package gimp-gap
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           gimp-gap
Version:        2.6.0
Release:        0
# Patched code is built by default.
# Use rpmbuild -D 'BUILD_ORIG 1' to build original code.
# Use rpmbuild -D 'BUILD_ORIG 1' -D 'BUILD_ORIG_ADDON 1' to name original code as -orig.
BuildRequires:  automake
BuildRequires:  gimp-devel >= 2.6.0
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  translation-update-upstream
%if 0%{?BUILD_ORIG}
%if ! 0%{?BUILD_ORIG_ADDON}
Provides:       %{name}-orig = %{version}
Obsoletes:      %{name}-orig < %{version}-%{release}
%endif
%else
Provides:       patched_build
Conflicts:      %{name}-orig
%endif
Url:            http://www.gimp.org/
Requires:       %{name}-lang = %{version}
Summary:        GIMP Animation Package
License:        GPL-2.0
Group:          Productivity/Multimedia/Video/Editors and Convertors
%if 0%{?BUILD_ORIG}
Source:         ftp://ftp.gimp.org/pub/gimp/plug-ins/v2.6/gap/%{name}-%{version}.tar.bz2
%else
# WARNING: This is not a comment, but the real command to repack souce:
#%(bash %{_sourcedir}/%{name}-patch-source.sh %{name}-%{version}.tar.bz2)
Source:         %{name}-%{version}-patched.tar.bz2
%endif
Patch:          %{name}-patched.patch
# PATCH-FIX-OPENSUSE gimp-gap-no-strict-aliasing.patch sbrabec@suse.cz -- Disables strict aliasing for part of the code.
Patch1:         %{name}-no-strict-aliasing.patch
# PATCH-FIX-UPSTREAM gimp-gap-warnings.patch bgo585343 sbrabec@suse.cz -- Fix of serious warnings.
Patch2:         %{name}-warnings.patch
# PATCH-FIX-UPSTREAM gimp-gap-warnings-orig-addon.patch bgo585343 sbrabec@suse.cz -- Fix of serious warnings.
Patch3:         %{name}-warnings-orig-addon.patch
# PATCH-FIX-UPSTREAM gimp-gap-link-lm.patch bgo#660443 idoenmez@suse.de -- Link to -lm where needed
Patch4:         %{name}-link-lm.patch
# PATCH-FIX-UPSTREAM gimp-gap-gimp28.patch dimstar@opensuse.org -- Fix build with gimp 2.8. Patch not upstreamed, as there are a bunch of commits addressing the same.
Patch5:         gimp-gap-gimp28.patch
Source1:        %{name}-patch-source.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{?gimp_api_version:1}0
Requires:       gimp(abi) = %{gimp_abi_version}
Requires:       gimp(api) = %{gimp_api_version}
%else
%requires_eq gimp
%endif

%description
The GIMP-GAP (GIMP Animation Package) is a collection of Plug-Ins to
extend the GIMP with capabilities to edit and create animations as
sequences of single frames.

%if 0%{?BUILD_ORIG}
%if 0%{?BUILD_ORIG_ADDON}

%package orig
Summary:        GIMP Animation Package
Group:          Productivity/Multimedia/Video/Editors and Convertors
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description orig
The GIMP-GAP (GIMP Animation Package) is a collection of Plug-Ins to
extend the GIMP with capabilities to edit and create animations as
sequences of single frames.

%endif
%endif
%lang_package

%prep
%setup -q
chmod -x ChangeLog
%if ! 0%{?BUILD_ORIG}
%patch
%endif
translation-update-upstream
%if 0%{?BUILD_ORIG}
%patch1
%endif
%patch2
%if 0%{?BUILD_ORIG}
%patch3
%endif
%patch4
%patch5 -p1
sed -i -e "s,sr@Latn,sr@latin," po/LINGUAS
mv po/sr@Latn.po po/sr@latin.po

%build
autoreconf -f -i
%if 0%{?BUILD_ORIG}
# FIXME: Ugly work-around of:
#...ld: bitstream.o: relocation R_X86_64_32 against `a local symbol' can not be used when making a shared object; recompile with -fPIC
#bitstream.o: could not read symbols: Bad value
#export CFLAGS="-fPIC -DPIC $RPM_OPT_FLAGS"
#export LDFLAGS="-fPIC"
%configure
%else
%configure\
	--disable-libavformat
%endif
# First cimpilation of ffmpeg may fail on missing documentation:
make %{?jobs:-j%jobs} STRIP=/bin/true  || :
make %{?jobs:-j%jobs} STRIP=/bin/true

%install
%makeinstall
%find_lang gimp20-gap
%if 0%{?BUILD_ORIG}
rm -f $RPM_BUILD_ROOT%{_libdir}/gimp-gap-2.6/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT
%if 0%{?BUILD_ORIG}
%if 0%{?BUILD_ORIG_ADDON}

%files orig
%else

%files
%endif
%else

%files
%endif
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog* NEWS README
%{_libdir}/gimp-gap-2.6
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/2.0
%dir %{_libdir}/gimp/2.0/plug-ins
%{_libdir}/gimp/2.0/plug-ins/*
%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/2.0
%dir %{_datadir}/gimp/2.0/scripts
%{_datadir}/gimp/2.0/scripts/*.scm

%files lang -f gimp20-gap.lang

%changelog
