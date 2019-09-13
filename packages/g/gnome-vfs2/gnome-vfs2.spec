#
# spec file for package gnome-vfs2
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


%define _name gnome-vfs
Name:           gnome-vfs2
Version:        2.24.4
Release:        0
Summary:        The GNOME 2.x Desktop Virtual File System Libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org/
Source:         ftp://ftp.gnome.org/pub/gnome/sources/%{_name}/2.24/%{_name}-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FEATURE-OPENSUSE gnome-vfs-url_handler_news.patch vuntz@novell.com -- add news: url handler schema
Patch20:        gnome-vfs-url_handler_news.patch
# PATCH-FEATURE-OPENSUSE gnome-vfs-url_handler_ftp.patch vuntz@novell.com -- add ftp: url handler schema
Patch22:        gnome-vfs-url_handler_ftp.patch
# PATCH-FEATURE-SLE gnome-vfs2-172680-novell-services.diff bnc172680 -- Needed for novell-nautilus-plugin integration in network://
Patch35:        gnome-vfs2-172680-novell-services.diff
# PATCH-FIX-OPENSUSE gnome-vfs-no-mime-data.patch vuntz@novell.com -- This is bgo336952. Technically, this is wrong (since gnome-mime-data is still a dependency for deprecated API), but in practice, this should be fine.
Patch39:        gnome-vfs-no-mime-data.patch
# PATCH-FIX-SLE gnome-vfs2-293856-novfs-file-method.diff bnc293856
Patch40:        gnome-vfs2-293856-novfs-file-method.diff
# PATCH-FEATURE-OPENSUSE gnome-vfs-url_handler_irc.patch bnc372232 vuntz@novell.com -- add irc: url handler schema
Patch41:        gnome-vfs-url_handler_irc.patch
# PATCH-FIX-UPSTREAM gnome-vfs2-non_void.patch bgo#611574 ro@novell.com -- Fix no-return-in-non-void-function.
Patch42:        gnome-vfs2-non_void.patch
# PATCH-FIX-OPENSUSE gnome-vfs2-ssl.patch bgo#681242 crrodriguez@opensuse.org - Never negotiate SSLv2 because it is broken
Patch43:        gnome-vfs2-ssl.patch
# PATCH-FIX-UPSTREAM gnome-vfs2-g_memmove-no-more.patch dimstar@opensuse.org -- Use memmove() instead of obsolete g_memmove()
Patch44:        gnome-vfs2-g_memmove-no-more.patch
# PATCH-FIX-SLE gnome-vfs2-2.12.2-smb-method-fixes.patch bnc#832381 dliang@suse.com -- porting some missing patches from SLE to openSUSE
Patch45:        gnome-vfs2-2.12.2-smb-method-fixes.patch
# PATCH-FIX-SLE gnome-vfs2-bug338168-cannot-access-from-location-input.patch bnc#832381 dliang@suse.com -- porting some missing patches from SLE to openSUSE
Patch46:        gnome-vfs2-bug338168-cannot-access-from-location-input.patch
# PATCH-FIX-OPENSUSE gnome-vfs2-openssl11.patch bsc#1042650 meissner@suse.com -- openssl 1.1 enablement: replacing old openssl construct by a better strategy
Patch50:        gnome-vfs2-openssl11.patch
BuildRequires:  cdparanoia
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gamin-devel
BuildRequires:  gcc-c++
BuildRequires:  gconf2-devel
BuildRequires:  gnome-common
BuildRequires:  gnome-patch-translation
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libavahi-glib-devel
BuildRequires:  libbz2-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libxml2-devel
BuildRequires:  samba
Requires:       desktop-file-utils
Recommends:     %{name}-lang
#
Obsoletes:      gnome-vfs-extras
Provides:       gnome-vfs-extras
%{gconf_schemas_prereq}

%description
GNOME VFS is the GNOME virtual file system. It is the foundation of the
Nautilus file manager. It provides a modular architecture and ships
with several modules that implement support for file systems, HTTP,
FTP, and others. It provides a URI-based API, a back-end supporting
asynchronous file operations, a MIME type manipulation library, and
other features.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       gconf2-devel
Requires:       glib2-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%package doc
Summary:        Additional Package Documentation for gnome-vfs2
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
GNOME VFS is the GNOME virtual file system. It is the foundation for
the Nautilus file manager. It provides a modular architecture and ships
with several modules that implement support for file systems, HTTP,
FTP, and more. It provides a URI-based API, a back-end that supports
asynchronous file operations, a MIME type manipulation library, and
other features.

This package contains additional documentation for the main package.

%lang_package

%prep
%setup -q -n %{_name}-%{version}
gnome-patch-translation-prepare
%patch35 -p1
%patch39
%patch40
%patch42
%patch43
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch50 -p1

# ^ Place for your patches is here
#
gnome-patch-translation-update
# Put here only patches with its own translation management:
%patch20
%patch22
%patch41 -p1
# ^ Add no patches here!
#
# Put your patches upper from gnome-patch-translation-update
# Generate translations for "news", "ftp" and "irc" entries from "h323".
# These entries are identical with exception of URL type string.
for po in po/*.po ; do
    tr '\n' '\1' <$po |
	sed $'s/\1\1/\\n\\n/g' |
	sed $'
	    s/\(.*desktop_gnome_url_handlers.schemas.*msgid ".*\)h323\\(.*"\1msgstr ".*\\)h323\\(.*\\)$/&\\n\\n\\1news\\2news\\3\\n\\n\\1ftp\\2ftp\\3\\n\\n\\1irc\\2irc\\3/
	' |
	tr '\1' '\n' >$po.new
	mv $po.new $po
done
# Fix build with automake 1.13, which does not like $(srcdir) in TESTS statements
sed -i 's:$(srcdir)/auto-test:../auto-test:' test/Makefile.am

%build
gtkdocize --copy
autoreconf -f -i
%configure --with-pic \
	--libexecdir=%{_prefix}/lib/gnome-vfs-2.0\
	--disable-static\
        --disable-howl \
        --enable-selinux \
        --with-samba-includes=%{_includedir}/samba-4.0 \
	ac_cv_path_SSH_PROGRAM=%{_bindir}/ssh
echo "#undef G_DISABLE_DEPRECATED" >> config.h
make %{?_smp_mflags}

%install
%make_install
%find_lang gnome-vfs-2.0
%find_gconf_schemas
cat %{name}.schemas_list >%{name}.lst
# Some sites use different partitions for /usr/(lib|lib64) and /usr/share.  Since you
# can't create hardlinks across partitions, we'll do this more than once.
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_bindir}

%pre -f %{name}.schemas_pre
%post -p /sbin/ldconfig
%posttrans -f %{name}.schemas_posttrans
%preun -f %{name}.schemas_preun
%postun -p /sbin/ldconfig

%files -f %{name}.lst
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/dbus-1/services/gnome-vfs-daemon.service
%{_libdir}/*.so.*
%dir %{_libdir}/gnome-vfs-2.0
%{_libdir}/gnome-vfs-2.0/modules
%if "%{_libdir}" != "%{_prefix}/lib"
%dir %{_prefix}/lib/gnome-vfs-2.0
%endif
%{_prefix}/lib/gnome-vfs-2.0/gnome-vfs-daemon
%config %{_sysconfdir}/gnome-vfs-2.0

%files lang -f gnome-vfs-2.0.lang

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_libdir}/gnome-vfs-2.0/include
%{_libdir}/*.so

%files doc
%{_datadir}/gtk-doc/html/gnome-vfs-2.0

%changelog
