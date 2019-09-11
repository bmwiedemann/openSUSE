#
# spec file for package kubic-pause
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kubic-pause
Version:        0.9
Release:        0
Summary:        A binary reaping children
License:        Apache-2.0
Group:          System/GUI/KDE
Url:            https://github.com/kubernetes/federation
Source1:        https://raw.githubusercontent.com/kubernetes/federation/ccbc47b7f65e09a4bfbc27e157120e0396156d67/build/pause/pause.c
Source2:        https://raw.githubusercontent.com/kubernetes/federation/ccbc47b7f65e09a4bfbc27e157120e0396156d67/LICENSE
BuildRequires:  gcc
BuildRequires:  glibc-devel-static

%description
This executable can be used as a minimal init process inside a container.

%prep
%autosetup -T -c
cp %{SOURCE2} .

%build
gcc %{optflags} -static -DVERSION=%{version} %{SOURCE1} -o kubic-pause

%install
install -m0755 -D kubic-pause %{buildroot}/usr/bin/kubic-pause

%files
%license LICENSE
%{_bindir}/kubic-pause

%changelog
