#
# spec file for package graphviz-addons
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


#fixes build failure caused by new .debug files, not sure how to fix correctly

%define mname graphviz
%define libname libgraphviz6
# name of the plugin config file that dot creates
%define config_file config6
# Build with extras or not, determines pulling additional dependencies
# and breaks build cycle
%bcond_without extras
# Java and ocaml are not in ring1, thus this gets overriden in staging
%bcond_without java
%bcond_with    ocaml
# PHP7 requires swig >= 3.0.11, not available on Leap 42.x
%if 0%{?suse_version} >= 1500
%define php_version 7
%else
%define php_version 5
%endif

%if 0%{?suse_version} > 1510
%define ruby_version 2.6
%else
%define ruby_version 2.5
%endif

# No pkgconfig(gts) in sle12 GA or SPx, but in sle15
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%define sle12 1
%else
%define sle12 0
%endif
Name:           graphviz-addons
Version:        2.42.1
Release:        0
Summary:        Graph Visualization Tools
License:        EPL-1.0
Group:          Productivity/Graphics/Visualization/Graph
Url:            http://www.graphviz.org/
Source:         https://www2.graphviz.org/Packages/stable/portable_source/graphviz-%{version}.tar.gz
Source2:        graphviz-rpmlintrc
#PATCH-FIX-UPSTREAM add flags to also link against libGLU and libGL
Patch1:         graphviz-smyrna-link_against_glu.patch
Patch2:         graphviz-fix-pkgIndex.patch
#PATCH-FIX-UPSTREAM Off-by-one bug
Patch3:         graphviz-array_overflow.patch

Patch6:         graphviz-2.20.2-interpreter_names.patch
#PATCH-FIX-UPSTREAM Don't warn about harmless issues with swig generated code
Patch7:         graphviz-useless_warnings.patch
Patch8:         graphviz-no_strict_aliasing.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  guile-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
%if 0%{sle12} != 1
BuildRequires:  pkgconfig(gts)
%endif
BuildRequires:  pkgconfig(zlib)
Requires:       graphviz-plugins-core = %{version}
Recommends:     graphviz-gd = %{version}
%if %{with extras}
BuildRequires:  argon2-devel
BuildRequires:  freeglut-devel

BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  perl
BuildRequires:  python3-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  php7-devel
BuildRequires:  swig >= 3.0.11
%else
BuildRequires:  php5-devel
BuildRequires:  swig
%endif
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2) >= 2
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtkglext-1.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(ijs)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
%if %{with java}
BuildRequires:  java-devel >= 1.6.0
%endif
%if %{with ocaml}
BuildRequires:  ocaml
%endif
%endif

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in bar charts).

%package -n graphviz-gvedit
Summary:        Graph editor based on Qt
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz

%description -n graphviz-gvedit
The Qt5 graph editor included with graphviz, packaged
separately to avoid cycles in the build of the graphviz
package.

%package -n graphviz-smyrna
Summary:        Large graph viewer
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz

%description -n graphviz-smyrna
Experimental large graph viewer using graphviz

%package -n graphviz-gnome
Summary:        Graphviz plugins that use gtk/GNOME
Group:          Productivity/Graphics/Visualization/Graph
Recommends:     plugin-core = %{version}
Requires(post): graphviz = %{version}
Supplements:    packageand(graphviz:xorg-x11-fonts-core)

%description -n graphviz-gnome
Graphviz plugins that use gtk/GNOME.

%package -n graphviz-gd
Summary:        Graphviz plugin for renderers based on gd
Group:          Productivity/Graphics/Visualization/Graph
Requires(post): graphviz >= %{version}

%description -n graphviz-gd
The graphviz-gd package contains the gd extensions for the graphviz
tools.

%package -n graphviz-guile
Summary:        Graph Visualization Tools
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       guile

%description -n graphviz-guile
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in bar charts).

%package -n graphviz-java
Summary:        Graph Visualization Tools
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       java

%description -n graphviz-java
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in bar charts).

%package -n graphviz-x11
Summary:        Graph editors based on X11
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz

%description -n graphviz-x11
The lefty/dotty/lneato X11 graph editors included with graphviz,
packaged separately to reduce build dependencies.

%package -n graphviz-lua
Summary:        Lua extension for graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       lua

%description -n graphviz-lua
The graphviz-lua package contains the lua extension for the graphviz
tools.

%package -n graphviz-ocaml
Summary:        OCAML extension for graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       ocaml

%description -n graphviz-ocaml
The graphviz-ocaml package contains the Objective Caml extension for
the graphviz tools.

%package -n graphviz-perl
Summary:        Perl extension for Graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       perl = %{perl_version}

%description -n graphviz-perl
The graphviz-perl package contains the Perl extension for the graphviz
tools.

%package -n graphviz-php
Summary:        PHP Extension for Graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       php%{php_version}

%description -n graphviz-php
The graphviz-php package contains the PHP extension for the graphviz
tools.

%package -n graphviz-python
Summary:        Python Extension for Graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       python

%description -n graphviz-python
The graphviz-python package contains the Python extension for the
graphviz tools.

%package -n graphviz-ruby
Summary:        Ruby Extension for Graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
Requires:       ruby

%description -n graphviz-ruby
The graphviz-ruby package contains the ruby extension for the graphviz
tools.

%package -n graphviz-tcl
Summary:        Tcl extension tools for graphviz
Group:          Development/Libraries/Tcl
Requires:       graphviz = %{version}
Requires:       tcl >= 8.3
Requires:       tk

%description -n graphviz-tcl
The graphviz-tcl package contains the various tcl packages (extensions)
for the graphviz tools.

%package -n graphviz-doc
Summary:        Documentation for graphviz
Group:          Documentation/Howto

%description -n graphviz-doc
Provides some additional PDF and HTML documentation for graphviz.

%package -n %{libname}
Summary:        Library for the manipulation of layout of graphs
Group:          System/Libraries
Recommends:     graphviz-plugins-core

%description -n %{libname}
Library for the manipulation of layout of graphs (as in nodes and edges,
not as in bar charts).

%package plugins-core
Summary:        Core plugins for graphviz
# Needed for dot binary
Group:          Productivity/Graphics/Visualization/Graph
Requires(post): %{mname}

%description plugins-core
Core plugins for graphviz:
 * libgvplugin_core
 * libgvplugin_dot_layout
 * libgvplugin_neato_layout

%package devel
Summary:        Graphviz development package
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{mname} = %{version}

%description devel
The graphviz-devel package contains all that's necessary for developing
programs that use the graphviz libraries including man3 pages.


#autosetup breaks graphviz-addons
%prep
%setup -q -n %{mname}-%{version}

%patch1
%patch2
%patch3

%patch6
%patch7
%patch8

# pkg-config returns 0 (TRUE) when guile-2.2 is present
if pkg-config --atleast-version=2.2 guile-2.2; then
sed "s/guile-2.0/guile-2.2/" -i configure.ac
fi

rm -f contrib/gprof2dot.awk

# Fix path for lua/php install
sed -i \
    -e 's@LUA_INSTALL_DIR="/usr.*@LUA_INSTALL_DIR=%{lua_archdir}@' \
    -e 's@\(PHP_INSTALL_DIR=.*\)/php/modules@\1/php%{php_version}/extensions@' \
    -e 's@\(PHP_INSTALL_DATADIR=.*\)/php@\1/php%{php_version}@' \
    configure.ac

%build
./autogen.sh RUBY_VER=%{ruby_version}
CFLAGS="%{optflags} -ffast-math -fno-strict-aliasing -fno-strict-overflow -fPIC"

%if %{with extras}

CFLAGS="$CFLAGS -I/usr/include/ruby-%{ruby_version}.0"
#seems to be broken? gives -I/usr/lib64/ruby/2.6.0/x86_64-linux-gnu, ruby.h is in /usr/lib64/ruby/2.6.0
#CFLAGS="$CFLAGS $(pkg-config --cflags ruby-$(echo {rb_ver} | sed 's|\.[^.]*$||'))"

%endif

export CFLAGS="$CFLAGS"
export CPPFLAGS="$CFLAGS"
export LDFLAGS="-pie"
%configure \
      --disable-static \
      --without-included-ltdl \
      --disable-ltdl-install \
      --with-ipsepcola \
      --without-ming \
      --disable-io \
      --without-visio \
%if %{with extras}
      --with-x \
      --with-qt \
      --with-smyrna \
      RUBY_VER=%{ruby_version} \
%else
      --without-mylibgd \
      --without-libgd \
%endif
      --disable-silent-rules
make %{?_smp_mflags}

%install
make install \
	DESTDIR=%{buildroot} \
	docdir=%{buildroot}%{_docdir}/%{mname} \
	pkgconfigdir=%{_libdir}/pkgconfig

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}/%{_docdir}
mkdir -p %{buildroot}%{_datadir}/%{nmame}

rm -f %{buildroot}/%{_libdir}/%{mname}/pkgIndex.tcl
chmod -x %{buildroot}%{_datadir}/%{mname}/lefty/*

mkdir -p %{buildroot}%{_libdir}/graphviz
touch %{buildroot}%{_libdir}/graphviz/%{config_file}

mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
cat <<EOF >%{buildroot}%{_sysconfdir}/ld.so.conf.d/%{mname}.conf
%{_libdir}/%{mname}
%{_libdir}/%{mname}/sharp
%{_libdir}/%{mname}/java
%{_libdir}/%{mname}/perl
%{_libdir}/%{mname}/php
%{_libdir}/%{mname}/ocaml
%{_libdir}/%{mname}/python
%{_libdir}/%{mname}/lua
%{_libdir}/%{mname}/tcl
%{_libdir}/%{mname}/guile
%{_libdir}/%{mname}/ruby
EOF

#Correct the path to the shared library
for manfile in $(find %{buildroot} -name \*.man); do
    sed -i \
        -e 's$%{_prefix}/lib/graphviz$%{_libdir}/%{mname}$g' \
        $manfile
done

# There are no such binaries distributed by us
rm -f %{buildroot}%{_mandir}/man1/mingle.1

%if %{with extras}
# Fix doc location
cp -a %{buildroot}%{_datadir}/%{mname}/doc %{buildroot}%{_defaultdocdir}/%{mname}-doc
%fdupes -s %{buildroot}%{_defaultdocdir}/%{mname}-doc
# Prune all the content of the base graphviz package
rm -rf %{buildroot}%{_libdir}/pkgconfig
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_datadir}/graphviz/examples
rm -rf %{buildroot}%{_datadir}/graphviz/graphs
rm -rf %{buildroot}%{_datadir}/graphviz/gvpr
rm -f  %{buildroot}%{_mandir}/man3/*.3
rm -f  %{buildroot}%{_mandir}/man7/*.7
rm -f  %{buildroot}%{_libdir}/graphviz/%{config_file}
rm -f  %{buildroot}%{_libdir}/graphviz/libgvplugin_core*
rm -f  %{buildroot}%{_libdir}/graphviz/libgvplugin_dot_layout*
rm -f  %{buildroot}%{_libdir}/graphviz/libgvplugin_neato_layout*
# binaries removal
for i in acyclic bcomps ccomps circo cluster dijkstra dot dot2gxl dot_builtins edgepaint fdp gc gml2gv graphml2gv gv2gml gv2gxl gvcolor gvgen gvmap gvmap.sh gvpack gvpr gxl2dot gxl2gv mm2gv neato nop osage patchwork prune sccmap sfdp tred twopi unflatten vimdot; do
    rm -f %{buildroot}%{_bindir}/$i
    rm -f %{buildroot}%{_mandir}/man1/$i.1
done
# libraries removal
rm -f %{buildroot}%{_sysconfdir}/ld.so.conf.d/graphviz.conf
rm -f %{buildroot}%{_libdir}/lib{cdt,cgraph,gvc,gvpr,pathplan,xdot,lab_gamut}.so*
# Fix tcl locations
for lib in libgdtclft* libgv_tcl.so libtcldot* libtclplan* ; do
   mv %{buildroot}%{_libdir}/%{mname}/tcl/${lib} %{buildroot}%{_libdir}
done
# remove duplicated tcl files
for i in libgdtclft.so.0.0.0 libgv_tcl.so libtcldot.so.0.0.0 libtcldot_builtin.so.0.0.0 libtclplan.so.0.0.0; do
    rm -f %{buildroot}%{_libdir}/tcl8.6/graphviz/$i
    ln -s %{_libdir}/$i %{buildroot}%{_libdir}/tcl8.6/graphviz/$i
done
mkdir -p %{buildroot}%{_datadir}/tcl/%{mname}/
mv %{buildroot}%{_libdir}/%{mname}/tcl/pkgIndex.tcl %{buildroot}%{_datadir}/tcl/%{mname}/pkgIndex.tcl
# remove graphviz bindings from graphviz dir, these are installed into the language specific directories
rm -rf %{buildroot}%{_libdir}/graphviz/lua
rm -rf %{buildroot}%{_libdir}/graphviz/perl
rm -rf %{buildroot}%{_libdir}/graphviz/php
rm -rf %{buildroot}%{_libdir}/graphviz/python
rm -rf %{buildroot}%{_libdir}/graphviz/ruby
%else
# These are part of gnome subpkg
rm -f %{buildroot}%{_libdir}/graphviz/libgvplugin_pango*
rm -f %{buildroot}%{_libdir}/graphviz/libgvplugin_xlib*
# This is part of the gd subpkg only
rm -f %{buildroot}%{_mandir}/man1/{diffimg.1*,dotty.1*,lefty.1*,lneato.1*}
# This is part of the x11 subpkg only
rm -rf %{buildroot}%{_datadir}/graphviz/lefty
%endif
# Remove wrongly located docs
rm -rf %{buildroot}%{_datadir}/%{mname}/doc

%post plugins-core
# run "dot -c" to generate plugin config %%{_libdir}/graphviz/config
dot -c
test -s %{_libdir}/graphviz/%{config_file} || echo "%{_libdir}/graphviz/%{config_file} doesn't exist! Check installation."

%postun plugins-core
if ! test -x %{_bindir}/dot; then
    rm -f %{_libdir}/%{mname}/%{config_file}
fi

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%if %{with extras}
%files -n graphviz-gvedit
%license COPYING
%{_bindir}/gvedit
%dir %{_datadir}/%{mname}/gvedit
%{_datadir}/%{mname}/gvedit/attrs.txt
%{_mandir}/man1/gvedit.1%{ext_man}

%files -n graphviz-smyrna
%license COPYING
%{_bindir}/smyrna
%{_datadir}/%{mname}/smyrna
%{_mandir}/man1/smyrna.1%{ext_man}

%files -n graphviz-gd
%{_bindir}/diffimg
%{_mandir}/man1/diffimg.1%{ext_man}
%{_libdir}/graphviz/libgvplugin_gd.so*

%post -n graphviz-gd
%{_bindir}/dot -c

%postun -n graphviz-gd
%{_bindir}/dot -c 2>/dev/null

%post -n graphviz-gnome
%{_bindir}/dot -c

%postun -n graphviz-gnome
%{_bindir}/dot -c 2>/dev/null

%files -n graphviz-gnome
%{_libdir}/graphviz/libgvplugin_gs*
%{_libdir}/graphviz/libgvplugin_rsvg*
%{_libdir}/graphviz/libgvplugin_pango*
%{_libdir}/graphviz/libgvplugin_gtk*
%{_libdir}/graphviz/libgvplugin_xlib*
%{_libdir}/graphviz/libgvplugin_gdk*

%post -n graphviz-tcl -p /sbin/ldconfig
%postun -n graphviz-tcl -p /sbin/ldconfig

%files -n graphviz-guile
%{_libdir}/graphviz/guile
%{_mandir}/man3/gv.3guile%{ext_man}

%if %{with java}
%files -n graphviz-java
%{_libdir}/graphviz/java
%{_mandir}/man3/gv.3java%{ext_man}
%endif

%files -n graphviz-lua
%{lua_archdir}/gv.so
%{_mandir}/man3/gv.3lua%{ext_man}

%files -n graphviz-x11
%license COPYING
%{_bindir}/dotty
%{_bindir}/lefty
%{_bindir}/lneato
%{_datadir}/%{mname}/lefty
%{_mandir}/man1/dotty.1%{ext_man}
%{_mandir}/man1/lefty.1%{ext_man}
%{_mandir}/man1/lneato.1%{ext_man}

%if %{with ocaml}
%files -n graphviz-ocaml
%{_libdir}/graphviz/ocaml
%{_mandir}/man3/gv.3ocaml%{ext_man}
%endif

%files -n graphviz-perl
%{perl_vendorarch}/gv.pm
%{perl_vendorarch}/gv.so
%{_mandir}/man3/gv.3perl%{ext_man}

%files -n graphviz-php
%{_libdir}/php%{php_version}/extensions/gv.so
%{_datadir}/php%{php_version}/gv.php
%{_mandir}/man3/gv.3php%{ext_man}

%files -n graphviz-python
%dir %{_libdir}/graphviz/python2
%dir %{_libdir}/graphviz/python3
%{python_sitearch}/_gv.so
%{python_sitearch}/gv.py
%{_libdir}/graphviz/python2/_gv.so
%{_libdir}/graphviz/python2/gv.py
%{_libdir}/graphviz/python2/libgv_python2.so
%{python3_sitearch}/_gv.so
%{python3_sitearch}/gv.py
%{_libdir}/graphviz/python3/_gv.so
%{_libdir}/graphviz/python3/gv.py
%{_libdir}/graphviz/python3/libgv_python3.so
%{_mandir}/man3/gv.3python%{ext_man}

%files -n graphviz-ruby
%{rb_vendorarchdir}/gv.so
%{_mandir}/man3/gv.3ruby%{ext_man}

%files -n graphviz-tcl
%dir %{_datadir}/tcl/%{mname}
%{_libdir}/tcl[0-9].[0-9]
%{_libdir}/libgdtclft*
%{_libdir}/libgv_tcl.so
%{_libdir}/libtcldot*
%{_libdir}/libtclplan*
%{_datadir}/tcl/%{mname}/pkgIndex.tcl
%{_mandir}/man3/*.3tcl*

%files -n graphviz-doc
%docdir %{_defaultdocdir}/%{mname}-doc
%{_defaultdocdir}/%{mname}-doc
%{_datadir}/graphviz/demo

%else
%files
%doc doc/FAQ.html AUTHORS README NEWS ChangeLog
%license COPYING
%{_bindir}/acyclic
%{_bindir}/bcomps
%{_bindir}/ccomps
%{_bindir}/circo
%{_bindir}/cluster
%{_bindir}/dijkstra
%{_bindir}/dot
%{_bindir}/dot2gxl
%{_bindir}/dot_builtins
%{_bindir}/edgepaint
%{_bindir}/fdp
%{_bindir}/gc
%{_bindir}/gml2gv
%{_bindir}/graphml2gv
%{_bindir}/gv2gml
%{_bindir}/gv2gxl
%{_bindir}/gvcolor
%{_bindir}/gvgen
%{_bindir}/gvmap
%{_bindir}/gvmap.sh
%{_bindir}/gvpack
%{_bindir}/gvpr
%{_bindir}/gxl2dot
%{_bindir}/gxl2gv
%{_bindir}/mm2gv
%{_bindir}/neato
%{_bindir}/nop
%{_bindir}/osage
%{_bindir}/patchwork
%{_bindir}/prune
%{_bindir}/sccmap
%{_bindir}/sfdp
%{_bindir}/tred
%{_bindir}/twopi
%{_bindir}/unflatten
%dir %{_datadir}/%{mname}
%{_datadir}/%{mname}/graphs
%dir %{_datadir}/%{mname}/gvpr
%{_datadir}/%{mname}/gvpr/addranks
%{_datadir}/%{mname}/gvpr/addrings
%{_datadir}/%{mname}/gvpr/anon
%{_datadir}/%{mname}/gvpr/attr
%{_datadir}/%{mname}/gvpr/bb
%{_datadir}/%{mname}/gvpr/bbox
%{_datadir}/%{mname}/gvpr/cliptree
%{_datadir}/%{mname}/gvpr/col
%{_datadir}/%{mname}/gvpr/collapse
%{_datadir}/%{mname}/gvpr/color
%{_datadir}/%{mname}/gvpr/dechain
%{_datadir}/%{mname}/gvpr/deghist
%{_datadir}/%{mname}/gvpr/deledges
%{_datadir}/%{mname}/gvpr/delmulti
%{_datadir}/%{mname}/gvpr/delnodes
%{_datadir}/%{mname}/gvpr/depath
%{_datadir}/%{mname}/gvpr/dijkstra
%{_datadir}/%{mname}/gvpr/flatten
%{_datadir}/%{mname}/gvpr/get-layers-list
%{_datadir}/%{mname}/gvpr/group
%{_datadir}/%{mname}/gvpr/indent
%{_datadir}/%{mname}/gvpr/knbhd
%{_datadir}/%{mname}/gvpr/maxdeg
%{_datadir}/%{mname}/gvpr/path
%{_datadir}/%{mname}/gvpr/rotate
%{_datadir}/%{mname}/gvpr/scale
%{_datadir}/%{mname}/gvpr/scalexy
%{_datadir}/%{mname}/gvpr/span
%{_datadir}/%{mname}/gvpr/topon
%{_datadir}/%{mname}/gvpr/treetoclust
%{_datadir}/%{mname}/gvpr/chkclusters
%{_datadir}/%{mname}/gvpr/cycle
%{_datadir}/%{mname}/gvpr/addedges
%{_datadir}/%{mname}/gvpr/binduce
%{_datadir}/%{mname}/gvpr/bipart
%{_datadir}/%{mname}/gvpr/chkedges
%{_datadir}/%{mname}/gvpr/histogram
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man7/*.7%{ext_man}
%exclude %{_mandir}/man1/smyrna.1%{ext_man}

%files -n %{libname}
%{_libdir}/*.so.*
%config %{_sysconfdir}/ld.so.conf.d/graphviz.conf

%files plugins-core
%dir %{_libdir}/%{name}
%ghost %{_libdir}/%{name}/%{config_file}
%{_libdir}/%{name}/*.so*

%files devel
%{_includedir}/graphviz
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3%{ext_man}
%endif

%changelog
