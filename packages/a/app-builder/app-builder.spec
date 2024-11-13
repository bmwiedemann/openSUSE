#
# Copyright (c) 2021 SUSE LLC
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

#macros for Fedora
%global goipath  github.com/develar/app-builder
%global extractdir0 app-builder-5.0.0-alpha.11

Name:           app-builder
Version:        5.0.0~alpha.11
Release:        0
License:        MIT
Summary:        Generic helper tool to build app in a distributable format
Url:            https://github.com/develar/app-builder
Source0:        https://github.com/develar/app-builder/archive/v5.0.0-alpha.11.tar.gz
Source1:        vendor.tar.gz
%if 0%{?fedora}
BuildRequires:  golang
BuildRequires:  go-rpm-macros
BuildRequires:  golang-ipath(golang.org/x/sys)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
%if 0%{fedora} < 41
BuildRequires:  golang(github.com/alecthomas/template)
%endif
BuildRequires:  golang(github.com/alecthomas/units)
BuildRequires:  golang(github.com/aws/aws-sdk-go)
BuildRequires:  golang(github.com/disintegration/imaging)
BuildRequires:  golang(github.com/dustin/go-humanize)
BuildRequires:  golang(github.com/json-iterator/go)
BuildRequires:  golang(github.com/mattn/go-colorable)
BuildRequires:  golang(github.com/mattn/go-isatty)
%if 0%{fedora} < 39
BuildRequires:  golang(github.com/minio/blake2b-simd)
%endif
BuildRequires:  golang(github.com/mitchellh/go-homedir)
BuildRequires:  golang(github.com/oxtoacart/bpool)
BuildRequires:  golang(github.com/phayes/permbits)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/pkg/xattr)
BuildRequires:  golang(github.com/segmentio/ksuid)
BuildRequires:  golang(go.uber.org/zap)
BuildRequires:  golang(go.uber.org/zap/buffer)
BuildRequires:  golang(go.uber.org/zap/zapcore)
BuildRequires:  golang(howett.net/plist)
%if 0%{fedora} >= 41
BuildRequires: compat-golang-github-imdario-mergo-devel
%endif
%else
BuildRequires:  golang(API)
BuildRequires:  golang-packaging
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150600
# Go source packages are horribly broken on Leap (mismatching compiler versions between libraries and toolchain)
BuildRequires:  golang-org-x-sys
%endif

%description
Generic helper tool to build app in a distributable formats.
Used by electron-builder but applicable not only for building Electron applications.

%if 0%{?fedora}
%gopkg
%endif
 
%prep
%autosetup  -a1 -n app-builder-5.0.0-alpha.11
# remove bundled dependencies 
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150700 || 0%{?fedora}
rm -rf vendor/golang.org/x/sys
%endif

%if 0%{?fedora}
rm -rf vendor/github.com/{alecthomas/kingpin,alecthomas/units,aws,disintegration,dustin,hpcloud,jmespath,json-iterator,mattn,mitchellh,modern-go,onsi,oxtoacart,phayes,pkg,samber,segmentio}
rm -rf vendor/go.uber.org
rm -rf vendor/golang.org
rm -rf vendor/gopkg.in/{fsnotify.v1,tomb.v1,yaml.v2}
rm -rf vendor/howett.net

%if 0%{fedora} < 39
rm -rf vendor/github.com/minio
%endif

%if 0%{fedora} < 41
rm -rf vendor/github.com/alecthomas
%endif

grep -FrlZ 'github.com/alecthomas/kingpin' | xargs -tr0 -P$(nproc) -- sed -i 's|github.com/alecthomas/kingpin|gopkg.in/alecthomas/kingpin.v2|g'
%endif

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

export CGO_CFLAGS="$CFLAGS -fpie"
export CGO_CXXFLAGS="$CXXFLAGS -fpie"
export CGO_LDFLAGS="%{?build_ldflags}"

%if 0%{?fedora}
%goprep -k -e
%else
%goprep %goipath
export GO111MODULE=off
%endif


export GOFLAGS='-ldflags=-compressdwarf=false' #fix broken debuginfo
%gobuild

%install
install -pvDm755 \
%if 0%{?fedora}
%name \
%else
%{_builddir}/go/bin/%{name} \
%endif
"%{buildroot}/%{_bindir}/%{name}"


%files
%{_bindir}/%{name}
%license LICENSE
%doc readme.md CHANGELOG.md

%changelog
