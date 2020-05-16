#
# spec file for package suse-xsl-stylesheets
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           suse-xsl-stylesheets
Version:        2.0.16
Release:        0

%define reponame          suse-xsl
%define susexsl_catalog   catalog-for-%{name}.xml
%define db_xml_dir        %{_datadir}/xml/docbook
%define suse_styles_dir   %{db_xml_dir}/stylesheet

Summary:        SUSE-Branded Stylesheets for DocBook
License:        GPL-2.0 or GPL-3.0
Group:          Productivity/Publishing/XML
Url:            https://github.com/openSUSE/suse-xsl
Source0:        %{reponame}-%{version}.tar.bz2
Source2:        %{name}.rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

BuildRequires:  docbook-xsl-stylesheets >= 1.77
BuildRequires:  docbook5-xsl-stylesheets >= 1.77
BuildRequires:  fdupes
BuildRequires:  libxml2-tools
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  fontpackages-devel
BuildRequires:  trang

# docbook_4/docbook_5 are required to be able to transform DocBook documents
# that use predefined DocBook entities.
Requires:       docbook_4
Requires:       docbook_5
Requires:       docbook-xsl-stylesheets >= 1.77
Requires:       docbook5-xsl-stylesheets >= 1.77
Requires:       libxslt
Requires:       sgml-skel >= 0.7
Requires(post): sgml-skel >= 0.7
Requires(postun): sgml-skel >= 0.7


# FONTS

# Western fallback: currently necessary for building with XEP, it seems.
Requires:       ghostscript-fonts-std
# Western fallback 2: These should make the Ghostscript fonts unnecessary.
Requires:       gnu-free-fonts
# "Generic" font for use in cases where we don't want one of the gnu-free-fonts
Requires:       dejavu-fonts

# FONTS USED IN "suse" (aka "suse2005") STYLESHEETS
# Proprietary Western:
Recommends:     agfa-fonts
# Fallback for proprietary Western:
Requires:       liberation-fonts

# Japanese:
Requires:       sazanami-fonts
# Korean:
Requires:       un-fonts
# Chinese:
Requires:       wqy-microhei-fonts

# FONTS USED IN "suse2013"/"opensuse2013"/"daps2013/"suse2020" STYLESHEETS
# Western fonts:
Requires:       google-opensans-fonts
Requires:       sil-charis-fonts
# Monospace -- dejavu-fonts, already required
# Western fonts fallback -- gnu-free-fonts, already required
# Chinese simplified -- wqy-microhei-fonts, already required
# Chinese traditional:
Requires:       arphic-uming-fonts
# Japanese:
Requires:       ipa-pgothic-fonts
Requires:       ipa-pmincho-fonts
# Korean -- un-fonts, already required
# Arabic:
Requires:       arabic-amiri-fonts


%description
These are SUSE-branded XSLT 1.0 stylesheets for DocBook 4 and 5 that are be used
to create the HTML, PDF, and EPUB versions of SUSE documentation. These
stylesheets are based on the original DocBook XSLT 1.0 stylesheets.


%prep
%setup -q -n %{reponame}-%{version}


%build
%__make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir}

# create symlinks:
%fdupes -s %{buildroot}/%{_datadir}


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
%defattr(-,root,root)

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
#%dir %{suse_styles_dir}/suse2020
#%dir %{suse_styles_dir}/suse2020-ns

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
#%{suse_styles_dir}/suse2020/*
#%{suse_styles_dir}/suse2020-ns/*

# catalogs
%config %{_sysconfdir}/xml/catalog.d/%{name}.xml

# fonts
%{_ttfontsdir}/*

# documentation
%doc %{_defaultdocdir}/%{name}/*


%changelog
