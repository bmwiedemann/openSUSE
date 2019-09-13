#
# spec file for package brise
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           brise
Version:        0.39+git20190120.8d5bc2e
Release:        0
Summary:        Rime Input Schemas Collection
License:        GPL-3.0+
Group:          System/I18n/Chinese
Url:            https://github.com/rime/brise
Source:         brise-%{version}.tar.xz
Source1:        rime-plum-go.tar.xz
Source99:       README
BuildRequires:  go
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rime is an Traditional Chinese input method engine.
Its idea comes from ancient Chinese brush and carving art.
Mainly it's about to express your thinking with your keystrokes.

Brise is the input schemas collection of Rime.

%package -n rime-plum
Summary:    Rime's configuration manager
Group:      System/I18n/Chinese

%description -n rime-plum
Plum is rime's configuration manager.

%prep
%setup -q
echo %{_builddir}
mkdir -p %{_builddir}/go/src/github.com/marguerite
tar -xf %{S:1} -C %{_builddir}/go/src/github.com/marguerite
cp -r %{_builddir}/go/src/github.com/marguerite/rime-plum-go/vendor/* %{_builddir}/go/src/

%build
pushd %{_builddir}/go/src/github.com/marguerite/rime-plum-go
export GOPATH=%{_builddir}/go
go build plum.go
popd

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/go/src/github.com/marguerite/rime-plum-go/plum %{buildroot}%{_bindir}/rime-plum
mkdir -p %{buildroot}%{_datadir}/rime-data
rm -rf package
cp -r * %{buildroot}%{_datadir}/rime-data

%files
%defattr(-,root,root)
%{_datadir}/rime-data/

%files -n rime-plum
%{_bindir}/rime-plum

%changelog
