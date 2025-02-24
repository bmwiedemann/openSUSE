#
# spec file for package eatmydata
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           eatmydata
Version:        131
Release:        0
Summary:        A library to disable fsync calls
License:        GPL-3.0-only
Group:          Development/Tools/Other
URL:            https://www.flamingspork.com/projects/libeatmydata/
Source0:        http://www.flamingspork.com/projects/libeatmydata/libeatmydata-%{version}.tar.gz
Source1:        http://www.flamingspork.com/projects/libeatmydata/libeatmydata-%{version}.tar.gz.asc
Source2:        https://www.flamingspork.com/stewart.gpg#/%{name}.keyring
Source3:        eatmydata-rpmlintrc
BuildRequires:  strace

%description
libeatmydata is a small LD_PRELOAD library designed to (transparently)
disable fsync (and friends, like open(O_SYNC)). This has two side-effects:
making software that writes data safely to disk a lot quicker and making
this software no longer crash safe.

%prep
%autosetup -n lib%{name}-%{version} -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
# qemu does not implement ptrace
%if !0%{?qemu_user_space_build}
%make_build check
%endif

%files
%license COPYING
%doc AUTHORS README.md
%attr(0755,root,root) %{_bindir}/eatmydata
%attr(0755,root,root) %{_libexecdir}/eatmydata.sh
%{_libdir}/libeatmydata.so*

%changelog
