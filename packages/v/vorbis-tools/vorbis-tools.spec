#
# spec file for package vorbis-tools
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vorbis-tools
Version:        1.4.0
Release:        0
Summary:        Ogg Vorbis Tools
License:        GPL-2.0
Group:          Productivity/Multimedia/Sound/Utilities
Url:            http://www.xiph.org/
Source0:        http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE warning-fixes.diff -- Fix rpm post-build-check failure for serious compiler warnings
Patch0:         warning-fixes.diff
# PATCH-FIX-OPENSUSE vorbis-tools-cflags.diff bnc#93888 -- Remove -fsigned-char option
Patch1:         vorbis-tools-cflags.diff
# PATCH-FIX-OPENSUSE vcut-fix-segfault.diff bnc#888360 -- Fix segfault of vcut
Patch2:         vcut-fix-segfault.diff
# PATCH-FIX-UPSTREAM vorbis-tools-r19117-CVE-2014-9640.patch bsc#914938 CVE-201409640
Patch3:         vorbis-tools-r19117-CVE-2014-9640.patch
# PATCH-FIX-SUSE vorbis-tools-oggenc-CVE-2014-9639.patch bnc#914439 bnc#914441 CVE-2014-9638 CVE-2014-9639
Patch4:         vorbis-tools-oggenc-CVE-2014-9639.patch
# PATCH-FIX-SUSE oggenc-Fix-large-alloca-on-bad-AIFF-input.patch bsc#943795 CVE-2015-6749
Patch5:         oggenc-Fix-large-alloca-on-bad-AIFF-input.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  flac-devel
BuildRequires:  gettext-tools
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
%if 0%{?suse_version} >= 1140
BuildRequires:  libkate-devel
%endif
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkg-config
BuildRequires:  speex-devel
Recommends:     %{name}-lang = %{version}

%description
This package contains some tools for Ogg Vorbis:

oggenc (an encoder) and ogg123 (a playback tool). It also has vorbiscomment (to
add comments to Vorbis files), ogginfo (to give all useful information about an
Ogg file, including streams in it), oggdec (a simple command line decoder), and
vcut (which allows you to cut up Vorbis files).



Authors:
--------
    Michael Smith <msmith@xiph.org>
    Kenneth Arnold <kcarnold-xiph@arnoldnet.net>
    Stan Seibert <volsung@xiph.org>
    Segher Boessenkool <segher@xiph.org>
    Michael Gold <mgold@ncf.ca>
    Xiphophorus Company <team@xiph.org>


%lang_package
%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# automake 1.13 deprecated AM_CONFIG_HEADER
sed -i 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac

%build
# Because of patch vorbis-tools-cflags.diff regenerate build system
%{?suse_update_config:%{suse_update_config -f}}
cp /usr/share/gettext/config.rpath .
autoreconf --force --install
# test ! -f po/Makevars.template || mv po/Makevars.template po/Makevars

export CFLAGS="$RPM_OPT_FLAGS -fPIE"
export LDFLAGS="-pie"
%configure --disable-rpath
make %{?_smp_mflags}

%install
%make_install

# Remove unneeded files (they will be included in /usr/share/doc/packages/vorbis-tools/)
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}/

%find_lang %{name}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES COPYING README
%doc ogg123/ogg123rc-example
%{_bindir}/ogg123
%{_bindir}/oggdec
%{_bindir}/oggenc
%{_bindir}/ogginfo
%{_bindir}/vcut
%{_bindir}/vorbiscomment
%doc %{_mandir}/man1/ogg123.1%{ext_man}
%doc %{_mandir}/man1/oggdec.1%{ext_man}
%doc %{_mandir}/man1/oggenc.1%{ext_man}
%doc %{_mandir}/man1/ogginfo.1%{ext_man}
%doc %{_mandir}/man1/vcut.1%{ext_man}
%doc %{_mandir}/man1/vorbiscomment.1%{ext_man}

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%changelog
