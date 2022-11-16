#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" != ""
%define psuffix -%{flavor}
%else
%define psuffix %{nil}
%endif

#fixes build failure caused by new .debug files, not sure how to fix correctly

%define mname graphviz
# name of the plugin config file that dot creates
%define config_file config6
# Java and ocaml are not in ring1, thus this gets overriden in staging
# Also, both install into generic locations instead of a language
# specific prefix, disable both
%bcond_with    java
%bcond_with    ocaml
%if "%{flavor}" == "addons"
# PHP7 requires swig >= 3.0.11, not available on Leap 42.x
# PHP8 requires swig >= 4.1.0, https://github.com/swig/swig/commit/56d74355735f3661406d69d04d89d1bdb4ca96f9
%if 0%{?suse_version} >= 1599
%define php_version 8
%elif 0%{?suse_version} >= 1500
%define php_version 7
%else
%define php_version 5
%endif
%define phpconf_dir %{_sysconfdir}/php%{php_version}/conf.d
%define phpext_dir  %(%{__php_config} --extension-dir)

%define ruby_version $(pkg-config --variable=RUBY_API_VERSION %{_libdir}/pkgconfig/ruby-*.pc)
%endif

# No pkgconfig(gts) in sle12 GA or SPx, but in sle15
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%bcond_with    gts
%else
%bcond_without gts
%endif

%define cdt_soversion 5
%define cgraph_soversion 6
%define gvc_soversion 6
%define gvpr_soversion 2
%define lab_gamut_soversion 1
%define pathplan_soversion 4
%define xdot_soversion 4

Name:           graphviz%{psuffix}
Version:        2.49.3
Release:        0
Summary:        Graph Visualization Tools
License:        EPL-1.0
Group:          Productivity/Graphics/Visualization/Graph
URL:            https://www.graphviz.org/
Source0:        https://gitlab.com/graphviz/graphviz/-/archive/%version/graphviz-%{version}.tar.bz2
Source1:        graphviz-rpmlintrc
#PATCH-FIX-UPSTREAM add flags to also link against libGLU and libGL
Patch0:         graphviz-smyrna-link_against_glu.patch
Patch1:         graphviz-fix-pkgIndex.patch
#PATCH-FIX-UPSTREAM Off-by-one bug
Patch2:         graphviz-array_overflow.patch
Patch3:         graphviz-2.20.2-interpreter_names.patch
#PATCH-FIX-UPSTREAM Don't warn about harmless issues with swig generated code
Patch4:         graphviz-useless_warnings.patch
Patch5:         graphviz-no_strict_aliasing.patch
Patch6:         graphviz-no_php_extra_libs.patch
# https://gitlab.com/graphviz/graphviz/-/issues/2303
Patch7:         swig-4.1.0.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  groff
BuildRequires:  guile-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
%if %{with gts}
BuildRequires:  pkgconfig(gts)
%endif
BuildRequires:  pkgconfig(zlib)
Requires:       graphviz-plugins-core = %{version}
Recommends:     graphviz-gd = %{version}
%if "%{flavor}" == "addons"
BuildRequires:  freeglut-devel
BuildRequires:  ghostscript
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libwebp-devel
BuildRequires:  perl
%if %{php_version} == 8
BuildRequires:  php8-devel
BuildRequires:  swig >= 4.1.0
%elif %{php_version} == 7
BuildRequires:  php7-devel
BuildRequires:  swig >= 3.0.11
%else
BuildRequires:  php5-devel
BuildRequires:  swig
%endif
BuildRequires:  ruby-devel
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
BuildRequires:  pkgconfig(python3)
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
%else
BuildRequires:  ghostscript_any
%endif
%if "%{flavor}" == "qt5"
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
%endif

%description
A collection of tools and tcl packages for the manipulation and layout
of graphs (as in nodes and edges, not as in bar charts).

%if "%{flavor}" == "qt5"
%package -n graphviz-gvedit
Summary:        Graph editor based on Qt
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz

%description -n graphviz-gvedit
The Qt5 graph editor included with graphviz.
%endif

%package -n graphviz-smyrna
Summary:        Large graph viewer
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz

%description -n graphviz-smyrna
Experimental large graph viewer using graphviz

%package -n graphviz-gnome
Summary:        Graphviz plugins that use gtk/GNOME
Group:          Productivity/Graphics/Visualization/Graph
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
The lefty/dotty/lneato X11 graph editors included with graphviz.

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
Requires:       php(api) = %{php_core_api}
Requires:       php(zend-abi) = %{php_zend_api}

%description -n graphviz-php
The graphviz-php package contains the PHP extension for the graphviz
tools.

%package -n python3-gv
Summary:        Python 3 Extension for Graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}

%description -n python3-gv
The package contains the Python extension for the
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

%package -n graphviz-webp
Summary:        WebP support for graphviz
Group:          Productivity/Graphics/Visualization/Graph
Requires:       graphviz = %{version}
# depends on cairo in libgvplugin_pango
Requires:       graphviz-gnome = %{version}
Requires(post): graphviz >= %{version}

%description -n graphviz-webp
The graphviz-webp package contains files needed for the support of WebP images

%package -n graphviz-doc
Summary:        Documentation for graphviz
Group:          Documentation/Howto

%description -n graphviz-doc
Provides some additional PDF and HTML documentation for graphviz.

%package -n libcdt%{cdt_soversion}
Summary:        Container data types for Graphviz
Group:          System/Libraries

%description -n libcdt%{cdt_soversion}
Library providing container data types for Graphviz.

%package -n libcgraph%{cgraph_soversion}
Summary:        Library for graph programming
Group:          System/Libraries

%description -n libcgraph%{cgraph_soversion}
Libcgraph supports graph programming by maintaining graphs in memory and
reading and writing graph files. Graphs are composed of nodes, edges, and
nested subgraphs. These graph objects may be attributed with string
name-value pairs and programmer-defined records.

%package -n libgvc%{gvc_soversion}
Summary:        Graphviz context library
Group:          System/Libraries
Provides:       libgraphviz6:%{_libdir}/libgvc.so.6
Obsoletes:      libgraphviz6 < %{version}-%{release}

%description -n libgvc%{gvc_soversion}
libgvc provides a context for applications wishing to manipulate and render
graphs. It provides a command line parsing, common rendering code, and a
plugin mechanism for renderers.

%package -n libgvpr%{gvpr_soversion}
Summary:        Library for graph filtering
Group:          System/Libraries
Provides:       libgraphviz6:%{_libdir}/libgvpr.so.2
Obsoletes:      libgraphviz6 < %{version}-%{release}

%description -n libgvpr%{gvpr_soversion}
The gvpr library allows an application to perform general-purpose graph
manipulation and filtering based on an awk-like language

%package -n libpathplan%{pathplan_soversion}
Summary:        Library for finding smooth shortest paths
Group:          System/Libraries
Provides:       libgraphviz6:%{_libdir}/libpathplan.so.4
Obsoletes:      libgraphviz6 < %{version}-%{release}

%description -n libpathplan%{pathplan_soversion}
The pathplan library contains functions for finding shortest paths in polygons
in fitting bezier curves to those paths.

%package -n libxdot%{xdot_soversion}
Summary:        Library for parsing and deparsing of xdot operations
Group:          System/Libraries
Provides:       libgraphviz6:%{_libdir}/libxdot.so.4
Obsoletes:      libgraphviz6 < %{version}-%{release}

%description -n libxdot%{xdot_soversion}
The libxdot library provides support for parsing and deparsing graphical
operations specified by the xdot language.

%package -n liblab_gamut%{lab_gamut_soversion}
Summary:        Library containing a rich set of graph drawing tools
Group:          System/Libraries
Provides:       libgraphviz6:%{_libdir}/liblab_gamut.so.1
Obsoletes:      libgraphviz6 < %{version}-%{release}

%description -n liblab_gamut%{lab_gamut_soversion}
The lab_gamut library contains a rich set of graph drawing tools.

%package plugins-core
Summary:        Core plugins for graphviz
Group:          Productivity/Graphics/Visualization/Graph
# Needed for dot binary
Requires(post): %{mname}

%description plugins-core
Core plugins for graphviz:
 * libgvplugin_core
 * libgvplugin_dot_layout
 * libgvplugin_neato_layout

%package devel
Summary:        Graphviz development package
Group:          Development/Libraries/C and C++
Requires:       %{mname} = %{version}
Requires:       libcdt%{cdt_soversion} = %{version}
Requires:       libcgraph%{cgraph_soversion} = %{version}
Requires:       libgvc%{gvc_soversion} = %{version}
Requires:       libgvpr%{gvpr_soversion} = %{version}
Requires:       liblab_gamut%{lab_gamut_soversion} = %{version}
Requires:       libpathplan%{pathplan_soversion} = %{version}
Requires:       libxdot%{xdot_soversion} = %{version}

%description devel
The graphviz-devel package contains all that's necessary for developing
programs that use the graphviz libraries including man3 pages.

%prep
#autosetup breaks graphviz-addons
%setup -q -n %{mname}-%{version}
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5 -p1
%patch6
%patch7 -p1

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
./autogen.sh RUBY_VER=%{?ruby_version}
CFLAGS="%{optflags} -ffast-math -fno-strict-aliasing -fno-strict-overflow -fPIC"

%if "%{flavor}" == "addons"

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
%if "%{flavor}" == "addons"
      --with-x \
      --enable-lefty \
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

# Unversioned symlinks for plugins are pointless, and
# break shared library packaging policy
find %{buildroot}/%{_libdir}/graphviz/ -name "libgvplugin_*.so" -print -delete

mkdir -p %{buildroot}/%{_docdir}
mkdir -p %{buildroot}%{_datadir}/%{nmame}

rm -f %{buildroot}/%{_libdir}/%{mname}/pkgIndex.tcl
chmod -x %{buildroot}%{_datadir}/%{mname}/lefty/*

mkdir -p %{buildroot}%{_libdir}/graphviz
touch %{buildroot}%{_libdir}/graphviz/%{config_file}

#Correct the path to the shared library
for manfile in $(find %{buildroot} -name \*.man); do
    sed -i \
        -e 's$%{_prefix}/lib/graphviz$%{_libdir}/%{mname}$g' \
        $manfile
done

# There are no such binaries distributed by us
rm -f %{buildroot}%{_mandir}/man1/mingle.1

%if "%{flavor}" == "addons"
mkdir -p %{buildroot}/%{phpconf_dir}
cat > %{buildroot}%{phpconf_dir}/gv.ini <<EOF
; comment out next line to disable gv extension in php
extension = gv.so
EOF

# Fix doc location
cp -a %{buildroot}%{_datadir}/%{mname}/doc %{buildroot}%{_defaultdocdir}/%{mname}-doc
%fdupes %{buildroot}%{_defaultdocdir}/%{mname}-doc
%fdupes %{buildroot}%{_datadir}/graphviz/demo
%endif

%if "%{flavor}" == "addons" || "%{flavor}" == "qt5"
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
%endif
%if "%{flavor}" == "addons"
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
rm -rf %{buildroot}%{_libdir}/graphviz/python*
rm -rf %{buildroot}%{_libdir}/graphviz/ruby
%endif
%if "%{flavor}" == "" || "%{flavor}" == "qt5"
# These are part of gnome subpkg
rm -f %{buildroot}%{_libdir}/graphviz/libgvplugin_pango*
rm -f %{buildroot}%{_libdir}/graphviz/libgvplugin_xlib*
# This is part of the gd subpkg only
rm -f %{buildroot}%{_mandir}/man1/{diffimg.1*,dotty.1*,lefty.1*,lneato.1*}
rm -f %{buildroot}%{_bindir}/{dotty,lneato}
# This is part of the x11 subpkg only
rm -rf %{buildroot}%{_datadir}/graphviz/lefty
%endif
# Remove wrongly located docs
rm -rf %{buildroot}%{_datadir}/%{mname}/doc

%post plugins-core
# run "dot -c" to generate plugin config %%{_libdir}/graphviz/config
%{_bindir}/dot -c
test -s %{_libdir}/graphviz/%{config_file} || echo "%{_libdir}/graphviz/%{config_file} doesn't exist! Check installation."

%post -n libcdt%{cdt_soversion} -p /sbin/ldconfig

%postun -n libcdt%{cdt_soversion} -p /sbin/ldconfig

%post -n libcgraph%{cgraph_soversion} -p /sbin/ldconfig

%postun -n libcgraph%{cgraph_soversion} -p /sbin/ldconfig

%post -n libgvc%{gvc_soversion} -p /sbin/ldconfig

%postun -n libgvc%{gvc_soversion} -p /sbin/ldconfig

%post -n libgvpr%{gvpr_soversion} -p /sbin/ldconfig

%postun -n libgvpr%{gvpr_soversion} -p /sbin/ldconfig

%post -n libpathplan%{pathplan_soversion} -p /sbin/ldconfig

%postun -n libpathplan%{pathplan_soversion} -p /sbin/ldconfig

%post -n libxdot%{xdot_soversion} -p /sbin/ldconfig

%postun -n libxdot%{xdot_soversion} -p /sbin/ldconfig

%post -n liblab_gamut%{lab_gamut_soversion} -p /sbin/ldconfig

%postun -n liblab_gamut%{lab_gamut_soversion} -p /sbin/ldconfig

%if "%{flavor}" == "qt5"
%files -n graphviz-gvedit
%license epl-v10.txt
%{_bindir}/gvedit
%dir %{_datadir}/%{mname}/gvedit
%{_datadir}/%{mname}/gvedit/attrs.txt
%{_mandir}/man1/gvedit.1%{ext_man}
%endif

%if "%{flavor}" == "addons"
%files -n graphviz-smyrna
%license epl-v10.txt
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
if test -x %{_bindir}/dot; then rm -f %{_libdir}/graphviz/%{config_file} ; %{_bindir}/dot -c ; fi

%files -n graphviz-gnome
%{_libdir}/graphviz/libgvplugin_gs*
%{_libdir}/graphviz/libgvplugin_rsvg*
%{_libdir}/graphviz/libgvplugin_pango*
%{_libdir}/graphviz/libgvplugin_gtk*
%{_libdir}/graphviz/libgvplugin_xlib*
%{_libdir}/graphviz/libgvplugin_gdk*

%post -n graphviz-gnome
%{_bindir}/dot -c

%postun -n graphviz-gnome
if test -x %{_bindir}/dot; then rm -f %{_libdir}/graphviz/%{config_file} ; %{_bindir}/dot -c ; fi

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
%license epl-v10.txt
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
%{phpext_dir}/gv.so
%{_datadir}/php%{php_version}/gv.php
%{_mandir}/man3/gv.3php%{ext_man}
%config(noreplace) %{phpconf_dir}/gv.ini

%files -n python3-gv
%{python3_sitearch}/_gv.so
%{python3_sitearch}/gv.py
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

%post -n graphviz-tcl -p /sbin/ldconfig
%postun -n graphviz-tcl -p /sbin/ldconfig

%files -n graphviz-webp
%{_libdir}/graphviz/libgvplugin_webp.so*

%post -n graphviz-webp
%{_bindir}/dot -c

%postun -n graphviz-webp
if test -x %{_bindir}/dot; then %{_bindir}/dot -c ; fi

%files -n graphviz-doc
%docdir %{_defaultdocdir}/%{mname}-doc
%{_defaultdocdir}/%{mname}-doc
%{_datadir}/graphviz/demo

%endif

%if "%{flavor}" == ""
%files
%doc doc/FAQ.html AUTHORS README NEWS ChangeLog
%license epl-v10.txt
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

%files -n libcdt%{cdt_soversion}
%{_libdir}/libcdt.so.%{cdt_soversion}*

%files -n libcgraph%{cgraph_soversion}
%{_libdir}/libcgraph.so.%{cgraph_soversion}*

%files -n libgvc%{gvc_soversion}
%{_libdir}/libgvc.so.%{gvc_soversion}*

%files -n libgvpr%{gvpr_soversion}
%{_libdir}/libgvpr.so.%{gvpr_soversion}*

%files -n libpathplan%{pathplan_soversion}
%{_libdir}/libpathplan.so.%{pathplan_soversion}*

%files -n libxdot%{xdot_soversion}
%{_libdir}/libxdot.so.%{xdot_soversion}*

%files -n liblab_gamut%{lab_gamut_soversion}
%{_libdir}/liblab_gamut.so.%{lab_gamut_soversion}*

%files plugins-core
%dir %{_libdir}/%{name}
%ghost %{_libdir}/%{name}/%{config_file}
%{_libdir}/%{name}/*.so*

%files devel
%{_includedir}/graphviz
%{_libdir}/libcdt.so
%{_libdir}/libcgraph.so
%{_libdir}/libgvc.so
%{_libdir}/libgvpr.so
%{_libdir}/liblab_gamut.so
%{_libdir}/libpathplan.so
%{_libdir}/libxdot.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3%{ext_man}
%endif

%changelog
