#
# spec file for package openjade
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


%define INSTALL_DIR       install -m755 -d
%define INSTALL_DATA      install -m644
%define sgml_dir          %{_datadir}/sgml
%define sgml_dir_pkg      %{sgml_dir}/%{name}

Name:           openjade
Version:        1.3.2
Release:        0
Summary:        DSSSL Engine for SGML Documents
License:        MIT
Group:          Productivity/Publishing/SGML
URL:            https://openjade.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        jade_style-sheet.dtd
Patch1:         openjade-1.3.1-autoconf.dif
Patch2:         openjade-1.3.2-makefile.patch
Patch3:         openjade-1.3.2-shared.patch
Patch4:         gcc46_default_ctors.patch
Patch5:         openjade-1.3.2-getopts.patch
BuildRequires:  gcc-c++
BuildRequires:  opensp-devel
Requires:       opensp
Requires(post): sgml-skel
Requires(postun): sgml-skel
Provides:       jade

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

%prep
%autosetup -p1
cp %{SOURCE1} dsssl

%build
export CXXFLAGS="%{optflags} -fno-lifetime-dse"
%configure --with-pic   \
           --enable-mif  \
           --enable-http  \
           --with-gnu-ld   \
           --disable-static \
           --enable-splibdir=%{_libdir}  \
           --datadir=%{sgml_dir}/openjade \
           --enable-default-catalog="CATALOG:%{_sysconfdir}/sgml/catalog:%{sgml_dir}/CATALOG"

%make_build

%install
%{INSTALL_DIR} %{buildroot}%{_libdir}     \
               %{buildroot}%{sgml_dir_pkg} \
               %{buildroot}%{_includedir}/%{name}

%make_install install-man

ln -sf openjade %{buildroot}%{_bindir}/jade
if [ -r jade/openjade-valid-fo ]; then
  install -s jade/openjade-valid-fo %{buildroot}%{_bindir}
fi

pushd %{buildroot}%{_mandir}/man1
    ln -sf openjade.1 jade.1
popd

%{INSTALL_DATA} generic/*.h     \
                grove/Node.h     \
                style/dsssl_ns.h  \
                style/DssslApp.h   \
                style/FOTBuilder.h  \
                style/GroveManager.h \
                spgrove/GroveApp.h    \
                spgrove/GroveBuilder.h %{buildroot}%{_includedir}/%{name}

pushd dsssl
  %{INSTALL_DATA} fot.dtd    \
                  catalog     \
                  dsssl.dtd    \
                  builtins.dsl  \
                  extensions.dsl \
                  style-sheet.dtd \
                  jade_style-sheet.dtd %{buildroot}%{sgml_dir_pkg}

  sed 's:"\([^"]*\(dtd\|dsl\)\)"$:"%{sgml_dir_pkg}/\1":' catalog \
    > %{buildroot}%{sgml_dir}/CATALOG.%{name}
  ln -sf CATALOG.%{name} %{buildroot}%{sgml_dir}/CATALOG.jade_dsl
popd

%{INSTALL_DIR} %{buildroot}%{sgml_dir}/OpenJade/dtd   \
               %{buildroot}%{sgml_dir}/James_Clark/dtd \
               %{buildroot}%{sgml_dir}/ISO_IEC_10179:1996/dtd

pushd %{buildroot}%{sgml_dir}/OpenJade/dtd
  ln -sf ../../%{name}/style-sheet.dtd DSSSL_Style_Sheet
popd

pushd %{buildroot}%{sgml_dir}/James_Clark/dtd
  ln -sf ../../%{name}/jade_style-sheet.dtd DSSSL_Style_Sheet
  ln -sf ../../%{name}/fot.dtd DSSSL_Flow_Object_Tree
popd

pushd %{buildroot}%{sgml_dir}/ISO_IEC_10179:1996/dtd
  ln -sf ../../%{name}/dsssl.dtd DSSSL_Architecture
popd

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
sgml-register-catalog -a %{sgml_dir}/CATALOG.%{name} >/dev/null 2>&1 || :

%postun
/sbin/ldconfig
if [ "$1" = "0" ] && [ -x %{_bindir}/sgml-register-catalog ]; then
  sgml-register-catalog -r %{sgml_dir}/CATALOG.%{name} >/dev/null 2>&1 || :
fi

%files
%license COPYING
%doc NEWS README*
%doc index.html html
%doc dsssl develdoc testsuite
%doc japan.sgmldecl
%doc releasenotes.{html,pdf}
%{_bindir}/jade
%{_bindir}/openjade
%{_libdir}/*.so.*
%{sgml_dir}/%{name}
%{sgml_dir}/OpenJade
%{sgml_dir}/James_Clark
%{sgml_dir}/ISO_IEC_10179:1996
%{sgml_dir}/CATALOG.%{name}
%{sgml_dir}/CATALOG.jade_dsl
%{_mandir}/man1/*jade.1.gz

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.so
%exclude %{_libdir}/*a

%changelog
