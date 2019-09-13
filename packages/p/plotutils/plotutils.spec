#
# spec file for package plotutils
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           plotutils
Version:        2.6
Release:        0
Summary:        GNU Plotting Utilities
License:        GPL-2.0+ and GPL-3.0+
Group:          Productivity/Graphics/Visualization/Graph
Url:            http://www.gnu.org/software/plotutils/plotutils.html
Source:         http://ftp.gnu.org/gnu/plotutils/%{name}-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/plotutils/plotutils-2.6.tar.gz.sig
Source2:        plotutils.keyring
Patch0:         plotutils-man.patch
Patch1:         plotutils-uninitialized.patch
Patch2:         plotutils-dasharray-format.patch
Patch3:         plotutils-autoreconf.patch
# libpng15.patch sent 2012-08-30 at rsm@math.arizona.edu
Patch4:         plotutils-libpng15.patch
# PATCH-FIX-UPSTREAM Arithmetic overflow in Hershey pointing hands glyphs
Patch5:         plotutils-hershey_glyphs.patch
# PATCH-FIX-UPSTREAM --no-of-intervals arugment is documented wrongly originall
Patch6:         plotutils-man-spline.patch
# PATCH-FIX-UPSTREAM repairs postscript output
Patch7:         plotutils-postscript.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  fontpackages-devel
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if %suse_version < 1220
BuildRequires:  xorg-x11-devel
%else
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xt)
%endif
Requires(pre):  %install_info_prereq
Requires(pre):  %suseconfig_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The GNU plotting utilities consist of seven command line programs: the
graphics programs `graph', `plot', `tek2plot', and `plotfont', and the
mathematical programs `spline', `ode', and `double'.  GNU `libplot' is
distributed with these programs; it is the library on which the
graphics programs are based. `Libplot' is a function library for
device-independent two-dimensional vector graphics, including vector
graphics animations under the X Window System.

%package devel
Summary:        GNU Plotting Utilities
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libplot2 = %{version}
Requires:       libplotter2 = %{version}
Requires:       libstdc++-devel
Requires:       libxmi0 = %{version}
Requires:       xorg-x11-libX11-devel

%description devel
The GNU plotting utilities consist of seven command line programs: the
graphics programs `graph', `plot', `tek2plot', and `plotfont', and the
mathematical programs `spline', `ode', and `double'.  GNU `libplot' is
distributed with these programs; it is the library on which the
graphics programs are based. `Libplot' is a function library for
device-independent two-dimensional vector graphics, including vector
graphics animations under the X Window System.

%package -n libplot2
Summary:        GNU Plotting Utilities
Group:          System/Libraries

%description -n libplot2
The GNU plotting utilities consist of seven command line programs: the
graphics programs `graph', `plot', `tek2plot', and `plotfont', and the
mathematical programs `spline', `ode', and `double'.  GNU `libplot' is
distributed with these programs; it is the library on which the
graphics programs are based. `Libplot' is a function library for
device-independent two-dimensional vector graphics, including vector
graphics animations under the X Window System.

%package -n libplotter2
Summary:        GNU Plotting Utilities
Group:          System/Libraries

%description -n libplotter2
The GNU plotting utilities consist of seven command line programs: the
graphics programs `graph', `plot', `tek2plot', and `plotfont', and the
mathematical programs `spline', `ode', and `double'.  GNU `libplot' is
distributed with these programs; it is the library on which the
graphics programs are based. `Libplot' is a function library for
device-independent two-dimensional vector graphics, including vector
graphics animations under the X Window System.

%package -n libxmi0
Summary:        GNU Plotting Utilities
Group:          System/Libraries

%description -n libxmi0
The GNU plotting utilities consist of seven command line programs: the
graphics programs `graph', `plot', `tek2plot', and `plotfont', and the
mathematical programs `spline', `ode', and `double'.  GNU `libplot' is
distributed with these programs; it is the library on which the
graphics programs are based. `Libplot' is a function library for
device-independent two-dimensional vector graphics, including vector
graphics animations under the X Window System.

%prep
%{?gpg_verify: %gpg_verify %{S:1}}
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p0
# Avoid update lex and bison code as otherwise we may see broken code (bnc#829479)
# that is do *not* remove any lex\yacc code
grep -rslE '(made by GNU Bison|A Bison parser, made from|"lex.yy.c")' . | xargs -r touch

%build
export CXXFLAGS="%optflags -fvisibility-inlines-hidden"
autoreconf -f -i
%configure --with-pic\
	--disable-static\
	--enable-libplotter\
	--enable-libxmi
# FIXME: lex/bison update break parallel build:
#make %{?jobs:-j%jobs}
make

%install
%makeinstall\
	libplotdatadir=%{_docdir}/%{name}/libplot\
	odedatadir=%{_docdir}/%{name}/ode\
	tek2plotdatadir=%{_docdir}/%{name}/tek2plot\
	pic2plotdatadir=%{_docdir}/%{name}/pic2plot
#
install -m 0644\
	AUTHORS COMPAT COPYING INSTALL.fonts KNOWN_BUGS PROBLEMS README THANKS\
	TODO %{buildroot}%{_defaultdocdir}/%{name}
#
install -d %{buildroot}%{_miscfontsdir}
install -m 0644 fonts/pcf/*.pcf %{buildroot}%{_miscfontsdir}
gzip -n -9 %{buildroot}%{_miscfontsdir}/*.pcf
#
install -m 0644 manpage.1 %{buildroot}%{_mandir}/man1/plotutils.1
ln -s plotutils.1.gz %{buildroot}%{_mandir}/man1/double.1.gz
ln -s plotutils.1.gz %{buildroot}%{_mandir}/man1/graph.1.gz
ln -s plotutils.1.gz %{buildroot}%{_mandir}/man1/pic2plot.1.gz
rm -f %{buildroot}%{_libdir}/*.la

%post
%install_info --info-dir=%{_infodir} %{_infodir}/plotutils.info.gz
%reconfigure_fonts_post

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/plotutils.info.gz
%reconfigure_fonts_postun

%posttrans
%reconfigure_fonts_posttrans

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/libxmi.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/libxmi.info.gz

%post -n libplot2 -p /sbin/ldconfig

%postun -n libplot2 -p /sbin/ldconfig

%post -n libplotter2 -p /sbin/ldconfig

%postun -n libplotter2 -p /sbin/ldconfig

%post -n libxmi0 -p /sbin/ldconfig

%postun -n libxmi0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc %{_docdir}/%{name}
%{_bindir}/*
%doc %{_infodir}/plotutils*.info*
%doc %{_mandir}/man?/*.*
%{_miscfontsdir}

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_includedir}/*.h
%doc %{_infodir}/libxmi*.info*

%files -n libplot2
%defattr(-,root,root)
%{_libdir}/libplot.so.*

%files -n libplotter2
%defattr(-,root,root)
%{_libdir}/libplotter.so.*

%files -n libxmi0
%defattr(-,root,root)
%{_libdir}/libxmi.so.*

%changelog
