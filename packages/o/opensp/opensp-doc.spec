#
# spec file for package opensp-doc
#
# Copyright (c) 2025 SUSE LLC
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


Name:           opensp-doc
%define rname opensp
%define doc_package 1
BuildRequires:  gcc-c++
BuildRequires:  libtool
%if 0%{?doc_package}
BuildRequires:  xmlto
%endif
License:        MIT
Group:          Productivity/Publishing/SGML
Version:        1.5.2
Release:        0
Source:         http://sourceforge.net/projects/openjade/files/opensp/%{version}/OpenSP-%{version}.tar.gz
Patch11:        opensp-nodeids.patch
Patch12:        opensp-lfs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?doc_package}
BuildArch:      noarch
%endif
URL:            http://openjade.sourceforge.net/
%define regcat /usr/bin/sgml-register-catalog
PreReq:         %{regcat}
Summary:        The OpenJade Group's SGML and XML Parsing Tools
Provides:       OpenSP
Provides:       sp
Provides:       sp_libs
Obsoletes:      sp
Obsoletes:      sp_libs

%description
The tools in this package provide the ability to manage SGML and XML
documents.

This package contains the parser nsgmls and the related programs
sgmlnorm, spcat, spam, spent, and sgml2xml (previously known as sx).
Sgml2xml is useful as a tool for converting from SGML to XML, the
coming WWW standard.

This package is a fork from James Clark's SP suite.

%if ! 0%{?doc_package}

%package    -n opensp-devel
License:        MIT
Summary:        SGML parser tools (development package)
Group:          Productivity/Publishing/SGML
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libstdc++-devel
Provides:       OpenSP-devel
Provides:       sp-devel
Obsoletes:      sp-devel

%description -n opensp-devel
Libraries and includes to compile applications that use the SGML parser
tools (package 'opensp').



%endif
%define INSTALL install -m755 -s
%define INSTALL_DIR install -d -m755
%define INSTALL_DATA install -m644
%define sgml_dir %{_datadir}/sgml
%define sgml_dir_pkg %{sgml_dir}/%{name}
%define sgml_var_dir /var/lib/sgml
%if 0%{?doc_package}
%define MAKE_ARGS -C docsrc
%endif

%prep
%setup -q -n OpenSP-%{version}
# %%patch -P 0 -p1
# %%patch -P 1 -p1
%patch -P 11 -p1
%patch -P 12

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
autoreconf -fi
# --datadir=%{sgml_dir}/openjade
#  set XMLTO or consider --disable-doc-build
%configure \
            --disable-nls \
            --with-gnu-ld \
            --enable-http \
%if ! 0%{?doc_package}
            --disable-doc-build \
%endif
            --enable-default-catalog="CATALOG:/etc/sgml/catalog:%{sgml_dir}/CATALOG" \
            --disable-static \
            --with-pic
make %{?MAKE_ARGS}
perl -pi -e 's/sx/sgml2xml/g; s/SX/SGML2XML/g;' doc/sx.htm
perl -pi -e 's/>sx/>sgml2xml/g; s/>SX/>SGML2XML/g;' doc/{new,index}.htm
# make check

%install
%{INSTALL_DIR} $RPM_BUILD_ROOT%{_libdir}
# %{INSTALL_DIR} $RPM_BUILD_ROOT%{_includedir}/opensp
make %{?MAKE_ARGS} install DESTDIR=$RPM_BUILD_ROOT
%if ! 0%{?doc_package}
make install-man DESTDIR=$RPM_BUILD_ROOT
%endif
# Unwanted doc stuff
rm -fr $RPM_BUILD_ROOT%{_datadir}/{OpenSP,doc} \
  $RPM_BUILD_ROOT%{_prefix}/doc
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}
# pushd $RPM_BUILD_ROOT%{_includedir}
# ln -sf OpenSP opensp
# ln -sf opensp sp
# popd
%if 0%{?doc_package}
if [ -d $RPM_BUILD_ROOT%{_mandir}/man1 ]; then
  pushd $RPM_BUILD_ROOT%{_mandir}/man1
  cp osx.1 s2x.1
  cp osx.1 osgml2xml.1
  for b in o*; do
    ln -sf ${b} ${b#o}
  done
  rm -f sx*
  popd
fi
%else
pushd $RPM_BUILD_ROOT%{_bindir}
for b in os* onsgmls; do
  ln -sf ${b} ${b#o}
done
# avoid conflict with rzsz package
rm -f sx
ln -sf osx s2x
ln -sf osx sgml2xml
ln -sf osx osgml2xml
popd
%endif
# %{INSTALL_DIR} $RPM_BUILD_ROOT/etc/profile.d
# %{INSTALL_DATA} sp.sh $RPM_BUILD_ROOT/etc/profile.d
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_dir_pkg}
{
  for c in opensp-implied.dcl japan.dcl xml.dcl; do
    %{INSTALL_DATA} pubtext/$c $RPM_BUILD_ROOT%{sgml_dir_pkg}/$c
    echo "-- SGMLDECL \"%{sgml_dir_pkg}/$c\" --"
  done
} > CATALOG.opensp
sed 's|decl|dcl|' pubtext/xml.soc > $RPM_BUILD_ROOT%{sgml_dir_pkg}/xml.soc
%{INSTALL_DIR} $RPM_BUILD_ROOT%{sgml_var_dir}
%{INSTALL_DATA} CATALOG.opensp $RPM_BUILD_ROOT%{sgml_var_dir}
ln -sf ../../../%{sgml_var_dir}/CATALOG.opensp \
  $RPM_BUILD_ROOT%{sgml_dir}/CATALOG.opensp
%{INSTALL_DIR} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/
{
  echo '# Cf. %{_datadir}/doc/packages/opensp/html/charset.htm'
  echo '# SP_CHARSET_FIXED'
  echo '# SP_SYSTEM_CHARSET'
  echo '# SP_ENCODING'
  echo '# SP_BCTF'
} > opensp.sh
%{INSTALL_DATA} opensp.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/opensp.sh
sed -e 's/\(# \)/\1setenv /' opensp.sh \
  >$RPM_BUILD_ROOT%{_sysconfdir}/profile.d/opensp.csh
rm -fr html
mkdir html
cp doc/catalog doc/*htm html
%define DOCFILES COPYING README NEWS AUTHORS ABOUT-NLS
{
  echo "<html><head><title>OpenSP documentation directory</title></head>"
  echo "<body>"
  for f in %{DOCFILES}; do
    [ -f $f ] || continue
    echo "<a href=\"$f\">$f</a>"
  done
  echo "<a href=\"html/index.htm\">OpenSP</a>, official documentation (html)"
} >index.html
find . -name .cvsignore | xargs rm
%if 0%{?doc_package}
rm -rf $RPM_BUILD_ROOT/etc
rm -rf $RPM_BUILD_ROOT/usr/bin
rm -rf $RPM_BUILD_ROOT/usr/include
rm -rf $RPM_BUILD_ROOT/usr/lib
rm -rf $RPM_BUILD_ROOT/usr/share/doc
rm -rf $RPM_BUILD_ROOT/usr/share/locale
rm -rf $RPM_BUILD_ROOT/usr/share/sgml
rm -rf $RPM_BUILD_ROOT/var
find unicode -name Makefile\* -print -delete
%endif
%if ! 0%{?doc_package}

%post
/sbin/ldconfig
if [ -x %{regcat} ]; then
  %{regcat} -a %{sgml_dir}/CATALOG.opensp >/dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
if [ "$1" = "0" -a -x %{regcat} ]; then
  %{regcat} -r %{sgml_dir}/CATALOG.opensp >/dev/null 2>&1 || :
fi
%endif

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-, root, root,755)
%if 0%{?doc_package}
%doc %{DOCFILES} index.html
%doc html
%doc unicode
# pubtext comes with html-dtd
# %doc pubtext
%{_mandir}/*/*sp*
%{_mandir}/*/*s2x*
%{_mandir}/*/*sx*
%{_mandir}/*/*sgml*
%else
%config %{_sysconfdir}/profile.d/opensp.*
%{_bindir}/*nsgmls
%{_bindir}/*sgmlnorm
%{_bindir}/*spcat
%{_bindir}/*spam
%{_bindir}/*spent
%{_bindir}/osx
%{_bindir}/*s2x
%{_bindir}/*sgml2xml
%{_libdir}/lib*.so.*
%{sgml_dir_pkg}
%dir %{sgml_var_dir}
%config %{sgml_var_dir}/CATALOG.opensp
%{sgml_dir}/CATALOG.opensp
# %{_datadir}/locale/*/LC_MESSAGES/*.mo

%files -n opensp-devel
%defattr(-, root, root)
%{_includedir}/OpenSP
%{_libdir}/lib*.so
%exclude %{_libdir}/*a
%endif

%changelog
