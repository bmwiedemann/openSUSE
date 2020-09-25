#
# spec file for package cramfsswap
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


Name:           cramfsswap
Version:        1.4.1
Release:        0
Summary:        Swap endianess of a cram filesystem (cramfs)
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            http://kju.de/projekte/cramfsswap/
Source:         https://deb.debian.org/debian/pool/main/c/cramfsswap/cramfsswap_%{version}-1.2.tar.gz
Patch0:         cramfsswap-obey-cflags.patch
BuildRequires:  zlib-devel

%description
cramfs is a highly compressed and size optimized linux filesystem which is
mainly used for embedded applications. the problem with cramfs is that it
is endianess sensitive, meaning you can't mount a cramfs for a big endian
target on a little endian machine and vice versa. this is often especially
a problem in the development phase.

cramfsswap solves that problem by allowing you to swap to endianess of a
cramfs filesystem.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="%optflags"
%make_build debian

%install
install -D -p -m0755 cramfsswap %{buildroot}/%{_bindir}/cramfsswap
install -D -p -m0644 cramfsswap.1 %{buildroot}%{_mandir}/man1/cramfsswap.1

%files
%license COPYING
%doc README
%{_bindir}/cramfsswap
%{_mandir}/man1/cramfsswap.1%{?ext_man}

%changelog
