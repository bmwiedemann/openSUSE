#
# Copyright (c) 2020, Duarte Pousa pousaduarte@gmail.com
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

%global provider        github
%global provider_tld    com
%global project         muesli
%global repo            duf
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global debug_package   %{nil}

Name:           duf
Version:        0.8.1+git64.24c3369
Release:        0
License:        MIT
Summary:        Disk Usage/Free Utility
Group:          System/Management
Url:            https://github.com/muesli/duf
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz

BuildRequires:  go >= 1.11
BuildRequires:  go-md2man
BuildRequires:  fdupes

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
 
%description
Disk Usage/Free Utility (Linux, BSD, macOS & Windows)
 
%prep
%setup -q
%setup -q T -D -a 1
find . -iname "vendor" -type d

%build
export VERSION=%{version}
export COMMIT=%{commit}
export CGO_ENABLED=0
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags "-s -w -X main.CommitSHA=$COMMIT -X main.Version=$VERSION" \
   -o %{name} ;

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Build the man pages.
go-md2man -in README.md -out %{name}.1

# Install the man pages.
mkdir -p "%{buildroot}/%{_mandir}/man1"
install -D -m 0644 %{name}.1 "%{buildroot}/%{_mandir}/man1"

#hardlink duplicated files
%fdupes %{buildroot}

%files
%defattr(-,root,root)
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1.gz

%changelog
