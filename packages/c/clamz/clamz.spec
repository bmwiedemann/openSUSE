#
# spec file for package clamz
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version}
BuildRequires:  libexpat-devel
%else
BuildRequires:  expat-devel
%endif
BuildRequires:  libcurl-devel libgcrypt-devel pkgconfig update-desktop-files
#

Name:           clamz
Url:            http://code.google.com/p/clamz/
Summary:        Command-line tool to download MP3 files from Amazon
Version:        0.5
Release:        0
License:        GPL-3.0+
Group:          Productivity/Networking/Web/Utilities
Source:         http://clamz.googlecode.com/files/clamz-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Clamz is a little command-line program to download MP3 files from
Amazon.com's music store. It is intended to serve as a substitute
for Amazon's official MP3 Downloader, which is not free software.
Clamz can be used to download either individual songs or complete
albums that you have purchased from Amazon.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" UPDATE_MIME_DATABASE=: UPDATE_DESKTOP_DATABASE=: install

%suse_update_desktop_file clamz

%post
%if %{defined mime_database_post}
%mime_database_post
%endif
%if %{defined desktop_database_post}
%desktop_database_post
%endif

%postun
%if %{defined mime_database_postun}
%mime_database_postun
%endif
%if %{defined desktop_database_postun}
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc COPYING README 
%{_bindir}/clamz
%{_mandir}/man?/clamz.*
%{_datadir}/applications/clamz.desktop
%{_datadir}/mime/packages/clamz.xml

%changelog
