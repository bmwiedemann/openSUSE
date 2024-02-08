#
# spec file for package jpm
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


Name:           jpm
Version:        1.1.0
Release:        0
Summary:        Janet Project Manager
License:        MIT
URL:            https://janet-lang.org
Source0:        https://github.com/janet-lang/jpm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  janet
Requires:       janet

%description
JPM is the Janet Project Manager tool. It is for automating builds and downloading dependencies of Janet projects.

%prep
%setup -q

%build

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} janet bootstrap.janet
# fix for libpath location: should be /usr/lib64 on 64-bit systems
sed -i 's|:libpath "/usr/lib"|:libpath "%{_libdir}"|g' %{buildroot}%{_libdir}/janet/%{name}/default-config.janet

%files
%{_bindir}/%{name}
%dir %{_libdir}/janet/.manifests
%{_libdir}/janet/.manifests/jpm.jdn
%dir %{_libdir}/janet/%{name}
%{_libdir}/janet/%{name}/*.janet
%{_mandir}/man1/%{name}.1%{?ext_man}
%doc *.md
%license LICENSE

%changelog
