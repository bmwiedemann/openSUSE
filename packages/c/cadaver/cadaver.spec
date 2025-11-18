#
# spec file for package cadaver
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           cadaver
Version:        0.28
Release:        0
Summary:        Command-line WebDAV client
License:        GPL-2.0-or-later
URL:            https://notroj.github.io/cadaver/
Source:         %{url}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(openssl)

%description
cadaver is a command-line WebDAV client, with support for file upload,
download, on-screen display, in-place editing, namespace operations
(move/copy), collection creation and deletion, property manipulation,
and resource locking.

%lang_package

%prep
%autosetup -p1

%build
%configure \
  --with-libxml2 \
  --with-ssl \
  %{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc NEWS FAQ README.md
%{_bindir}/cadaver
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog

