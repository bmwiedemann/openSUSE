#
# spec file for package harec
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


Name:           harec
Release:        0
Version:        1701558776.08af325
Summary:        Bootstrap compiler for hare
Group:          Development/Tools/Building
URL:            https://git.sr.ht/~sircmpwn/harec
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  make
BuildRequires:  qbe
BuildRequires:  zstd
License:        GPL-3.0-only

%description

HareC is a bootstrap compiler for the Hare programming language. Written in C11 for
POSIX-compatible systems.

%prep
%setup -q
mkdir -p build/

%build

export CFLAGS="%optflags"

# Harec does not use autoconf
pushd build/
../configure
make %{?_smp_mflags}
popd

%install
export CFLAGS="%optflags"
pushd build/
make %{?_smp_mflags} DESTDIR="%{buildroot}" BINDIR="%{_bindir}" install
popd

%check
export CFLAGS="%optflags"
cd build
../configure
make %{?_smp_mflags} check

%files
%{_bindir}/%{name}
%license COPYING
%doc     README.md

%changelog
