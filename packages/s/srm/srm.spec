#
# spec file for package srm
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


Name:           srm
Version:        1.2.15
Release:        0
# COPYING file has the MIT license, but also a extra no-advertising clause
Summary:        A secure replacement for rm
License:        SGI-B-2.0
Group:          Hardware/Other
URL:            http://srm.sf.net
Source0:        https://sourceforge.net/projects/srm/files/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Unlike the standard rm, srm overwrites the data in the target files before unlinking them. This prevents command-line recovery of the data by examining the raw block device. It may also help frustrate physical examination of the disk, although it's unlikely that it can completely prevent that type of recovery. It is, essentially, a paper shredder for sensitive files.

srm is ideal for personal computers or workstations with Internet connections. It can help prevent malicious users from breaking in and undeleting personal files, such as old emails. It's also useful for permanently removing files from expensive media. For example, cleaning your diary off the zip disk you're using to send vacation pictures to Uncle Lou. Because it uses the exact same options as rm(1), srm is simple to use. Just subsitute it for rm whenever you want to destroy files, rather than just unlinking them.

%prep
%setup -q

%build
%configure --disable-debug
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%defattr(-, root, root)
%license COPYING
%{_bindir}/fill_test
%{_bindir}/%{name}
%{_mandir}/man?/%{name}*

%changelog
