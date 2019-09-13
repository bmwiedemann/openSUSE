#
# spec file for package pagein
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           pagein
Version:        0.01.00
Release:        0
Summary:        A tool to force swapped out pages back into memory
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            http://kernel.ubuntu.com/~cking/pagein/
Source:         http://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

%description
Pagein is a tool that forces pages that are in swap to be paged in back
to memory. The main usecase for pagein is to exercise the VM and swap
subsystems for testing purposes.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%{_bindir}/pagein
%{_mandir}/man1/pagein.1%{?ext_man}

%changelog
