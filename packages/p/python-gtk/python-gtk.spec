#
# spec file for package python-gtk
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


%define lparen (
%define rparen )
%define python_gtk_req %(zgrep -a _required_version %{SOURCE0} | sed -n 's/_required_version,[[:space:]]*/ >= /;s/%{rparen}$//;s/1.0.2%{rparen} dnl or 1.1.7/1.1.7/;s/\\%{lparen}glib\\|gtk\\|libglade\\|gobject\\%{rparen}/&2/;s/py\\%{lparen}.*\\%{rparen} /python-\\1 /;/gtk2unixprint/d;s/^m4_define%{lparen}//p' | tr '\\n' ' ')
Name:           python-gtk
Version:        2.24.0
Release:        0
Summary:        Python bindings for the GTK+ widget set
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            http://www.pygtk.org/
Source:         http://ftp.gnome.org/pub/GNOME/sources/pygtk/2.24/pygtk-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM pygtk-2.22.0-capsule.patch bgo#623965 bnc#669802 jmatejek@novell.com -- Conditionally use the new Capsule API instead of PyCObject
Patch0:         pygtk-2.22.0-capsule.patch
# PATCH-FIX-UPSTREAM pygtk-Drop-the-PangoFont-find_shaper-virtual-method.patch dimstar@opensuse.org -- Drop the PangoFont find_shaper virtual method
Patch1:         https://raw.githubusercontent.com/flathub/org.glimpse_editor.Glimpse/master/patches/pygtk-Drop-the-PangoFont-find_shaper-virtual-method.patch
# Patch to fix C99 violations [boo#1225916]
# originally from https://bugzilla.redhat.com/show_bug.cgi?id=2190017
Patch2:         pygtk2-c99.patch
BuildRequires:  fdupes
# Only for directory ownership:
BuildRequires:  gtk-doc
BuildRequires:  libglade2-devel
BuildRequires:  python-cairo-devel
BuildRequires:  python-devel
BuildRequires:  python-gobject2-devel
BuildRequires:  python-rpm-macros
Requires:       %{python_gtk_req}
# for cross-distro compatibility:
Provides:       pygtk2 = %{version}
Provides:       python2-gtk = %{version}

%description
PyGTK is an extension module for python that gives you access to the
GTK+ widget set.  Just about anything you can write in C with GTK+ you
can write in python with PyGTK (within reason), but with all of
python's benefits.

%package devel
Summary:        Files needed to build wrappers for GTK+ addon libraries
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
Requires:       python-cairo-devel
Requires:       python-gobject2-devel
Provides:       python2-gtk-devel = %{version}

%description devel
This package contains files required to build wrappers for GTK+ addon
libraries so that they interoperate with pygtk.

%package doc
Summary:        Python bindings for the GTK+ widget set
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
PyGTK is an extension module for python that gives you access to the
GTK+ widget set.  Just about anything you can write in C with GTK+ you
can write in python with PyGTK (within reason), but with all of
python's benefits.

%prep
%autosetup -p1 -n pygtk-%{version}

find examples -type f -name "*.py" -exec sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python2|" {} \;
find examples -type f -name "*.py" -exec sed -i "s|#! %{_bindir}/env python|#!%{_bindir}/python2|" {} \;

%build
%configure
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -name '*.la' -or -name '*.a' | xargs rm -v

# move the docs to FHS-correct directory
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/gtk-doc %{buildroot}%{_docdir}/%{name}

sed -i "s|#!%{_bindir}/python|#!%{_bindir}/python2|" %{buildroot}%{_bindir}/pygtk-demo

rm examples/Makefile*
# demo is already in devel package
rm -rf examples/pygtk-demo
chmod +x %{buildroot}%{_libdir}/pygtk/2.0/{,*/}*.py
%fdupes %{buildroot}%{_libdir}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README MAPPING ChangeLog THREADS
%exclude %{_docdir}/%{name}/html/
%{python2_sitearch}/gtk-2.0/gtk/
%{python2_sitearch}/gtk-2.0/atk.so
%{python2_sitearch}/gtk-2.0/gtkunixprint.so
%{python2_sitearch}/gtk-2.0/pango*.so

%files devel
%{_bindir}/pygtk-codegen-2.0
%{_bindir}/pygtk-demo
%{_includedir}/pygtk-2.0/pygtk/
%{_libdir}/pkgconfig/*.pc
# we explicitly list the directories here to be sure we don't include something
# that should live in the main package
%dir %{_datadir}/pygtk
%dir %{_libdir}/pygtk
%dir %{_datadir}/pygtk/2.0
%dir %{_libdir}/pygtk/2.0
%{_datadir}/pygtk/2.0/defs/
%{_libdir}/pygtk/2.0/pygtk-demo.py*
%{_libdir}/pygtk/2.0/demos/

%files doc
%doc examples/
%{_docdir}/%{name}/html/

%changelog
