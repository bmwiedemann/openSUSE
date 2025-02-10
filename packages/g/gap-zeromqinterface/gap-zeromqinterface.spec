#
# spec file for package gap-zeromqinterface
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


Name:           gap-zeromqinterface
Version:        0.16
Release:        0
Summary:        GAP: ZeroMQ bindings
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-packages.github.io/ZeroMQInterface/
#Git-Clone:     https://github.com/gap-packages/ZeroMQInterface
Source:         https://github.com/gap-packages/ZeroMQInterface/releases/download/v%version/ZeroMQInterface-%version.tar.gz
BuildRequires:  c_compiler
BuildRequires:  gap-devel
BuildRequires:  gap-rpm-devel
BuildRequires:  pkgconfig(libzmq) >= 2
Requires:       gap-core >= 4.12
Requires:       gap-gapdoc >= 1.6.1

%description
ZeroMQ bindings for the GAP CAS.

%prep
%autosetup -n ZeroMQInterface-%version

%build
./configure --with-gaproot="%gapdir"
%make_build

%install
%gappkg_simple_install
pushd "%buildroot/$moddir"
rm -Rfv config.* configure cnf src
popd

%files -f %name.files

%changelog
