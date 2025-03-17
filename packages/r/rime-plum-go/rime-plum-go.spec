#
# spec file for package rime-plum-go
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

Name:           rime-plum-go
Version:        1.0.3
Release:        0
Summary:        RIME's plum configuration manager in golang
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/marguerite/rime-plum-go
Source1:        rime-plum-go-%{version}.tar.gz
Source2:        vendor.tar.zst
BuildRequires:  zstd
BuildRequires:  golang(API) >= 1.17

%description
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

rime-plum-go is RIME's plum configuration manager in golang

%package -n rime-plum
Summary:        Rime's configuration manager
Group:          System/I18n/Chinese

%description -n rime-plum
Plum is rime's configuration manager in golang.

%prep
echo %{_builddir}
mkdir -p %{_builddir}/go/src/github.com/marguerite
tar -xf %{SOURCE1} -C %{_builddir}/go/src/github.com/marguerite
tar -xf %{SOURCE2} -C %{_builddir}/go/src/github.com/marguerite/rime-plum-go-%{version}/
cp -r %{_builddir}/go/src/github.com/marguerite/rime-plum-go-%{version}/vendor/* %{_builddir}/go/src/

%build
pushd %{_builddir}/go/src/github.com/marguerite/rime-plum-go-%{version}
export GOPATH=%{_builddir}/go
go build -ldflags "-buildid="
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/go/src/github.com/marguerite/rime-plum-go-%{version}/rime-plum-go %{buildroot}%{_bindir}/rime-plum

%files -n rime-plum
%{_bindir}/rime-plum

%changelog
