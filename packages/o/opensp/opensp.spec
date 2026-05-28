#
# spec file for package opensp
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define INSTALL_DIR  install -m755 -d
%define INSTALL_DATA install -m644 -p
%define sgml_dir     %{_datadir}/sgml
%define sgml_dir_pkg %{sgml_dir}/%{name}

Name:           opensp
Version:        1.5.2
Release:        0
Summary:        The OpenJade Group's SGML and XML Parsing Tools
License:        MIT
Group:          Productivity/Publishing/SGML
URL:            https://openjade.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/openjade/%{name}/%{version}/OpenSP-%{version}.tar.gz
Patch11:        opensp-nodeids.patch
Patch12:        opensp-lfs.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  xmlto
Requires(post): sgml-skel
Requires(postun): sgml-skel
Provides:       OpenSP
Provides:       sp
Provides:       sp_libs

%description
The tools in this package provide the ability to manage SGML and XML
documents.

This package contains the parser nsgmls and the related programs
sgmlnorm, spcat, spam, spent, and sgml2xml (previously known as sx).
Sgml2xml is useful as a tool for converting from SGML to XML, the
coming WWW standard.

This package is a fork from James Clark's SP suite.

%package doc
Summary:        Documentation for OpenSP
BuildArch:      noarch

%description doc
This package provides the documentation for OpenSP.

%package devel
Summary:        SGML parser tools (development package)
Requires:       %{name} = %{version}
Requires:       glibc-devel
Requires:       libstdc++-devel
Provides:       OpenSP-devel
Provides:       sp-devel

%description devel
Libraries and includes to compile applications that use the SGML parser
tools (package 'opensp').

%prep
%autosetup -p1 -n OpenSP-%{version}

%build
autoreconf -fi
%configure --disable-nls \
           --with-gnu-ld \
           --enable-http \
           --enable-default-catalog="CATALOG:/etc/sgml/catalog:%{sgml_dir}/CATALOG" \
           --disable-static \
           --with-pic
%make_build
perl -pi -e 's/sx/sgml2xml/g; s/SX/SGML2XML/g;' doc/sx.htm
perl -pi -e 's/>sx/>sgml2xml/g; s/>SX/>SGML2XML/g;' doc/{new,index}.htm

%install
%make_install

# Remove unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/{OpenSP,doc} %{buildroot}%{_prefix}/doc

pushd %{buildroot}%{_mandir}/man1
  ln -sf osx.1 s2x.1
  ln -sf osx.1 osgml2xml.1
  for b in o*; do
    ln -sf ${b} ${b#o}
  done
  rm -f sx*
popd

pushd %{buildroot}%{_bindir}
  for b in os* onsgmls; do
    ln -sf ${b} ${b#o}
  done

  # avoid conflict with rzsz package
  rm -f sx

  ln -sf osx s2x
  ln -sf osx sgml2xml
  ln -sf osx osgml2xml
popd

%{INSTALL_DIR} %{buildroot}%{sgml_dir_pkg}
{
  for c in opensp-implied.dcl japan.dcl xml.dcl; do
    %{INSTALL_DATA} pubtext/$c %{buildroot}%{sgml_dir_pkg}/$c
    echo "-- SGMLDECL \"%{sgml_dir_pkg}/$c\" --"
  done
} > CATALOG.opensp
%{INSTALL_DATA} CATALOG.opensp %{buildroot}%{sgml_dir}/

sed 's|decl|dcl|' pubtext/xml.soc > %{buildroot}%{sgml_dir_pkg}/xml.soc

%{INSTALL_DIR} %{buildroot}%{_sysconfdir}/profile.d/
{
  echo '# Cf. %{_docdir}/%{name}-doc/html/charset.htm'
  echo '# SP_CHARSET_FIXED'
  echo '# SP_SYSTEM_CHARSET'
  echo '# SP_ENCODING'
  echo '# SP_BCTF'
} > opensp.sh
%{INSTALL_DATA} opensp.sh %{buildroot}%{_sysconfdir}/profile.d/opensp.sh
sed -e 's/\(# \)/\1setenv /' opensp.sh > %{buildroot}%{_sysconfdir}/profile.d/opensp.csh

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
find unicode -name Makefile\* -print -delete

%post
/sbin/ldconfig
sgml-register-catalog -a %{sgml_dir}/CATALOG.opensp >/dev/null 2>&1 || :

%postun
/sbin/ldconfig
if [ "$1" = "0" ] && [ -x %{_bindir}/sgml-register-catalog ]; then
  sgml-register-catalog -r %{sgml_dir}/CATALOG.opensp >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root,755)
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
%{sgml_dir}/CATALOG.opensp

%files doc
%doc %{DOCFILES}
%doc index.html
%doc html
%doc unicode
%{_mandir}/*/*sp*
%{_mandir}/*/*s2x*
%{_mandir}/*/*sx*
%{_mandir}/*/*sgml*

%files devel
%defattr(-, root, root)
%{_includedir}/OpenSP
%{_libdir}/lib*.so
%exclude %{_libdir}/*a

%changelog
