#
# spec file for package gq
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

Name:           gq
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  gtk2-devel
BuildRequires:  krb5-devel
BuildRequires:  libglade2-devel
%if 0%{?suse_version} >= 1130
BuildRequires:  libgnome-keyring-devel
%else
BuildRequires:  gnome-keyring-devel
%endif
BuildRequires:  libgcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  openldap2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
Summary:        An LDAP Client for GTK
License:        GPL-2.0+
Group:          Productivity/Networking/LDAP/Clients
Version:        1.2.3
Release:        0
Url:            http://gq-project.org/
Source0:        gq-%{version}.tar.bz2
Source1:        gq-%{version}-langpack-1.tar.bz2
# PATCH-FIX-UPSTREAM gq-fix-linking.patch vuntz@opensuse.org -- Fix linking issue, taken from git
Patch0:         gq-fix-linking.patch
# PATCH-FIX-UPSTREAM gq-glib-2.31.patch dimstar@opensuse.org -- Fix build with glib 2.31. Sent upstream by mail (vuntz, 2011-01-05)
Patch1:         gq-glib-2.31.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An LDAP client for GTK.

%prep
%setup -q
%setup -T -D -a 1
%patch0 -p1
%patch1 -p1

%build
# needed for patch0
autoreconf -fi -I macros
gq-%{version}-langpack-1/langpack .
export CFLAGS="-DLDAP_DEPRECATED $RPM_OPT_FLAGS -fcommon"
%configure \
    --enable-browser-dnd 		\
    --disable-update-mimedb             \
    --disable-debugging
%__make %{?jobs:-j%jobs}

%install
%makeinstall
%suse_update_desktop_file %name System ServiceConfiguration

%clean
rm -rf $RPM_BUILD_ROOT

%if 0%{?suse_version} > 1130

%post
%desktop_database_post
%mime_database_post
%endif

%if 0%{?suse_version} > 1130

%postun
%desktop_database_postun
%mime_database_postun
%endif

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/gq
%{_datadir}/pixmaps/gq/
#%{prefix}/share/locale/*/LC_MESSAGES/gq.mo
%{_datadir}/applications/gq.desktop
%{_datadir}/gq
%{_datadir}/mime/packages/gq-ldif.xml

%changelog
