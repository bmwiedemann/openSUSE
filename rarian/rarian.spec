#
# spec file for package rarian
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


Name:           rarian
Version:        0.8.1
Release:        0
Summary:        Document cataloging system
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            ftp://ftp.gnome.org/pub/gnome/sources/rarian/
Source0:        http://download.gnome.org/sources/rarian/0.8/%{name}-%{version}.tar.bz2
Source1:        scrollkeeper-omf.dtd
Source99:       %{name}-rpmlintrc
Patch1:         rarian-0.5.6-reg-parse-bugs.patch
Patch2:         rarian-0.7.1-return.patch
Patch3:         rarian-0.5.6-docs-from-desktop-entries-and-bundles.patch
# PATCH-FIX-OPENSUSE rarian-opensuse-manuals.patch vuntz@novell.com -- Find openSUSE manuals
Patch4:         rarian-opensuse-manuals.patch
# PATCH-FIX-OPENSUSE rarian-help-bundle.patch vuntz@novell.com -- Grab manual in /usr/share/gnome/help-bundle when it makes sense
Patch5:         rarian-help-bundle.patch
# PATCH-FIX-UPSTREAM rarian-no-warning-X-lines.patch bfo18317 vuntz@novell.com -- No warning on X- lines
Patch6:         rarian-no-warning-X-lines.patch
# PATCH-FIX-OPENSUSE rarian-no-warning-desktop-entry.patch vuntz@novell.com -- We have a patch to read .desktop file, but we don't want lots of warnings because of this...
Patch7:         rarian-no-warning-desktop-entry.patch
# PATCH-FIX-UPSTREAM rarian-no-info.patch fdo24277 vuntz@opensuse.org -- Crash when there's no info at all
Patch8:         rarian-no-info.patch
# PATCH-FIX-UPSTREAM rarian-quiet.patch fdo24276 vuntz@opensuse.org -- Make rarian a bit quieter
Patch9:         rarian-quiet.patch
# PATCH-FIX-UPSTREAM rarian-no-warning-localized-icon.patch fdo#33560 vuntz@opensuse.org -- Icons can be localized, so don't warn for localized icons. It's not the fix that should go upstream, but a real fix would potentially imply some API break.
Patch10:        rarian-no-warning-localized-icon.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook_4
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %{_bindir}/xmlcatalog
PreReq:         /bin/touch
PreReq:         sgml-skel

%description
Rarian is a document cataloging system.
It manages documentation metadata, as specified by the Open Source Metadata Framework (OMF)
Rarian is designed to be a replacement for scrollkeeper.

%package scrollkeeper-compat
Summary:        Rarian is designed to be a replacement for scrollkeeper
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       scrollkeeper
Obsoletes:      scrollkeeper <= 0.3.14

%description scrollkeeper-compat
Rarian is designed to be a replacement for scrollkeeper, and with this package, all your
known scrollkeeper-based scripts and commands will transparently keep on working.

%package devel
Summary:        Development files for rarian
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Rarian is a document cataloging system.

This package contains the files for developing applications using rarian.

%prep
%setup -q
%patch1 -p1
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
find . -name Makefile -print -delete
find . -name configure -print -delete
libtoolize --force --copy
aclocal
autoheader
automake --add-missing --foreign
autoreconf
%configure --disable-static --with-pic
make %{?_smp_mflags}

# Prepare for the XML Catalog for scrollkeeper compatibility; snipped copied from scrollkeeper.spec
xmlcatbin=%{_bindir}/xmlcatalog
CATALOG=scrollkeeper.xml
$xmlcatbin --noout --create $CATALOG
$xmlcatbin --noout --add "public" \
  "-//OMF//DTD Scrollkeeper OMF Variant V1.0//EN" \
  "file://%{_datadir}/xml/scrollkeeper/dtds/scrollkeeper-omf.dtd" $CATALOG
%define FOR_ROOT_CAT for-catalog-%{name}-%{version}.xml
CATALOG=etc/xml/$CATALOG
rm -f %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --create %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "delegatePublic" \
  "-//OMF//DTD Scrollkeeper OMF Variant V1.0//EN" \
  "file:///$CATALOG" %{FOR_ROOT_CAT}.tmp
$xmlcatbin --noout --add "rewriteSystem" \
    "http://scrollkeeper.sourceforge.net/dtds/scrollkeeper-omf-1.0" \
    "file://%{_datadir}/xml/scrollkeeper/dtds" %{FOR_ROOT_CAT}.tmp
# Create tag
sed '/<catalog/a\
  <group id="%{name}-%{version}">
/<\/catalog/i\
  </group>' \
  %{FOR_ROOT_CAT}.tmp > %{FOR_ROOT_CAT}
# End scrollkeeper compatibility

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Install DTD as was shipped with scrollkeeper
mkdir -p %{buildroot}%{_datadir}/xml/scrollkeeper/dtds
cp %{SOURCE1} %{buildroot}%{_datadir}/xml/scrollkeeper/dtds

# Register the scrollkeeper DTDs for offline usage; replicated from scrollkeeper's .spec files
# xml catalog
cat_dir=%{buildroot}%{_sysconfdir}/xml
install -d -m755 $cat_dir
install -m644 %{FOR_ROOT_CAT} scrollkeeper.xml $cat_dir

# Prepare for update-alternatives usage
mkdir -p %{buildroot}%{_sysconfdir}/alternatives

for target in scrollkeeper-config scrollkeeper-extract scrollkeeper-gen-seriesid scrollkeeper-get-cl scrollkeeper-get-content-list scrollkeeper-get-extended-content-list scrollkeeper-get-index-from-docpath scrollkeeper-get-toc-from-docpath scrollkeeper-get-toc-from-id scrollkeeper-install scrollkeeper-preinstall scrollkeeper-rebuilddb scrollkeeper-uninstall scrollkeeper-update; do
  ln -s -f %{_sysconfdir}/alternatives/$target %{buildroot}%{_bindir}/$target
done

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post scrollkeeper-compat
# If the scrollkeeper-config group is in automatic mode, then this
# will also switch all symlinks automatically
update-alternatives \
	--install %{_bindir}/scrollkeeper-config scrollkeeper-config %{_bindir}/rarian-sk-config 10 \
	--slave %{_bindir}/scrollkeeper-extract scrollkeeper-extract %{_bindir}/rarian-sk-extract \
	--slave %{_bindir}/scrollkeeper-gen-seriesid scrollkeeper-gen-seriesid %{_bindir}/rarian-sk-gen-uuid \
	--slave %{_bindir}/scrollkeeper-get-cl scrollkeeper-get-cl %{_bindir}/rarian-sk-get-cl \
	--slave %{_bindir}/scrollkeeper-get-content-list scrollkeeper-get-content-list %{_bindir}/rarian-sk-get-content-list \
	--slave %{_bindir}/scrollkeeper-get-extended-content-list scrollkeeper-get-extended-content-list %{_bindir}/rarian-sk-get-extended-content-list \
	--slave %{_bindir}/scrollkeeper-get-index-from-docpath scrollkeeper-get-index-from-docpath %{_bindir}/rarian-sk-get-scripts \
	--slave %{_bindir}/scrollkeeper-get-toc-from-docpath scrollkeeper-get-toc-from-docpath %{_bindir}/rarian-sk-get-scripts \
	--slave %{_bindir}/scrollkeeper-get-toc-from-id scrollkeeper-get-toc-from-id %{_bindir}/rarian-sk-get-scripts \
	--slave %{_bindir}/scrollkeeper-install scrollkeeper-install %{_bindir}/rarian-sk-install \
	--slave %{_bindir}/scrollkeeper-preinstall scrollkeeper-preinstall %{_bindir}/rarian-sk-preinstall \
	--slave %{_bindir}/scrollkeeper-rebuilddb scrollkeeper-rebuilddb %{_bindir}/rarian-sk-rebuild \
	--slave %{_bindir}/scrollkeeper-uninstall scrollkeeper-uninstall %{_bindir}/rarian-sk-install \
	--slave %{_bindir}/scrollkeeper-update scrollkeeper-update %{_bindir}/rarian-sk-update

# Update the cache
%{_bindir}/rarian-sk-update

# Register scrollkeeper DTD
edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
  --add %{_sysconfdir}/xml/%{FOR_ROOT_CAT}

%postun scrollkeeper-compat
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_bindir}/rarian-sk-config ]; then
  update-alternatives --remove scrollkeeper-config %{_bindir}/rarian-sk-config
fi

# remove entries only on removal of file
if [ ! -f %{_sysconfdir}/xml/%{FOR_ROOT_CAT} -a -x %{_bindir}/edit-xml-catalog ] ; then
  edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
    --del %{name}-%{version}
fi

%files
%license COPYING
%doc README NEWS
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/*
# in scrollkeeper-compat
%exclude %{_bindir}/scrollkeeper-*
%exclude %{_bindir}/rarian-sk-*
%exclude %{_datadir}/xml/

%files scrollkeeper-compat
%{_bindir}/rarian-sk-*
%{_datadir}/xml/*
%config %{_sysconfdir}/xml/for-catalog-rarian-0.8.1.xml
%config %{_sysconfdir}/xml/scrollkeeper.xml
%{_bindir}/scrollkeeper-config
%{_bindir}/scrollkeeper-extract
%{_bindir}/scrollkeeper-gen-seriesid
%{_bindir}/scrollkeeper-get-cl
%{_bindir}/scrollkeeper-get-content-list
%{_bindir}/scrollkeeper-get-extended-content-list
%{_bindir}/scrollkeeper-get-index-from-docpath
%{_bindir}/scrollkeeper-get-toc-from-docpath
%{_bindir}/scrollkeeper-get-toc-from-id
%{_bindir}/scrollkeeper-install
%{_bindir}/scrollkeeper-preinstall
%{_bindir}/scrollkeeper-rebuilddb
%{_bindir}/scrollkeeper-uninstall
%{_bindir}/scrollkeeper-update
%ghost %{_sysconfdir}/alternatives/scrollkeeper-config
%ghost %{_sysconfdir}/alternatives/scrollkeeper-extract
%ghost %{_sysconfdir}/alternatives/scrollkeeper-gen-seriesid
%ghost %{_sysconfdir}/alternatives/scrollkeeper-get-cl
%ghost %{_sysconfdir}/alternatives/scrollkeeper-get-content-list
%ghost %{_sysconfdir}/alternatives/scrollkeeper-get-extended-content-list
%ghost %{_sysconfdir}/alternatives/scrollkeeper-get-index-from-docpath
%ghost %{_sysconfdir}/alternatives/scrollkeeper-get-toc-from-docpath
%ghost %{_sysconfdir}/alternatives/scrollkeeper-get-toc-from-id
%ghost %{_sysconfdir}/alternatives/scrollkeeper-install
%ghost %{_sysconfdir}/alternatives/scrollkeeper-preinstall
%ghost %{_sysconfdir}/alternatives/scrollkeeper-rebuilddb
%ghost %{_sysconfdir}/alternatives/scrollkeeper-uninstall
%ghost %{_sysconfdir}/alternatives/scrollkeeper-update

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
