#
# spec file for package tei-xsl-stylesheets
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define xml_dir %{_datadir}/xml
%define xml_mod_dir %{xml_dir}/tei
%define xml_mod_style_dir %{xml_mod_dir}/stylesheet
%define xml_mod_style_prod_dir %{xml_mod_style_dir}/rahtz
%define xml_mod_style_prod_ver_dir %{xml_mod_style_prod_dir}/%{version}

Name:           tei-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  unzip
Summary:        XSL stylesheets for TEI XML
Version:        7.40.1
Release:        0
License:        LGPL-2.1+
Group:          Productivity/Publishing/XML
Source0:        http://sourceforge.net/projects/tei/files/Stylesheets/tei-xsl-%{version}.zip
Url:            http://www.tei-c.org/Stylesheets/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Stylesheets to transform TEI XML documents (version p4 and p5) to HTML
or to XSL Formatting Objects (FO). You can also produce LaTeX output.

Use it with xsltproc (part of libxslt), Saxon, or any other XSLT
processor.

%prep
%setup -q -c
/bin/chmod -Rf a+rX,g-w,o-w .

%build

%install
install -d -m755 %{buildroot}%{xml_mod_style_prod_ver_dir}
cp -a xml/tei/stylesheet/* %{buildroot}%{xml_mod_style_prod_ver_dir}
pushd %{buildroot}%{xml_mod_style_prod_ver_dir}
  mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
  ln -sf %{_defaultdocdir}/%{name} doc
popd
pushd %{buildroot}%{xml_mod_style_prod_dir}
  ln -sf %{version} current
popd

%fdupes -s doc/tei-xsl
%fdupes -s xml/tei/stylesheet

%files
%defattr(644, root, root, 755)
%doc doc/tei-xsl/*
%dir %{xml_mod_dir}
%dir %{xml_mod_style_dir}
%dir %{xml_mod_style_prod_dir}
%{xml_mod_style_prod_dir}/current
%{xml_mod_style_prod_ver_dir}

%changelog