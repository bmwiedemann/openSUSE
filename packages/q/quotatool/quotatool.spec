#
# spec file for package quotatool
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


Name:           quotatool
Version:        1.6.4
Release:        0
Summary:        A utility for setting and manipulating filesystem quotas from the command line
License:        GPL-2.0-only
Group:          System/Filesystems
URL:            https://quotatool.ekenberg.se
Source0:        https://github.com/ekenberg/quotatool/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
quotatool is a utility for setting and manipulating filesystem quotas from
the command line. It supports quota on Linux (versions 2.6, 2.4, and 2.2,
with ext2, ext3, ReiserFS, and XFS), Solaris, and AIX.

%prep
%setup -q

%build
%configure
%make_build

%install
install -Dpm 0755 quotatool \
  %{buildroot}%{_sbindir}/quotatool
install -Dpm 0644 man/quotatool.8 \
  %{buildroot}%{_mandir}/man8/quotatool.8

%files
%license COPYING
%doc AUTHORS ChangeLog README.md TODO
%{_sbindir}/quotatool
%{_mandir}/man8/quotatool.8%{?ext_man}

%changelog
