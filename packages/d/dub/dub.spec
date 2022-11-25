#
# spec file for package dub
#
# Copyright (c) 2022 SUSE LLC
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


# DMD is available only on x86*. Use LDC otherwise.
%ifarch %{ix86} x86_64
%bcond_without dcompiler_dmd
%else
%bcond_with dcompiler_dmd
%endif
Name:           dub
Version:        1.29.0
Release:        0
Summary:        Package manager and meta build tool for the D programming language
License:        MIT
Group:          Development/Languages/Other
URL:            https://code.dlang.org
Source:         https://github.com/dlang/dub/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
%if %{with dcompiler_dmd}
BuildRequires:  dmd
BuildRequires:  phobos-devel
%else
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
%endif

%description
Package Manager for the D Programming language.
DUB emerged as a more general replacement for vibe.d's package manager.
It does not imply a dependecy to vibe.d for packages and was extended to
not only directly build projects, but also to generate project files
(currently VisualD). Mono-D also support the use of dub.json
(dub's package description) as project file.

%prep
%autosetup

# reproducible builds:
perl -i -pe 's{__DATE__}{""}g' source/dub/commandline.d

%build
echo Generating version file...
echo "module dub.version_;" > source/dub/version_.d
echo "enum dubVersion = \"%{version}\";" >> source/dub/version_.d

%if %{with dcompiler_dmd}
  dmd -defaultlib=:libphobos2.so \
  -g \
%else
  ldmd2 \
%ifnarch %{arm} %{ix86}
  -g \
%endif
%endif
  -ofbin/dub -w -O \
  -version=DubUseCurl -Isource -L-lcurl @build-files.txt

%install
mkdir -p %{buildroot}%{_bindir}/
install -D -m 755 bin/%{name} %{buildroot}%{_bindir}/

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
