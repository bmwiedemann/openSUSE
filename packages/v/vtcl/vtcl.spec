#
# spec file for package vtcl
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


Name:           vtcl
Version:        1.6.1a1
Release:        0
Summary:        Visual Tcl
License:        GPL-2.0+
Group:          Development/Languages/Tcl
Url:            http://vtcl.sourceforge.net
Source:         http://sourceforge.net/projects/vtcl/files/%name-%version.tar.bz2
Source1:        vtcl
Patch0:         vtcl-tkversion.patch
Patch1:         vtcl-browser.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       tcl
Requires:       tix
Requires:       tk
Requires:       xdg-utils

%description
Visual Tcl is a freely-available, high-quality application development
environment for UNIX, Windows, and Macintosh platforms. Writing
entirely in Tcl and generating pure Tcl should make porting either
unnecessary or trivial.



Authors:
--------
    Stewart Allen <stewart@neuron.com>

%prep
%setup -q
%patch0
%patch1

%build
#
# There is nothing to build here :)
#

%install
  LIBDIR=$RPM_BUILD_ROOT/usr/share/vtcl
  BINDIR=$RPM_BUILD_ROOT%_bindir
  mkdir -p $BINDIR $LIBDIR
  cp -a *.tcl images lib $LIBDIR
  install -m 755 %SOURCE1 $BINDIR

  # avoid rpmlint errors.
  ls
  mv sample examples
  ln -s examples sample
  ls

%files
%defattr(-,root,root)
%_datadir/vtcl
%_bindir/vtcl
%doc LICENSE ChangeLog README doc demo sample examples

%changelog
