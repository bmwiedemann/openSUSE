#
# spec file for package svg-schema
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define regcat %{_bindir}/sgml-register-catalog
%define all_cat svg-1.0 svg-1.1
#
%define sgml_dir %{_datadir}/sgml
%define sgml_var_dir %{_localstatedir}/lib/sgml
#
%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/svg
%define xml_mod_dtd_dir %{xml_mod_dir}/schema/dtd
%define xml_mod_rng_dir %{xml_mod_dir}/schema/rng
%define xml_mod_custom_dir %{xml_mod_dir}/custom
%define xml_mod_style_dir %{xml_mod_dir}/stylesheet
%define xml_mod_style_prod_dir %{xml_mod_style_dir}
%define xml_sysconf_dir %{_sysconfdir}/xml
#
Name:           svg-schema
Version:        20030114
Release:        0
Summary:        SVG DTD and RELAX NG Schema
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            http://www.w3.org/Graphics/SVG/
Source0:        http://www.w3.org/TR/2001/REC-SVG-20010904/REC-SVG-20010904.zip
Source1:        http://www.w3.org/TR/SVG11/REC-SVG11-20030114.zip
Source2:        CATALOG.svg-1.0
Source3:        CATALOG.svg-1.1
Source4:        svg-1.0.xml
Source5:        svg-1.1.xml
Source10:       http://www.w3.org/Graphics/SVG/1.1/rng/rng.zip
BuildRequires:  fdupes
BuildRequires:  sgml-skel >= 0.7
BuildRequires:  unzip
Requires:       sgml-skel >= 0.7
Requires(post): libxml2-tools
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Provides:       svg-dtd = %{version}
BuildArch:      noarch

%description
Contains the following DTDs:

* "Scalable Vector Graphics" (SVG) 1.0 Specification, W3C
   Recommendation 04 September 2001.

* "Scalable Vector Graphics" (SVG) 1.1 Specification, W3C
Recommendation 14 January 2003

%package doc
Summary:        Documentation of SVG Schemas
Group:          Productivity/Graphics/Other

%description doc
SVG DTD and RELAX NG Schema Documentation in HTML

%prep
%setup -q -c -T
unzip -q -a %{SOURCE1}
unzip -q -a %{SOURCE0} -d svg-dtd-20010904
unzip -q -a %{SOURCE10} -d rng11

cp %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .
find -type d | xargs chmod 755
find -type f | xargs chmod 644

%build
# nop

%install
# Catalogs:
install -d -m755 %{buildroot}%{xml_sysconf_dir}/catalog.d
#RNG
install -d -m755 %{buildroot}%{xml_mod_rng_dir}/1.1
cp rng11/* %{buildroot}%{xml_mod_rng_dir}/1.1
#DTD
install -d -m755 %{buildroot}%{xml_mod_dtd_dir}/1.{0,1} \
  %{buildroot}%{sgml_var_dir} %{buildroot}%{sgml_dir} \
  %{buildroot}%{_docdir}/%{name}/{1.0,1.1}
# Data:
install -m644 CATALOG.* %{buildroot}%{sgml_var_dir}
install -m644 svg-1.[01].xml %{buildroot}%{xml_sysconf_dir}/catalog.d/

pushd REC-SVG11-20030114
 cp -a * %{buildroot}%{_docdir}/%{name}/1.1
 rm -fr %{buildroot}%{_docdir}/%{name}/1.1/{DTD,zip}
 ln -sf %{xml_mod_dtd_dir}/1.1 %{buildroot}%{_docdir}/%{name}/1.1/DTD
 cp -a DTD/[a-su-z][!C]* %{buildroot}%{xml_mod_dtd_dir}/1.1
#
popd
pushd svg-dtd-20010904
 cp -a * %{buildroot}%{_docdir}/%{name}/1.0
 rm -fr %{buildroot}%{_docdir}/%{name}/1.0/{DTD,zip}
 ln -sf %{xml_mod_dtd_dir}/1.0 %{buildroot}%{_docdir}/%{name}/1.0/DTD
 cp -a DTD/[a-su-z][!C]* %{buildroot}%{xml_mod_dtd_dir}/1.0
 pushd %{buildroot}%{sgml_dir}
    for c in ../../..%{_localstatedir}/lib/sgml/CATALOG.*; do
      ln -sf $c .
    done
 popd

 xmlcatalog --noout --create %{buildroot}%{xml_sysconf_dir}/catalog.d/svg11-rng.xml
 # PUBLIC "-//W3C//DTD SVG 1.1 Tiny//EN"
 # SYSTEM "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11-tiny.dtd"
 # RNG
 xmlcatalog --noout --add "uri" \
  "http://www.w3.org/Graphics/SVG/1.1/rng/svg11.rng" \
     "file://%{xml_mod_rng_dir}/1.1/svg11.rng" %{buildroot}%{xml_sysconf_dir}/catalog.d/svg11-rng.xml
popd

install -d -m755 %{buildroot}%{_sysconfdir}/xml
%fdupes %{buildroot}%{_docdir}

%post
if [ -x %{regcat} ]; then
  for c in  %{all_cat}; do
    grep -q -e "%{sgml_dir}/CATALOG.$c\\>" %{_sysconfdir}/sgml/catalog \
      || %{regcat} -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
update-xml-catalog

%postun
if [ "$1" = "0" -a -x %{regcat} ]; then
  for c in  %{all_cat}; do
    %{regcat} -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
update-xml-catalog

%files
%config %{sgml_var_dir}/CATALOG.*
%config %{_sysconfdir}/xml/catalog.d/*.xml
%{sgml_dir}/CATALOG.*
%{xml_mod_dir}

%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/1.0/DTD
%exclude %{_docdir}/%{name}/1.1/DTD

%changelog
