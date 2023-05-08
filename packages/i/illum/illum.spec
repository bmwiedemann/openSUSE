#
# spec file for package illum
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


%global ccan_commit 1cebc0895d236bfc5cd6797d03e02c55c773ddf1
%global owner jmesmon
Name:           illum
Version:        0.5
Release:        0
Summary:        A daemon that responds to brightness keys by changing the backlight level
License:        AGPL-3.0-only
Group:          System/Base
URL:            https://github.com/jmesmon/illum
Source0:        https://github.com/%{owner}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{owner}/ccan/archive/%{ccan_commit}/ccan-%{ccan_commit}.tar.gz
BuildRequires:  libev-devel
BuildRequires:  libevdev-devel
BuildRequires:  libudev-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig

%description
While there are tools that can be configured to adjust brightness illum adjusts
brightness as soon as you install and enable it.

It uses exponential brightness stepping which happens to work well with many
screens and is hard to achieve with a plain shell script bound to a key with
more generic tool.

%prep
%setup -q
tar -zxf %{SOURCE1}
rmdir ccan
mv $(basename %{SOURCE1} .tar.gz) ccan

%build
./build

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} ./do-install

%files
%doc README
%{_bindir}/%{name}-d
%{_prefix}/lib/systemd/system/%{name}.service

%changelog
