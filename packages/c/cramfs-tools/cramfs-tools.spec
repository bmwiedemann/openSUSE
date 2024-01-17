#
# spec file for package cramfs-tools
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           cramfs-tools
Version:        2.1
Release:        0
Summary:        Tools for CramFs (Compressed ROM File System)
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/npitre/cramfs-tools/
Source:         https://github.com/npitre/cramfs-tools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         cramfs-tools-obey-cflags.patch
BuildRequires:  help2man
BuildRequires:  zlib-devel

%description
This package contains tools that let you construct a CramFs
(Compressed ROM File System) image from the contents of a given
directory, as well as checking a constructed CramFs image and
extracting its contents.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%optflags"
%make_build
help2man ./cramfsck --version-string="%{version}" --no-info > cramfsck.1
help2man ./mkcramfs --version-string="%{version}" --no-info > mkcramfs.1

%install
install -d %{buildroot}/%{_bindir}/
install -p -m0755 cramfsck %{buildroot}/%{_bindir}/cramfsck
install -p -m0755 mkcramfs %{buildroot}/%{_bindir}/mkcramfs
install -d %{buildroot}%{_mandir}/man1/
install -p -m0644 cramfsck.1 %{buildroot}%{_mandir}/man1/cramfsck.1
install -p -m0644 mkcramfs.1 %{buildroot}%{_mandir}/man1/mkcramfs.1

%files
%license COPYING
%doc NOTES README
%{_bindir}/cramfsck
%{_bindir}/mkcramfs
%{_mandir}/man1/cramfsck.1%{?ext_man}
%{_mandir}/man1/mkcramfs.1%{?ext_man}

%changelog
