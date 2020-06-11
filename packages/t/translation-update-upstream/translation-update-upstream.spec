#
# spec file for package translation-update-upstream
#
# Copyright (c) 2020 SUSE LLC
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


Name:           translation-update-upstream
Version:        20200601
Release:        0
Summary:        Tool for Translation Update from Upstream
# Ignore cracklib, as it causes build loop cracklib <-> translation-update-upstream
#!BuildIgnore: cracklib libcrack2
License:        GPL-2.0-or-later
Group:          System/Localization
Provides:       translation-update-tool
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.in
Source2:        %{name}-AUTHORS
Source3:        %{name}-COPYING
Source4:        %{name}-README
Source5:        %{name}-HOWTO
Source6:        msgheadermerge
Source7:        msgheadermerge-compose
Source8:        msgheadermerge-parse
Source9:        msgheadermerge-empty.pot
Source10:       %{name}-embedded-README
Source11:       translation-update-mandatory-%{version}.tar.bz2
Patch:          %{name}-embedded.patch
# Files below are package maintainer tools, not used for package build:
Source50:       upstream-collect.sh
Source51:       upstream-collect.conf
Source52:       upstream-collect-template.hook
Source53:       create-tlst-step1-list-all-po-projects.sh
Source54:       create-tlst-step2-create-gnome_gtp.sh
Source55:       create-tlst.conf
Source56:       translation-update-upstream-to-translation-update.sh
Source57:       translation-update-static.tar.bz2
Source58:       check-translation-completeness.sh
# Configuration files for package maintainer tools:
Source60:       upstream-gnome_gtp.tlst
Source61:       upstream-gnome_gtp.hook
Source62:       freedesktop_org.tlst
Source63:       lcn-sle.tlst
Source65:       misc.tlst
Source66:       opensuse.tlst
Source67:       static.tlst
Source69:       github.tlst
Source70:       upstream-gnome_gtp-not-on-media.tlst
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       coreutils
Requires:       gettext-tools
Requires:       grep
Requires:       intltool
Requires:       sed
BuildArch:      noarch

%description
This is a tool providing update of translations using available
upstream resources.

The tool tool is intended for use during package compilation as a first
command after unpacking of source code.

For more see README and HOWTO.

This package also includes translation update data files.

%prep

%setup -q -T -a0 -a11 -c %{name}-%{version}
cp -a %{S:1} translation-update-upstream.in
cp -a %{S:2} AUTHORS
cp -a %{S:3} COPYING
cp -a %{S:4} README
cp -a %{S:5} HOWTO
cp -a %{S:6} %{S:7} %{S:8} %{S:9} .
cp -a %{S:10} translation-update-upstream-embedded.README
sed 's:@DATADIR@:%{_datadir}:g;s:@LIBEXECDIR@:%{_prefix}/lib:g' <translation-update-upstream.in >translation-update-upstream
sed 's/@LIBEXECDIR@/\$BASE_DIR/g;s:@DATADIR@/translation-update-upstream:\$BASE_DIR/translation-update-upstream/po:g;s/translation-update-upstream\./translation-update-upstream-embedded./g' <translation-update-upstream.in >translation-update-upstream-embedded.sh
%patch
chmod +x translation-update-upstream-embedded.sh

%build
. %{_sourcedir}/upstream-collect.conf

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name} $RPM_BUILD_ROOT%{_prefix}/lib/translation-update-upstream
cp -a po po-mandatory $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
install translation-update-upstream $RPM_BUILD_ROOT%{_bindir}/
install -m0755 msgheadermerge msgheadermerge-compose msgheadermerge-parse $RPM_BUILD_ROOT%{_prefix}/lib/translation-update-upstream/
install -m0644 msgheadermerge-empty.pot $RPM_BUILD_ROOT%{_prefix}/lib/translation-update-upstream/
ln -s translation-update-upstream $RPM_BUILD_ROOT%{_bindir}/translation-update-tool
#
#
# obsolete or bad locales
#
# gnome-i18n says nds_NFE is wrong, remove until upstream clearified that
rm -fv $RPM_BUILD_ROOT%{_datadir}/%{name}/po/*/nds?NFE.po
#
# invalid locales
#
# should be @latin
rm -fv $RPM_BUILD_ROOT%{_datadir}/%{name}/po/*/*@Latn.po
# should be nb
rm -fv $RPM_BUILD_ROOT%{_datadir}/%{name}/po/*/no.po
# should be nb
rm -fv $RPM_BUILD_ROOT%{_datadir}/%{name}/po/*/no_nb.po
# should be ar
rm -fv $RPM_BUILD_ROOT%{_datadir}/%{name}/po/*/ara.po
# testing locale, should not appear in packages
rm -fv $RPM_BUILD_ROOT%{_datadir}/%{name}/po/*/en_IGID.po
# short form of these locales should be used
rm -fv $RPM_BUILD_ROOT%{_datadir}/%{name}/po/*/my_MM.po
# these are nonsenses
#rm -v $RPM_BUILD_ROOT%{_datadir}/%{name}/po/glib-networking/master.po
#rm -v $RPM_BUILD_ROOT%{_datadir}/%{name}/po/glib20/glib.glib-2-30.gu.po
#
# go through valid locales and fail in invalid ones
#
set +x
cd $RPM_BUILD_ROOT%{_datadir} ;
echo translation*/*/*.po | sed 's:.*/::;s:\.po$::' | sort -u
for LOCALE in $(set +x ; cd $RPM_BUILD_ROOT%{_datadir} ; ls -1 translation*/*/*/*.po | sed 's:.*/::;s:\.po$::' | sort -u) ; do
        if ! test -d /usr/share/locale/$LOCALE ; then
           for file in $RPM_BUILD_ROOT%{_datadir}/translation*/*/*/$LOCALE.po; do
               # fake it so it looks like removed from %%find_lang
               package=$(echo $file | sed -e 's,.*translation[^/]*/po/,,; s,/[^/]*.po,,')
               echo -n "removing translation /usr/share/locale/$LOCALE/LC_MESSAGES/$package.mo: "
               msgfmt -o - $file | msgunfmt -o - -| msgfmt --statistics -o /dev/null -
           done
        fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS COPYING README HOWTO
%{_bindir}/*
%{_datadir}/%{name}
%{_prefix}/lib/translation-update-upstream

%changelog
