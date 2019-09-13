#
# spec file for package zsync
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

Name:           zsync
Version:        0.6.2
Release:        0
Source:         http://zsync.moria.org.uk/download/zsync-%{version}.tar.bz2
Url:            http://zsync.moria.org.uk/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  make
Summary:        Client-side Implementation of the Rsync Algorithm over HTTP
License:        Artistic-2.0
Group:          Productivity/Networking/Other
# PATCH-FIX-OPENSUSE avoid build time in generated files for build compare
Patch:          zsync-no-build-date.patch

%description
zsync is a implementation of rsync over HTTP. It allows updating of files from
a remote Web server without requiring a full download or a special remote
server application. It uses a metafile, which is created on the server,
to determine which parts of a file the user already has; it then downloads
the remaining parts via HTTP. No special server or Web server module is
needed. It also works with gzip files, and content on the server can be
compressed to further reduce download times.

%package devel
Requires:       %{name} == %{version}
Summary:        Client-side Implementation of the Rsync Algorithm over HTTP

%description devel
zsync is a implementation of rsync over HTTP. It allows updating of files from
a remote Web server without requiring a full download or a special remote
server application. It uses a metafile, which is created on the server,
to determine which parts of a file the user already has; it then downloads
the remaining parts via HTTP. No special server or Web server module is
needed. It also works with gzip files, and content on the server can be
compressed to further reduce download times.


%prep
%setup -q
%patch

%build
%configure
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall
%__mkdir_p %{buildroot}%{_includedir}/zsync
%__install libzsync/*.h %{buildroot}%{_includedir}/zsync

%__mkdir_p %{buildroot}%{_libdir}
%__install libzsync/*.a %{buildroot}%{_libdir}

%__mkdir_p %{buildroot}%{_docdir}/zsync
mv %{buildroot}%{_datadir}/doc/zsync/* "%{buildroot}%{_docdir}/zsync"
%__rm -rf "%{buildroot}%{_datadir}/doc"

%clean

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/zsync
%{_bindir}/zsyncmake
%doc %{_mandir}/man1/zsync.1*
%doc %{_mandir}/man1/zsyncmake.1*

%files devel
%defattr(-,root,root)
%dir %{_prefix}/include/zsync
%{_prefix}/include/*
%{_libdir}/*.a

%changelog
