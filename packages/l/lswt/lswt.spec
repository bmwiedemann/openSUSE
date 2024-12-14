#
# spec file for package lswt
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


Name:           lswt
Version:        2.0.0
Release:        0
Summary:        Wayland toplevel lister
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://git.sr.ht/~leon_plickat/lswt
Source:         https://git.sr.ht/~leon_plickat/lswt/archive/v2.0.0.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         Makefile.patch
Patch1:         https://git.sr.ht/~leon_plickat/lswt/commit/ea45c1a8cf66d102e6525d29b03126693949e562.patch
Patch2:         https://git.sr.ht/~leon_plickat/lswt/commit/c1ea4ee2a6e4a4e579a17f1e15351f225cb23a1d.patch
Patch3:         https://git.sr.ht/~leon_plickat/lswt/commit/8d76a317ad2da073a638d72eac8a24df33ae01f1.patch
Patch4:         https://git.sr.ht/~leon_plickat/lswt/commit/fdf0932f2939696a8398b63871ccc85335274c1f.patch
Patch5:         https://git.sr.ht/~leon_plickat/lswt/commit/fbb7be4354508b41552ce2159b1203db123916ac.patch
Patch6:         https://git.sr.ht/~leon_plickat/lswt/commit/e4ebefcb30053a990cb821a75c4e1310fc967673.patch
Patch7:         https://git.sr.ht/~leon_plickat/lswt/commit/55a29650a110928cb7ad612182c8096424ebb70a.patch
Patch8:         https://git.sr.ht/~leon_plickat/lswt/commit/ade15dbc3d11325a2569a0efd543d43a3ecb3547.patch
Patch9:         https://git.sr.ht/~leon_plickat/lswt/commit/d35786da4383388c19f5437128fd393a6f16f74f.patch
Patch10:        https://git.sr.ht/~leon_plickat/lswt/commit/29329779b72cb0a7958b7491296782816de8e477.patch
Patch11:        https://git.sr.ht/~leon_plickat/lswt/commit/a39b55080dcb50edc9321d38af8775af22cf852f.patch
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  pkgconfig(wayland-client)

%description
A program to list Wayland toplevels.

Requires the Wayland server to implement the foreign-toplevel-management-unstable-v1
protocol extension.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README
%{_bindir}/lswt
%{_mandir}/man1/lswt.1.gz
%{_datadir}/bash-completion/completions/lswt

%changelog
