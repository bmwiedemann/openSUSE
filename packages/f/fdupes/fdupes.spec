#
# spec file for package fdupes
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


%{?!_rpmmacrodir:%define _rpmmacrodir /usr/lib/rpm/macros.d}

Name:           fdupes
Version:        2.2.1
Release:        0
Summary:        Tool to identify or delete duplicate files
License:        MIT
Group:          Productivity/Archiving/Compression
URL:            https://github.com/adrianlopezroche/fdupes
Source0:        https://github.com/adrianlopezroche/fdupes/releases/download/v%{version}/fdupes-%{version}.tar.gz
Source1:        macros.fdupes
Source2:        fdupes_wrapper.cpp
BuildRequires:  gcc-c++

%description
FDUPES is a program for identifying or deleting duplicate files
residing within specified directories.

%prep
%autosetup -p1

%build
%configure --without-ncurses
%make_build
g++ $RPM_OPT_FLAGS %{S:2} -o fdupes_wrapper

%install
%make_install
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.%{name}
install -D -m755 fdupes_wrapper  %{buildroot}/usr/lib/rpm/fdupes_wrapper

%check
./%{name} testdir
./%{name} --omitfirst testdir
./%{name} --recurse testdir
./%{name} --size testdir

# Check wrapper
PATH=`pwd`:$PATH
(cd testdir; md5sum ./* ./*/* > ../testdir.md5 || true)
for operation in '-n' '-s' ' '; do
  cp -R testdir "testdir${operation}"
  ./fdupes_wrapper ${operation} "testdir${operation}"
  (cd "testdir${operation}"; md5sum --check ../testdir.md5)
done
# Check order does not depend on creation order - x should be target
mkdir testdir_order
for t in "a b x" "x a b" "a x b"; do
  pushd testdir_order
  for f in $t ; do cp ../testdir.md5 $f; done
  ../fdupes_wrapper -s ./
  test -h ./a
  test -h ./b
  rm *
  popd
done

%files
%doc CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_rpmmacrodir}/macros.%{name}
/usr/lib/rpm/fdupes_wrapper

%changelog
