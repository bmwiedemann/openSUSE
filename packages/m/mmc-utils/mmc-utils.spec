#
# spec file for package mmc-utils
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mmc-utils
Version:        0.1+git.20230209
Release:        0
Summary:        Tools for MMC/SD devices
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://git.kernel.org/cgit/linux/kernel/git/cjb/mmc-utils.git/
Source0:        %{name}-%{version}.tar.gz
Source1:        https://www.gnu.org/licenses/gpl-2.0.txt

%description
Userspace tools for controlling and querying MMC/SD storage devices

%prep
%autosetup
cp %{SOURCE1} LICENSE.GPL-2.0

%build
%make_build CFLAGS="%{optflags}" CHECKFLAGS="-Wall -Wuninitialized -Wundef"

%install
%make_install prefix=%{_prefix}
install -D -p -m 0644 man/mmc.1 \
  %{buildroot}%{_mandir}/man1/mmc.1

%files
%license LICENSE.GPL-2.0
%{_bindir}/mmc
%{_mandir}/man1/mmc.1%{?ext_man}

%changelog
