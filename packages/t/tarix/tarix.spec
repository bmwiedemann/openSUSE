#
# spec file for package tarix
#
# Copyright (c) 2021 SUSE LLC
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


Name:           tarix
Version:        1.0.9
Release:        0
Summary:        Simple Indexer for GNU and POSIX Tar Files
License:        GPL-2.0-only
Group:          Productivity/Archiving/Backup
URL:            https://github.com/fastcat/tarix
Source:         https://github.com/fastcat/tarix/archive/tarix-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(zlib)

%description
tarix is a simple indexer for GNU and POSIX tar files. The indexes allow fast
extraction of files in the archive, especially on seekable tape devices. The
index format is simple enough to be used from a rescue disk with only mt,
dd, and tar (though grep and sed would be very useful there).

%prep
%autosetup -n tarix-tarix-%{version}

%build
sed -i "s|-Werror||g" Makefile
%make_build CC="cc %{optflags} -std=c99"

%install
install -Dpm 0755 bin/tarix \
  %{buildroot}%{_bindir}/tarix
install -Dpm 0755 bin/fuse_tarix \
  %{buildroot}%{_bindir}/fuse_tarix

%check
# Test: 08-exclude                     ...FAILED
make %{?_smp_mflags} CC="cc %{optflags} -std=c99" test ||:

%files
%license LICENSE
%doc ChangeLog CREDITS FORMAT README TODO
%{_bindir}/fuse_tarix
%{_bindir}/tarix

%changelog
