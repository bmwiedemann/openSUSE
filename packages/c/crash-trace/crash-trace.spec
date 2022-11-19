#
# spec file for package crash-trace
#
# Copyright (c) 2022 SUSE LLC
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


Name:           crash-trace
Version:        3.0
Release:        0
Summary:        The trace command for crash
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            https://github.com/fujitsu/crash-trace
Source:         https://github.com/fujitsu/crash-trace/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         %{name}-fix-aarch64-ppc64le.patch
BuildRequires:  crash-devel

%description
This extension implements the "trace" command for the crash tool.

%prep
%setup -q
%autopatch -p1

%build
%make_build

%install
mkdir -p %{buildroot}%{_libdir}/crash/extensions
install -m 0644 trace.so %{buildroot}%{_libdir}/crash/extensions

%files
%license COPYING
%{_libdir}/crash/extensions/trace.so

%changelog
