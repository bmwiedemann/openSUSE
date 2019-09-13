#
# spec file for package docbook-xsl
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


%define realversion            %{version}
#
%define db4rootdir             %{_datadir}/xml/docbook/stylesheet/nwalsh
%define db4package             docbook-xsl-stylesheets
%define db4style_catalog       %{db4package}.xml
#
%define db5rootdir             %{_datadir}/xml/docbook/stylesheet/nwalsh5
%define db5package             docbook5-xsl-stylesheets
%define db5style_catalog       %{db5package}.xml
#
%define etcxmlcatalogd         %{_sysconfdir}/xml/catalog.d
#
Name:           docbook-xsl
Version:        1.79.2
Release:        0
Summary:        XSL Stylesheets for DocBook
License:        MPL-1.1 AND MIT
Group:          Productivity/Publishing/DocBook
Url:            https://github.com/docbook/xslt10-stylesheets
Source0:        https://github.com/docbook/xslt10-stylesheets/releases/download/release%%2F%{version}/docbook-xsl-%{version}.tar.bz2
Source1:        https://github.com/docbook/xslt10-stylesheets/releases/download/release%%2F%{version}/docbook-xsl-doc-%{version}.tar.bz2
Source2:        %{db4style_catalog}
Source3:        %{db5style_catalog}
# Build scripts
Source10:       dbxslt-install.sh
Source11:       xslnons-build
## PATCH-FIX-OPENSUSE docbook-xsl-stylesheets-dbtoepub.patch Fixed dirname
Patch0:         %{name}-dbtoepub.patch
## PATCH-FIX-OPENSUSE docbook-xsl-stylesheets-non-recursive_string_subst.patch Use EXSLT replace function to avoid recursive implementation of string.subst
Patch1:         %{name}-non-recursive_string_subst.patch
BuildRequires:  fdupes
BuildRequires:  sgml-skel >= 0.7
BuildRequires:  unzip
Requires:       docbook_4
Requires:       sgml-skel >= 0.7
Requires:       xmlcharent
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Requires(pre):  %{_bindir}/xmlcatalog
BuildArch:      noarch
#--------------------------------------------------------------------------

%description
%{summary}.

Wrapper package for DocBook 4 and 5 stylesheets.

%package        -n %{db4package}
Summary:        XSL Stylesheets for DocBook 4
Group:          Productivity/Publishing/XML
Requires:       docbook_4
Requires:       sgml-skel >= 0.7
Requires:       xmlcharent
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Suggests:       rubygem(dbtoepub)

%description   -n %{db4package}
These are the XSL stylesheets for DocBook XML and "Simplified" DocBook
DTDs. Use these stylesheets for documents based on DocBook 4 and
earlier; they are not aware of the namespace feature.

The stylesheets transform DocBook 4 documents into HTML, XHTML, Manpages,
XSL-FO (for PDF), and a few other formats.

XSL is a standard W3C stylesheet language for both print and online
rendering. For more information about XSL, see the XSL page at the W3C:
http://www.w3.org/Style/XSL/

%package        -n docbook5-xsl-stylesheets
Summary:        XSL Stylesheets for DocBook 5
Group:          Productivity/Publishing/XML
Requires:       docbook_5
Requires:       sgml-skel >= 0.7
Requires:       xmlcharent
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
Suggests:       rubygem(dbtoepub)

%description   -n docbook5-xsl-stylesheets
These are the XSL stylesheets for DocBook 5 XML and "Simplified" DocBook 5.
Use these stylesheets for documents based on DocBook 5; they are aware
of the namespace feature.

The stylesheets transform DocBook 5 documents into HTML, XHTML, Manpages,
XSL-FO (for PDF), and a few other formats.

XSL is a standard W3C stylesheet language for both print and online
rendering. For more information about XSL, see the XSL page at the W3C:
http://www.w3.org/Style/XSL/

%package        pdf2index
# License:       MPL-1.1 and MIT
Summary:        Script to create Indices for FOP
Group:          Productivity/Publishing/XML
Requires:       ImageMagick
Requires:       perl

%description   pdf2index

Contains the script pdf2index which creates indices for FOP.

%prep
# %%setup -q -n docbook-xsl-%%{realversion} -b1
%setup -q -c -T -n docbook-xsl

# Prepare directories:
mkdir docbook-xsl-%{realversion}-ns docbook-xsl-%{realversion}-nons

# Copy all source files and make scripts executable:
cp %{SOURCE2} %{SOURCE3} %{SOURCE10} %{SOURCE11} .
chmod +x $(basename %{SOURCE10}) $(basename %{SOURCE11})

# Replace version in XML catalog files
db4=$(basename %{SOURCE2})
db5=$(basename %{SOURCE3})
sed --in-place 's/@VERSION@/%{realversion}/g' $db4
sed --in-place 's/@VERSION@/%{realversion}/g' $db5

# Unpack stylesheet and doc sources into the correct directory:
tar xf %{SOURCE0} -C docbook-xsl-%{realversion}-ns --strip-components 1
tar xf %{SOURCE1} -C docbook-xsl-%{realversion}-ns --strip-components 1

# Patch the orginal source and remove unnecessary files:
(cd docbook-xsl-%{realversion}-ns
%patch0 -p1
%patch1 -p1

# Remove some Python and Java extensions
# Remove dbtoepub Ruby script. This has been moved to devel:languages:ruby:extensions
# see rubygem-dbtoepub
rm -rf extensions/*.py extensions/saxon65.jar extensions/xalan27.jar \
       extensions/build.xml epub/bin
)

%build
pushd docbook-xsl-%{realversion}-ns

find slides -regex ".*\.\(xml\|htc\|\|hu\|js\|svg\|css\|html\.*\|txt\|rnc\|xhtml\)" \
   -exec sed -i 's/\r//' {} \;

# Fix wrong end-of-line encoding:
sed -i 's/\r//' params/*
# Correct file and directory properties:
find -type f -exec chmod 644 {} \;
find -type d -exec chmod 755 {} \;

# Remove any .htaccess files:
find -type f -name "\.htaccess" -exec rm {} \;

popd

# Create the non-NS variant from the NS original source:
./xslnons-build docbook-xsl-%{realversion}-ns docbook-xsl-%{realversion}-nons

%install
mkdir -p %{buildroot}%{_sysconfdir}/xml/catalog.d \
         %{buildroot}%{rb_libdir}/

./dbxslt-install.sh --debug --buildroot=%{buildroot} \
            --package-version=%{realversion} \
            --package-name=%{db4package} \
            --sourcedir=docbook-xsl-%{realversion}-nons

./dbxslt-install.sh --debug --buildroot=%{buildroot} \
            --package-version=%{realversion} \
            --package-name=%{db5package} \
            --db-xsl-suffix=nwalsh5 \
            --sourcedir=docbook-xsl-%{realversion}-ns

# The directory is already available at this point:
install -m644 %{db4style_catalog} %{db5style_catalog} %{buildroot}%{etcxmlcatalogd}

%fdupes -s %{buildroot}

%post   -n %{db4package}
update-xml-catalog

%postun -n %{db4package}
update-xml-catalog

%post   -n %{db5package}
update-xml-catalog

%postun -n %{db5package}
update-xml-catalog

%files -n %{db4package}
%config %{_sysconfdir}/xml/catalog.d/%{db4style_catalog}
%doc docbook-xsl-%{realversion}-nons/BUGS docbook-xsl-%{realversion}-nons/NEWS
%doc docbook-xsl-%{realversion}-nons/README docbook-xsl-%{realversion}-nons/RELEASE-NOTES.*
%doc docbook-xsl-%{realversion}-nons/TODO
%dir %{_datadir}/xml/docbook/stylesheet
%dir %{db4rootdir}
%dir %{db4rootdir}/%{realversion}
%exclude %{db4rootdir}/%{realversion}/fo/pdf2index

%{db4rootdir}/current
%{db4rootdir}/%{realversion}/*

%files -n %{db5package}
%config %{_sysconfdir}/xml/catalog.d/%{db5style_catalog}
%doc docbook-xsl-%{realversion}-ns/BUGS docbook-xsl-%{realversion}-ns/NEWS
%doc docbook-xsl-%{realversion}-ns/README docbook-xsl-%{realversion}-ns/RELEASE-NOTES.*
%doc docbook-xsl-%{realversion}-ns/TODO
%dir %{_datadir}/xml/docbook/stylesheet
%dir %{db5rootdir}
%dir %{db5rootdir}/%{realversion}
%exclude %{db5rootdir}/%{realversion}/fo/pdf2index

%{db5rootdir}/current
%{db5rootdir}/%{realversion}/*

%files pdf2index
%attr(0755,root,root) %{_bindir}/pdf2index

%changelog
