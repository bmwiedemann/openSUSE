#
# spec file for package openjade
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define regcat %{_bindir}/sgml-register-catalog
Name:           openjade
Version:        1.3.2
Release:        0
Summary:        DSSSL Engine for SGML Documents
License:        MIT
Group:          Productivity/Publishing/SGML
Url:            http://openjade.sourceforge.net/
Source:         http://switch.dl.sourceforge.net/sourceforge/openjade/openjade-1.3.2.tar.bz2
Source1:        jade_style-sheet.dtd
Source2:        %{name}-README.SUSE
Patch1:         openjade-1.3.1-autoconf.dif
Patch2:         openjade-1.3.2-makefile.patch
Patch3:         openjade-1.3.2-shared.patch
Patch4:         gcc46_default_ctors.patch
Patch5:         openjade-1.3.2-getopts.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  opensp-devel
Requires:       opensp
Requires(pre):  %{regcat}
# Conflicts: jade_dsl
Obsoletes:      jade_dsl
Provides:       jade
Provides:       jade_dsl

%description
OpenJade, the follow-up to Jade by James Clark, is an implementation of
the ISO/IEC 10179:1996 standard DSSSL (Document Style, Semantics, and
Specification Language); pronounce it "dissl"--it rhymes with whistle.

It has back-ends for SGML, RTF, MIF, TeX, and HTML.

The parser, "nsgmls," and helper tools like "sgmlnorm," "spam,"
"spent," and "sx" are now included in the separate "opensp" package.

%package devel
Summary:        DSSSL Engine (development package)
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
Libraries and includes to compile applications that use the OpenJade
framework (package 'openjade').

%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define sgml_dir %{_datadir}/sgml
%define sgml_dir_pkg %{sgml_dir}/%{name}
%define sgml_var_dir %{_localstatedir}/lib/sgml

%prep
%setup -q
# -n %%{name}-1.3.2-rc2
cp %{SOURCE1} dsssl
cp %{SOURCE2} README.SUSE
%patch1
%patch2 -p1
%patch3
%patch4
%patch5

%build
# export CXXFLAGS='-O'
%if 0%{?suse_version} > 1320
export CXXFLAGS="%{optflags} -fno-lifetime-dse"
%else
export CXXFLAGS="%{optflags}"
%endif
# export CXXFLAGS="-g -march=i486 -mcpu=i686"
# export DEFAULT_SCHEME_BUILTINS=/usr/share/sgml/openjade/builtins.dsl
# % {?suse_update_config:% {suse_update_config config}}
rm -fv aclocal.m4 missing
[ -r config/configure.in ] && mv config/configure.in .
libtoolize --force
aclocal -I config
#automake --force --copy
# libtoolize --copy --force
autoconf --force
# # not using autoconf, because we don't have Makefile.am and that is
# # the only way to pass flags to aclocal called by autoreconf
# autoreconf --force --install -I config
%configure --disable-static --with-gnu-ld --with-pic \
  --datadir=%{sgml_dir}/openjade \
  --enable-splibdir=%{_libdir} \
  --enable-http \
  --enable-mif \
  --enable-default-catalog="CATALOG:%{_sysconfdir}/sgml/catalog:%{sgml_dir}/CATALOG"
# [ -r jade/openjade.orig ] && mv jade/openjade.orig jade/openjade
make %{?_smp_mflags}
# # now start building the debug version
# mv jade/openjade jade/openjade.orig
# zcat %%{P:5} | patch -s -p 1
# make
# mv jade/openjade jade/openjade-valid-fo
# mv jade/openjade.orig jade/openjade

%install
%{INSTALL_DIR} %{buildroot}%{_libdir} \
  %{buildroot}%{sgml_dir}/%{name} \
  %{buildroot}%{_includedir}/%{name}
%make_install
ln -sf openjade %{buildroot}%{_bindir}/jade
[ -r jade/openjade-valid-fo ] && install -s jade/openjade-valid-fo %{buildroot}%{_bindir}
make install-man DESTDIR=%{buildroot}
pushd %{buildroot}%{_mandir}
# find . ! -name 'jade*' -exec rm -f {} \;
pushd man1 && ln -sf openjade.1 jade.1 && popd
popd
/sbin/ldconfig -n %{buildroot}%{_libdir}
# %%{INSTALL_DATA} include/*.* $RPM_BUILD_ROOT%%{_includedir}/%%{name}
%{INSTALL_DATA} generic/*.h %{buildroot}%{_includedir}/%{name}
%{INSTALL_DATA} grove/Node.h %{buildroot}%{_includedir}/%{name}
%{INSTALL_DATA} spgrove/GroveApp.h \
                spgrove/GroveBuilder.h %{buildroot}%{_includedir}/%{name}
%{INSTALL_DATA} style/FOTBuilder.h style/GroveManager.h \
                style/DssslApp.h style/dsssl_ns.h \
                %{buildroot}%{_includedir}/%{name}
# pushd $RPM_BUILD_ROOT%%{_mandir}/man1
# popd
# pushd $RPM_BUILD_ROOT%%{_bindir}
# popd
# %%{INSTALL_DIR} $RPM_BUILD_ROOT/etc/profile.d
# %%{INSTALL_DATA} jade_dsl.sh $RPM_BUILD_ROOT/etc/profile.d
%{INSTALL_DIR} %{buildroot}%{sgml_dir_pkg}
# comes with opensp:
# %%{INSTALL_DATA} japan.sgmldecl $RPM_BUILD_ROOT%%{sgml_dir_pkg}/japan.dcl
# %%{INSTALL_DATA} pubtext/xml.dcl $RPM_BUILD_ROOT%%{sgml_dir_pkg}/xml.dcl
# sed 's|decl|dcl|' pubtext/xml.soc > $RPM_BUILD_ROOT%%{sgml_dir_pkg}/xml.soc
pushd dsssl
%{INSTALL_DATA} catalog dsssl.dtd extensions.dsl fot.dtd style-sheet.dtd \
  builtins.dsl jade_style-sheet.dtd %{buildroot}%{sgml_dir_pkg}
%{INSTALL_DIR} %{buildroot}%{sgml_var_dir}
sed 's:"\([^"]*\(dtd\|dsl\)\)"$:"%{sgml_dir_pkg}/\1":' catalog \
  > %{buildroot}%{sgml_var_dir}/CATALOG.%{name}
ln -sf CATALOG.%{name} %{buildroot}%{sgml_var_dir}/CATALOG.jade_dsl
cd %{buildroot}%{sgml_dir} \
  && ln -sf ../../..%{sgml_var_dir}/CATALOG.%{name} CATALOG.%{name} \
  && ln -sf ../../..%{sgml_var_dir}/CATALOG.%{name} CATALOG.jade_dsl
popd
%{INSTALL_DIR} %{buildroot}%{sgml_dir}/James_Clark/dtd
%{INSTALL_DIR} %{buildroot}%{sgml_dir}/OpenJade/dtd
%{INSTALL_DIR} %{buildroot}%{sgml_dir}/ISO_IEC_10179:1996/dtd
(cd %{buildroot}%{sgml_dir}/James_Clark/dtd \
   && ln -sf ../../$RPM_PACKAGE_NAME/jade_style-sheet.dtd DSSSL_Style_Sheet \
   && ln -sf ../../$RPM_PACKAGE_NAME/fot.dtd DSSSL_Flow_Object_Tree)
(cd %{buildroot}%{sgml_dir}/OpenJade/dtd \
   && ln -sf ../../$RPM_PACKAGE_NAME/style-sheet.dtd DSSSL_Style_Sheet)
(cd %{buildroot}%{sgml_dir}/ISO_IEC_10179:1996/dtd \
   && ln -sf ../../$RPM_PACKAGE_NAME/dsssl.dtd DSSSL_Architecture)
# for compatibility with SL <= 8.1
pushd %{buildroot}%{sgml_dir}
  pushd %{name}
  ln -s ../opensp/japan.dcl .
  ln -s ../opensp/opensp-implied.dcl sp_implied.dcl
  ln -s ../opensp/xml.dcl .
  ln -s ../opensp/xml.soc .
  for d in *.dcl; do
    ln -sf $d ${d/.dcl/.decl}
  done
  popd
popd
rm -fr html
cp -a jadedoc html
echo "\
<a href=\"README.SUSE\">README.SUSE</a>
<a href=\"html/index.htm\">OpenJade documentation</a> (html)" > index.html
grep -r include %{buildroot}%{_includedir}

%post
/sbin/ldconfig
if [ -x %{regcat} ]; then
  %{regcat} -a %{sgml_dir}/CATALOG.%{name} >/dev/null 2>&1
fi
exit 0

%postun
/sbin/ldconfig
if [ "$1" = "0" -a -x %{regcat} ]; then
  %{regcat} -r %{sgml_dir}/CATALOG.%{name} >/dev/null 2>&1
fi
exit 0

%files
%doc COPYING NEWS README*
%doc index.html html
%doc dsssl develdoc testsuite
%doc japan.sgmldecl
%doc releasenotes.{html,pdf}
%{sgml_dir}/openjade
%{_bindir}/*jade*
# %%{_mandir}/*/*jade*
%{_mandir}/*/*
# %%config /etc/profile.d/jade_dsl.sh
%{sgml_dir}/CATALOG.%{name}
%config %{sgml_var_dir}/CATALOG.%{name}
#for compatibility <= 8.1
%{sgml_dir}/CATALOG.jade_dsl
%{sgml_var_dir}/CATALOG.jade_dsl
%{sgml_dir}/ISO_IEC_10179:1996
%{sgml_dir}/James_Clark
%{sgml_dir}/OpenJade
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%exclude %{_libdir}/*a

%changelog
