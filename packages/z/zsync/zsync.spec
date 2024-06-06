#
# spec file for package zsync
#
# Copyright (c) 2024 SUSE LLC
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


Name:           zsync
Version:        0.6.2
Release:        0
Summary:        Client-side Implementation of the Rsync Algorithm over HTTP
License:        Artistic-2.0
Group:          Productivity/Networking/Other
URL:            http://zsync.moria.org.uk/
Source0:        http://zsync.moria.org.uk/download/zsync-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE avoid build time in generated files for build compare
Patch0:         zsync-no-build-date.patch
# PATCH-FIX-OPENSUSE build with gcc14
Patch1:         zsync-gcc14.patch
BuildRequires:  gcc
BuildRequires:  make

%description
zsync is a implementation of rsync over HTTP. It allows updating of files from
a remote Web server without requiring a full download or a special remote
server application. It uses a metafile, which is created on the server,
to determine which parts of a file the user already has; it then downloads
the remaining parts via HTTP. No special server or Web server module is
needed. It also works with gzip files, and content on the server can be
compressed to further reduce download times.

%prep
%autosetup -p0

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

rm -rf %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_bindir}/%{name}make
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}make.1%{?ext_man}

%changelog
