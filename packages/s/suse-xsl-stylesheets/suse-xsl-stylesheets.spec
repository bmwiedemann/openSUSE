#
# spec file for package suse-xsl-stylesheets
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


%define reponame          suse-xsl
%define susexsl_catalog   catalog-for-%{name}.xml
%define db_xml_dir        %{_datadir}/xml/docbook
%define suse_styles_dir   %{db_xml_dir}/stylesheet
#
Name:           suse-xsl-stylesheets
Version:        2.87.1
Release:        0
Summary:        SUSE-Branded Stylesheets for DocBook
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Publishing/XML
URL:            https://github.com/openSUSE/suse-xsl
Source0:        %{reponame}-%{version}.tar.bz2
Source2:        %{name}.rpmlintrc
#
BuildRequires:  docbook-xsl-stylesheets >= 1.77
BuildRequires:  docbook5-xsl-stylesheets >= 1.77
BuildRequires:  fdupes
BuildRequires:  fontpackages-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  make
BuildRequires:  trang
# DocBook schemas and stylesheets are required to be able to transform
# DocBook documents.
# DocBook4 is needed when documents use predefined DocBook entities.
Requires:       docbook_4
Requires:       docbook_5
Requires:       docbook-xsl-stylesheets >= 1.77
Requires:       docbook5-xsl-stylesheets >= 1.77
#
Requires:       libxslt-tools
Requires:       sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7
#
#
# FONTS
# "Default" fonts for suse2022 stylesheets
Requires:       dejavu-fonts
Requires:       google-opensans-fonts
Requires:       google-poppins-fonts
Requires:       sil-charis-fonts
#
# Western fallback: currently necessary for building with XEP, it seems.
Requires:       ghostscript-fonts-std
#
# Western fallback 2: These should make the Ghostscript fonts unnecessary.
Requires:       gnu-free-fonts
#
# Arabic:
Requires:       arabic-amiri-fonts
#
# Japanese (regular/bold):
Requires:       google-noto-sans-jp-bold-fonts
Requires:       google-noto-sans-jp-regular-fonts
#
# Korean (regular/bold):
Requires:       google-noto-sans-kr-bold-fonts
Requires:       google-noto-sans-kr-regular-fonts
#
# Chinese, simplified  (regular/bold):
Requires:       google-noto-sans-sc-bold-fonts
Requires:       google-noto-sans-sc-regular-fonts
#
# Chinese, traditional (regular/bold):
Requires:       google-noto-sans-tc-bold-fonts
Requires:       google-noto-sans-tc-regular-fonts
#
#
# Fonts for older stylesheets variants
# We use a very weak relationship as these fonts shouldn't be really
# used anymore (or needed, unless you need to build with older suse variants)
#
# Proprietary Western:
Suggests:       agfa-fonts
# Chinese traditional:
Suggests:       arphic-uming-fonts
# Fallback for proprietary Western:
Suggests:       liberation-fonts
# Japanese:
Suggests:       sazanami-fonts
Suggests:       ipa-pgothic-fonts
Suggests:       ipa-pmincho-fonts
# Korean:
Suggests:       un-fonts
# Chinese
Suggests:       wqy-microhei-fonts
#
BuildArch:      noarch

%description
These are SUSE-branded XSLT 1.0 stylesheets for DocBook 4 and 5 that are be used
to create the HTML, PDF, and EPUB versions of SUSE documentation. These
stylesheets are based on the original DocBook XSLT 1.0 stylesheets.

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%make_build

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir}

# create symlinks:
# (intentionally no slash between the variables -- %%{_datadir} has a leading slash already.)
%fdupes -s %{buildroot}%{_datadir}


%post
# XML Catalogs
#
# remove old existing entries first - needed for
# zypper in, since it does not call postun.

# delete ...
if [ "2" = "$1" ]; then
  edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
    --del %{name} || true
fi

# ... and (re)insert new catalogs
update-xml-catalog

%reconfigure_fonts_post
exit 0

%postun
update-xml-catalog

if [ "0" = "$1" ]; then
  %reconfigure_fonts_post

  edit-xml-catalog --group --catalog %{_sysconfdir}/xml/suse-catalog.xml \
    --del %{name} || true
fi

exit 0

%posttrans
%reconfigure_fonts_posttrans

%files

# directories
%dir %{suse_styles_dir}
%dir %{suse_styles_dir}/suse
%dir %{suse_styles_dir}/suse-ns
%dir %{suse_styles_dir}/suse2013
%dir %{suse_styles_dir}/suse2013-ns
%dir %{suse_styles_dir}/daps2013
%dir %{suse_styles_dir}/daps2013-ns
%dir %{suse_styles_dir}/opensuse2013
%dir %{suse_styles_dir}/opensuse2013-ns
%dir %{suse_styles_dir}/suse2021-ns
%dir %{suse_styles_dir}/suse2022-ns
%dir %{suse_styles_dir}/sbp

%dir %{_ttfontsdir}

%dir %{_defaultdocdir}/%{name}

# stylesheets
%{suse_styles_dir}/suse/*
%{suse_styles_dir}/suse-ns/*
%{suse_styles_dir}/suse2013/*
%{suse_styles_dir}/suse2013-ns/*
%{suse_styles_dir}/daps2013/*
%{suse_styles_dir}/daps2013-ns/*
%{suse_styles_dir}/opensuse2013/*
%{suse_styles_dir}/opensuse2013-ns/*
%{suse_styles_dir}/suse2021-ns/*
%{suse_styles_dir}/suse2022-ns/*
%{suse_styles_dir}/sbp/*

# catalogs
%config %{_sysconfdir}/xml/catalog.d/%{name}.xml

# fonts
%{_ttfontsdir}/*

# documentation
%doc %{_defaultdocdir}/%{name}/*

%changelog
