#
# spec file for package ht
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ht
Version:        2.1.0
Release:        0
Summary:        Disassembler, object dumper and hex editor
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
URL:            http://hte.sf.net/

#Git-Clone:	https://github.com/sebastianbiallas/ht
Source:         http://downloads.sf.net/hte/%name-%version.tar.bz2
Patch1:         ht-no-date.diff
Patch2:         ht-gcc10.diff
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  lzo-devel
BuildRequires:  ncurses-devel
Requires:       hte = %version

%description
The HT editor is a file viewer, editor and analyzer for text, binary,
and (especially) executable files.

This subpackage provides the program under its original name, "ht",
though texlive's tex4ht utility clashes with it, which is why the
real program is in the "hte" subpackage.

%package -n hte
Summary:        Disassembler, object dumper and hex editor
Group:          Development/Tools/Debuggers

%description -n hte
The HT editor is a file viewer, editor and analyzer for text, binary,
and (especially) executable files.

%prep
%autosetup -p1

%build
%configure --enable-release CFLAGS="%optflags -Wno-narrowing"
make %{?_smp_mflags}

%install
%make_install
pushd "%buildroot/%_bindir/"
mv ht hte
ln -s hte ht
popd

%files
%_bindir/ht

%files -n hte
%_bindir/hte
%doc AUTHORS ChangeLog KNOWNBUGS NEWS README TODO

%changelog
