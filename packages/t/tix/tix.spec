#
# spec file for package tix
#
# Copyright (c) 2024 SUSE LLC
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


Name:           tix
BuildRequires:  autoconf
BuildRequires:  fdupes
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(x11)
Version:        8.4.3
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Tools for tk
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Source:         Tix%version-src.tar.bz2
Patch0:         %name.patch
Patch1:         %name-c89.patch
Patch2:         %name-implicit-int.patch
Patch3:         %name-includes.patch
%requires_ge    tk tcl

%description
The Tix library has, by far, the greatest collection of widgets for
programming with Tcl/Tk. Highlights include: hierarchical list box,
directory list/tree view, spreadsheet, tabular list box, combo box,
Motif style file select box, MS Windows style file select box, paned
window, note book, spin control widget and many more. With these new
widgets, your applications will look great and interact with your users
in intuitive ways.

%prep
%autosetup -p0 -n Tix%version
find docs -type f | xargs chmod a-x

%build
autoreconf
export CFLAGS="$RPM_OPT_FLAGS -DUSE_INTERP_RESULT -fno-strict-aliasing"
%configure \
	--with-tcl=%_libdir \
	--with-tk=%_libdir
make

%install
make install DESTDIR=%buildroot libdir=%_libdir/tcl
MANN=%buildroot/%_mandir/mann
mkdir -p $MANN
pushd man
for f in *.n; do
  sed -e '/man\.macros/r man.macros' -e '/man\.macros/d' $f > $MANN/$f
done
popd

%files
%defattr(-,root,root)
%doc ABOUT* README* ChangeLog license.terms index.html
%doc docs/Release* docs/*html docs/img docs/pdf/* demos
%doc %_mandir/*/*
%_libdir/tcl

%changelog
