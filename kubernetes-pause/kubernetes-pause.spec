#
# spec file for package kubernetes-pause
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


Name:           kubernetes-pause
Version:        3.1
Release:        0
Summary:        A binary reaping children
License:        Apache-2.0
Group:          System/GUI/KDE
Url:            https://github.com/kubernetes/kubernetes/tree/master/build/pause
Source1:        https://raw.githubusercontent.com/kubernetes/kubernetes/release-1.15/build/pause/pause.c
Source2:        https://raw.githubusercontent.com/kubernetes/kubernetes/release-1.15/LICENSE
Provides:       kubic-pause = %version-%release
Obsoletes:      kubic-pause < %version-%release
BuildRequires:  gcc
BuildRequires:  glibc-devel-static

%description
This executable can be used as a minimal init process inside a container.

%prep
%autosetup -T -c
cp %{SOURCE2} .

%build
gcc %{optflags} -static -DVERSION=%{version} %{SOURCE1} -o pause

%install
install -m0755 -D pause %{buildroot}/usr/bin/pause

%files
%license LICENSE
%{_bindir}/pause

%changelog
