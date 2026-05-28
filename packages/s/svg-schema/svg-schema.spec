#
# spec file for package svg-schema
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


%define UNZIP          TZ=UTC unzip -a -u -qq
%define INSTALL_DIR    install -m755 -d
%define INSTALL_DATA   install -m644 -p
%define svg_dir        %{_datadir}/xml/svg
%define dtd_dir        %{svg_dir}/schema/dtd
%define rng_dir        %{svg_dir}/schema/rng
%define sgml_dir       %{_datadir}/sgml
%define xmlcatalog_dir %{_sysconfdir}/xml/catalog.d

Name:           svg-schema
Version:        20030114
Release:        0
Summary:        SVG DTD and RELAX NG Schema
License:        BSD-3-Clause
URL:            https://www.w3.org/Graphics/SVG/
Source0:        https://www.w3.org/TR/2001/REC-SVG-20010904/REC-SVG-20010904.zip
Source1:        https://www.w3.org/TR/2003/REC-SVG11-20030114/REC-SVG11-20030114.zip
Source2:        CATALOG.svg-1.0
Source3:        CATALOG.svg-1.1
Source4:        svg-1.0.xml
Source5:        svg-1.1.xml
Source10:       https://www.w3.org/Graphics/SVG/1.1/rng/rng.zip
BuildRequires:  /usr/bin/xmlcatalog
BuildRequires:  fdupes
BuildRequires:  sgml-skel >= 0.7
BuildRequires:  unzip
Requires:       sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Provides:       svg-dtd = %{version}
BuildArch:      noarch

%description
Contains the following DTDs:

* "Scalable Vector Graphics" (SVG) 1.0 Specification, W3C
  Recommendation 04 September 2001.

* "Scalable Vector Graphics" (SVG) 1.1 Specification, W3C
  Recommendation 14 January 2003.

%package doc
Summary:        Documentation of SVG Schemas
Group:          Productivity/Graphics/Other

%description doc
SVG DTD and RELAX NG Schema Documentation in HTML

%prep
%autosetup -c -T
%{UNZIP} %{SOURCE1}
%{UNZIP} %{SOURCE0}  -d REC-SVG-20010904
%{UNZIP} %{SOURCE10} -d rng
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .
find -type d | xargs chmod 755
find -type f | xargs chmod 644

%build
# nop

%install
%{INSTALL_DIR} %{buildroot}%{sgml_dir}       \
               %{buildroot}%{xmlcatalog_dir}  \
               %{buildroot}%{rng_dir}/1.1      \
               %{buildroot}%{dtd_dir}/{1.0,1.1} \
               %{buildroot}%{_docdir}/%{name}/{1.0,1.1}

%{INSTALL_DATA} rng/*             %{buildroot}%{rng_dir}/1.1/
%{INSTALL_DATA} CATALOG.*         %{buildroot}%{sgml_dir}/
%{INSTALL_DATA} svg-{1.0,1.1}.xml %{buildroot}%{xmlcatalog_dir}/

pushd REC-SVG11-20030114
 cp -a * %{buildroot}%{_docdir}/%{name}/1.1
 rm -fr %{buildroot}%{_docdir}/%{name}/1.1/{DTD,zip}
 ln -sf %{dtd_dir}/1.1 %{buildroot}%{_docdir}/%{name}/1.1/DTD
 cp -a DTD/[a-su-z][!C]* %{buildroot}%{dtd_dir}/1.1
popd

pushd REC-SVG-20010904
 cp -a * %{buildroot}%{_docdir}/%{name}/1.0
 rm -fr %{buildroot}%{_docdir}/%{name}/1.0/{DTD,zip}
 ln -sf %{dtd_dir}/1.0 %{buildroot}%{_docdir}/%{name}/1.0/DTD
 cp -a DTD/[a-su-z][!C]* %{buildroot}%{dtd_dir}/1.0

 xmlcatalog --noout --create %{buildroot}%{xmlcatalog_dir}/svg11-rng.xml
 # PUBLIC "-//W3C//DTD SVG 1.1 Tiny//EN"
 # SYSTEM "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11-tiny.dtd"
 # RNG
 xmlcatalog --noout --add "uri" \
  "http://www.w3.org/Graphics/SVG/1.1/rng/svg11.rng" \
     "file://%{rng_dir}/1.1/svg11.rng" %{buildroot}%{xmlcatalog_dir}/svg11-rng.xml
popd

%{INSTALL_DIR} %{buildroot}%{_sysconfdir}/xml
%fdupes %{buildroot}%{_docdir}

%post
for c in svg-1.0 svg-1.1; do
  sgml-register-catalog -a %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
done
update-xml-catalog

%postun
if [ "$1" = "0" ] && [ -x %{_bindir}/sgml-register-catalog ]; then
  for c in svg-1.0 svg-1.1; do
    sgml-register-catalog -r %{sgml_dir}/CATALOG.$c >/dev/null 2>&1 || :
  done
fi
update-xml-catalog

%files
%{svg_dir}
%{sgml_dir}/CATALOG.*
%config %{xmlcatalog_dir}/*.xml

%files doc
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/1.0/DTD
%exclude %{_docdir}/%{name}/1.1/DTD

%changelog
