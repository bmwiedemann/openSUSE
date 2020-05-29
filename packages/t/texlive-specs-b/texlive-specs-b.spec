#
# spec file for package texlive-specs-b
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


%bcond_with	zypper_posttrans

%define texlive_version  2020
%define texlive_previous 2019
%define texlive_release  20200327
%define texlive_noarch   176

#!BuildIgnore:          texlive
#!BuildIgnore:          texlive-scripts
#!BuildIgnore:          texlive-scripts-extra
#!BuildIgnore:          texlive-scripts-bin
#!BuildIgnore:          texlive-scripts-extra-bin
#!BuildIgnore:          texlive-gsftopk
#!BuildIgnore:          texlive-gsftopk-bin
#!BuildIgnore:          texlive-kpathsea
#!BuildIgnore:          texlive-kpathsea-bin

%global _varlib         %{_localstatedir}/lib
%global _libexecdir     %{_prefix}/lib

%define _texmfdistdir   %{_datadir}/texmf
%if 0%{texlive_version} >= 2013
%define _texmfmaindir   %{_texmfdistdir}
%define _texmfdirs      %{_texmfdistdir}
%else
%define _texmfmaindir   %{_libexecdir}/texmf
%define _texmfdirs      \{%{_texmfdistdir},%{_texmfmaindir}\}
%endif

%define _texmfconfdir   %{_sysconfdir}/texmf
%define _texmfvardir    %{_varlib}/texmf
%define _texmfcache     %{_localstatedir}/cache/texmf
%define _fontcache      %{_texmfcache}/fonts
#
%define _x11bin         %{_prefix}/bin
%define _x11lib         %{_libdir}
%define _x11data        %{_datadir}/X11
%define _x11inc         %{_includedir}
%define _appdefdir      %{_x11data}/app-defaults

Name:           texlive-specs-b
Version:        2020
Release:        0
BuildRequires:  ed
BuildRequires:  fontconfig
BuildRequires:  fontpackages-devel
BuildRequires:  t1utils
BuildRequires:  texlive-filesystem
BuildRequires:  xz
BuildArch:      noarch
Summary:        Meta package for b
License:        BSD-3-Clause and GPL-2.0+ and LGPL-3.0+ and LPPL-1.0 and OFL-1.1 and SUSE-Public-Domain and SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            https://build.opensuse.org/package/show/Publishing:TeXLive/Meta
Source0:        texlive-specs-b-rpmlintrc

%description
Meta package to build tons of noarch texlive packages.

%package -n texlive-around-the-bend
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Typeset exercises in TeX, with answers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source1:        around-the-bend.doc.tar.xz

%description -n texlive-around-the-bend
This is a typeset version of the files of the aro-bend, plus
three extra questions (with their answers) that Michael Downes
didn't manage to get onto CTAN.
%post -n texlive-around-the-bend
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-around-the-bend 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-around-the-bend
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-around-the-bend
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/around-the-bend/AroundTheBend.pdf
%{_texmfdistdir}/doc/generic/around-the-bend/AroundTheBend.tex
%{_texmfdistdir}/doc/generic/around-the-bend/README
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-around-the-bend-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-arphic
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Arphic (Chinese) font packages
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-arphic-fonts >= %{texlive_version}
Recommends:     texlive-arphic-doc >= %{texlive_version}
Provides:       tex(bkaimp00.tfm)
Provides:       tex(bkaimp00.vf)
Provides:       tex(bkaimp01.tfm)
Provides:       tex(bkaimp01.vf)
Provides:       tex(bkaimp02.tfm)
Provides:       tex(bkaimp02.vf)
Provides:       tex(bkaimp03.tfm)
Provides:       tex(bkaimp03.vf)
Provides:       tex(bkaimp04.tfm)
Provides:       tex(bkaimp04.vf)
Provides:       tex(bkaimp05.tfm)
Provides:       tex(bkaimp05.vf)
Provides:       tex(bkaimp06.tfm)
Provides:       tex(bkaimp06.vf)
Provides:       tex(bkaimp07.tfm)
Provides:       tex(bkaimp07.vf)
Provides:       tex(bkaimp08.tfm)
Provides:       tex(bkaimp08.vf)
Provides:       tex(bkaimp09.tfm)
Provides:       tex(bkaimp09.vf)
Provides:       tex(bkaimp10.tfm)
Provides:       tex(bkaimp10.vf)
Provides:       tex(bkaimp11.tfm)
Provides:       tex(bkaimp11.vf)
Provides:       tex(bkaimp12.tfm)
Provides:       tex(bkaimp12.vf)
Provides:       tex(bkaimp13.tfm)
Provides:       tex(bkaimp13.vf)
Provides:       tex(bkaimp14.tfm)
Provides:       tex(bkaimp14.vf)
Provides:       tex(bkaimp15.tfm)
Provides:       tex(bkaimp15.vf)
Provides:       tex(bkaimp16.tfm)
Provides:       tex(bkaimp16.vf)
Provides:       tex(bkaimp17.tfm)
Provides:       tex(bkaimp17.vf)
Provides:       tex(bkaimp18.tfm)
Provides:       tex(bkaimp18.vf)
Provides:       tex(bkaimp19.tfm)
Provides:       tex(bkaimp19.vf)
Provides:       tex(bkaimp20.tfm)
Provides:       tex(bkaimp20.vf)
Provides:       tex(bkaimp21.tfm)
Provides:       tex(bkaimp21.vf)
Provides:       tex(bkaimp22.tfm)
Provides:       tex(bkaimp22.vf)
Provides:       tex(bkaimp23.tfm)
Provides:       tex(bkaimp23.vf)
Provides:       tex(bkaimp25.tfm)
Provides:       tex(bkaimp25.vf)
Provides:       tex(bkaimp26.tfm)
Provides:       tex(bkaimp26.vf)
Provides:       tex(bkaimp27.tfm)
Provides:       tex(bkaimp27.vf)
Provides:       tex(bkaimp28.tfm)
Provides:       tex(bkaimp28.vf)
Provides:       tex(bkaimp29.tfm)
Provides:       tex(bkaimp29.vf)
Provides:       tex(bkaimp30.tfm)
Provides:       tex(bkaimp30.vf)
Provides:       tex(bkaimp31.tfm)
Provides:       tex(bkaimp31.vf)
Provides:       tex(bkaimp32.tfm)
Provides:       tex(bkaimp32.vf)
Provides:       tex(bkaimp33.tfm)
Provides:       tex(bkaimp33.vf)
Provides:       tex(bkaimp34.tfm)
Provides:       tex(bkaimp34.vf)
Provides:       tex(bkaimp35.tfm)
Provides:       tex(bkaimp35.vf)
Provides:       tex(bkaimp36.tfm)
Provides:       tex(bkaimp36.vf)
Provides:       tex(bkaimp37.tfm)
Provides:       tex(bkaimp37.vf)
Provides:       tex(bkaimp38.tfm)
Provides:       tex(bkaimp38.vf)
Provides:       tex(bkaimp39.tfm)
Provides:       tex(bkaimp39.vf)
Provides:       tex(bkaimp40.tfm)
Provides:       tex(bkaimp40.vf)
Provides:       tex(bkaimp41.tfm)
Provides:       tex(bkaimp41.vf)
Provides:       tex(bkaimp42.tfm)
Provides:       tex(bkaimp42.vf)
Provides:       tex(bkaimp43.tfm)
Provides:       tex(bkaimp43.vf)
Provides:       tex(bkaimp44.tfm)
Provides:       tex(bkaimp44.vf)
Provides:       tex(bkaimp45.tfm)
Provides:       tex(bkaimp45.vf)
Provides:       tex(bkaimp46.tfm)
Provides:       tex(bkaimp46.vf)
Provides:       tex(bkaimp47.tfm)
Provides:       tex(bkaimp47.vf)
Provides:       tex(bkaimp48.tfm)
Provides:       tex(bkaimp48.vf)
Provides:       tex(bkaimp49.tfm)
Provides:       tex(bkaimp49.vf)
Provides:       tex(bkaimp50.tfm)
Provides:       tex(bkaimp50.vf)
Provides:       tex(bkaimp51.tfm)
Provides:       tex(bkaimp51.vf)
Provides:       tex(bkaimp52.tfm)
Provides:       tex(bkaimp52.vf)
Provides:       tex(bkaimp53.tfm)
Provides:       tex(bkaimp53.vf)
Provides:       tex(bkaimp54.tfm)
Provides:       tex(bkaimp54.vf)
Provides:       tex(bkaimp55.tfm)
Provides:       tex(bkaimp55.vf)
Provides:       tex(bkaimpv.tfm)
Provides:       tex(bkaimpv.vf)
Provides:       tex(bkaiu.map)
Provides:       tex(bkaiu00.tfm)
Provides:       tex(bkaiu02.tfm)
Provides:       tex(bkaiu03.tfm)
Provides:       tex(bkaiu20.tfm)
Provides:       tex(bkaiu21.tfm)
Provides:       tex(bkaiu22.tfm)
Provides:       tex(bkaiu25.tfm)
Provides:       tex(bkaiu26.tfm)
Provides:       tex(bkaiu30.tfm)
Provides:       tex(bkaiu31.tfm)
Provides:       tex(bkaiu32.tfm)
Provides:       tex(bkaiu33.tfm)
Provides:       tex(bkaiu4e.tfm)
Provides:       tex(bkaiu4f.tfm)
Provides:       tex(bkaiu50.tfm)
Provides:       tex(bkaiu51.tfm)
Provides:       tex(bkaiu52.tfm)
Provides:       tex(bkaiu53.tfm)
Provides:       tex(bkaiu54.tfm)
Provides:       tex(bkaiu55.tfm)
Provides:       tex(bkaiu56.tfm)
Provides:       tex(bkaiu57.tfm)
Provides:       tex(bkaiu58.tfm)
Provides:       tex(bkaiu59.tfm)
Provides:       tex(bkaiu5a.tfm)
Provides:       tex(bkaiu5b.tfm)
Provides:       tex(bkaiu5c.tfm)
Provides:       tex(bkaiu5d.tfm)
Provides:       tex(bkaiu5e.tfm)
Provides:       tex(bkaiu5f.tfm)
Provides:       tex(bkaiu60.tfm)
Provides:       tex(bkaiu61.tfm)
Provides:       tex(bkaiu62.tfm)
Provides:       tex(bkaiu63.tfm)
Provides:       tex(bkaiu64.tfm)
Provides:       tex(bkaiu65.tfm)
Provides:       tex(bkaiu66.tfm)
Provides:       tex(bkaiu67.tfm)
Provides:       tex(bkaiu68.tfm)
Provides:       tex(bkaiu69.tfm)
Provides:       tex(bkaiu6a.tfm)
Provides:       tex(bkaiu6b.tfm)
Provides:       tex(bkaiu6c.tfm)
Provides:       tex(bkaiu6d.tfm)
Provides:       tex(bkaiu6e.tfm)
Provides:       tex(bkaiu6f.tfm)
Provides:       tex(bkaiu70.tfm)
Provides:       tex(bkaiu71.tfm)
Provides:       tex(bkaiu72.tfm)
Provides:       tex(bkaiu73.tfm)
Provides:       tex(bkaiu74.tfm)
Provides:       tex(bkaiu75.tfm)
Provides:       tex(bkaiu76.tfm)
Provides:       tex(bkaiu77.tfm)
Provides:       tex(bkaiu78.tfm)
Provides:       tex(bkaiu79.tfm)
Provides:       tex(bkaiu7a.tfm)
Provides:       tex(bkaiu7b.tfm)
Provides:       tex(bkaiu7c.tfm)
Provides:       tex(bkaiu7d.tfm)
Provides:       tex(bkaiu7e.tfm)
Provides:       tex(bkaiu7f.tfm)
Provides:       tex(bkaiu80.tfm)
Provides:       tex(bkaiu81.tfm)
Provides:       tex(bkaiu82.tfm)
Provides:       tex(bkaiu83.tfm)
Provides:       tex(bkaiu84.tfm)
Provides:       tex(bkaiu85.tfm)
Provides:       tex(bkaiu86.tfm)
Provides:       tex(bkaiu87.tfm)
Provides:       tex(bkaiu88.tfm)
Provides:       tex(bkaiu89.tfm)
Provides:       tex(bkaiu8a.tfm)
Provides:       tex(bkaiu8b.tfm)
Provides:       tex(bkaiu8c.tfm)
Provides:       tex(bkaiu8d.tfm)
Provides:       tex(bkaiu8e.tfm)
Provides:       tex(bkaiu8f.tfm)
Provides:       tex(bkaiu90.tfm)
Provides:       tex(bkaiu91.tfm)
Provides:       tex(bkaiu92.tfm)
Provides:       tex(bkaiu93.tfm)
Provides:       tex(bkaiu94.tfm)
Provides:       tex(bkaiu95.tfm)
Provides:       tex(bkaiu96.tfm)
Provides:       tex(bkaiu97.tfm)
Provides:       tex(bkaiu98.tfm)
Provides:       tex(bkaiu99.tfm)
Provides:       tex(bkaiu9a.tfm)
Provides:       tex(bkaiu9b.tfm)
Provides:       tex(bkaiu9c.tfm)
Provides:       tex(bkaiu9d.tfm)
Provides:       tex(bkaiu9e.tfm)
Provides:       tex(bkaiu9f.tfm)
Provides:       tex(bkaiuee.tfm)
Provides:       tex(bkaiuf6.tfm)
Provides:       tex(bkaiuf7.tfm)
Provides:       tex(bkaiuf8.tfm)
Provides:       tex(bkaiufa.tfm)
Provides:       tex(bkaiufe.tfm)
Provides:       tex(bkaiuff.tfm)
Provides:       tex(bkaiuv.tfm)
Provides:       tex(bsmilp00.tfm)
Provides:       tex(bsmilp00.vf)
Provides:       tex(bsmilp01.tfm)
Provides:       tex(bsmilp01.vf)
Provides:       tex(bsmilp02.tfm)
Provides:       tex(bsmilp02.vf)
Provides:       tex(bsmilp03.tfm)
Provides:       tex(bsmilp03.vf)
Provides:       tex(bsmilp04.tfm)
Provides:       tex(bsmilp04.vf)
Provides:       tex(bsmilp05.tfm)
Provides:       tex(bsmilp05.vf)
Provides:       tex(bsmilp06.tfm)
Provides:       tex(bsmilp06.vf)
Provides:       tex(bsmilp07.tfm)
Provides:       tex(bsmilp07.vf)
Provides:       tex(bsmilp08.tfm)
Provides:       tex(bsmilp08.vf)
Provides:       tex(bsmilp09.tfm)
Provides:       tex(bsmilp09.vf)
Provides:       tex(bsmilp10.tfm)
Provides:       tex(bsmilp10.vf)
Provides:       tex(bsmilp11.tfm)
Provides:       tex(bsmilp11.vf)
Provides:       tex(bsmilp12.tfm)
Provides:       tex(bsmilp12.vf)
Provides:       tex(bsmilp13.tfm)
Provides:       tex(bsmilp13.vf)
Provides:       tex(bsmilp14.tfm)
Provides:       tex(bsmilp14.vf)
Provides:       tex(bsmilp15.tfm)
Provides:       tex(bsmilp15.vf)
Provides:       tex(bsmilp16.tfm)
Provides:       tex(bsmilp16.vf)
Provides:       tex(bsmilp17.tfm)
Provides:       tex(bsmilp17.vf)
Provides:       tex(bsmilp18.tfm)
Provides:       tex(bsmilp18.vf)
Provides:       tex(bsmilp19.tfm)
Provides:       tex(bsmilp19.vf)
Provides:       tex(bsmilp20.tfm)
Provides:       tex(bsmilp20.vf)
Provides:       tex(bsmilp21.tfm)
Provides:       tex(bsmilp21.vf)
Provides:       tex(bsmilp22.tfm)
Provides:       tex(bsmilp22.vf)
Provides:       tex(bsmilp23.tfm)
Provides:       tex(bsmilp23.vf)
Provides:       tex(bsmilp25.tfm)
Provides:       tex(bsmilp25.vf)
Provides:       tex(bsmilp26.tfm)
Provides:       tex(bsmilp26.vf)
Provides:       tex(bsmilp27.tfm)
Provides:       tex(bsmilp27.vf)
Provides:       tex(bsmilp28.tfm)
Provides:       tex(bsmilp28.vf)
Provides:       tex(bsmilp29.tfm)
Provides:       tex(bsmilp29.vf)
Provides:       tex(bsmilp30.tfm)
Provides:       tex(bsmilp30.vf)
Provides:       tex(bsmilp31.tfm)
Provides:       tex(bsmilp31.vf)
Provides:       tex(bsmilp32.tfm)
Provides:       tex(bsmilp32.vf)
Provides:       tex(bsmilp33.tfm)
Provides:       tex(bsmilp33.vf)
Provides:       tex(bsmilp34.tfm)
Provides:       tex(bsmilp34.vf)
Provides:       tex(bsmilp35.tfm)
Provides:       tex(bsmilp35.vf)
Provides:       tex(bsmilp36.tfm)
Provides:       tex(bsmilp36.vf)
Provides:       tex(bsmilp37.tfm)
Provides:       tex(bsmilp37.vf)
Provides:       tex(bsmilp38.tfm)
Provides:       tex(bsmilp38.vf)
Provides:       tex(bsmilp39.tfm)
Provides:       tex(bsmilp39.vf)
Provides:       tex(bsmilp40.tfm)
Provides:       tex(bsmilp40.vf)
Provides:       tex(bsmilp41.tfm)
Provides:       tex(bsmilp41.vf)
Provides:       tex(bsmilp42.tfm)
Provides:       tex(bsmilp42.vf)
Provides:       tex(bsmilp43.tfm)
Provides:       tex(bsmilp43.vf)
Provides:       tex(bsmilp44.tfm)
Provides:       tex(bsmilp44.vf)
Provides:       tex(bsmilp45.tfm)
Provides:       tex(bsmilp45.vf)
Provides:       tex(bsmilp46.tfm)
Provides:       tex(bsmilp46.vf)
Provides:       tex(bsmilp47.tfm)
Provides:       tex(bsmilp47.vf)
Provides:       tex(bsmilp48.tfm)
Provides:       tex(bsmilp48.vf)
Provides:       tex(bsmilp49.tfm)
Provides:       tex(bsmilp49.vf)
Provides:       tex(bsmilp50.tfm)
Provides:       tex(bsmilp50.vf)
Provides:       tex(bsmilp51.tfm)
Provides:       tex(bsmilp51.vf)
Provides:       tex(bsmilp52.tfm)
Provides:       tex(bsmilp52.vf)
Provides:       tex(bsmilp53.tfm)
Provides:       tex(bsmilp53.vf)
Provides:       tex(bsmilp54.tfm)
Provides:       tex(bsmilp54.vf)
Provides:       tex(bsmilp55.tfm)
Provides:       tex(bsmilp55.vf)
Provides:       tex(bsmilpv.tfm)
Provides:       tex(bsmilpv.vf)
Provides:       tex(bsmiu.map)
Provides:       tex(bsmiu00.tfm)
Provides:       tex(bsmiu02.tfm)
Provides:       tex(bsmiu03.tfm)
Provides:       tex(bsmiu20.tfm)
Provides:       tex(bsmiu21.tfm)
Provides:       tex(bsmiu22.tfm)
Provides:       tex(bsmiu25.tfm)
Provides:       tex(bsmiu26.tfm)
Provides:       tex(bsmiu30.tfm)
Provides:       tex(bsmiu31.tfm)
Provides:       tex(bsmiu32.tfm)
Provides:       tex(bsmiu33.tfm)
Provides:       tex(bsmiu4e.tfm)
Provides:       tex(bsmiu4f.tfm)
Provides:       tex(bsmiu50.tfm)
Provides:       tex(bsmiu51.tfm)
Provides:       tex(bsmiu52.tfm)
Provides:       tex(bsmiu53.tfm)
Provides:       tex(bsmiu54.tfm)
Provides:       tex(bsmiu55.tfm)
Provides:       tex(bsmiu56.tfm)
Provides:       tex(bsmiu57.tfm)
Provides:       tex(bsmiu58.tfm)
Provides:       tex(bsmiu59.tfm)
Provides:       tex(bsmiu5a.tfm)
Provides:       tex(bsmiu5b.tfm)
Provides:       tex(bsmiu5c.tfm)
Provides:       tex(bsmiu5d.tfm)
Provides:       tex(bsmiu5e.tfm)
Provides:       tex(bsmiu5f.tfm)
Provides:       tex(bsmiu60.tfm)
Provides:       tex(bsmiu61.tfm)
Provides:       tex(bsmiu62.tfm)
Provides:       tex(bsmiu63.tfm)
Provides:       tex(bsmiu64.tfm)
Provides:       tex(bsmiu65.tfm)
Provides:       tex(bsmiu66.tfm)
Provides:       tex(bsmiu67.tfm)
Provides:       tex(bsmiu68.tfm)
Provides:       tex(bsmiu69.tfm)
Provides:       tex(bsmiu6a.tfm)
Provides:       tex(bsmiu6b.tfm)
Provides:       tex(bsmiu6c.tfm)
Provides:       tex(bsmiu6d.tfm)
Provides:       tex(bsmiu6e.tfm)
Provides:       tex(bsmiu6f.tfm)
Provides:       tex(bsmiu70.tfm)
Provides:       tex(bsmiu71.tfm)
Provides:       tex(bsmiu72.tfm)
Provides:       tex(bsmiu73.tfm)
Provides:       tex(bsmiu74.tfm)
Provides:       tex(bsmiu75.tfm)
Provides:       tex(bsmiu76.tfm)
Provides:       tex(bsmiu77.tfm)
Provides:       tex(bsmiu78.tfm)
Provides:       tex(bsmiu79.tfm)
Provides:       tex(bsmiu7a.tfm)
Provides:       tex(bsmiu7b.tfm)
Provides:       tex(bsmiu7c.tfm)
Provides:       tex(bsmiu7d.tfm)
Provides:       tex(bsmiu7e.tfm)
Provides:       tex(bsmiu7f.tfm)
Provides:       tex(bsmiu80.tfm)
Provides:       tex(bsmiu81.tfm)
Provides:       tex(bsmiu82.tfm)
Provides:       tex(bsmiu83.tfm)
Provides:       tex(bsmiu84.tfm)
Provides:       tex(bsmiu85.tfm)
Provides:       tex(bsmiu86.tfm)
Provides:       tex(bsmiu87.tfm)
Provides:       tex(bsmiu88.tfm)
Provides:       tex(bsmiu89.tfm)
Provides:       tex(bsmiu8a.tfm)
Provides:       tex(bsmiu8b.tfm)
Provides:       tex(bsmiu8c.tfm)
Provides:       tex(bsmiu8d.tfm)
Provides:       tex(bsmiu8e.tfm)
Provides:       tex(bsmiu8f.tfm)
Provides:       tex(bsmiu90.tfm)
Provides:       tex(bsmiu91.tfm)
Provides:       tex(bsmiu92.tfm)
Provides:       tex(bsmiu93.tfm)
Provides:       tex(bsmiu94.tfm)
Provides:       tex(bsmiu95.tfm)
Provides:       tex(bsmiu96.tfm)
Provides:       tex(bsmiu97.tfm)
Provides:       tex(bsmiu98.tfm)
Provides:       tex(bsmiu99.tfm)
Provides:       tex(bsmiu9a.tfm)
Provides:       tex(bsmiu9b.tfm)
Provides:       tex(bsmiu9c.tfm)
Provides:       tex(bsmiu9d.tfm)
Provides:       tex(bsmiu9e.tfm)
Provides:       tex(bsmiu9f.tfm)
Provides:       tex(bsmiuee.tfm)
Provides:       tex(bsmiuf6.tfm)
Provides:       tex(bsmiuf7.tfm)
Provides:       tex(bsmiuf8.tfm)
Provides:       tex(bsmiufa.tfm)
Provides:       tex(bsmiufe.tfm)
Provides:       tex(bsmiuff.tfm)
Provides:       tex(bsmiuv.tfm)
Provides:       tex(gbsnlp00.tfm)
Provides:       tex(gbsnlp00.vf)
Provides:       tex(gbsnlp01.tfm)
Provides:       tex(gbsnlp01.vf)
Provides:       tex(gbsnlp02.tfm)
Provides:       tex(gbsnlp02.vf)
Provides:       tex(gbsnlp03.tfm)
Provides:       tex(gbsnlp03.vf)
Provides:       tex(gbsnlp04.tfm)
Provides:       tex(gbsnlp04.vf)
Provides:       tex(gbsnlp06.tfm)
Provides:       tex(gbsnlp06.vf)
Provides:       tex(gbsnlp07.tfm)
Provides:       tex(gbsnlp07.vf)
Provides:       tex(gbsnlp08.tfm)
Provides:       tex(gbsnlp08.vf)
Provides:       tex(gbsnlp09.tfm)
Provides:       tex(gbsnlp09.vf)
Provides:       tex(gbsnlp10.tfm)
Provides:       tex(gbsnlp10.vf)
Provides:       tex(gbsnlp11.tfm)
Provides:       tex(gbsnlp11.vf)
Provides:       tex(gbsnlp12.tfm)
Provides:       tex(gbsnlp12.vf)
Provides:       tex(gbsnlp13.tfm)
Provides:       tex(gbsnlp13.vf)
Provides:       tex(gbsnlp14.tfm)
Provides:       tex(gbsnlp14.vf)
Provides:       tex(gbsnlp15.tfm)
Provides:       tex(gbsnlp15.vf)
Provides:       tex(gbsnlp16.tfm)
Provides:       tex(gbsnlp16.vf)
Provides:       tex(gbsnlp17.tfm)
Provides:       tex(gbsnlp17.vf)
Provides:       tex(gbsnlp18.tfm)
Provides:       tex(gbsnlp18.vf)
Provides:       tex(gbsnlp19.tfm)
Provides:       tex(gbsnlp19.vf)
Provides:       tex(gbsnlp20.tfm)
Provides:       tex(gbsnlp20.vf)
Provides:       tex(gbsnlp21.tfm)
Provides:       tex(gbsnlp21.vf)
Provides:       tex(gbsnlp22.tfm)
Provides:       tex(gbsnlp22.vf)
Provides:       tex(gbsnlp23.tfm)
Provides:       tex(gbsnlp23.vf)
Provides:       tex(gbsnlp24.tfm)
Provides:       tex(gbsnlp24.vf)
Provides:       tex(gbsnlp25.tfm)
Provides:       tex(gbsnlp25.vf)
Provides:       tex(gbsnlp26.tfm)
Provides:       tex(gbsnlp26.vf)
Provides:       tex(gbsnlp27.tfm)
Provides:       tex(gbsnlp27.vf)
Provides:       tex(gbsnlp28.tfm)
Provides:       tex(gbsnlp28.vf)
Provides:       tex(gbsnlp29.tfm)
Provides:       tex(gbsnlp29.vf)
Provides:       tex(gbsnlp30.tfm)
Provides:       tex(gbsnlp30.vf)
Provides:       tex(gbsnlp31.tfm)
Provides:       tex(gbsnlp31.vf)
Provides:       tex(gbsnlp32.tfm)
Provides:       tex(gbsnlp32.vf)
Provides:       tex(gbsnu.map)
Provides:       tex(gbsnu00.tfm)
Provides:       tex(gbsnu01.tfm)
Provides:       tex(gbsnu02.tfm)
Provides:       tex(gbsnu03.tfm)
Provides:       tex(gbsnu04.tfm)
Provides:       tex(gbsnu20.tfm)
Provides:       tex(gbsnu21.tfm)
Provides:       tex(gbsnu22.tfm)
Provides:       tex(gbsnu23.tfm)
Provides:       tex(gbsnu24.tfm)
Provides:       tex(gbsnu25.tfm)
Provides:       tex(gbsnu26.tfm)
Provides:       tex(gbsnu30.tfm)
Provides:       tex(gbsnu31.tfm)
Provides:       tex(gbsnu32.tfm)
Provides:       tex(gbsnu4e.tfm)
Provides:       tex(gbsnu4f.tfm)
Provides:       tex(gbsnu50.tfm)
Provides:       tex(gbsnu51.tfm)
Provides:       tex(gbsnu52.tfm)
Provides:       tex(gbsnu53.tfm)
Provides:       tex(gbsnu54.tfm)
Provides:       tex(gbsnu55.tfm)
Provides:       tex(gbsnu56.tfm)
Provides:       tex(gbsnu57.tfm)
Provides:       tex(gbsnu58.tfm)
Provides:       tex(gbsnu59.tfm)
Provides:       tex(gbsnu5a.tfm)
Provides:       tex(gbsnu5b.tfm)
Provides:       tex(gbsnu5c.tfm)
Provides:       tex(gbsnu5d.tfm)
Provides:       tex(gbsnu5e.tfm)
Provides:       tex(gbsnu5f.tfm)
Provides:       tex(gbsnu60.tfm)
Provides:       tex(gbsnu61.tfm)
Provides:       tex(gbsnu62.tfm)
Provides:       tex(gbsnu63.tfm)
Provides:       tex(gbsnu64.tfm)
Provides:       tex(gbsnu65.tfm)
Provides:       tex(gbsnu66.tfm)
Provides:       tex(gbsnu67.tfm)
Provides:       tex(gbsnu68.tfm)
Provides:       tex(gbsnu69.tfm)
Provides:       tex(gbsnu6a.tfm)
Provides:       tex(gbsnu6b.tfm)
Provides:       tex(gbsnu6c.tfm)
Provides:       tex(gbsnu6d.tfm)
Provides:       tex(gbsnu6e.tfm)
Provides:       tex(gbsnu6f.tfm)
Provides:       tex(gbsnu70.tfm)
Provides:       tex(gbsnu71.tfm)
Provides:       tex(gbsnu72.tfm)
Provides:       tex(gbsnu73.tfm)
Provides:       tex(gbsnu74.tfm)
Provides:       tex(gbsnu75.tfm)
Provides:       tex(gbsnu76.tfm)
Provides:       tex(gbsnu77.tfm)
Provides:       tex(gbsnu78.tfm)
Provides:       tex(gbsnu79.tfm)
Provides:       tex(gbsnu7a.tfm)
Provides:       tex(gbsnu7b.tfm)
Provides:       tex(gbsnu7c.tfm)
Provides:       tex(gbsnu7d.tfm)
Provides:       tex(gbsnu7e.tfm)
Provides:       tex(gbsnu7f.tfm)
Provides:       tex(gbsnu80.tfm)
Provides:       tex(gbsnu81.tfm)
Provides:       tex(gbsnu82.tfm)
Provides:       tex(gbsnu83.tfm)
Provides:       tex(gbsnu84.tfm)
Provides:       tex(gbsnu85.tfm)
Provides:       tex(gbsnu86.tfm)
Provides:       tex(gbsnu87.tfm)
Provides:       tex(gbsnu88.tfm)
Provides:       tex(gbsnu89.tfm)
Provides:       tex(gbsnu8a.tfm)
Provides:       tex(gbsnu8b.tfm)
Provides:       tex(gbsnu8c.tfm)
Provides:       tex(gbsnu8d.tfm)
Provides:       tex(gbsnu8e.tfm)
Provides:       tex(gbsnu8f.tfm)
Provides:       tex(gbsnu90.tfm)
Provides:       tex(gbsnu91.tfm)
Provides:       tex(gbsnu92.tfm)
Provides:       tex(gbsnu93.tfm)
Provides:       tex(gbsnu94.tfm)
Provides:       tex(gbsnu95.tfm)
Provides:       tex(gbsnu96.tfm)
Provides:       tex(gbsnu97.tfm)
Provides:       tex(gbsnu98.tfm)
Provides:       tex(gbsnu99.tfm)
Provides:       tex(gbsnu9a.tfm)
Provides:       tex(gbsnu9b.tfm)
Provides:       tex(gbsnu9c.tfm)
Provides:       tex(gbsnu9e.tfm)
Provides:       tex(gbsnu9f.tfm)
Provides:       tex(gbsnufe.tfm)
Provides:       tex(gbsnuff.tfm)
Provides:       tex(gkaimp00.tfm)
Provides:       tex(gkaimp00.vf)
Provides:       tex(gkaimp01.tfm)
Provides:       tex(gkaimp01.vf)
Provides:       tex(gkaimp02.tfm)
Provides:       tex(gkaimp02.vf)
Provides:       tex(gkaimp03.tfm)
Provides:       tex(gkaimp03.vf)
Provides:       tex(gkaimp04.tfm)
Provides:       tex(gkaimp04.vf)
Provides:       tex(gkaimp06.tfm)
Provides:       tex(gkaimp06.vf)
Provides:       tex(gkaimp07.tfm)
Provides:       tex(gkaimp07.vf)
Provides:       tex(gkaimp08.tfm)
Provides:       tex(gkaimp08.vf)
Provides:       tex(gkaimp09.tfm)
Provides:       tex(gkaimp09.vf)
Provides:       tex(gkaimp10.tfm)
Provides:       tex(gkaimp10.vf)
Provides:       tex(gkaimp11.tfm)
Provides:       tex(gkaimp11.vf)
Provides:       tex(gkaimp12.tfm)
Provides:       tex(gkaimp12.vf)
Provides:       tex(gkaimp13.tfm)
Provides:       tex(gkaimp13.vf)
Provides:       tex(gkaimp14.tfm)
Provides:       tex(gkaimp14.vf)
Provides:       tex(gkaimp15.tfm)
Provides:       tex(gkaimp15.vf)
Provides:       tex(gkaimp16.tfm)
Provides:       tex(gkaimp16.vf)
Provides:       tex(gkaimp17.tfm)
Provides:       tex(gkaimp17.vf)
Provides:       tex(gkaimp18.tfm)
Provides:       tex(gkaimp18.vf)
Provides:       tex(gkaimp19.tfm)
Provides:       tex(gkaimp19.vf)
Provides:       tex(gkaimp20.tfm)
Provides:       tex(gkaimp20.vf)
Provides:       tex(gkaimp21.tfm)
Provides:       tex(gkaimp21.vf)
Provides:       tex(gkaimp22.tfm)
Provides:       tex(gkaimp22.vf)
Provides:       tex(gkaimp23.tfm)
Provides:       tex(gkaimp23.vf)
Provides:       tex(gkaimp24.tfm)
Provides:       tex(gkaimp24.vf)
Provides:       tex(gkaimp25.tfm)
Provides:       tex(gkaimp25.vf)
Provides:       tex(gkaimp26.tfm)
Provides:       tex(gkaimp26.vf)
Provides:       tex(gkaimp27.tfm)
Provides:       tex(gkaimp27.vf)
Provides:       tex(gkaimp28.tfm)
Provides:       tex(gkaimp28.vf)
Provides:       tex(gkaimp29.tfm)
Provides:       tex(gkaimp29.vf)
Provides:       tex(gkaimp30.tfm)
Provides:       tex(gkaimp30.vf)
Provides:       tex(gkaimp31.tfm)
Provides:       tex(gkaimp31.vf)
Provides:       tex(gkaimp32.tfm)
Provides:       tex(gkaimp32.vf)
Provides:       tex(gkaiu.map)
Provides:       tex(gkaiu00.tfm)
Provides:       tex(gkaiu01.tfm)
Provides:       tex(gkaiu02.tfm)
Provides:       tex(gkaiu03.tfm)
Provides:       tex(gkaiu04.tfm)
Provides:       tex(gkaiu20.tfm)
Provides:       tex(gkaiu21.tfm)
Provides:       tex(gkaiu22.tfm)
Provides:       tex(gkaiu23.tfm)
Provides:       tex(gkaiu24.tfm)
Provides:       tex(gkaiu25.tfm)
Provides:       tex(gkaiu26.tfm)
Provides:       tex(gkaiu30.tfm)
Provides:       tex(gkaiu31.tfm)
Provides:       tex(gkaiu32.tfm)
Provides:       tex(gkaiu4e.tfm)
Provides:       tex(gkaiu4f.tfm)
Provides:       tex(gkaiu50.tfm)
Provides:       tex(gkaiu51.tfm)
Provides:       tex(gkaiu52.tfm)
Provides:       tex(gkaiu53.tfm)
Provides:       tex(gkaiu54.tfm)
Provides:       tex(gkaiu55.tfm)
Provides:       tex(gkaiu56.tfm)
Provides:       tex(gkaiu57.tfm)
Provides:       tex(gkaiu58.tfm)
Provides:       tex(gkaiu59.tfm)
Provides:       tex(gkaiu5a.tfm)
Provides:       tex(gkaiu5b.tfm)
Provides:       tex(gkaiu5c.tfm)
Provides:       tex(gkaiu5d.tfm)
Provides:       tex(gkaiu5e.tfm)
Provides:       tex(gkaiu5f.tfm)
Provides:       tex(gkaiu60.tfm)
Provides:       tex(gkaiu61.tfm)
Provides:       tex(gkaiu62.tfm)
Provides:       tex(gkaiu63.tfm)
Provides:       tex(gkaiu64.tfm)
Provides:       tex(gkaiu65.tfm)
Provides:       tex(gkaiu66.tfm)
Provides:       tex(gkaiu67.tfm)
Provides:       tex(gkaiu68.tfm)
Provides:       tex(gkaiu69.tfm)
Provides:       tex(gkaiu6a.tfm)
Provides:       tex(gkaiu6b.tfm)
Provides:       tex(gkaiu6c.tfm)
Provides:       tex(gkaiu6d.tfm)
Provides:       tex(gkaiu6e.tfm)
Provides:       tex(gkaiu6f.tfm)
Provides:       tex(gkaiu70.tfm)
Provides:       tex(gkaiu71.tfm)
Provides:       tex(gkaiu72.tfm)
Provides:       tex(gkaiu73.tfm)
Provides:       tex(gkaiu74.tfm)
Provides:       tex(gkaiu75.tfm)
Provides:       tex(gkaiu76.tfm)
Provides:       tex(gkaiu77.tfm)
Provides:       tex(gkaiu78.tfm)
Provides:       tex(gkaiu79.tfm)
Provides:       tex(gkaiu7a.tfm)
Provides:       tex(gkaiu7b.tfm)
Provides:       tex(gkaiu7c.tfm)
Provides:       tex(gkaiu7d.tfm)
Provides:       tex(gkaiu7e.tfm)
Provides:       tex(gkaiu7f.tfm)
Provides:       tex(gkaiu80.tfm)
Provides:       tex(gkaiu81.tfm)
Provides:       tex(gkaiu82.tfm)
Provides:       tex(gkaiu83.tfm)
Provides:       tex(gkaiu84.tfm)
Provides:       tex(gkaiu85.tfm)
Provides:       tex(gkaiu86.tfm)
Provides:       tex(gkaiu87.tfm)
Provides:       tex(gkaiu88.tfm)
Provides:       tex(gkaiu89.tfm)
Provides:       tex(gkaiu8a.tfm)
Provides:       tex(gkaiu8b.tfm)
Provides:       tex(gkaiu8c.tfm)
Provides:       tex(gkaiu8d.tfm)
Provides:       tex(gkaiu8e.tfm)
Provides:       tex(gkaiu8f.tfm)
Provides:       tex(gkaiu90.tfm)
Provides:       tex(gkaiu91.tfm)
Provides:       tex(gkaiu92.tfm)
Provides:       tex(gkaiu93.tfm)
Provides:       tex(gkaiu94.tfm)
Provides:       tex(gkaiu95.tfm)
Provides:       tex(gkaiu96.tfm)
Provides:       tex(gkaiu97.tfm)
Provides:       tex(gkaiu98.tfm)
Provides:       tex(gkaiu99.tfm)
Provides:       tex(gkaiu9a.tfm)
Provides:       tex(gkaiu9b.tfm)
Provides:       tex(gkaiu9c.tfm)
Provides:       tex(gkaiu9e.tfm)
Provides:       tex(gkaiu9f.tfm)
Provides:       tex(gkaiufe.tfm)
Provides:       tex(gkaiuff.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source2:        arphic.tar.xz
Source3:        arphic.doc.tar.xz

%description -n texlive-arphic
These are font bundles for the Chinese Arphic fonts which work
with the CJK package. TrueType versions of these fonts for use
with XeLaTeX and LuaLaTeX are provided by the arphic-ttf
package. Arphic is actually the name of the company which
created these fonts (and put them under a GPL-like licence).

%package -n texlive-arphic-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-arphic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-arphic-doc
This package includes the documentation for texlive-arphic


%package -n texlive-arphic-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Severed fonts for texlive-arphic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-arphic-fonts
The  separated fonts package for texlive-arphic
%post -n texlive-arphic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap bkaiu.map' >> /var/run/texlive/run-updmap
echo 'addMap bsmiu.map' >> /var/run/texlive/run-updmap
echo 'addMap gbsnu.map' >> /var/run/texlive/run-updmap
echo 'addMap gkaiu.map' >> /var/run/texlive/run-updmap

%postun -n texlive-arphic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap bkaiu.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap bsmiu.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap gbsnu.map' >> /var/run/texlive/run-updmap
    echo 'deleteMap gkaiu.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-arphic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-arphic-fonts
%files -n texlive-arphic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/arphic/arphic-sampler.pdf
%{_texmfdistdir}/doc/fonts/arphic/arphic-sampler.tex
%{_texmfdistdir}/doc/fonts/arphic/bkaiu/README
%{_texmfdistdir}/doc/fonts/arphic/bsmiu/README
%{_texmfdistdir}/doc/fonts/arphic/gbsnu/README
%{_texmfdistdir}/doc/fonts/arphic/gkaiu/README

%files -n texlive-arphic
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/arphic/config.bkaiu
%{_texmfdistdir}/dvips/arphic/config.bsmiu
%{_texmfdistdir}/dvips/arphic/config.gbsnu
%{_texmfdistdir}/dvips/arphic/config.gkaiu
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu00.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu02.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu03.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu20.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu21.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu22.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu25.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu26.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu30.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu31.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu32.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu33.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu4e.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu4f.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu50.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu51.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu52.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu53.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu54.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu55.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu56.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu57.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu58.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu59.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu5a.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu5b.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu5c.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu5d.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu5e.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu5f.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu60.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu61.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu62.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu63.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu64.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu65.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu66.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu67.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu68.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu69.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu6a.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu6b.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu6c.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu6d.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu6e.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu6f.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu70.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu71.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu72.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu73.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu74.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu75.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu76.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu77.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu78.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu79.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu7a.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu7b.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu7c.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu7d.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu7e.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu7f.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu80.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu81.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu82.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu83.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu84.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu85.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu86.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu87.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu88.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu89.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu8a.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu8b.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu8c.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu8d.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu8e.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu8f.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu90.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu91.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu92.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu93.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu94.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu95.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu96.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu97.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu98.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu99.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu9a.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu9b.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu9c.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu9d.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu9e.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiu9f.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiuee.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiuf6.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiuf7.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiuf8.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiufa.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiufe.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiuff.afm
%{_texmfdistdir}/fonts/afm/arphic/bkaiu/bkaiuv.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu00.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu02.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu03.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu20.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu21.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu22.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu25.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu26.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu30.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu31.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu32.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu33.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu4e.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu4f.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu50.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu51.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu52.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu53.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu54.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu55.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu56.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu57.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu58.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu59.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu5a.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu5b.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu5c.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu5d.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu5e.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu5f.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu60.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu61.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu62.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu63.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu64.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu65.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu66.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu67.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu68.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu69.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu6a.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu6b.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu6c.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu6d.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu6e.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu6f.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu70.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu71.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu72.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu73.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu74.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu75.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu76.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu77.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu78.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu79.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu7a.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu7b.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu7c.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu7d.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu7e.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu7f.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu80.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu81.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu82.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu83.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu84.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu85.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu86.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu87.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu88.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu89.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu8a.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu8b.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu8c.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu8d.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu8e.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu8f.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu90.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu91.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu92.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu93.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu94.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu95.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu96.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu97.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu98.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu99.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu9a.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu9b.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu9c.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu9d.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu9e.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiu9f.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiuee.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiuf6.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiuf7.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiuf8.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiufa.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiufe.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiuff.afm
%{_texmfdistdir}/fonts/afm/arphic/bsmiu/bsmiuv.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu00.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu01.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu02.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu03.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu04.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu20.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu21.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu22.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu23.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu24.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu25.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu26.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu30.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu31.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu32.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu4e.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu4f.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu50.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu51.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu52.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu53.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu54.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu55.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu56.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu57.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu58.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu59.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu5a.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu5b.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu5c.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu5d.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu5e.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu5f.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu60.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu61.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu62.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu63.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu64.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu65.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu66.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu67.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu68.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu69.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu6a.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu6b.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu6c.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu6d.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu6e.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu6f.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu70.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu71.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu72.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu73.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu74.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu75.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu76.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu77.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu78.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu79.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu7a.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu7b.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu7c.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu7d.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu7e.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu7f.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu80.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu81.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu82.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu83.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu84.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu85.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu86.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu87.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu88.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu89.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu8a.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu8b.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu8c.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu8d.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu8e.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu8f.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu90.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu91.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu92.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu93.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu94.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu95.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu96.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu97.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu98.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu99.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu9a.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu9b.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu9c.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu9e.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnu9f.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnufe.afm
%{_texmfdistdir}/fonts/afm/arphic/gbsnu/gbsnuff.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu00.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu01.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu02.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu03.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu04.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu20.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu21.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu22.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu23.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu24.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu25.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu26.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu30.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu31.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu32.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu4e.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu4f.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu50.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu51.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu52.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu53.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu54.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu55.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu56.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu57.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu58.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu59.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu5a.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu5b.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu5c.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu5d.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu5e.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu5f.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu60.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu61.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu62.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu63.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu64.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu65.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu66.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu67.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu68.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu69.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu6a.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu6b.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu6c.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu6d.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu6e.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu6f.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu70.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu71.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu72.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu73.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu74.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu75.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu76.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu77.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu78.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu79.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu7a.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu7b.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu7c.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu7d.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu7e.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu7f.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu80.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu81.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu82.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu83.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu84.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu85.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu86.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu87.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu88.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu89.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu8a.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu8b.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu8c.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu8d.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu8e.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu8f.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu90.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu91.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu92.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu93.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu94.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu95.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu96.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu97.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu98.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu99.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu9a.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu9b.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu9c.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu9e.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiu9f.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiufe.afm
%{_texmfdistdir}/fonts/afm/arphic/gkaiu/gkaiuff.afm
%{_texmfdistdir}/fonts/map/dvips/arphic/bkaiu.map
%{_texmfdistdir}/fonts/map/dvips/arphic/bsmiu.map
%{_texmfdistdir}/fonts/map/dvips/arphic/gbsnu.map
%{_texmfdistdir}/fonts/map/dvips/arphic/gkaiu.map
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp01.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp04.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp05.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp06.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp07.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp08.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp09.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp10.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp11.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp12.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp13.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp14.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp15.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp16.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp17.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp18.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp19.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp23.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp27.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp28.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp29.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp33.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp34.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp35.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp36.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp37.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp38.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp39.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp40.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp41.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp42.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp43.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp44.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp45.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp46.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp47.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp48.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp49.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp50.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp51.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp52.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp53.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp54.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimp55.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaimp/bkaimpv.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu33.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu4e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu4f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu50.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu51.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu52.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu53.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu54.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu55.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu56.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu57.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu58.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu59.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu5a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu5b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu5c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu5d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu5e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu5f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu60.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu61.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu62.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu63.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu64.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu65.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu66.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu67.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu68.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu69.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu6a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu6b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu6c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu6d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu6e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu6f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu70.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu71.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu72.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu73.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu74.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu75.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu76.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu77.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu78.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu79.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu7a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu7b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu7c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu7d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu7e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu7f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu80.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu81.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu82.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu83.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu84.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu85.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu86.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu87.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu88.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu89.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu8a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu8b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu8c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu8d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu8e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu8f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu90.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu91.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu92.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu93.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu94.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu95.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu96.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu97.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu98.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu99.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu9a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu9b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu9c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu9d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu9e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiu9f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiuee.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiuf6.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiuf7.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiuf8.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiufa.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiufe.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiuff.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bkaiu/bkaiuv.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp01.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp04.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp05.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp06.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp07.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp08.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp09.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp10.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp11.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp12.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp13.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp14.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp15.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp16.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp17.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp18.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp19.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp23.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp27.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp28.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp29.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp33.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp34.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp35.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp36.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp37.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp38.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp39.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp40.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp41.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp42.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp43.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp44.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp45.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp46.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp47.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp48.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp49.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp50.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp51.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp52.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp53.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp54.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilp55.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmilp/bsmilpv.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu33.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu4e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu4f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu50.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu51.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu52.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu53.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu54.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu55.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu56.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu57.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu58.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu59.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu5a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu5b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu5c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu5d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu5e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu5f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu60.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu61.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu62.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu63.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu64.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu65.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu66.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu67.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu68.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu69.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu6a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu6b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu6c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu6d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu6e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu6f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu70.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu71.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu72.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu73.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu74.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu75.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu76.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu77.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu78.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu79.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu7a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu7b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu7c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu7d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu7e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu7f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu80.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu81.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu82.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu83.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu84.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu85.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu86.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu87.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu88.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu89.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu8a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu8b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu8c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu8d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu8e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu8f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu90.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu91.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu92.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu93.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu94.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu95.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu96.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu97.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu98.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu99.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu9a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu9b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu9c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu9d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu9e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiu9f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiuee.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiuf6.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiuf7.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiuf8.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiufa.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiufe.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiuff.tfm
%{_texmfdistdir}/fonts/tfm/arphic/bsmiu/bsmiuv.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp01.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp04.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp06.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp07.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp08.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp09.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp10.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp11.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp12.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp13.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp14.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp15.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp16.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp17.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp18.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp19.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp23.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp24.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp27.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp28.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp29.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnlp/gbsnlp32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu01.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu04.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu23.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu24.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu4e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu4f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu50.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu51.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu52.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu53.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu54.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu55.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu56.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu57.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu58.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu59.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu5a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu5b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu5c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu5d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu5e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu5f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu60.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu61.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu62.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu63.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu64.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu65.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu66.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu67.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu68.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu69.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu6a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu6b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu6c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu6d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu6e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu6f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu70.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu71.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu72.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu73.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu74.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu75.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu76.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu77.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu78.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu79.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu7a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu7b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu7c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu7d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu7e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu7f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu80.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu81.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu82.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu83.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu84.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu85.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu86.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu87.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu88.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu89.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu8a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu8b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu8c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu8d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu8e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu8f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu90.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu91.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu92.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu93.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu94.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu95.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu96.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu97.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu98.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu99.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu9a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu9b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu9c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu9e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnu9f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnufe.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gbsnu/gbsnuff.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp01.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp04.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp06.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp07.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp08.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp09.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp10.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp11.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp12.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp13.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp14.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp15.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp16.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp17.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp18.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp19.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp23.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp24.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp27.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp28.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp29.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaimp/gkaimp32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu00.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu01.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu02.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu03.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu04.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu20.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu21.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu22.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu23.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu24.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu25.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu26.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu30.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu31.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu32.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu4e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu4f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu50.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu51.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu52.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu53.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu54.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu55.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu56.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu57.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu58.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu59.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu5a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu5b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu5c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu5d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu5e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu5f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu60.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu61.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu62.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu63.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu64.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu65.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu66.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu67.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu68.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu69.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu6a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu6b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu6c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu6d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu6e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu6f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu70.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu71.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu72.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu73.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu74.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu75.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu76.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu77.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu78.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu79.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu7a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu7b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu7c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu7d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu7e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu7f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu80.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu81.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu82.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu83.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu84.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu85.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu86.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu87.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu88.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu89.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu8a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu8b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu8c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu8d.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu8e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu8f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu90.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu91.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu92.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu93.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu94.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu95.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu96.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu97.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu98.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu99.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu9a.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu9b.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu9c.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu9e.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiu9f.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiufe.tfm
%{_texmfdistdir}/fonts/tfm/arphic/gkaiu/gkaiuff.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu00.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu02.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu03.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu20.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu21.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu22.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu25.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu26.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu30.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu31.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu32.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu33.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu4e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu4f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu50.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu51.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu52.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu53.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu54.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu55.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu56.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu57.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu58.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu59.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu5a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu5b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu5c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu5d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu5e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu5f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu60.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu61.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu62.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu63.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu64.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu65.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu66.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu67.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu68.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu69.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu6a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu6b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu6c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu6d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu6e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu6f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu70.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu71.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu72.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu73.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu74.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu75.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu76.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu77.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu78.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu79.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu7a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu7b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu7c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu7d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu7e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu7f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu80.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu81.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu82.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu83.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu84.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu85.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu86.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu87.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu88.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu89.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu8b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu8d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu8e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu8f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu90.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu91.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu92.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu93.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu94.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu95.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu96.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu97.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu98.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu99.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu9a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu9b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu9c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu9d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu9e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiu9f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiuee.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiuf6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiuf7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiuf8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiufa.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiufe.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiuff.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bkaiu/bkaiuv.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu00.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu02.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu03.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu20.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu21.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu22.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu25.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu26.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu30.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu31.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu32.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu33.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu4e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu4f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu50.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu51.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu52.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu53.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu54.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu55.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu56.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu57.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu58.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu59.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu5a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu5b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu5c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu5d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu5e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu5f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu60.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu61.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu62.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu63.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu64.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu65.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu66.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu67.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu68.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu69.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu6a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu6b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu6c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu6d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu6e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu6f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu70.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu71.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu72.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu73.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu74.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu75.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu76.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu77.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu78.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu79.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu7a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu7b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu7c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu7d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu7e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu7f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu80.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu81.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu82.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu83.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu84.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu85.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu86.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu87.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu88.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu89.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu8b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu8d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu8e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu8f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu90.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu91.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu92.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu93.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu94.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu95.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu96.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu97.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu98.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu99.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu9a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu9b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu9c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu9d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu9e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiu9f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiuee.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiuf6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiuf7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiuf8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiufa.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiufe.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiuff.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/bsmiu/bsmiuv.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu00.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu01.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu02.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu03.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu04.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu20.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu21.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu22.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu23.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu25.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu26.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu30.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu31.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu32.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu4e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu4f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu50.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu51.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu52.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu53.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu54.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu55.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu56.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu57.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu58.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu59.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu5a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu5b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu5c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu5d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu5e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu5f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu60.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu61.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu62.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu63.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu64.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu65.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu66.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu67.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu68.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu69.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu6a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu6b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu6c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu6d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu6e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu6f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu70.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu71.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu72.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu73.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu74.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu75.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu76.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu77.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu78.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu79.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu7a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu7b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu7c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu7d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu7e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu7f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu80.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu81.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu82.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu83.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu84.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu85.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu86.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu87.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu88.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu89.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu8b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu8d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu8e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu8f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu90.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu91.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu92.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu93.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu94.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu95.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu96.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu97.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu98.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu99.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu9a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu9b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu9c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu9e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnu9f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnufe.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gbsnu/gbsnuff.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu00.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu01.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu02.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu03.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu04.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu20.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu21.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu22.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu23.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu24.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu25.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu26.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu30.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu31.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu32.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu4e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu4f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu50.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu51.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu52.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu53.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu54.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu55.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu56.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu57.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu58.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu59.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu5a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu5b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu5c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu5d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu5e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu5f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu60.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu61.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu62.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu63.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu64.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu65.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu66.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu67.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu68.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu69.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu6a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu6b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu6c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu6d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu6e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu6f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu70.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu71.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu72.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu73.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu74.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu75.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu76.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu77.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu78.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu79.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu7a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu7b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu7c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu7d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu7e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu7f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu80.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu81.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu82.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu83.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu84.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu85.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu86.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu87.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu88.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu89.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu8a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu8b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu8c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu8d.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu8e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu8f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu90.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu91.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu92.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu93.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu94.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu95.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu96.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu97.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu98.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu99.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu9a.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu9b.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu9c.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu9e.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiu9f.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiufe.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/arphic/gkaiu/gkaiuff.pfb
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp00.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp01.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp02.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp03.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp04.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp05.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp06.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp07.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp08.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp09.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp10.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp11.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp12.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp13.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp14.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp15.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp16.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp17.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp18.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp19.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp20.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp21.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp22.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp23.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp25.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp26.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp27.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp28.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp29.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp30.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp31.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp32.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp33.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp34.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp35.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp36.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp37.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp38.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp39.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp40.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp41.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp42.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp43.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp44.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp45.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp46.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp47.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp48.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp49.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp50.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp51.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp52.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp53.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp54.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimp55.vf
%{_texmfdistdir}/fonts/vf/arphic/bkaimp/bkaimpv.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp00.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp01.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp02.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp03.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp04.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp05.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp06.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp07.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp08.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp09.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp10.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp11.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp12.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp13.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp14.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp15.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp16.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp17.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp18.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp19.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp20.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp21.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp22.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp23.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp25.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp26.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp27.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp28.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp29.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp30.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp31.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp32.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp33.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp34.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp35.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp36.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp37.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp38.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp39.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp40.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp41.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp42.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp43.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp44.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp45.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp46.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp47.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp48.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp49.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp50.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp51.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp52.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp53.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp54.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilp55.vf
%{_texmfdistdir}/fonts/vf/arphic/bsmilp/bsmilpv.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp00.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp01.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp02.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp03.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp04.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp06.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp07.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp08.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp09.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp10.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp11.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp12.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp13.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp14.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp15.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp16.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp17.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp18.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp19.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp20.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp21.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp22.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp23.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp24.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp25.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp26.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp27.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp28.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp29.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp30.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp31.vf
%{_texmfdistdir}/fonts/vf/arphic/gbsnlp/gbsnlp32.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp00.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp01.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp02.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp03.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp04.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp06.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp07.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp08.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp09.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp10.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp11.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp12.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp13.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp14.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp15.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp16.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp17.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp18.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp19.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp20.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp21.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp22.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp23.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp24.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp25.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp26.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp27.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp28.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp29.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp30.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp31.vf
%{_texmfdistdir}/fonts/vf/arphic/gkaimp/gkaimp32.vf

%files -n texlive-arphic-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-arphic
%{_datadir}/fontconfig/conf.avail/58-texlive-arphic.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-arphic/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-arphic/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-arphic/fonts.scale
%{_datadir}/fonts/texlive-arphic/bkaiu00.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu02.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu03.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu20.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu21.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu22.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu25.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu26.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu30.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu31.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu32.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu33.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu4e.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu4f.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu50.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu51.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu52.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu53.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu54.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu55.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu56.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu57.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu58.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu59.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu5a.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu5b.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu5c.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu5d.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu5e.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu5f.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu60.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu61.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu62.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu63.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu64.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu65.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu66.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu67.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu68.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu69.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu6a.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu6b.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu6c.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu6d.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu6e.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu6f.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu70.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu71.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu72.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu73.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu74.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu75.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu76.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu77.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu78.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu79.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu7a.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu7b.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu7c.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu7d.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu7e.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu7f.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu80.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu81.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu82.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu83.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu84.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu85.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu86.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu87.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu88.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu89.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu8a.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu8b.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu8c.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu8d.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu8e.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu8f.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu90.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu91.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu92.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu93.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu94.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu95.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu96.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu97.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu98.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu99.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu9a.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu9b.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu9c.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu9d.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu9e.pfb
%{_datadir}/fonts/texlive-arphic/bkaiu9f.pfb
%{_datadir}/fonts/texlive-arphic/bkaiuee.pfb
%{_datadir}/fonts/texlive-arphic/bkaiuf6.pfb
%{_datadir}/fonts/texlive-arphic/bkaiuf7.pfb
%{_datadir}/fonts/texlive-arphic/bkaiuf8.pfb
%{_datadir}/fonts/texlive-arphic/bkaiufa.pfb
%{_datadir}/fonts/texlive-arphic/bkaiufe.pfb
%{_datadir}/fonts/texlive-arphic/bkaiuff.pfb
%{_datadir}/fonts/texlive-arphic/bkaiuv.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu00.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu02.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu03.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu20.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu21.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu22.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu25.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu26.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu30.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu31.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu32.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu33.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu4e.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu4f.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu50.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu51.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu52.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu53.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu54.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu55.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu56.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu57.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu58.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu59.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu5a.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu5b.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu5c.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu5d.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu5e.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu5f.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu60.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu61.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu62.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu63.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu64.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu65.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu66.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu67.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu68.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu69.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu6a.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu6b.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu6c.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu6d.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu6e.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu6f.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu70.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu71.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu72.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu73.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu74.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu75.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu76.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu77.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu78.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu79.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu7a.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu7b.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu7c.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu7d.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu7e.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu7f.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu80.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu81.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu82.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu83.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu84.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu85.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu86.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu87.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu88.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu89.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu8a.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu8b.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu8c.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu8d.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu8e.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu8f.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu90.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu91.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu92.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu93.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu94.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu95.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu96.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu97.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu98.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu99.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu9a.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu9b.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu9c.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu9d.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu9e.pfb
%{_datadir}/fonts/texlive-arphic/bsmiu9f.pfb
%{_datadir}/fonts/texlive-arphic/bsmiuee.pfb
%{_datadir}/fonts/texlive-arphic/bsmiuf6.pfb
%{_datadir}/fonts/texlive-arphic/bsmiuf7.pfb
%{_datadir}/fonts/texlive-arphic/bsmiuf8.pfb
%{_datadir}/fonts/texlive-arphic/bsmiufa.pfb
%{_datadir}/fonts/texlive-arphic/bsmiufe.pfb
%{_datadir}/fonts/texlive-arphic/bsmiuff.pfb
%{_datadir}/fonts/texlive-arphic/bsmiuv.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu00.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu01.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu02.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu03.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu04.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu20.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu21.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu22.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu23.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu24.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu25.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu26.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu30.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu31.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu32.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu4e.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu4f.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu50.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu51.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu52.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu53.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu54.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu55.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu56.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu57.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu58.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu59.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu5a.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu5b.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu5c.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu5d.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu5e.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu5f.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu60.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu61.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu62.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu63.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu64.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu65.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu66.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu67.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu68.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu69.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu6a.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu6b.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu6c.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu6d.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu6e.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu6f.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu70.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu71.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu72.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu73.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu74.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu75.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu76.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu77.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu78.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu79.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu7a.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu7b.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu7c.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu7d.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu7e.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu7f.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu80.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu81.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu82.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu83.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu84.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu85.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu86.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu87.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu88.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu89.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu8a.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu8b.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu8c.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu8d.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu8e.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu8f.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu90.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu91.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu92.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu93.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu94.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu95.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu96.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu97.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu98.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu99.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu9a.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu9b.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu9c.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu9e.pfb
%{_datadir}/fonts/texlive-arphic/gbsnu9f.pfb
%{_datadir}/fonts/texlive-arphic/gbsnufe.pfb
%{_datadir}/fonts/texlive-arphic/gbsnuff.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu00.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu01.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu02.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu03.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu04.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu20.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu21.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu22.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu23.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu24.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu25.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu26.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu30.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu31.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu32.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu4e.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu4f.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu50.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu51.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu52.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu53.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu54.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu55.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu56.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu57.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu58.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu59.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu5a.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu5b.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu5c.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu5d.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu5e.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu5f.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu60.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu61.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu62.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu63.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu64.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu65.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu66.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu67.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu68.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu69.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu6a.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu6b.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu6c.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu6d.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu6e.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu6f.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu70.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu71.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu72.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu73.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu74.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu75.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu76.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu77.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu78.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu79.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu7a.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu7b.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu7c.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu7d.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu7e.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu7f.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu80.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu81.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu82.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu83.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu84.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu85.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu86.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu87.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu88.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu89.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu8a.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu8b.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu8c.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu8d.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu8e.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu8f.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu90.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu91.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu92.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu93.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu94.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu95.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu96.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu97.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu98.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu99.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu9a.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu9b.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu9c.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu9e.pfb
%{_datadir}/fonts/texlive-arphic/gkaiu9f.pfb
%{_datadir}/fonts/texlive-arphic/gkaiufe.pfb
%{_datadir}/fonts/texlive-arphic/gkaiuff.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-arphic-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-arphic-ttf
Version:        %{texlive_version}.%{texlive_noarch}.svn42675
Release:        0
Summary:        TrueType version of Chinese Arphic fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-arphic-ttf-fonts >= %{texlive_version}
Recommends:     texlive-arphic-ttf-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source4:        arphic-ttf.tar.xz
Source5:        arphic-ttf.doc.tar.xz

%description -n texlive-arphic-ttf
This package provides TrueType versions of the Chinese Arphic
fonts for use with XeLaTeX and LuaLaTeX. Type1 versions of
these fonts, for use with pdfLaTeX and the cjk package, are
provided by the arphic package. Arphic is actually the name of
the company which created these fonts.

%package -n texlive-arphic-ttf-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn42675
Release:        0
Summary:        Documentation for texlive-arphic-ttf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-arphic-ttf-doc
This package includes the documentation for texlive-arphic-ttf


%package -n texlive-arphic-ttf-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn42675
Release:        0
Summary:        Severed fonts for texlive-arphic-ttf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-arphic-ttf-fonts
The  separated fonts package for texlive-arphic-ttf
%post -n texlive-arphic-ttf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-arphic-ttf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-arphic-ttf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-arphic-ttf-fonts
%files -n texlive-arphic-ttf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/arphic-ttf/ANNOUNCE.Big5
%{_texmfdistdir}/doc/fonts/arphic-ttf/ANNOUNCE.GB
%{_texmfdistdir}/doc/fonts/arphic-ttf/ARPHICPL.big5
%{_texmfdistdir}/doc/fonts/arphic-ttf/ARPHICPL.gb
%{_texmfdistdir}/doc/fonts/arphic-ttf/ARPHICPL.txt
%{_texmfdistdir}/doc/fonts/arphic-ttf/README.md
%{_texmfdistdir}/doc/fonts/arphic-ttf/changelog.Debian.bkai00mp
%{_texmfdistdir}/doc/fonts/arphic-ttf/changelog.Debian.bsmi00lp
%{_texmfdistdir}/doc/fonts/arphic-ttf/changelog.Debian.gbsn00lp
%{_texmfdistdir}/doc/fonts/arphic-ttf/changelog.Debian.gkai00mp
%{_texmfdistdir}/doc/fonts/arphic-ttf/copyright.Debian
%{_texmfdistdir}/doc/fonts/arphic-ttf/release.txt

%files -n texlive-arphic-ttf
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/truetype/public/arphic-ttf/bkai00mp.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/arphic-ttf/bsmi00lp.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/arphic-ttf/gbsn00lp.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/arphic-ttf/gkai00mp.ttf

%files -n texlive-arphic-ttf-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-arphic-ttf
%{_datadir}/fontconfig/conf.avail/58-texlive-arphic-ttf.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-arphic-ttf/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-arphic-ttf/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-arphic-ttf/fonts.scale
%{_datadir}/fonts/texlive-arphic-ttf/bkai00mp.ttf
%{_datadir}/fonts/texlive-arphic-ttf/bsmi00lp.ttf
%{_datadir}/fonts/texlive-arphic-ttf/gbsn00lp.ttf
%{_datadir}/fonts/texlive-arphic-ttf/gkai00mp.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-arphic-ttf-fonts-%{texlive_version}.%{texlive_noarch}.svn42675-%{release}-zypper
%endif

%package -n texlive-arraycols
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn51491
Release:        0
Summary:        New column types for array and tabular environments
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-arraycols-doc >= %{texlive_version}
Provides:       tex(arraycols.sty)
Requires:       tex(array.sty)
Requires:       tex(cellspace.sty)
Requires:       tex(makecell.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source6:        arraycols.tar.xz
Source7:        arraycols.doc.tar.xz

%description -n texlive-arraycols
This small package provides new column types for array and
tabular environments, horizontally and vertically centered, or
with adjusted height for big mathematical expressions. The
columns width can be fixed or calculated like in tabularx
environments. Macros for drawing vertical and horizontal rules
of variable thickness are also provided.

%package -n texlive-arraycols-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn51491
Release:        0
Summary:        Documentation for texlive-arraycols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-arraycols-doc
This package includes the documentation for texlive-arraycols

%post -n texlive-arraycols
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-arraycols 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-arraycols
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-arraycols-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/arraycols/README.md
%{_texmfdistdir}/doc/latex/arraycols/arraycols.pdf

%files -n texlive-arraycols
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/arraycols/arraycols.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-arraycols-%{texlive_version}.%{texlive_noarch}.1.0svn51491-%{release}-zypper
%endif

%package -n texlive-arrayjobx
Version:        %{texlive_version}.%{texlive_noarch}.1.04svn18125
Release:        0
Summary:        Array data structures for (La)TeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-arrayjobx-doc >= %{texlive_version}
Provides:       tex(arrayjob.sty)
Provides:       tex(arrayjobx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source8:        arrayjobx.tar.xz
Source9:        arrayjobx.doc.tar.xz

%description -n texlive-arrayjobx
This package provides array data structures in (La)TeX, in the
meaning of the classical procedural programming languages like
Fortran, Ada or C, and macros to manipulate them. Arrays can be
mono or bi-dimensional. This is useful for applications which
require high level programming techniques, like algorithmic
graphics programmed in the TeX language. The package supersedes
the arrayjob package.

%package -n texlive-arrayjobx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.04svn18125
Release:        0
Summary:        Documentation for texlive-arrayjobx
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-arrayjobx-doc
This package includes the documentation for texlive-arrayjobx

%post -n texlive-arrayjobx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-arrayjobx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-arrayjobx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-arrayjobx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/arrayjobx/README
%{_texmfdistdir}/doc/generic/arrayjobx/arrayjob.pdf
%{_texmfdistdir}/doc/generic/arrayjobx/arrayjob.tex
%{_texmfdistdir}/doc/generic/arrayjobx/arrayjobx.pdf
%{_texmfdistdir}/doc/generic/arrayjobx/arrayjobx.tex

%files -n texlive-arrayjobx
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/arrayjobx/arrayjob.sty
%{_texmfdistdir}/tex/generic/arrayjobx/arrayjobx.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-arrayjobx-%{texlive_version}.%{texlive_noarch}.1.04svn18125-%{release}-zypper
%endif

%package -n texlive-arraysort
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn31576
Release:        0
Summary:        Sort arrays (or portions of them)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-arraysort-doc >= %{texlive_version}
Provides:       tex(arraysort.sty)
Requires:       tex(arrayjobx.sty)
Requires:       tex(calc.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lcg.sty)
Requires:       tex(macroswap.sty)
Requires:       tex(pdftexcmds.sty)
Requires:       tex(xargs.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source10:       arraysort.tar.xz
Source11:       arraysort.doc.tar.xz

%description -n texlive-arraysort
The package provides a mechanism for sorting arrays (or
portions of them); the arrays should have been created using
the arrayjobx package.

%package -n texlive-arraysort-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn31576
Release:        0
Summary:        Documentation for texlive-arraysort
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-arraysort-doc
This package includes the documentation for texlive-arraysort

%post -n texlive-arraysort
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-arraysort 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-arraysort
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-arraysort-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/arraysort/Makefile
%{_texmfdistdir}/doc/latex/arraysort/README
%{_texmfdistdir}/doc/latex/arraysort/arraysort.pdf

%files -n texlive-arraysort
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/arraysort/arraysort.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-arraysort-%{texlive_version}.%{texlive_noarch}.1.0svn31576-%{release}-zypper
%endif

%package -n texlive-arsclassica
Version:        %{texlive_version}.%{texlive_noarch}.svn45656
Release:        0
Summary:        A different view of the ClassicThesis package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-arsclassica-doc >= %{texlive_version}
Provides:       tex(arsclassica.sty)
Requires:       tex(caption.sty)
Requires:       tex(classicthesis.sty)
Requires:       tex(soul.sty)
Requires:       tex(titlesec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source12:       arsclassica.tar.xz
Source13:       arsclassica.doc.tar.xz

%description -n texlive-arsclassica
The package changes some typographical points of the
ClassicThesis style, by Andre Miede. It enables the user to
reproduce the look of the guide The art of writing with LaTeX
(the web page is in Italian).

%package -n texlive-arsclassica-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn45656
Release:        0
Summary:        Documentation for texlive-arsclassica
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-arsclassica-doc:en)

%description -n texlive-arsclassica-doc
This package includes the documentation for texlive-arsclassica

%post -n texlive-arsclassica
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-arsclassica 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-arsclassica
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-arsclassica-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/arsclassica/ArsClassica.pdf
%{_texmfdistdir}/doc/latex/arsclassica/ArsClassica.tex
%{_texmfdistdir}/doc/latex/arsclassica/Bibliography.bib
%{_texmfdistdir}/doc/latex/arsclassica/Changes
%{_texmfdistdir}/doc/latex/arsclassica/Chapters/Code.tex
%{_texmfdistdir}/doc/latex/arsclassica/Chapters/Fundamentals.tex
%{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Acknowledgements.tex
%{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Bibliography.tex
%{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Contents.tex
%{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Titleback.tex
%{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Titlepage.tex
%{_texmfdistdir}/doc/latex/arsclassica/Graphics/Dolor.jpg
%{_texmfdistdir}/doc/latex/arsclassica/Graphics/Ipsum.jpg
%{_texmfdistdir}/doc/latex/arsclassica/Graphics/Lorem.jpg
%{_texmfdistdir}/doc/latex/arsclassica/Graphics/Sit.jpg
%{_texmfdistdir}/doc/latex/arsclassica/Graphics/TFZSuperEllisse.pdf
%{_texmfdistdir}/doc/latex/arsclassica/README
%{_texmfdistdir}/doc/latex/arsclassica/arsclassica-settings.tex

%files -n texlive-arsclassica
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/arsclassica/arsclassica.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-arsclassica-%{texlive_version}.%{texlive_noarch}.svn45656-%{release}-zypper
%endif

%package -n texlive-articleingud
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn38741
Release:        0
Summary:        LaTeX class for articles published in INGENIERIA review
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-articleingud-doc >= %{texlive_version}
Provides:       tex(articleingud.cls)
Requires:       tex(article.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source14:       articleingud.tar.xz
Source15:       articleingud.doc.tar.xz

%description -n texlive-articleingud
The class is for articles published in INGENIERIA review. It is
derived from the standard LaTeX class article.

%package -n texlive-articleingud-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn38741
Release:        0
Summary:        Documentation for texlive-articleingud
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-articleingud-doc:es)

%description -n texlive-articleingud-doc
This package includes the documentation for texlive-articleingud

%post -n texlive-articleingud
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-articleingud 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-articleingud
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-articleingud-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/articleingud/README
%{_texmfdistdir}/doc/latex/articleingud/articleingud.pdf
%{_texmfdistdir}/doc/latex/articleingud/plantilla.tex
%{_texmfdistdir}/doc/latex/articleingud/template.tex

%files -n texlive-articleingud
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/articleingud/articleingud.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-articleingud-%{texlive_version}.%{texlive_noarch}.0.0.3svn38741-%{release}-zypper
%endif

%package -n texlive-arydshln
Version:        %{texlive_version}.%{texlive_noarch}.1.76svn50084
Release:        0
Summary:        Draw dash-lines in array/tabular
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-arydshln-doc >= %{texlive_version}
Provides:       tex(arydshln.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source16:       arydshln.tar.xz
Source17:       arydshln.doc.tar.xz

%description -n texlive-arydshln
The package is to draw dash-lines in array/tabular
environments. Horizontal lines are drawn by \hdashline and
\cdashline while vertical ones can be specified as a part of
the preamble using ':'. The shape of dash-lines may be
controlled through style parameters or optional arguments. The
package is compatible with array, colortab, longtable, and
colortbl.

%package -n texlive-arydshln-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.76svn50084
Release:        0
Summary:        Documentation for texlive-arydshln
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-arydshln-doc
This package includes the documentation for texlive-arydshln

%post -n texlive-arydshln
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-arydshln 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-arydshln
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-arydshln-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/arydshln/README
%{_texmfdistdir}/doc/latex/arydshln/arydshln-man.pdf
%{_texmfdistdir}/doc/latex/arydshln/arydshln-man.tex
%{_texmfdistdir}/doc/latex/arydshln/arydshln.pdf

%files -n texlive-arydshln
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/arydshln/arydshln.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-arydshln-%{texlive_version}.%{texlive_noarch}.1.76svn50084-%{release}-zypper
%endif

%package -n texlive-asaetr
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn15878
Release:        0
Summary:        Transactions of the ASAE
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-asaetr-doc >= %{texlive_version}
Provides:       tex(asaesub.sty)
Provides:       tex(asaetr.cls)
Provides:       tex(asaetr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source18:       asaetr.tar.xz
Source19:       asaetr.doc.tar.xz

%description -n texlive-asaetr
A class and BibTeX style for submissions to the Transactions of
the American Society of Agricultural Engineers. Also included
is the Metafont source of a slanted Computer Modern Caps and
Small Caps font.

%package -n texlive-asaetr-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn15878
Release:        0
Summary:        Documentation for texlive-asaetr
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-asaetr-doc
This package includes the documentation for texlive-asaetr

%post -n texlive-asaetr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asaetr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asaetr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asaetr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/asaetr/MANIFEST
%{_texmfdistdir}/doc/latex/asaetr/asaetr.bib
%{_texmfdistdir}/doc/latex/asaetr/asaetr.pdf
%{_texmfdistdir}/doc/latex/asaetr/asaetr.tex
%{_texmfdistdir}/doc/latex/asaetr/cmcscsl10.mf

%files -n texlive-asaetr
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/asaetr/asaetr.bst
%{_texmfdistdir}/tex/latex/asaetr/asaesub.sty
%{_texmfdistdir}/tex/latex/asaetr/asaetr.cls
%{_texmfdistdir}/tex/latex/asaetr/asaetr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asaetr-%{texlive_version}.%{texlive_noarch}.1.0asvn15878-%{release}-zypper
%endif

%package -n texlive-asapsym
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn40201
Release:        0
Summary:        Using the free ASAP Symbol font with LaTeX and Plain TeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-asapsym-fonts >= %{texlive_version}
Recommends:     texlive-asapsym-doc >= %{texlive_version}
Provides:       tex(asapsym-generic.tex)
Provides:       tex(asapsym.code.tex)
Provides:       tex(asapsym.sty)
Requires:       tex(fontspec.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source20:       asapsym.tar.xz
Source21:       asapsym.doc.tar.xz

%description -n texlive-asapsym
The package provides macros (usable with LaTeX or Plain TeX)
for using the freely available ASAP Symbol font, which is also
included. The font is distributed in OpenType format, and makes
extensive use of OpenType features. Therefore, at this time,
only XeTeX and LuaTeX are supported. An error message is issued
if an OTF-capable engine is not detected.

%package -n texlive-asapsym-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn40201
Release:        0
Summary:        Documentation for texlive-asapsym
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-asapsym-doc
This package includes the documentation for texlive-asapsym


%package -n texlive-asapsym-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn40201
Release:        0
Summary:        Severed fonts for texlive-asapsym
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-asapsym-fonts
The  separated fonts package for texlive-asapsym
%post -n texlive-asapsym
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asapsym 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asapsym
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-asapsym-fonts
%files -n texlive-asapsym-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/asapsym/README.md
%{_texmfdistdir}/doc/fonts/asapsym/asapsym.pdf

%files -n texlive-asapsym
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/opentype/omnibus-type/asapsym/Asap-Symbol.otf
%{_texmfdistdir}/tex/generic/asapsym/asapsym-generic.tex
%{_texmfdistdir}/tex/latex/asapsym/asapsym.sty
%{_texmfdistdir}/tex/plain/asapsym/asapsym.code.tex

%files -n texlive-asapsym-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-asapsym
%{_datadir}/fontconfig/conf.avail/58-texlive-asapsym.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-asapsym/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-asapsym/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-asapsym/fonts.scale
%{_datadir}/fonts/texlive-asapsym/Asap-Symbol.otf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asapsym-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn40201-%{release}-zypper
%endif

%package -n texlive-ascelike
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn29129
Release:        0
Summary:        Bibliography style for the ASCE
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-ascelike-doc >= %{texlive_version}
Provides:       tex(ascelike.cls)
Requires:       tex(article.cls)
Requires:       tex(endfloat.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(lineno.sty)
Requires:       tex(setspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source22:       ascelike.tar.xz
Source23:       ascelike.doc.tar.xz

%description -n texlive-ascelike
A document class and bibliographic style that prepares
documents in the style required by the American Society of
Civil Engineers (ASCE). These are unofficial files, not
sanctioned by that organization, and the files specifically
give this caveat. Also included is a short
documentation/example of how to use the class.

%package -n texlive-ascelike-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3svn29129
Release:        0
Summary:        Documentation for texlive-ascelike
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ascelike-doc
This package includes the documentation for texlive-ascelike

%post -n texlive-ascelike
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ascelike 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ascelike
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ascelike-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ascelike/README
%{_texmfdistdir}/doc/latex/ascelike/ascexmpl.bib
%{_texmfdistdir}/doc/latex/ascelike/ascexmpl.pdf
%{_texmfdistdir}/doc/latex/ascelike/ascexmpl.tex

%files -n texlive-ascelike
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/ascelike/ascelike.bst
%{_texmfdistdir}/tex/latex/ascelike/ascelike.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ascelike-%{texlive_version}.%{texlive_noarch}.2.3svn29129-%{release}-zypper
%endif

%package -n texlive-ascii-chart
Version:        %{texlive_version}.%{texlive_noarch}.svn20536
Release:        0
Summary:        An ASCII wall chart
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source24:       ascii-chart.doc.tar.xz

%description -n texlive-ascii-chart
The document may be converted between Plain TeX and LaTeX
(2.09) by a simple editing action.
%post -n texlive-ascii-chart
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-ascii-chart 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-ascii-chart
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-ascii-chart
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/ascii-chart/ascii.pdf
%{_texmfdistdir}/doc/support/ascii-chart/ascii.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ascii-chart-%{texlive_version}.%{texlive_noarch}.svn20536-%{release}-zypper
%endif

%package -n texlive-ascii-font
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn29989
Release:        0
Summary:        Use the ASCII "font" in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Obsoletes:      texlive-ascii <= 2012
Provides:       texlive-ascii = %{texlive_version}
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-ascii-font-fonts >= %{texlive_version}
Recommends:     texlive-ascii-font-doc >= %{texlive_version}
Provides:       tex(ASCII.tfm)
Provides:       tex(ascii.map)
Provides:       tex(ascii.sty)
Requires:       tex(xspace.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source25:       ascii-font.tar.xz
Source26:       ascii-font.doc.tar.xz

%description -n texlive-ascii-font
The package provides glyph and font access commands so that
LaTeX users can use the ASCII glyphs in their documents. The
ASCII font is encoded according to the IBM PC Code Page 437 C0
Graphics. This package replaces any early LaTeX 2.09 package
and "font" by R. Ramasubramanian and R.W.D. Nickalls.

%package -n texlive-ascii-font-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn29989
Release:        0
Summary:        Documentation for texlive-ascii-font
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-ascii-font-doc
This package includes the documentation for texlive-ascii-font


%package -n texlive-ascii-font-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn29989
Release:        0
Summary:        Severed fonts for texlive-ascii-font
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-ascii-font-fonts
The  separated fonts package for texlive-ascii-font
%post -n texlive-ascii-font
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap ascii.map' >> /var/run/texlive/run-updmap

%postun -n texlive-ascii-font 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap ascii.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-ascii-font
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-ascii-font-fonts
%files -n texlive-ascii-font-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/ascii-font/README.TEXLIVE

%files -n texlive-ascii-font
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/ascii-font/ascii.map
%{_texmfdistdir}/fonts/tfm/public/ascii-font/ASCII.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/ascii-font/ASCII.pfb
%{_texmfdistdir}/tex/latex/ascii-font/ascii.sty

%files -n texlive-ascii-font-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-ascii-font
%{_datadir}/fontconfig/conf.avail/58-texlive-ascii-font.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ascii-font/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ascii-font/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ascii-font/fonts.scale
%{_datadir}/fonts/texlive-ascii-font/ASCII.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ascii-font-fonts-%{texlive_version}.%{texlive_noarch}.2.0svn29989-%{release}-zypper
%endif

%package -n texlive-asciilist
Version:        %{texlive_version}.%{texlive_noarch}.2.2bsvn49060
Release:        0
Summary:        Environments AsciiList and AsciiDocList for prototyping nested lists in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-asciilist-doc >= %{texlive_version}
Provides:       tex(asciilist.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(trimspaces.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source27:       asciilist.tar.xz
Source28:       asciilist.doc.tar.xz

%description -n texlive-asciilist
The asciilist provides the environments AsciiList and
AsciiDocList, which enable quickly typesetting nested lists in
LaTeX without having to type individual item macros or
opening/closing list environments. The package provides
auxiliary functionality for loading such lists from files and
provides macros for configuring the use of the list
environments and the appearance of the typeset results.

%package -n texlive-asciilist-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2bsvn49060
Release:        0
Summary:        Documentation for texlive-asciilist
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-asciilist-doc
This package includes the documentation for texlive-asciilist

%post -n texlive-asciilist
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asciilist 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asciilist
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asciilist-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/asciilist/AsciiDocList.example
%{_texmfdistdir}/doc/latex/asciilist/AsciiList.example
%{_texmfdistdir}/doc/latex/asciilist/README.md
%{_texmfdistdir}/doc/latex/asciilist/asciilist.pdf

%files -n texlive-asciilist
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/asciilist/asciilist.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asciilist-%{texlive_version}.%{texlive_noarch}.2.2bsvn49060-%{release}-zypper
%endif

%package -n texlive-ascmac
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn53411
Release:        0
Summary:        Boxes and picture macros with Japanese vertical writing support
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-ascmac-fonts >= %{texlive_version}
Recommends:     texlive-ascmac-doc >= %{texlive_version}
Provides:       tex(ascgrp.tfm)
Provides:       tex(ascii10.tfm)
Provides:       tex(ascii36.tfm)
Provides:       tex(ascmac.map)
Provides:       tex(ascmac.sty)
Provides:       tex(tascmac.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source29:       ascmac.tar.xz
Source30:       ascmac.doc.tar.xz

%description -n texlive-ascmac
The bundle provides boxes and picture macros with Japanese
vertical writing support. It uses only native picture macros
and fonts for drawing boxes and is thus driver-independent.
Formerly part of the Japanese pLaTeX bundle, it now supports
all LaTeX engines.

%package -n texlive-ascmac-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn53411
Release:        0
Summary:        Documentation for texlive-ascmac
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-ascmac-doc:ja)

%description -n texlive-ascmac-doc
This package includes the documentation for texlive-ascmac


%package -n texlive-ascmac-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn53411
Release:        0
Summary:        Severed fonts for texlive-ascmac
License:        BSD-3-Clause
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-ascmac-fonts
The  separated fonts package for texlive-ascmac
%post -n texlive-ascmac
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap ascmac.map' >> /var/run/texlive/run-updmap

%postun -n texlive-ascmac 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap ascmac.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-ascmac
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-ascmac-fonts
%files -n texlive-ascmac-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/ascmac/LICENSE
%{_texmfdistdir}/doc/latex/ascmac/README.md
%{_texmfdistdir}/doc/latex/ascmac/ascmac.pdf

%files -n texlive-ascmac
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/ascmac/ascmac.map
%{_texmfdistdir}/fonts/source/public/ascmac/ascgrp.mf
%{_texmfdistdir}/fonts/source/public/ascmac/ascii.mf
%{_texmfdistdir}/fonts/source/public/ascmac/ascii10.mf
%{_texmfdistdir}/fonts/source/public/ascmac/ascii36.mf
%{_texmfdistdir}/fonts/tfm/public/ascmac/ascgrp.tfm
%{_texmfdistdir}/fonts/tfm/public/ascmac/ascii10.tfm
%{_texmfdistdir}/fonts/tfm/public/ascmac/ascii36.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/ascmac/ascgrp.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/ascmac/ascii10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/ascmac/ascii36.pfb
%{_texmfdistdir}/tex/latex/ascmac/ascmac.sty
%{_texmfdistdir}/tex/latex/ascmac/tascmac.sty

%files -n texlive-ascmac-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-ascmac
%{_datadir}/fontconfig/conf.avail/58-texlive-ascmac.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ascmac/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ascmac/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-ascmac/fonts.scale
%{_datadir}/fonts/texlive-ascmac/ascgrp.pfb
%{_datadir}/fonts/texlive-ascmac/ascii10.pfb
%{_datadir}/fonts/texlive-ascmac/ascii36.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-ascmac-fonts-%{texlive_version}.%{texlive_noarch}.2.1svn53411-%{release}-zypper
%endif

%package -n texlive-askinclude
Version:        %{texlive_version}.%{texlive_noarch}.2.7svn54725
Release:        0
Summary:        Interactive use of \includeonly
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-askinclude-doc >= %{texlive_version}
Provides:       tex(askinclude.sty)
Requires:       tex(kvsetkeys.sty)
Requires:       tex(makematch.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source31:       askinclude.tar.xz
Source32:       askinclude.doc.tar.xz

%description -n texlive-askinclude
The package asks the user which files to put in a \includeonly
command. There is provision for answering "same as last time"
or "all files".

%package -n texlive-askinclude-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.7svn54725
Release:        0
Summary:        Documentation for texlive-askinclude
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-askinclude-doc
This package includes the documentation for texlive-askinclude

%post -n texlive-askinclude
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-askinclude 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-askinclude
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-askinclude-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/askinclude/README.md
%{_texmfdistdir}/doc/latex/askinclude/askinclude.bib
%{_texmfdistdir}/doc/latex/askinclude/askinclude.pdf

%files -n texlive-askinclude
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/askinclude/askinclude.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-askinclude-%{texlive_version}.%{texlive_noarch}.2.7svn54725-%{release}-zypper
%endif

%package -n texlive-askmaps
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn32320
Release:        0
Summary:        Typeset American style Karnaugh maps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-askmaps-doc >= %{texlive_version}
Provides:       tex(askmaps.sty)
Requires:       tex(pict2e.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source33:       askmaps.tar.xz
Source34:       askmaps.doc.tar.xz

%description -n texlive-askmaps
The package provides 2, 3, 4 and 5 variable Karnaugh maps, in
the style used in numerous textbooks on digital design. The
package draws K-maps where the most significant input variables
are placed on top of the columns and the least significant
variables are placed left of the rows.

%package -n texlive-askmaps-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn32320
Release:        0
Summary:        Documentation for texlive-askmaps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-askmaps-doc
This package includes the documentation for texlive-askmaps

%post -n texlive-askmaps
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-askmaps 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-askmaps
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-askmaps-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/askmaps/README
%{_texmfdistdir}/doc/latex/askmaps/askmaps.pdf
%{_texmfdistdir}/doc/latex/askmaps/askmaps.tex

%files -n texlive-askmaps
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/askmaps/askmaps.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-askmaps-%{texlive_version}.%{texlive_noarch}.0.0.1svn32320-%{release}-zypper
%endif

%package -n texlive-asmeconf
Version:        %{texlive_version}.%{texlive_noarch}.1.18svn54758
Release:        0
Summary:        A template for ASME conference papers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-asmeconf-doc >= %{texlive_version}
Provides:       tex(asmeconf.cls)
Requires:       tex(array.sty)
Requires:       tex(article.cls)
Requires:       tex(babel.sty)
Requires:       tex(bm.sty)
Requires:       tex(bookmark.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(doi.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(flushend.sty)
Requires:       tex(fnpos.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inconsolata.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(lineno.sty)
Requires:       tex(mathalfa.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(natbib.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(textcase.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(xcoffins.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source35:       asmeconf.tar.xz
Source36:       asmeconf.doc.tar.xz

%description -n texlive-asmeconf
This class provides a template to format ASME Conference papers
according to the requirements on ASME's web pages (as posted in
early 2020). The .tex and .cls files are commented and should
be self-explanatory. The package depends on newtx. This work is
not a publication of ASME itself.

%package -n texlive-asmeconf-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.18svn54758
Release:        0
Summary:        Documentation for texlive-asmeconf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-asmeconf-doc
This package includes the documentation for texlive-asmeconf

%post -n texlive-asmeconf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asmeconf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asmeconf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asmeconf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/asmeconf/README.md
%{_texmfdistdir}/doc/latex/asmeconf/asmeconf-sample.bib
%{_texmfdistdir}/doc/latex/asmeconf/asmeconf-template.pdf
%{_texmfdistdir}/doc/latex/asmeconf/asmeconf-template.tex
%{_texmfdistdir}/doc/latex/asmeconf/sample-figure-1.pdf
%{_texmfdistdir}/doc/latex/asmeconf/sample-figure-2a.pdf
%{_texmfdistdir}/doc/latex/asmeconf/sample-figure-2b.pdf

%files -n texlive-asmeconf
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/asmeconf/asmeconf.bst
%{_texmfdistdir}/tex/latex/asmeconf/asmeconf.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asmeconf-%{texlive_version}.%{texlive_noarch}.1.18svn54758-%{release}-zypper
%endif

%package -n texlive-asmejour
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn54758
Release:        0
Summary:        A template for ASME journal papers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-asmejour-doc >= %{texlive_version}
Provides:       tex(asmejour.cls)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(bm.sty)
Requires:       tex(booktabs.sty)
Requires:       tex(caption.sty)
Requires:       tex(dcolumn.sty)
Requires:       tex(doi.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(extarticle.cls)
Requires:       tex(fancyhdr.sty)
Requires:       tex(flushend.sty)
Requires:       tex(fnpos.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hologo.sty)
Requires:       tex(hyperxmp.sty)
Requires:       tex(iftex.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(inconsolata.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(lineno.sty)
Requires:       tex(mathalfa.sty)
Requires:       tex(mathtools.sty)
Requires:       tex(metalogo.sty)
Requires:       tex(natbib.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(subcaption.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(totcount.sty)
Requires:       tex(xcoffins.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source37:       asmejour.tar.xz
Source38:       asmejour.doc.tar.xz

%description -n texlive-asmejour
This package provides a LaTeX class, a BibTeX style, and a
LaTeX template to format journal papers for submission to the
American Society of Mechanical Engineers (ASME). The .tex and
.cls files are commented and should be self-explanatory. The
package depends on newtx. This work is not a publication of
ASME itself.

%package -n texlive-asmejour-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.12svn54758
Release:        0
Summary:        Documentation for texlive-asmejour
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-asmejour-doc
This package includes the documentation for texlive-asmejour

%post -n texlive-asmejour
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asmejour 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asmejour
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asmejour-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/asmejour/README.md
%{_texmfdistdir}/doc/latex/asmejour/asmejour-sample.bib
%{_texmfdistdir}/doc/latex/asmejour/asmejour-template.pdf
%{_texmfdistdir}/doc/latex/asmejour/asmejour-template.tex
%{_texmfdistdir}/doc/latex/asmejour/sample-figure-1.pdf
%{_texmfdistdir}/doc/latex/asmejour/sample-figure-2a.pdf
%{_texmfdistdir}/doc/latex/asmejour/sample-figure-2b.pdf

%files -n texlive-asmejour
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/asmejour/asmejour.bst
%{_texmfdistdir}/tex/latex/asmejour/asmejour.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asmejour-%{texlive_version}.%{texlive_noarch}.1.12svn54758-%{release}-zypper
%endif

%package -n texlive-aspectratio
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn25243
Release:        0
Summary:        Capital A and capital R ligature for Aspect Ratio
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-aspectratio-fonts >= %{texlive_version}
Recommends:     texlive-aspectratio-doc >= %{texlive_version}
Provides:       tex(amarbi.tfm)
Provides:       tex(amarri.tfm)
Provides:       tex(aparbi.tfm)
Provides:       tex(aparri.tfm)
Provides:       tex(ar.sty)
Provides:       tex(ar10.tfm)
Provides:       tex(ar12.tfm)
Provides:       tex(ar5.tfm)
Provides:       tex(ar6.tfm)
Provides:       tex(ar7.tfm)
Provides:       tex(ar8.tfm)
Provides:       tex(ar9.tfm)
Provides:       tex(arb10.tfm)
Provides:       tex(arb12.tfm)
Provides:       tex(arb5.tfm)
Provides:       tex(arb6.tfm)
Provides:       tex(arb7.tfm)
Provides:       tex(arb8.tfm)
Provides:       tex(arb9.tfm)
Provides:       tex(arssbi10.tfm)
Provides:       tex(arssi10.tfm)
Provides:       tex(artti10.tfm)
Provides:       tex(aspectratio.map)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source39:       aspectratio.tar.xz
Source40:       aspectratio.doc.tar.xz

%description -n texlive-aspectratio
The package provides fonts (both as Adobe Type 1 format, and as
Metafont source) for the 'AR' symbol (for Aspect Ratio) used by
aeronautical scientists and engineers. Note that the package
supersedes the package ar

%package -n texlive-aspectratio-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn25243
Release:        0
Summary:        Documentation for texlive-aspectratio
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-aspectratio-doc
This package includes the documentation for texlive-aspectratio


%package -n texlive-aspectratio-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn25243
Release:        0
Summary:        Severed fonts for texlive-aspectratio
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-aspectratio-fonts
The  separated fonts package for texlive-aspectratio
%post -n texlive-aspectratio
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap aspectratio.map' >> /var/run/texlive/run-updmap

%postun -n texlive-aspectratio 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap aspectratio.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-aspectratio
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-aspectratio-fonts
%files -n texlive-aspectratio-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/aspectratio/ar.pdf
%{_texmfdistdir}/doc/latex/aspectratio/ar.tex

%files -n texlive-aspectratio
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/map/dvips/aspectratio/aspectratio.map
%{_texmfdistdir}/fonts/source/public/aspectratio/ar10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar12.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar6.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar7.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar8.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/ar9.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb12.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb5.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb6.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb7.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb8.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arb9.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arssbi10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/arssi10.mf
%{_texmfdistdir}/fonts/source/public/aspectratio/artti10.mf
%{_texmfdistdir}/fonts/tfm/public/aspectratio/amarbi.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/amarri.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/aparbi.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/aparri.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar12.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar5.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar6.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar7.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar8.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/ar9.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb12.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb5.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb6.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb7.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb8.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arb9.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arssbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/arssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/aspectratio/artti10.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/amarbi.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/amarri.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/ar10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/ar12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/ar5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/ar6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/ar7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/ar8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/ar9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arb10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arb12.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arb5.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arb6.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arb7.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arb8.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arb9.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arssbi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/arssi10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aspectratio/artti10.pfb
%{_texmfdistdir}/tex/latex/aspectratio/ar.sty

%files -n texlive-aspectratio-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-aspectratio
%{_datadir}/fontconfig/conf.avail/58-texlive-aspectratio.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-aspectratio/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-aspectratio/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-aspectratio/fonts.scale
%{_datadir}/fonts/texlive-aspectratio/amarbi.pfb
%{_datadir}/fonts/texlive-aspectratio/amarri.pfb
%{_datadir}/fonts/texlive-aspectratio/ar10.pfb
%{_datadir}/fonts/texlive-aspectratio/ar12.pfb
%{_datadir}/fonts/texlive-aspectratio/ar5.pfb
%{_datadir}/fonts/texlive-aspectratio/ar6.pfb
%{_datadir}/fonts/texlive-aspectratio/ar7.pfb
%{_datadir}/fonts/texlive-aspectratio/ar8.pfb
%{_datadir}/fonts/texlive-aspectratio/ar9.pfb
%{_datadir}/fonts/texlive-aspectratio/arb10.pfb
%{_datadir}/fonts/texlive-aspectratio/arb12.pfb
%{_datadir}/fonts/texlive-aspectratio/arb5.pfb
%{_datadir}/fonts/texlive-aspectratio/arb6.pfb
%{_datadir}/fonts/texlive-aspectratio/arb7.pfb
%{_datadir}/fonts/texlive-aspectratio/arb8.pfb
%{_datadir}/fonts/texlive-aspectratio/arb9.pfb
%{_datadir}/fonts/texlive-aspectratio/arssbi10.pfb
%{_datadir}/fonts/texlive-aspectratio/arssi10.pfb
%{_datadir}/fonts/texlive-aspectratio/artti10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-aspectratio-fonts-%{texlive_version}.%{texlive_noarch}.2.0svn25243-%{release}-zypper
%endif

%package -n texlive-assignment
Version:        %{texlive_version}.%{texlive_noarch}.svn20431
Release:        0
Summary:        A class file for typesetting homework and lab assignments
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-assignment-doc >= %{texlive_version}
Provides:       tex(assignment.cls)
Requires:       tex(article.cls)
Requires:       tex(ifthen.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source41:       assignment.tar.xz
Source42:       assignment.doc.tar.xz

%description -n texlive-assignment
A class file for typesetting homework and lab assignments.

%package -n texlive-assignment-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20431
Release:        0
Summary:        Documentation for texlive-assignment
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-assignment-doc
This package includes the documentation for texlive-assignment

%post -n texlive-assignment
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-assignment 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-assignment
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-assignment-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/assignment/Changelog
%{_texmfdistdir}/doc/latex/assignment/LICENSE
%{_texmfdistdir}/doc/latex/assignment/README
%{_texmfdistdir}/doc/latex/assignment/assignment.pdf
%{_texmfdistdir}/doc/latex/assignment/assignment.tex

%files -n texlive-assignment
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/assignment/assignment.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-assignment-%{texlive_version}.%{texlive_noarch}.svn20431-%{release}-zypper
%endif

%package -n texlive-assoccnt
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn38497
Release:        0
Summary:        Associate counters, making them step when a master steps
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-assoccnt-doc >= %{texlive_version}
Provides:       tex(assoccnt.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source43:       assoccnt.tar.xz
Source44:       assoccnt.doc.tar.xz

%description -n texlive-assoccnt
The package provides the means of declaring a set of counters
to be stepped, each time some 'master' counter is stepped.

%package -n texlive-assoccnt-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.8svn38497
Release:        0
Summary:        Documentation for texlive-assoccnt
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-assoccnt-doc
This package includes the documentation for texlive-assoccnt

%post -n texlive-assoccnt
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-assoccnt 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-assoccnt
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-assoccnt-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/assoccnt/README
%{_texmfdistdir}/doc/latex/assoccnt/assoccnt_doc.pdf
%{_texmfdistdir}/doc/latex/assoccnt/assoccnt_doc.tex
%{_texmfdistdir}/doc/latex/assoccnt/assoccnt_example.pdf
%{_texmfdistdir}/doc/latex/assoccnt/assoccnt_example.tex

%files -n texlive-assoccnt
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/assoccnt/assoccnt.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-assoccnt-%{texlive_version}.%{texlive_noarch}.0.0.8svn38497-%{release}-zypper
%endif

%package -n texlive-astro
Version:        %{texlive_version}.%{texlive_noarch}.2.20svn15878
Release:        0
Summary:        Astronomical (planetary) symbols
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-astro-doc >= %{texlive_version}
Provides:       tex(astrosym.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source45:       astro.tar.xz
Source46:       astro.doc.tar.xz

%description -n texlive-astro
Astrosym is a font containing astronomical symbols, including
those used for the planets, four planetoids, the phases of the
moon, the signs of the zodiac, and some additional symbols. The
font is distributed as Metafont source.

%package -n texlive-astro-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.20svn15878
Release:        0
Summary:        Documentation for texlive-astro
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-astro-doc
This package includes the documentation for texlive-astro

%post -n texlive-astro
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-astro 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-astro
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-astro-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/astro/astrosym.tex
%{_texmfdistdir}/doc/fonts/astro/astrosym.txt

%files -n texlive-astro
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/astro/astrosym.cal
%{_texmfdistdir}/fonts/source/public/astro/astrosym.cmn
%{_texmfdistdir}/fonts/source/public/astro/astrosym.mac
%{_texmfdistdir}/fonts/source/public/astro/astrosym.mf
%{_texmfdistdir}/fonts/source/public/astro/astrosym.uni
%{_texmfdistdir}/fonts/source/public/astro/astrosym.xtr
%{_texmfdistdir}/fonts/tfm/public/astro/astrosym.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-astro-%{texlive_version}.%{texlive_noarch}.2.20svn15878-%{release}-zypper
%endif

%package -n texlive-asyfig
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn17512
Release:        0
Summary:        Commands for using Asymptote figures
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-asyfig-doc >= %{texlive_version}
Provides:       tex(asyalign.sty)
Provides:       tex(asyfig.sty)
Provides:       tex(asyprocess.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifmtarg.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(preview.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source47:       asyfig.tar.xz
Source48:       asyfig.doc.tar.xz

%description -n texlive-asyfig
The package provides a means of reading Asymptote figures from
separate files, rather than within the document, as is standard
in the asymptote package, which is provided as part of the
Asymptote bundle. The asymptote way can prove cumbersome in a
large document; the present package allows the user to process
one picture at a time, in simple test documents, and then to
migrate (with no fuss) to their use in the target document.

%package -n texlive-asyfig-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1csvn17512
Release:        0
Summary:        Documentation for texlive-asyfig
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-asyfig-doc
This package includes the documentation for texlive-asyfig

%post -n texlive-asyfig
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asyfig 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asyfig
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asyfig-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/asyfig/README
%{_texmfdistdir}/doc/latex/asyfig/asyfig.pdf
%{_texmfdistdir}/doc/latex/asyfig/example/frf.asy
%{_texmfdistdir}/doc/latex/asyfig/example/test-asyfig.tex

%files -n texlive-asyfig
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/asyfig/asyalign.sty
%{_texmfdistdir}/tex/latex/asyfig/asyfig.sty
%{_texmfdistdir}/tex/latex/asyfig/asyprocess.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asyfig-%{texlive_version}.%{texlive_noarch}.0.0.1csvn17512-%{release}-zypper
%endif

%package -n texlive-asymptote
Version:        %{texlive_version}.%{texlive_noarch}.2.65svn54567
Release:        0
Summary:        2D and 3D TeX-Aware Vector Graphics Language
License:        LGPL-3.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-asymptote-bin >= %{texlive_version}
#!BuildIgnore: texlive-asymptote-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-asymptote-doc >= %{texlive_version}
Requires:       python3-tk
Requires:       texlive-media9 >= %{texlive_version}
Requires:       texlive-movie15 >= %{texlive_version}
Provides:       tex(asycolors.sty)
Provides:       tex(asymptote.sty)
Provides:       tex(colo-asy.tex)
Provides:       tex(ocg.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(color.sty)
Requires:       tex(everypage.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source49:       asymptote.tar.xz
Source50:       asymptote.doc.tar.xz

%description -n texlive-asymptote
Asymptote is a powerful descriptive vector graphics language
for technical drawing, inspired by MetaPost but with an
improved C++-like syntax. Asymptote provides for figures the
same high-quality level of typesetting that LaTeX does for
scientific text.

%package -n texlive-asymptote-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.65svn54567
Release:        0
Summary:        Documentation for texlive-asymptote
License:        LGPL-3.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(asy.1)
Provides:       man(xasy.1)
Requires(preun): %install_info_prereq
Requires(post): %install_info_prereq

%description -n texlive-asymptote-doc
This package includes the documentation for texlive-asymptote

%post -n texlive-asymptote
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asymptote 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asymptote
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%preun -n texlive-asymptote-doc
if test $1 = 0; then
    %install_info_delete --info-dir=%{_infodir} %{_infodir}/asy-faq.info
    %install_info_delete --info-dir=%{_infodir} %{_infodir}/asymptote.info
fi

%post -n texlive-asymptote-doc
%install_info --info-dir=%{_infodir} %{_infodir}/asy-faq.info
%install_info --info-dir=%{_infodir} %{_infodir}/asymptote.info
%files -n texlive-asymptote-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/asymptote/CAD.pdf
%{_texmfdistdir}/doc/asymptote/TeXShopAndAsymptote.pdf
%{_texmfdistdir}/doc/asymptote/asy-latex.pdf
%{_texmfdistdir}/doc/asymptote/asyRefCard.pdf
%{_texmfdistdir}/doc/asymptote/asymptote.pdf
%{_texmfdistdir}/doc/asymptote/examples/100d.views
%{_texmfdistdir}/doc/asymptote/examples/1overx.asy
%{_texmfdistdir}/doc/asymptote/examples/BezierPatch.asy
%{_texmfdistdir}/doc/asymptote/examples/BezierSaddle.asy
%{_texmfdistdir}/doc/asymptote/examples/BezierSurface.asy
%{_texmfdistdir}/doc/asymptote/examples/BezierTriangle.asy
%{_texmfdistdir}/doc/asymptote/examples/Bode.asy
%{_texmfdistdir}/doc/asymptote/examples/CAD1.asy
%{_texmfdistdir}/doc/asymptote/examples/CDlabel.asy
%{_texmfdistdir}/doc/asymptote/examples/Coons.asy
%{_texmfdistdir}/doc/asymptote/examples/GaussianSurface.asy
%{_texmfdistdir}/doc/asymptote/examples/Gouraud.asy
%{_texmfdistdir}/doc/asymptote/examples/Gouraudcontour.asy
%{_texmfdistdir}/doc/asymptote/examples/HermiteSpline.asy
%{_texmfdistdir}/doc/asymptote/examples/Hobbycontrol.asy
%{_texmfdistdir}/doc/asymptote/examples/Hobbydir.asy
%{_texmfdistdir}/doc/asymptote/examples/Klein.asy
%{_texmfdistdir}/doc/asymptote/examples/NURBScurve.asy
%{_texmfdistdir}/doc/asymptote/examples/NURBSsphere.asy
%{_texmfdistdir}/doc/asymptote/examples/NURBSsurface.asy
%{_texmfdistdir}/doc/asymptote/examples/Pythagoras.asy
%{_texmfdistdir}/doc/asymptote/examples/PythagoreanTree.asy
%{_texmfdistdir}/doc/asymptote/examples/RiemannSphere.asy
%{_texmfdistdir}/doc/asymptote/examples/RiemannSurface.asy
%{_texmfdistdir}/doc/asymptote/examples/RiemannSurfaceRoot.asy
%{_texmfdistdir}/doc/asymptote/examples/Sierpinski.asy
%{_texmfdistdir}/doc/asymptote/examples/SierpinskiGasket.asy
%{_texmfdistdir}/doc/asymptote/examples/SierpinskiSponge.asy
%{_texmfdistdir}/doc/asymptote/examples/advection.asy
%{_texmfdistdir}/doc/asymptote/examples/alignbox.asy
%{_texmfdistdir}/doc/asymptote/examples/alignedaxis.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/cube.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/earthmoon.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/embeddedmovie.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/embeddedu3d.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/externalmovie.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/glmovie.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/heatequation.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/inlinemovie.tex
%{_texmfdistdir}/doc/asymptote/examples/animations/inlinemovie3.tex
%{_texmfdistdir}/doc/asymptote/examples/animations/pdfmovie.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/slidemovies.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/sphere.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/torusanimation.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/wavepacket.asy
%{_texmfdistdir}/doc/asymptote/examples/animations/wheel.asy
%{_texmfdistdir}/doc/asymptote/examples/annotation.asy
%{_texmfdistdir}/doc/asymptote/examples/arrows3.asy
%{_texmfdistdir}/doc/asymptote/examples/axis3.asy
%{_texmfdistdir}/doc/asymptote/examples/bars3.asy
%{_texmfdistdir}/doc/asymptote/examples/basealign.asy
%{_texmfdistdir}/doc/asymptote/examples/bezier.asy
%{_texmfdistdir}/doc/asymptote/examples/bezier2.asy
%{_texmfdistdir}/doc/asymptote/examples/beziercurve.asy
%{_texmfdistdir}/doc/asymptote/examples/bigdiagonal.asy
%{_texmfdistdir}/doc/asymptote/examples/billboard.asy
%{_texmfdistdir}/doc/asymptote/examples/binarytreetest.asy
%{_texmfdistdir}/doc/asymptote/examples/brokenaxis.asy
%{_texmfdistdir}/doc/asymptote/examples/buildcycle.asy
%{_texmfdistdir}/doc/asymptote/examples/cardioid.asy
%{_texmfdistdir}/doc/asymptote/examples/cards.asy
%{_texmfdistdir}/doc/asymptote/examples/centroidfg.asy
%{_texmfdistdir}/doc/asymptote/examples/cheese.asy
%{_texmfdistdir}/doc/asymptote/examples/circles.asy
%{_texmfdistdir}/doc/asymptote/examples/circumcircle.asy
%{_texmfdistdir}/doc/asymptote/examples/clockarray.asy
%{_texmfdistdir}/doc/asymptote/examples/coag.asy
%{_texmfdistdir}/doc/asymptote/examples/colons.asy
%{_texmfdistdir}/doc/asymptote/examples/colorpatch.asy
%{_texmfdistdir}/doc/asymptote/examples/colorplanes.asy
%{_texmfdistdir}/doc/asymptote/examples/colors.asy
%{_texmfdistdir}/doc/asymptote/examples/condor.asy
%{_texmfdistdir}/doc/asymptote/examples/cones.asy
%{_texmfdistdir}/doc/asymptote/examples/conicurv.asy
%{_texmfdistdir}/doc/asymptote/examples/contextfonts.asy
%{_texmfdistdir}/doc/asymptote/examples/controlsystem.asy
%{_texmfdistdir}/doc/asymptote/examples/cos2theta.asy
%{_texmfdistdir}/doc/asymptote/examples/cos3.asy
%{_texmfdistdir}/doc/asymptote/examples/cosaddition.asy
%{_texmfdistdir}/doc/asymptote/examples/cpkcolors.asy
%{_texmfdistdir}/doc/asymptote/examples/cube.asy
%{_texmfdistdir}/doc/asymptote/examples/curvedlabel.asy
%{_texmfdistdir}/doc/asymptote/examples/curvedlabel3.asy
%{_texmfdistdir}/doc/asymptote/examples/cyclohexane.asy
%{_texmfdistdir}/doc/asymptote/examples/cylinder.asy
%{_texmfdistdir}/doc/asymptote/examples/cylinderskeleton.asy
%{_texmfdistdir}/doc/asymptote/examples/datagraph.asy
%{_texmfdistdir}/doc/asymptote/examples/delu.asy
%{_texmfdistdir}/doc/asymptote/examples/diagonal.asy
%{_texmfdistdir}/doc/asymptote/examples/diatom.asy
%{_texmfdistdir}/doc/asymptote/examples/diatom.csv
%{_texmfdistdir}/doc/asymptote/examples/dimension.asy
%{_texmfdistdir}/doc/asymptote/examples/dots.asy
%{_texmfdistdir}/doc/asymptote/examples/dragon.asy
%{_texmfdistdir}/doc/asymptote/examples/eetomumu.asy
%{_texmfdistdir}/doc/asymptote/examples/electromagnetic.asy
%{_texmfdistdir}/doc/asymptote/examples/elevation.asy
%{_texmfdistdir}/doc/asymptote/examples/elliptic.asy
%{_texmfdistdir}/doc/asymptote/examples/epix.asy
%{_texmfdistdir}/doc/asymptote/examples/equilateral.asy
%{_texmfdistdir}/doc/asymptote/examples/equilchord.asy
%{_texmfdistdir}/doc/asymptote/examples/errorbars.asy
%{_texmfdistdir}/doc/asymptote/examples/exp.asy
%{_texmfdistdir}/doc/asymptote/examples/exp3.asy
%{_texmfdistdir}/doc/asymptote/examples/externalprc.tex
%{_texmfdistdir}/doc/asymptote/examples/extrudedcontour.asy
%{_texmfdistdir}/doc/asymptote/examples/fano.asy
%{_texmfdistdir}/doc/asymptote/examples/fequlogo.asy
%{_texmfdistdir}/doc/asymptote/examples/fermi.asy
%{_texmfdistdir}/doc/asymptote/examples/filegraph.asy
%{_texmfdistdir}/doc/asymptote/examples/filegraph.dat
%{_texmfdistdir}/doc/asymptote/examples/filesurface.asy
%{_texmfdistdir}/doc/asymptote/examples/filesurface.dat
%{_texmfdistdir}/doc/asymptote/examples/fillcontour.asy
%{_texmfdistdir}/doc/asymptote/examples/fin.asy
%{_texmfdistdir}/doc/asymptote/examples/fjortoft.asy
%{_texmfdistdir}/doc/asymptote/examples/floatingdisk.asy
%{_texmfdistdir}/doc/asymptote/examples/floor.asy
%{_texmfdistdir}/doc/asymptote/examples/flow.asy
%{_texmfdistdir}/doc/asymptote/examples/flowchartdemo.asy
%{_texmfdistdir}/doc/asymptote/examples/fractaltree.asy
%{_texmfdistdir}/doc/asymptote/examples/functionshading.asy
%{_texmfdistdir}/doc/asymptote/examples/galleon.asy
%{_texmfdistdir}/doc/asymptote/examples/gamma.asy
%{_texmfdistdir}/doc/asymptote/examples/gamma3.asy
%{_texmfdistdir}/doc/asymptote/examples/generalaxis.asy
%{_texmfdistdir}/doc/asymptote/examples/generalaxis3.asy
%{_texmfdistdir}/doc/asymptote/examples/genusthree.asy
%{_texmfdistdir}/doc/asymptote/examples/genustwo.asy
%{_texmfdistdir}/doc/asymptote/examples/graphmarkers.asy
%{_texmfdistdir}/doc/asymptote/examples/grid.asy
%{_texmfdistdir}/doc/asymptote/examples/grid3xyz.asy
%{_texmfdistdir}/doc/asymptote/examples/hatch.asy
%{_texmfdistdir}/doc/asymptote/examples/helix.asy
%{_texmfdistdir}/doc/asymptote/examples/hierarchy.asy
%{_texmfdistdir}/doc/asymptote/examples/histogram.asy
%{_texmfdistdir}/doc/asymptote/examples/hyperboloid.asy
%{_texmfdistdir}/doc/asymptote/examples/hyperboloidsilhouette.asy
%{_texmfdistdir}/doc/asymptote/examples/icon.asy
%{_texmfdistdir}/doc/asymptote/examples/image.asy
%{_texmfdistdir}/doc/asymptote/examples/imagecontour.asy
%{_texmfdistdir}/doc/asymptote/examples/imagehistogram.asy
%{_texmfdistdir}/doc/asymptote/examples/impact.asy
%{_texmfdistdir}/doc/asymptote/examples/integraltest.asy
%{_texmfdistdir}/doc/asymptote/examples/interpolate1.asy
%{_texmfdistdir}/doc/asymptote/examples/intro.asy
%{_texmfdistdir}/doc/asymptote/examples/irregularcontour.asy
%{_texmfdistdir}/doc/asymptote/examples/join.asy
%{_texmfdistdir}/doc/asymptote/examples/join3.asy
%{_texmfdistdir}/doc/asymptote/examples/jump.asy
%{_texmfdistdir}/doc/asymptote/examples/knots.asy
%{_texmfdistdir}/doc/asymptote/examples/label3.asy
%{_texmfdistdir}/doc/asymptote/examples/label3ribbon.asy
%{_texmfdistdir}/doc/asymptote/examples/label3solid.asy
%{_texmfdistdir}/doc/asymptote/examples/label3zoom.asy
%{_texmfdistdir}/doc/asymptote/examples/labelbox.asy
%{_texmfdistdir}/doc/asymptote/examples/labelsquare.asy
%{_texmfdistdir}/doc/asymptote/examples/laserlattice.asy
%{_texmfdistdir}/doc/asymptote/examples/latexusage.tex
%{_texmfdistdir}/doc/asymptote/examples/latticeshading.asy
%{_texmfdistdir}/doc/asymptote/examples/layers.asy
%{_texmfdistdir}/doc/asymptote/examples/leastsquares.asy
%{_texmfdistdir}/doc/asymptote/examples/leastsquares.dat
%{_texmfdistdir}/doc/asymptote/examples/legend.asy
%{_texmfdistdir}/doc/asymptote/examples/lever.asy
%{_texmfdistdir}/doc/asymptote/examples/limit.asy
%{_texmfdistdir}/doc/asymptote/examples/lineargraph.asy
%{_texmfdistdir}/doc/asymptote/examples/lineargraph0.asy
%{_texmfdistdir}/doc/asymptote/examples/linearregression.asy
%{_texmfdistdir}/doc/asymptote/examples/lines.asy
%{_texmfdistdir}/doc/asymptote/examples/linetype.asy
%{_texmfdistdir}/doc/asymptote/examples/lmfit1.asy
%{_texmfdistdir}/doc/asymptote/examples/log.asy
%{_texmfdistdir}/doc/asymptote/examples/log2graph.asy
%{_texmfdistdir}/doc/asymptote/examples/logdown.asy
%{_texmfdistdir}/doc/asymptote/examples/loggraph.asy
%{_texmfdistdir}/doc/asymptote/examples/loggrid.asy
%{_texmfdistdir}/doc/asymptote/examples/logimage.asy
%{_texmfdistdir}/doc/asymptote/examples/logo.asy
%{_texmfdistdir}/doc/asymptote/examples/logo3.asy
%{_texmfdistdir}/doc/asymptote/examples/logticks.asy
%{_texmfdistdir}/doc/asymptote/examples/lowint.asy
%{_texmfdistdir}/doc/asymptote/examples/lowupint.asy
%{_texmfdistdir}/doc/asymptote/examples/magnetic.asy
%{_texmfdistdir}/doc/asymptote/examples/makepen.asy
%{_texmfdistdir}/doc/asymptote/examples/markers1.asy
%{_texmfdistdir}/doc/asymptote/examples/markers2.asy
%{_texmfdistdir}/doc/asymptote/examples/markregular.asy
%{_texmfdistdir}/doc/asymptote/examples/mergeExample.asy
%{_texmfdistdir}/doc/asymptote/examples/mexicanhat.asy
%{_texmfdistdir}/doc/asymptote/examples/monthaxis.asy
%{_texmfdistdir}/doc/asymptote/examples/mosaic.asy
%{_texmfdistdir}/doc/asymptote/examples/mosquito.asy
%{_texmfdistdir}/doc/asymptote/examples/multicontour.asy
%{_texmfdistdir}/doc/asymptote/examples/near_earth.asy
%{_texmfdistdir}/doc/asymptote/examples/odetest.asy
%{_texmfdistdir}/doc/asymptote/examples/onecontour.asy
%{_texmfdistdir}/doc/asymptote/examples/oneoverx.asy
%{_texmfdistdir}/doc/asymptote/examples/orthocenter.asy
%{_texmfdistdir}/doc/asymptote/examples/p-orbital.asy
%{_texmfdistdir}/doc/asymptote/examples/parametricelevation.asy
%{_texmfdistdir}/doc/asymptote/examples/parametricgraph.asy
%{_texmfdistdir}/doc/asymptote/examples/parametricsurface.asy
%{_texmfdistdir}/doc/asymptote/examples/partialsurface.asy
%{_texmfdistdir}/doc/asymptote/examples/partitionExample.asy
%{_texmfdistdir}/doc/asymptote/examples/pathintersectsurface.asy
%{_texmfdistdir}/doc/asymptote/examples/pdb.asy
%{_texmfdistdir}/doc/asymptote/examples/penfunctionimage.asy
%{_texmfdistdir}/doc/asymptote/examples/penimage.asy
%{_texmfdistdir}/doc/asymptote/examples/phase.asy
%{_texmfdistdir}/doc/asymptote/examples/piicon.png
%{_texmfdistdir}/doc/asymptote/examples/pipeintersection.asy
%{_texmfdistdir}/doc/asymptote/examples/pipes.asy
%{_texmfdistdir}/doc/asymptote/examples/pixel.pdf
%{_texmfdistdir}/doc/asymptote/examples/planeproject.asy
%{_texmfdistdir}/doc/asymptote/examples/planes.asy
%{_texmfdistdir}/doc/asymptote/examples/polararea.asy
%{_texmfdistdir}/doc/asymptote/examples/polarcircle.asy
%{_texmfdistdir}/doc/asymptote/examples/polardatagraph.asy
%{_texmfdistdir}/doc/asymptote/examples/poster.asy
%{_texmfdistdir}/doc/asymptote/examples/progrid.asy
%{_texmfdistdir}/doc/asymptote/examples/projectelevation.asy
%{_texmfdistdir}/doc/asymptote/examples/projectrevolution.asy
%{_texmfdistdir}/doc/asymptote/examples/pseudosphere.asy
%{_texmfdistdir}/doc/asymptote/examples/quartercircle.asy
%{_texmfdistdir}/doc/asymptote/examples/quilt.asy
%{_texmfdistdir}/doc/asymptote/examples/rainbow.asy
%{_texmfdistdir}/doc/asymptote/examples/randompath3.asy
%{_texmfdistdir}/doc/asymptote/examples/refs.bib
%{_texmfdistdir}/doc/asymptote/examples/ring.asy
%{_texmfdistdir}/doc/asymptote/examples/roll.asy
%{_texmfdistdir}/doc/asymptote/examples/roundpath.asy
%{_texmfdistdir}/doc/asymptote/examples/sacone.asy
%{_texmfdistdir}/doc/asymptote/examples/sacone3D.asy
%{_texmfdistdir}/doc/asymptote/examples/sacylinder.asy
%{_texmfdistdir}/doc/asymptote/examples/sacylinder3D.asy
%{_texmfdistdir}/doc/asymptote/examples/saddle.asy
%{_texmfdistdir}/doc/asymptote/examples/scaledgraph.asy
%{_texmfdistdir}/doc/asymptote/examples/secondaryaxis.asy
%{_texmfdistdir}/doc/asymptote/examples/secondaryaxis.csv
%{_texmfdistdir}/doc/asymptote/examples/shade.asy
%{_texmfdistdir}/doc/asymptote/examples/shadedtiling.asy
%{_texmfdistdir}/doc/asymptote/examples/shadestroke.asy
%{_texmfdistdir}/doc/asymptote/examples/shellmethod.asy
%{_texmfdistdir}/doc/asymptote/examples/shellsqrtx01.asy
%{_texmfdistdir}/doc/asymptote/examples/sin1x.asy
%{_texmfdistdir}/doc/asymptote/examples/sin3.asy
%{_texmfdistdir}/doc/asymptote/examples/sinc.asy
%{_texmfdistdir}/doc/asymptote/examples/sinxlex.asy
%{_texmfdistdir}/doc/asymptote/examples/slidedemo.asy
%{_texmfdistdir}/doc/asymptote/examples/slope.asy
%{_texmfdistdir}/doc/asymptote/examples/slopefield1.asy
%{_texmfdistdir}/doc/asymptote/examples/smoothelevation.asy
%{_texmfdistdir}/doc/asymptote/examples/soccerball.asy
%{_texmfdistdir}/doc/asymptote/examples/spectrum.asy
%{_texmfdistdir}/doc/asymptote/examples/sphere.asy
%{_texmfdistdir}/doc/asymptote/examples/spheresilhouette.asy
%{_texmfdistdir}/doc/asymptote/examples/sphereskeleton.asy
%{_texmfdistdir}/doc/asymptote/examples/sphericalharmonic.asy
%{_texmfdistdir}/doc/asymptote/examples/spiral.asy
%{_texmfdistdir}/doc/asymptote/examples/spiral3.asy
%{_texmfdistdir}/doc/asymptote/examples/spline.asy
%{_texmfdistdir}/doc/asymptote/examples/splitpatch.asy
%{_texmfdistdir}/doc/asymptote/examples/spring.asy
%{_texmfdistdir}/doc/asymptote/examples/spring0.asy
%{_texmfdistdir}/doc/asymptote/examples/spring2.asy
%{_texmfdistdir}/doc/asymptote/examples/sqrtx01.asy
%{_texmfdistdir}/doc/asymptote/examples/sqrtx01y1.asy
%{_texmfdistdir}/doc/asymptote/examples/square.asy
%{_texmfdistdir}/doc/asymptote/examples/star.asy
%{_texmfdistdir}/doc/asymptote/examples/stereoscopic.asy
%{_texmfdistdir}/doc/asymptote/examples/stroke3.asy
%{_texmfdistdir}/doc/asymptote/examples/strokepath.asy
%{_texmfdistdir}/doc/asymptote/examples/strokeshade.asy
%{_texmfdistdir}/doc/asymptote/examples/subpictures.asy
%{_texmfdistdir}/doc/asymptote/examples/superpath.asy
%{_texmfdistdir}/doc/asymptote/examples/tanh.asy
%{_texmfdistdir}/doc/asymptote/examples/teapot.asy
%{_texmfdistdir}/doc/asymptote/examples/tensor.asy
%{_texmfdistdir}/doc/asymptote/examples/tetra.asy
%{_texmfdistdir}/doc/asymptote/examples/textpath.asy
%{_texmfdistdir}/doc/asymptote/examples/thermodynamics.asy
%{_texmfdistdir}/doc/asymptote/examples/threeviews.asy
%{_texmfdistdir}/doc/asymptote/examples/tile.asy
%{_texmfdistdir}/doc/asymptote/examples/tiling.asy
%{_texmfdistdir}/doc/asymptote/examples/torus.asy
%{_texmfdistdir}/doc/asymptote/examples/transparency.asy
%{_texmfdistdir}/doc/asymptote/examples/transparentCubes.asy
%{_texmfdistdir}/doc/asymptote/examples/treetest.asy
%{_texmfdistdir}/doc/asymptote/examples/trefoilknot.asy
%{_texmfdistdir}/doc/asymptote/examples/triads.asy
%{_texmfdistdir}/doc/asymptote/examples/triangle.asy
%{_texmfdistdir}/doc/asymptote/examples/triangles.asy
%{_texmfdistdir}/doc/asymptote/examples/triangulate.asy
%{_texmfdistdir}/doc/asymptote/examples/triceratops.asy
%{_texmfdistdir}/doc/asymptote/examples/trumpet.asy
%{_texmfdistdir}/doc/asymptote/examples/truncatedIcosahedron.asy
%{_texmfdistdir}/doc/asymptote/examples/tvgen.asy
%{_texmfdistdir}/doc/asymptote/examples/twistedtubes.asy
%{_texmfdistdir}/doc/asymptote/examples/unitcircle.asy
%{_texmfdistdir}/doc/asymptote/examples/unitcircle3.asy
%{_texmfdistdir}/doc/asymptote/examples/unitoctant.asy
%{_texmfdistdir}/doc/asymptote/examples/upint.asy
%{_texmfdistdir}/doc/asymptote/examples/vectorfield.asy
%{_texmfdistdir}/doc/asymptote/examples/vectorfield3.asy
%{_texmfdistdir}/doc/asymptote/examples/vectorfieldsphere.asy
%{_texmfdistdir}/doc/asymptote/examples/venn.asy
%{_texmfdistdir}/doc/asymptote/examples/venn3.asy
%{_texmfdistdir}/doc/asymptote/examples/vertexshading.asy
%{_texmfdistdir}/doc/asymptote/examples/washer.asy
%{_texmfdistdir}/doc/asymptote/examples/washermethod.asy
%{_texmfdistdir}/doc/asymptote/examples/wedge.asy
%{_texmfdistdir}/doc/asymptote/examples/westnile.asy
%{_texmfdistdir}/doc/asymptote/examples/westnile.csv
%{_texmfdistdir}/doc/asymptote/examples/workcone.asy
%{_texmfdistdir}/doc/asymptote/examples/worksheet.asy
%{_texmfdistdir}/doc/asymptote/examples/worldmap.asy
%{_texmfdistdir}/doc/asymptote/examples/worldmap.dat
%{_texmfdistdir}/doc/asymptote/examples/xsin1x.asy
%{_texmfdistdir}/doc/asymptote/examples/xstitch.asy
%{_texmfdistdir}/doc/asymptote/examples/xxsq01.asy
%{_texmfdistdir}/doc/asymptote/examples/xxsq01x-1.asy
%{_texmfdistdir}/doc/asymptote/examples/xxsq01y.asy
%{_texmfdistdir}/doc/asymptote/examples/yingyang.asy
%{_infodir}/asy-faq.info*
%{_infodir}/asymptote.info*
%{_mandir}/man1/asy.1*
%{_mandir}/man1/xasy.1*

%files -n texlive-asymptote
%defattr(-,root,root,755)
%{_texmfdistdir}/asymptote/CAD.asy
%{_texmfdistdir}/asymptote/GUI/CustMatTransform.py
%{_texmfdistdir}/asymptote/GUI/DebugFlags.py
%{_texmfdistdir}/asymptote/GUI/GuidesManager.py
%{_texmfdistdir}/asymptote/GUI/InplaceAddObj.py
%{_texmfdistdir}/asymptote/GUI/PrimitiveShape.py
%{_texmfdistdir}/asymptote/GUI/SetCustomAnchor.py
%{_texmfdistdir}/asymptote/GUI/UndoRedoStack.py
%{_texmfdistdir}/asymptote/GUI/Widg_addLabel.py
%{_texmfdistdir}/asymptote/GUI/Widg_addPolyOpt.py
%{_texmfdistdir}/asymptote/GUI/Widg_editBezier.py
%{_texmfdistdir}/asymptote/GUI/Window1.py
%{_texmfdistdir}/asymptote/GUI/__init__.py
%{_texmfdistdir}/asymptote/GUI/configs/xasyconfig.cson
%{_texmfdistdir}/asymptote/GUI/configs/xasykeymap.cson
%{_texmfdistdir}/asymptote/GUI/icons_rc.py
%{_texmfdistdir}/asymptote/GUI/labelEditor.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/custMatTransform.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/labelTextEditor.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/setCustomAnchor.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/widg_addLabel.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/widg_addPolyOpt.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/widg_editBezier.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/widgetPointEditor.py
%{_texmfdistdir}/asymptote/GUI/pyUIClass/window1.py
%{_texmfdistdir}/asymptote/GUI/res/icons.qrc
%{_texmfdistdir}/asymptote/GUI/res/icons/anchor.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-arrow-back.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-arrow-forward.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-camera.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-close.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-color-palette.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-delete.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-done.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-expand.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-folder-open.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-hand.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-locate.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-radio-button-off.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-radio-button-on.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/android-refresh.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/arrow-move.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/arrow-resize.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/bucket.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/center.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/centerorigin.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/check.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/chevron-with-circle-left.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/chevron-with-circle-right.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/circle.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/close-round.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/closedcurve.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/closedpolygon.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/code.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/edit.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/eye.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/filledbucket.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/grid.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/magnifying-glass.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/opencurve.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/openpolygon.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/plus-round.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/save.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/social-python.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/subdirectory-left.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/text.svg
%{_texmfdistdir}/asymptote/GUI/res/icons/triangle-stroked-15.svg
%{_texmfdistdir}/asymptote/GUI/setup.py
%{_texmfdistdir}/asymptote/GUI/xasy.py
%{_texmfdistdir}/asymptote/GUI/xasy2asy.py
%{_texmfdistdir}/asymptote/GUI/xasyArgs.py
%{_texmfdistdir}/asymptote/GUI/xasyBezierInterface.py
%{_texmfdistdir}/asymptote/GUI/xasyFile.py
%{_texmfdistdir}/asymptote/GUI/xasyOptions.py
%{_texmfdistdir}/asymptote/GUI/xasyStrings.py
%{_texmfdistdir}/asymptote/GUI/xasySvg.py
%{_texmfdistdir}/asymptote/GUI/xasyTransform.py
%{_texmfdistdir}/asymptote/GUI/xasyUtils.py
%{_texmfdistdir}/asymptote/GUI/xasyValidator.py
%{_texmfdistdir}/asymptote/GUI/xasyVersion.py
%{_texmfdistdir}/asymptote/animate.asy
%{_texmfdistdir}/asymptote/animation.asy
%{_texmfdistdir}/asymptote/annotate.asy
%{_texmfdistdir}/asymptote/asy-init.el
%{_texmfdistdir}/asymptote/asy-kate.sh
%{_texmfdistdir}/asymptote/asy-keywords.el
%{_texmfdistdir}/asymptote/asy-mode.el
%{_texmfdistdir}/asymptote/asy.vim
%{_texmfdistdir}/asymptote/asy_filetype.vim
%{_texmfdistdir}/asymptote/asymptote.py
%{_texmfdistdir}/asymptote/babel.asy
%{_texmfdistdir}/asymptote/bezulate.asy
%{_texmfdistdir}/asymptote/binarytree.asy
%{_texmfdistdir}/asymptote/bsp.asy
%{_texmfdistdir}/asymptote/colormap.asy
%{_texmfdistdir}/asymptote/contour.asy
%{_texmfdistdir}/asymptote/contour3.asy
%{_texmfdistdir}/asymptote/drawtree.asy
%{_texmfdistdir}/asymptote/embed.asy
%{_texmfdistdir}/asymptote/external.asy
%{_texmfdistdir}/asymptote/feynman.asy
%{_texmfdistdir}/asymptote/flowchart.asy
%{_texmfdistdir}/asymptote/fontsize.asy
%{_texmfdistdir}/asymptote/geometry.asy
%{_texmfdistdir}/asymptote/graph.asy
%{_texmfdistdir}/asymptote/graph3.asy
%{_texmfdistdir}/asymptote/graph_settings.asy
%{_texmfdistdir}/asymptote/graph_splinetype.asy
%{_texmfdistdir}/asymptote/grid3.asy
%{_texmfdistdir}/asymptote/interpolate.asy
%{_texmfdistdir}/asymptote/labelpath.asy
%{_texmfdistdir}/asymptote/labelpath3.asy
%{_texmfdistdir}/asymptote/latin1.asy
%{_texmfdistdir}/asymptote/lmfit.asy
%{_texmfdistdir}/asymptote/markers.asy
%{_texmfdistdir}/asymptote/math.asy
%{_texmfdistdir}/asymptote/metapost.asy
%{_texmfdistdir}/asymptote/nopapersize.ps
%{_texmfdistdir}/asymptote/obj.asy
%{_texmfdistdir}/asymptote/ode.asy
%{_texmfdistdir}/asymptote/palette.asy
%{_texmfdistdir}/asymptote/patterns.asy
%{_texmfdistdir}/asymptote/plain.asy
%{_texmfdistdir}/asymptote/plain_Label.asy
%{_texmfdistdir}/asymptote/plain_arcs.asy
%{_texmfdistdir}/asymptote/plain_arrows.asy
%{_texmfdistdir}/asymptote/plain_bounds.asy
%{_texmfdistdir}/asymptote/plain_boxes.asy
%{_texmfdistdir}/asymptote/plain_constants.asy
%{_texmfdistdir}/asymptote/plain_debugger.asy
%{_texmfdistdir}/asymptote/plain_filldraw.asy
%{_texmfdistdir}/asymptote/plain_margins.asy
%{_texmfdistdir}/asymptote/plain_markers.asy
%{_texmfdistdir}/asymptote/plain_paths.asy
%{_texmfdistdir}/asymptote/plain_pens.asy
%{_texmfdistdir}/asymptote/plain_picture.asy
%{_texmfdistdir}/asymptote/plain_prethree.asy
%{_texmfdistdir}/asymptote/plain_scaling.asy
%{_texmfdistdir}/asymptote/plain_shipout.asy
%{_texmfdistdir}/asymptote/plain_strings.asy
%{_texmfdistdir}/asymptote/pstoedit.asy
%{_texmfdistdir}/asymptote/rational.asy
%{_texmfdistdir}/asymptote/rationalSimplex.asy
%{_texmfdistdir}/asymptote/reload.js
%{_texmfdistdir}/asymptote/roundedpath.asy
%{_texmfdistdir}/asymptote/shaders/fragment.glsl
%{_texmfdistdir}/asymptote/shaders/vertex.glsl
%{_texmfdistdir}/asymptote/simplex.asy
%{_texmfdistdir}/asymptote/size10.asy
%{_texmfdistdir}/asymptote/size11.asy
%{_texmfdistdir}/asymptote/slide.asy
%{_texmfdistdir}/asymptote/slopefield.asy
%{_texmfdistdir}/asymptote/smoothcontour3.asy
%{_texmfdistdir}/asymptote/solids.asy
%{_texmfdistdir}/asymptote/stats.asy
%{_texmfdistdir}/asymptote/syzygy.asy
%{_texmfdistdir}/asymptote/texcolors.asy
%{_texmfdistdir}/asymptote/three.asy
%{_texmfdistdir}/asymptote/three_arrows.asy
%{_texmfdistdir}/asymptote/three_light.asy
%{_texmfdistdir}/asymptote/three_margins.asy
%{_texmfdistdir}/asymptote/three_surface.asy
%{_texmfdistdir}/asymptote/three_tube.asy
%{_texmfdistdir}/asymptote/tree.asy
%{_texmfdistdir}/asymptote/trembling.asy
%{_texmfdistdir}/asymptote/tube.asy
%{_texmfdistdir}/asymptote/unicode.asy
%{_texmfdistdir}/asymptote/version.asy
%{_texmfdistdir}/asymptote/webgl/asygl.js
%{_texmfdistdir}/asymptote/x11colors.asy
%{_texmfdistdir}/tex/context/third/asymptote/colo-asy.tex
%{_texmfdistdir}/tex/latex/asymptote/asycolors.sty
%{_texmfdistdir}/tex/latex/asymptote/asymptote.sty
%{_texmfdistdir}/tex/latex/asymptote/latexmkrc
%{_texmfdistdir}/tex/latex/asymptote/ocg.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asymptote-%{texlive_version}.%{texlive_noarch}.2.65svn54567-%{release}-zypper
%endif

%package -n texlive-asymptote-by-example-zh-cn
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Asymptote by example
License:        LGPL-3.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source51:       asymptote-by-example-zh-cn.doc.tar.xz

%description -n texlive-asymptote-by-example-zh-cn
This is a tutorial written in Simplified Chinese.
%post -n texlive-asymptote-by-example-zh-cn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asymptote-by-example-zh-cn 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asymptote-by-example-zh-cn
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asymptote-by-example-zh-cn
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/README
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/asymptote-by-example-zh-cn.pdf
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/asy.bib
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/asymptote.sty
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/asysyntex.sty
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/cleantmp
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/CJKmove.sty
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/area.asy
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/hanoi.asy
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/hyper.asy
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/movie15.sty
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/recplot.asy
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/stars.asy
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/tiling.asy
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/figure-src/xiantu.asy
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/gpl-3.0.tex
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/main.tex
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/makepdf
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/myfonts.sty
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/tiling.pdf
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/tiling.tex
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/xiantu-ancient.pdf
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/xiantu.pdf
%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/xiantu.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asymptote-by-example-zh-cn-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-asymptote-faq-zh-cn
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Asymptote FAQ (Chinese translation)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source52:       asymptote-faq-zh-cn.doc.tar.xz

%description -n texlive-asymptote-faq-zh-cn
This is a Chinese translation of the Asymptote FAQ
%post -n texlive-asymptote-faq-zh-cn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asymptote-faq-zh-cn 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asymptote-faq-zh-cn
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asymptote-faq-zh-cn
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/README
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/asymptote-faq-zh-cn.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/asy-faq.tex
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-1.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-1.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-2.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-2.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-7.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-7.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-8.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-8.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-9.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/4-9.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/5-1a.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/5-1a.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/5-2.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/5-2.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/5-4.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/5-4.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-1.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-1.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-11a.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-11a.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-11b.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-11b.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-12.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-12.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-14.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-14.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-15.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-15.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-19.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-19.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-2.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-2.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-3.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-3.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-4.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-4.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-5.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-5.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-6.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-6.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-7b.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-7b.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-7c.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-7c.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-8b.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-8b.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-8c.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-8c.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-9.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/6-9.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-4.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-4.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8a.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8a.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8b.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8b.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8c.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8c.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8d.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-8d.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-9a.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-9a.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-9b.asy
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/figures/8-9b.pdf
%{_texmfdistdir}/doc/support/asymptote-faq-zh-cn/src/preamble_newnew.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asymptote-faq-zh-cn-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-asymptote-manual-zh-cn
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        A Chinese translation of the asymptote manual
License:        LGPL-3.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source53:       asymptote-manual-zh-cn.doc.tar.xz

%description -n texlive-asymptote-manual-zh-cn
This is an (incomplete, simplified) Chinese translation of the
Asymptote manual.
%post -n texlive-asymptote-manual-zh-cn
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asymptote-manual-zh-cn 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asymptote-manual-zh-cn
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asymptote-manual-zh-cn
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/README
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/asymptote-manual-zh-cn.pdf
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/CDlabel.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/Coons.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/Gouraud.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/Pythagoras.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/adobefonts.tex
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/asycolors.sty
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/asysyntex.tex
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/axialshade.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/bezier2.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/beziercurve.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/bigsquare.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/cleantmp
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/clippath.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/colons.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/colors.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/cube.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/diagonal.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/dots.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/fzfonts.tex
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/hatch.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/join.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/labelalign.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/labelsquare.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/latticeshading.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/linecap.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/linejoin.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/linetype.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/logo.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/main.tex
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/makepdf
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/makepen.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/mexicanhat.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/quartercircle.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/shadedtiling.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/shadestroke.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/square.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/subpictures.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/superpath.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/tile.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/transparency.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/windingnumber.asy
%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/winfonts.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asymptote-manual-zh-cn-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-asypictureb
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn33490
Release:        0
Summary:        User-friendly integration of Asymptote into LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-asypictureb-doc >= %{texlive_version}
Provides:       tex(asypictureB.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(pgfkeys.sty)
Requires:       tex(verbatimcopy.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source54:       asypictureb.tar.xz
Source55:       asypictureb.doc.tar.xz

%description -n texlive-asypictureb
The package is an unofficial alternative to the package
provided with the Asymptote distribution, for including
pictures within a LaTeX source file. While it does not
duplicate all the features of the official package, this
package is more user-friendly in several ways. Most notably,
Asymptote errors are repackaged as LaTeX errors, making
debugging less of a pain. It also has a more robust mechanism
for identifying unchanged pictures that need not be recompiled.

%package -n texlive-asypictureb-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn33490
Release:        0
Summary:        Documentation for texlive-asypictureb
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-asypictureb-doc
This package includes the documentation for texlive-asypictureb

%post -n texlive-asypictureb
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-asypictureb 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-asypictureb
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-asypictureb-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/asypictureb/README
%{_texmfdistdir}/doc/latex/asypictureb/asypictureB.pdf

%files -n texlive-asypictureb
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/asypictureb/asypictureB.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-asypictureb-%{texlive_version}.%{texlive_noarch}.0.0.3svn33490-%{release}-zypper
%endif

%package -n texlive-atbegshi
Version:        %{texlive_version}.%{texlive_noarch}.1.19svn53051
Release:        0
Summary:        Execute stuff at \shipout time
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-atbegshi-doc >= %{texlive_version}
Provides:       tex(atbegshi.sty)
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(ltxcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source56:       atbegshi.tar.xz
Source57:       atbegshi.doc.tar.xz

%description -n texlive-atbegshi
This package is a modern reimplementation of package everyshi,
providing various commands to be executed before a \shipout
command. It makes use of e-TeX's facilities if they are
available. The package may be used either with LaTeX or with
plain TeX.

%package -n texlive-atbegshi-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.19svn53051
Release:        0
Summary:        Documentation for texlive-atbegshi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-atbegshi-doc
This package includes the documentation for texlive-atbegshi

%post -n texlive-atbegshi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-atbegshi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-atbegshi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-atbegshi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/atbegshi/README.md
%{_texmfdistdir}/doc/latex/atbegshi/atbegshi-example1.tex
%{_texmfdistdir}/doc/latex/atbegshi/atbegshi-example2.tex
%{_texmfdistdir}/doc/latex/atbegshi/atbegshi.pdf

%files -n texlive-atbegshi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/atbegshi/atbegshi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-atbegshi-%{texlive_version}.%{texlive_noarch}.1.19svn53051-%{release}-zypper
%endif

%package -n texlive-atenddvi
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn53107
Release:        0
Summary:        Provides the \AtEndDvi command
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-atenddvi-doc >= %{texlive_version}
Provides:       tex(atenddvi.sty)
Requires:       tex(atbegshi.sty)
Requires:       tex(zref-abspage.sty)
Requires:       tex(zref-lastpage.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source58:       atenddvi.tar.xz
Source59:       atenddvi.doc.tar.xz

%description -n texlive-atenddvi
LaTeX offers \AtBeginDvi. This package provides the counterpart
\AtEndDvi. The execution of its argument is delayed to the end
of the document at the end of the last page. At this point
\special and \write remain effective, because they are put into
the last page. This is the main difference from the LaTeX
command \AtEndDocument.

%package -n texlive-atenddvi-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn53107
Release:        0
Summary:        Documentation for texlive-atenddvi
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-atenddvi-doc
This package includes the documentation for texlive-atenddvi

%post -n texlive-atenddvi
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-atenddvi 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-atenddvi
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-atenddvi-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/atenddvi/README.md
%{_texmfdistdir}/doc/latex/atenddvi/atenddvi.pdf

%files -n texlive-atenddvi
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/atenddvi/atenddvi.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-atenddvi-%{texlive_version}.%{texlive_noarch}.1.4svn53107-%{release}-zypper
%endif

%package -n texlive-attachfile
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn42099
Release:        0
Summary:        Attach arbitrary files to a PDF document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-attachfile-doc >= %{texlive_version}
Provides:       tex(attachfile.sty)
Requires:       tex(calc.sty)
Requires:       tex(color.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source60:       attachfile.tar.xz
Source61:       attachfile.doc.tar.xz

%description -n texlive-attachfile
Starting with PDF 1.3 (Adobe Acrobat 4.0), PDF files can
contain file attachments -- arbitrary files that a reader can
extract, just like attachments to an e-mail message. The
attachfile package brings this functionality to pdfLaTeX and
provides some additional features not available in Acrobat,
such as the ability to use arbitrary LaTeX code for the file
icon -- including things like \includegraphics, tabular, and
mathematics. Settings can be made either globally or on a
per-attachment basis. Attachfile makes it easy to attach files
and customize their appearance in the enclosing document. The
package supports the Created, Modified, and Size keys in the
EmbeddedFile's Params dictionary.

%package -n texlive-attachfile-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9svn42099
Release:        0
Summary:        Documentation for texlive-attachfile
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-attachfile-doc
This package includes the documentation for texlive-attachfile

%post -n texlive-attachfile
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-attachfile 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-attachfile
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-attachfile-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/attachfile/README
%{_texmfdistdir}/doc/latex/attachfile/attachfile.pdf

%files -n texlive-attachfile
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bib/attachfile/attachfile.bib
%{_texmfdistdir}/tex/latex/attachfile/attachfile.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-attachfile-%{texlive_version}.%{texlive_noarch}.1.9svn42099-%{release}-zypper
%endif

%package -n texlive-attachfile2
Version:        %{texlive_version}.%{texlive_noarch}.2.11svn52929
Release:        0
Summary:        Attach files into PDF
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-attachfile2-bin >= %{texlive_version}
#!BuildIgnore: texlive-attachfile2-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-attachfile2-doc >= %{texlive_version}
Requires:       perl(Digest::MD5)
#!BuildIgnore:  perl(Digest::MD5)
Requires:       perl(Getopt::Long)
#!BuildIgnore:  perl(Getopt::Long)
Requires:       perl(POSIX)
#!BuildIgnore:  perl(POSIX)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Provides:       tex(atfi-dvipdfmx.def)
Provides:       tex(atfi-dvips.def)
Provides:       tex(atfi-luatex.def)
Provides:       tex(atfi-pdftex.def)
Provides:       tex(attachfile2.sty)
Requires:       tex(color.sty)
Requires:       tex(hycolor.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(iftex.sty)
Requires:       tex(infwarerr.sty)
Requires:       tex(keyval.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(ltxcmds.sty)
Requires:       tex(pdfescape.sty)
Requires:       tex(pdftexcmds.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source62:       attachfile2.tar.xz
Source63:       attachfile2.doc.tar.xz

%description -n texlive-attachfile2
This package can be used to attach files to a PDF document. It
is a further development of Scott Pakin's package attachfile
for pdfTeX. Apart from bug fixes, this package adds support for
dvips, some new options, and gets and writes meta information
data about the attached files.

%package -n texlive-attachfile2-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.11svn52929
Release:        0
Summary:        Documentation for texlive-attachfile2
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(pdfatfi.1)

%description -n texlive-attachfile2-doc
This package includes the documentation for texlive-attachfile2

%post -n texlive-attachfile2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-attachfile2 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-attachfile2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-attachfile2-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/attachfile2/README.md
%{_texmfdistdir}/doc/latex/attachfile2/attachfile2.pdf
%{_mandir}/man1/pdfatfi.1*

%files -n texlive-attachfile2
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/attachfile2/pdfatfi.pl
%{_texmfdistdir}/tex/latex/attachfile2/atfi-dvipdfmx.def
%{_texmfdistdir}/tex/latex/attachfile2/atfi-dvips.def
%{_texmfdistdir}/tex/latex/attachfile2/atfi-luatex.def
%{_texmfdistdir}/tex/latex/attachfile2/atfi-pdftex.def
%{_texmfdistdir}/tex/latex/attachfile2/attachfile2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-attachfile2-%{texlive_version}.%{texlive_noarch}.2.11svn52929-%{release}-zypper
%endif

%package -n texlive-atveryend
Version:        %{texlive_version}.%{texlive_noarch}.1.11svn53108
Release:        0
Summary:        Hooks at the very end of a document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-atveryend-doc >= %{texlive_version}
Provides:       tex(atveryend.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source64:       atveryend.tar.xz
Source65:       atveryend.doc.tar.xz

%description -n texlive-atveryend
This LaTeX packages provides two hooks for \end{document} that
are executed after the hook of \AtEndDocument:
\AfterLastShipout can be used for code that is to be executed
right after the last \clearpage before the `.aux' file is
closed. \AtVeryEndDocument is used for code after closing and
final reading of the `.aux' file.

%package -n texlive-atveryend-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.11svn53108
Release:        0
Summary:        Documentation for texlive-atveryend
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-atveryend-doc
This package includes the documentation for texlive-atveryend

%post -n texlive-atveryend
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-atveryend 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-atveryend
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-atveryend-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/atveryend/README.md
%{_texmfdistdir}/doc/latex/atveryend/atveryend.pdf

%files -n texlive-atveryend
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/atveryend/atveryend.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-atveryend-%{texlive_version}.%{texlive_noarch}.1.11svn53108-%{release}-zypper
%endif

%package -n texlive-aucklandthesis
Version:        %{texlive_version}.%{texlive_noarch}.svn51323
Release:        0
Summary:        Memoir-based class for formatting University of Auckland masters' and doctors' theses
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-aucklandthesis-doc >= %{texlive_version}
Provides:       tex(aucklandthesis.cls)
Requires:       tex(memoir.cls)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source66:       aucklandthesis.tar.xz
Source67:       aucklandthesis.doc.tar.xz

%description -n texlive-aucklandthesis
A memoir-based class for formatting University of Auckland
masters' and doctors' thesis dissertations in any discipline.
The title page does not handle short dissertations for
diplomas.

%package -n texlive-aucklandthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn51323
Release:        0
Summary:        Documentation for texlive-aucklandthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-aucklandthesis-doc
This package includes the documentation for texlive-aucklandthesis

%post -n texlive-aucklandthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-aucklandthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-aucklandthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-aucklandthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/aucklandthesis/README.TEXLIVE
%{_texmfdistdir}/doc/latex/aucklandthesis/README.txt
%{_texmfdistdir}/doc/latex/aucklandthesis/template.tex

%files -n texlive-aucklandthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/aucklandthesis/aucklandthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-aucklandthesis-%{texlive_version}.%{texlive_noarch}.svn51323-%{release}-zypper
%endif

%package -n texlive-augie
Version:        %{texlive_version}.%{texlive_noarch}.svn18948
Release:        0
Summary:        Calligraphic font for typesetting handwriting
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-augie-fonts >= %{texlive_version}
Recommends:     texlive-augie-doc >= %{texlive_version}
Provides:       tex(augie.map)
Provides:       tex(augie7t.tfm)
Provides:       tex(augie7t.vf)
Provides:       tex(augie8c.tfm)
Provides:       tex(augie8c.vf)
Provides:       tex(augie8r.tfm)
Provides:       tex(augie8t.tfm)
Provides:       tex(augie8t.vf)
Provides:       tex(augie___.tfm)
Provides:       tex(ot1augie.fd)
Provides:       tex(t1augie.fd)
Provides:       tex(ts1augie.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source68:       augie.tar.xz
Source69:       augie.doc.tar.xz

%description -n texlive-augie
A calligraphic font for simulating American-style informal
handwriting. The font is distributed in Adobe Type 1 format.

%package -n texlive-augie-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn18948
Release:        0
Summary:        Documentation for texlive-augie
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-augie-doc
This package includes the documentation for texlive-augie


%package -n texlive-augie-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn18948
Release:        0
Summary:        Severed fonts for texlive-augie
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-augie-fonts
The  separated fonts package for texlive-augie
%post -n texlive-augie
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap augie.map' >> /var/run/texlive/run-updmap

%postun -n texlive-augie 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap augie.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-augie
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-augie-fonts
%files -n texlive-augie-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/augie/README.augie
%{_texmfdistdir}/doc/latex/augie/augie.txt
%{_texmfdistdir}/doc/latex/augie/other/Augie___.pfm
%{_texmfdistdir}/doc/latex/augie/other/augie___.inf
%{_texmfdistdir}/doc/latex/augie/vtex/augie.ali

%files -n texlive-augie
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/augie/augie___.afm
%{_texmfdistdir}/fonts/map/dvips/augie/augie.map
%{_texmfdistdir}/fonts/tfm/public/augie/augie7t.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie8c.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie8r.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie8t.tfm
%{_texmfdistdir}/fonts/tfm/public/augie/augie___.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/augie/augie___.pfb
%{_texmfdistdir}/fonts/vf/public/augie/augie7t.vf
%{_texmfdistdir}/fonts/vf/public/augie/augie8c.vf
%{_texmfdistdir}/fonts/vf/public/augie/augie8t.vf
%{_texmfdistdir}/tex/latex/augie/ot1augie.fd
%{_texmfdistdir}/tex/latex/augie/t1augie.fd
%{_texmfdistdir}/tex/latex/augie/ts1augie.fd

%files -n texlive-augie-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-augie
%{_datadir}/fontconfig/conf.avail/58-texlive-augie.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-augie/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-augie/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-augie/fonts.scale
%{_datadir}/fonts/texlive-augie/augie___.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-augie-fonts-%{texlive_version}.%{texlive_noarch}.svn18948-%{release}-zypper
%endif

%package -n texlive-auncial-new
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Artificial Uncial font and LaTeX support macros
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-auncial-new-fonts >= %{texlive_version}
Recommends:     texlive-auncial-new-doc >= %{texlive_version}
Provides:       tex(allauncl.sty)
Provides:       tex(auncial.map)
Provides:       tex(auncial.sty)
Provides:       tex(auncl10.tfm)
Provides:       tex(aunclb10.tfm)
Provides:       tex(b1auncl.fd)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source70:       auncial-new.tar.xz
Source71:       auncial-new.doc.tar.xz

%description -n texlive-auncial-new
The auncial-new bundle provides packages and fonts for a script
based on the Artificial Uncial manuscript book-hand used
between the 6th & 10th century AD. The script consists of
minuscules and digits, with some appropriate period punctuation
marks. Both normal and bold versions are provided, and the font
is distributed in Adobe Type 1 format. This is an experimental
new version of the auncial bundle, which is one of a series of
bookhand fonts. The font follows the B1 encoding developed for
bookhands. Access to the encoding is essential. The encoding
mainly follows the standard T1 encoding.

%package -n texlive-auncial-new-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Documentation for texlive-auncial-new
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-auncial-new-doc
This package includes the documentation for texlive-auncial-new


%package -n texlive-auncial-new-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.0svn15878
Release:        0
Summary:        Severed fonts for texlive-auncial-new
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-auncial-new-fonts
The  separated fonts package for texlive-auncial-new
%post -n texlive-auncial-new
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap auncial.map' >> /var/run/texlive/run-updmap

%postun -n texlive-auncial-new 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap auncial.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-auncial-new
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-auncial-new-fonts
%files -n texlive-auncial-new-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/auncial-new/README
%{_texmfdistdir}/doc/fonts/auncial-new/auncial.pdf
%{_texmfdistdir}/doc/fonts/auncial-new/tryauncial.pdf
%{_texmfdistdir}/doc/fonts/auncial-new/tryauncial.tex

%files -n texlive-auncial-new
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/auncial-new/auncl10.afm
%{_texmfdistdir}/fonts/afm/public/auncial-new/aunclb10.afm
%{_texmfdistdir}/fonts/map/dvips/auncial-new/auncial.map
%{_texmfdistdir}/fonts/tfm/public/auncial-new/auncl10.tfm
%{_texmfdistdir}/fonts/tfm/public/auncial-new/aunclb10.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/auncial-new/auncl10.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/auncial-new/aunclb10.pfb
%{_texmfdistdir}/tex/latex/auncial-new/allauncl.sty
%{_texmfdistdir}/tex/latex/auncial-new/auncial.sty
%{_texmfdistdir}/tex/latex/auncial-new/b1auncl.fd

%files -n texlive-auncial-new-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-auncial-new
%{_datadir}/fontconfig/conf.avail/58-texlive-auncial-new.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-auncial-new/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-auncial-new/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-auncial-new/fonts.scale
%{_datadir}/fonts/texlive-auncial-new/auncl10.pfb
%{_datadir}/fonts/texlive-auncial-new/aunclb10.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-auncial-new-fonts-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif

%package -n texlive-aurical
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Calligraphic fonts for use with LaTeX in T1 encoding
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-aurical-fonts >= %{texlive_version}
Recommends:     texlive-aurical-doc >= %{texlive_version}
Provides:       tex(AmiciLogo.tfm)
Provides:       tex(AmiciLogoBold.tfm)
Provides:       tex(AmiciLogoBoldRslant.tfm)
Provides:       tex(AmiciLogoBoldSlant.tfm)
Provides:       tex(AmiciLogoRslant.tfm)
Provides:       tex(AmiciLogoSlant.tfm)
Provides:       tex(AuriocusKalligraphicus.tfm)
Provides:       tex(AuriocusKalligraphicusBold.tfm)
Provides:       tex(AuriocusKalligraphicusBoldRslant.tfm)
Provides:       tex(AuriocusKalligraphicusBoldSlant.tfm)
Provides:       tex(AuriocusKalligraphicusRslant.tfm)
Provides:       tex(AuriocusKalligraphicusSlant.tfm)
Provides:       tex(JanaSkrivana.tfm)
Provides:       tex(JanaSkrivanaBold.tfm)
Provides:       tex(JanaSkrivanaBoldRslant.tfm)
Provides:       tex(JanaSkrivanaBoldSlant.tfm)
Provides:       tex(JanaSkrivanaRslant.tfm)
Provides:       tex(JanaSkrivanaSlant.tfm)
Provides:       tex(LukasSvatba.tfm)
Provides:       tex(LukasSvatbaBold.tfm)
Provides:       tex(LukasSvatbaBoldRslant.tfm)
Provides:       tex(LukasSvatbaBoldSlant.tfm)
Provides:       tex(LukasSvatbaRslant.tfm)
Provides:       tex(LukasSvatbaSlant.tfm)
Provides:       tex(T1AmiciLogo.fd)
Provides:       tex(T1AuriocusKalligraphicus.fd)
Provides:       tex(T1JanaSkrivana.fd)
Provides:       tex(T1LukasSvatba.fd)
Provides:       tex(aurical.map)
Provides:       tex(aurical.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source72:       aurical.tar.xz
Source73:       aurical.doc.tar.xz

%description -n texlive-aurical
The package that implements a set (AuriocusKalligraphicus) of
three calligraphic fonts derived from the author's handwriting
in Adobe Type 1 Format, T1 encoding for use with LaTeX:
Auriocus Kalligraphicus; Lukas Svatba; and Jana Skrivana. Each
font features oldstyle digits and (machine-generated) boldface
and slanted versions. A variant of Lukas Svatba offers a 'long
s'.

%package -n texlive-aurical-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Documentation for texlive-aurical
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-aurical-doc
This package includes the documentation for texlive-aurical


%package -n texlive-aurical-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn15878
Release:        0
Summary:        Severed fonts for texlive-aurical
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-aurical-fonts
The  separated fonts package for texlive-aurical
%post -n texlive-aurical
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap aurical.map' >> /var/run/texlive/run-updmap

%postun -n texlive-aurical 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap aurical.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-aurical
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-aurical-fonts
%files -n texlive-aurical-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/aurical/aurical.pdf
%{_texmfdistdir}/doc/latex/aurical/aurical.tex

%files -n texlive-aurical
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogo.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AmiciLogoSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicus.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/AuriocusKalligraphicusSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivana.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/JanaSkrivanaSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatba.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaBold.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaBoldRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaBoldSlant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaRslant.afm
%{_texmfdistdir}/fonts/afm/public/aurical/LukasSvatbaSlant.afm
%{_texmfdistdir}/fonts/map/dvips/aurical/aurical.map
%{_texmfdistdir}/fonts/source/public/aurical/aurical_source.zip
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogo.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AmiciLogoSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicus.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/AuriocusKalligraphicusSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivana.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/JanaSkrivanaSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatba.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaBold.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaBoldRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaBoldSlant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaRslant.tfm
%{_texmfdistdir}/fonts/tfm/public/aurical/LukasSvatbaSlant.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogo.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoBoldRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoBoldSlant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AmiciLogoSlant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicus.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusBoldRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusBoldSlant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/AuriocusKalligraphicusSlant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivana.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaBoldRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaBoldSlant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/JanaSkrivanaSlant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatba.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaBold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaBoldRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaBoldSlant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaRslant.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/aurical/LukasSvatbaSlant.pfb
%{_texmfdistdir}/tex/latex/aurical/T1AmiciLogo.fd
%{_texmfdistdir}/tex/latex/aurical/T1AuriocusKalligraphicus.fd
%{_texmfdistdir}/tex/latex/aurical/T1JanaSkrivana.fd
%{_texmfdistdir}/tex/latex/aurical/T1LukasSvatba.fd
%{_texmfdistdir}/tex/latex/aurical/aurical.sty

%files -n texlive-aurical-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-aurical
%{_datadir}/fontconfig/conf.avail/58-texlive-aurical.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-aurical/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-aurical/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-aurical/fonts.scale
%{_datadir}/fonts/texlive-aurical/AmiciLogo.pfb
%{_datadir}/fonts/texlive-aurical/AmiciLogoBold.pfb
%{_datadir}/fonts/texlive-aurical/AmiciLogoBoldRslant.pfb
%{_datadir}/fonts/texlive-aurical/AmiciLogoBoldSlant.pfb
%{_datadir}/fonts/texlive-aurical/AmiciLogoRslant.pfb
%{_datadir}/fonts/texlive-aurical/AmiciLogoSlant.pfb
%{_datadir}/fonts/texlive-aurical/AuriocusKalligraphicus.pfb
%{_datadir}/fonts/texlive-aurical/AuriocusKalligraphicusBold.pfb
%{_datadir}/fonts/texlive-aurical/AuriocusKalligraphicusBoldRslant.pfb
%{_datadir}/fonts/texlive-aurical/AuriocusKalligraphicusBoldSlant.pfb
%{_datadir}/fonts/texlive-aurical/AuriocusKalligraphicusRslant.pfb
%{_datadir}/fonts/texlive-aurical/AuriocusKalligraphicusSlant.pfb
%{_datadir}/fonts/texlive-aurical/JanaSkrivana.pfb
%{_datadir}/fonts/texlive-aurical/JanaSkrivanaBold.pfb
%{_datadir}/fonts/texlive-aurical/JanaSkrivanaBoldRslant.pfb
%{_datadir}/fonts/texlive-aurical/JanaSkrivanaBoldSlant.pfb
%{_datadir}/fonts/texlive-aurical/JanaSkrivanaRslant.pfb
%{_datadir}/fonts/texlive-aurical/JanaSkrivanaSlant.pfb
%{_datadir}/fonts/texlive-aurical/LukasSvatba.pfb
%{_datadir}/fonts/texlive-aurical/LukasSvatbaBold.pfb
%{_datadir}/fonts/texlive-aurical/LukasSvatbaBoldRslant.pfb
%{_datadir}/fonts/texlive-aurical/LukasSvatbaBoldSlant.pfb
%{_datadir}/fonts/texlive-aurical/LukasSvatbaRslant.pfb
%{_datadir}/fonts/texlive-aurical/LukasSvatbaSlant.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-aurical-fonts-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif

%package -n texlive-aurl
Version:        %{texlive_version}.%{texlive_noarch}.svn41853
Release:        0
Summary:        Extends the hyperref package with a mechanism for hyperlinked URLs abbreviated with prefixes
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-aurl-doc >= %{texlive_version}
Provides:       tex(aurl.sty)
Requires:       tex(hyperref.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source74:       aurl.tar.xz
Source75:       aurl.doc.tar.xz

%description -n texlive-aurl
Semantic Web resource URLs are often abbreviated with prefixes,
like "owl:Class" or "rdf:type". The abbreviated URL (aurl)
package provides the correct hyperlinks for those URLs. The
1000 most common prefixes are predefined and more can be added.

%package -n texlive-aurl-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn41853
Release:        0
Summary:        Documentation for texlive-aurl
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-aurl-doc
This package includes the documentation for texlive-aurl

%post -n texlive-aurl
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-aurl 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-aurl
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-aurl-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/aurl/README.md
%{_texmfdistdir}/doc/latex/aurl/aurltest.tex

%files -n texlive-aurl
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/aurl/aurl.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-aurl-%{texlive_version}.%{texlive_noarch}.svn41853-%{release}-zypper
%endif

%package -n texlive-authoraftertitle
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn24863
Release:        0
Summary:        Make author, etc., available after \maketitle
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-authoraftertitle-doc >= %{texlive_version}
Provides:       tex(authoraftertitle.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source76:       authoraftertitle.tar.xz
Source77:       authoraftertitle.doc.tar.xz

%description -n texlive-authoraftertitle
This jiffy package makes the author, title and date of the
package available to the user (as \MyAuthor, etc) after the
\maketitle command has been executed.

%package -n texlive-authoraftertitle-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9svn24863
Release:        0
Summary:        Documentation for texlive-authoraftertitle
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-authoraftertitle-doc
This package includes the documentation for texlive-authoraftertitle

%post -n texlive-authoraftertitle
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-authoraftertitle 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-authoraftertitle
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-authoraftertitle-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.pdf
%{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.tex

%files -n texlive-authoraftertitle
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/authoraftertitle/authoraftertitle.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-authoraftertitle-%{texlive_version}.%{texlive_noarch}.0.0.9svn24863-%{release}-zypper
%endif

%package -n texlive-authorarchive
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Adds self-archiving information to scientific papers
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-authorarchive-doc >= %{texlive_version}
Provides:       tex(authorarchive.sty)
Requires:       tex(calc.sty)
Requires:       tex(dtk-logos.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(eso-pic.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(intopdf.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(lastpage.sty)
Requires:       tex(qrcode.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source78:       authorarchive.tar.xz
Source79:       authorarchive.doc.tar.xz

%description -n texlive-authorarchive
This is a LaTeX style for producing author self-archiving
copies of (academic) papers. The following layout-styles are
pre-defined: ACMfor the two-column layout used by many ACM
conferences IEEE for the two-column layout used by many IEEE
conferences LNCS for the LNCS layout (as used by Springer) LNI
for the Lecture Notes in Informatics, published by the GI ENTCS
for the Elsevier ENTCS layout

%package -n texlive-authorarchive-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1.1svn54512
Release:        0
Summary:        Documentation for texlive-authorarchive
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-authorarchive-doc
This package includes the documentation for texlive-authorarchive

%post -n texlive-authorarchive
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-authorarchive 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-authorarchive
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-authorarchive-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/authorarchive/CHANGELOG.md
%{_texmfdistdir}/doc/latex/authorarchive/LICENSE
%{_texmfdistdir}/doc/latex/authorarchive/README.md
%{_texmfdistdir}/doc/latex/authorarchive/examples/authorarchive.config
%{_texmfdistdir}/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.bib
%{_texmfdistdir}/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.enw
%{_texmfdistdir}/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.ris
%{_texmfdistdir}/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.word.xml
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran-nourl.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran-nourl.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-acmart.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-acmart.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-entcs.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-entcs.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs-a4.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs-a4.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-lni.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-lni.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-sig-alternate.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016-sig-alternate.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016.pdf
%{_texmfdistdir}/doc/latex/authorarchive/examples/brucker-authorarchive-2016.tex
%{_texmfdistdir}/doc/latex/authorarchive/examples/input/body.tex
%{_texmfdistdir}/doc/latex/authorarchive/icons/README.md
%{_texmfdistdir}/doc/latex/authorarchive/icons/vector_iD_icon.pdf
%{_texmfdistdir}/doc/latex/authorarchive/icons/vector_iD_icon.svg

%files -n texlive-authorarchive
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/authorarchive/authorarchive.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-authorarchive-%{texlive_version}.%{texlive_noarch}.1.1.1svn54512-%{release}-zypper
%endif

%package -n texlive-authordate
Version:        %{texlive_version}.%{texlive_noarch}.svn52564
Release:        0
Summary:        Author/date style citation styles
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-authordate-doc >= %{texlive_version}
Provides:       tex(authordate1-4.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source80:       authordate.tar.xz
Source81:       authordate.doc.tar.xz

%description -n texlive-authordate
Authordate produces styles loosely based on the recommendations
of British Standard 1629(1976), Butcher's Copy-editing and the
Chicago Manual of Style. The bundle provides four BibTeX styles
(authordate1, ..., authordate4), and a LaTeX package, for
citation in author/date style. The BibTeX styles differ in how
they format names and titles; one of them is necessary for the
LaTeX package to work.

%package -n texlive-authordate-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn52564
Release:        0
Summary:        Documentation for texlive-authordate
License:        SUSE-TeX
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-authordate-doc
This package includes the documentation for texlive-authordate

%post -n texlive-authordate
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-authordate 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-authordate
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-authordate-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/authordate/README
%{_texmfdistdir}/doc/bibtex/authordate/authordate1.ltx
%{_texmfdistdir}/doc/bibtex/authordate/authordate2.ltx
%{_texmfdistdir}/doc/bibtex/authordate/authordate3.ltx
%{_texmfdistdir}/doc/bibtex/authordate/authordate4.ltx
%{_texmfdistdir}/doc/bibtex/authordate/testadb.ltx

%files -n texlive-authordate
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/authordate/authordate1.bst
%{_texmfdistdir}/bibtex/bst/authordate/authordate2.bst
%{_texmfdistdir}/bibtex/bst/authordate/authordate3.bst
%{_texmfdistdir}/bibtex/bst/authordate/authordate4.bst
%{_texmfdistdir}/tex/latex/authordate/authordate1-4.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-authordate-%{texlive_version}.%{texlive_noarch}.svn52564-%{release}-zypper
%endif

%package -n texlive-authorindex
Version:        %{texlive_version}.%{texlive_noarch}.svn51757
Release:        0
Summary:        Index citations by author names
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-authorindex-bin >= %{texlive_version}
#!BuildIgnore: texlive-authorindex-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-authorindex-doc >= %{texlive_version}
Requires:       perl(Getopt::Std)
#!BuildIgnore:  perl(Getopt::Std)
Requires:       perl(strict)
#!BuildIgnore:  perl(strict)
Requires:       perl(warnings)
#!BuildIgnore:  perl(warnings)
Provides:       tex(authorindex.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source82:       authorindex.tar.xz
Source83:       authorindex.doc.tar.xz

%description -n texlive-authorindex
This package allows the user to create an index of all authors
cited in a LaTeX document. Each author entry in the index
contains the pages where these citations occur. Alternatively,
the package can list the labels of the citations that appear in
the references rather than the text pages. The package relies
on BibTeX being used to handle citations. Additionally, it
requires Perl (version 5 or higher).

%package -n texlive-authorindex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn51757
Release:        0
Summary:        Documentation for texlive-authorindex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-authorindex-doc
This package includes the documentation for texlive-authorindex

%post -n texlive-authorindex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-authorindex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-authorindex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-authorindex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/authorindex/COPYING
%{_texmfdistdir}/doc/latex/authorindex/NEWS
%{_texmfdistdir}/doc/latex/authorindex/README
%{_texmfdistdir}/doc/latex/authorindex/authorindex.pdf
%{_texmfdistdir}/doc/latex/authorindex/authorindex.tex

%files -n texlive-authorindex
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/authorindex/authorindex
%{_texmfdistdir}/tex/latex/authorindex/authorindex.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-authorindex-%{texlive_version}.%{texlive_noarch}.svn51757-%{release}-zypper
%endif

%package -n texlive-auto-pst-pdf
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn52849
Release:        0
Summary:        Wrapper for pst-pdf (with some psfrag features)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-ifplatform >= %{texlive_version}
#!BuildIgnore: texlive-ifplatform
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires:       texlive-xkeyval >= %{texlive_version}
#!BuildIgnore: texlive-xkeyval
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-auto-pst-pdf-doc >= %{texlive_version}
Provides:       tex(auto-pst-pdf.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(pst-pdf.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source84:       auto-pst-pdf.tar.xz
Source85:       auto-pst-pdf.doc.tar.xz

%description -n texlive-auto-pst-pdf
The package uses --shell-escape to execute pst-pdf when
necessary. This makes it especially easy to integrate into the
workflow of an editor with just "LaTeX" and "pdfLaTeX" buttons.
Wrappers are provided for various psfrag-related features so
that Matlab figures via laprint, Mathematica figures via
MathPSfrag, and regular psfrag figures can all be input
consistently and easily.

%package -n texlive-auto-pst-pdf-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn52849
Release:        0
Summary:        Documentation for texlive-auto-pst-pdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-auto-pst-pdf-doc:de;en)

%description -n texlive-auto-pst-pdf-doc
This package includes the documentation for texlive-auto-pst-pdf

%post -n texlive-auto-pst-pdf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-auto-pst-pdf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-auto-pst-pdf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-auto-pst-pdf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/auto-pst-pdf/README
%{_texmfdistdir}/doc/latex/auto-pst-pdf/auto-pst-pdf-DE.pdf
%{_texmfdistdir}/doc/latex/auto-pst-pdf/auto-pst-pdf-DE.tex
%{_texmfdistdir}/doc/latex/auto-pst-pdf/auto-pst-pdf.pdf
%{_texmfdistdir}/doc/latex/auto-pst-pdf/example-psfrag.tex
%{_texmfdistdir}/doc/latex/auto-pst-pdf/example.eps
%{_texmfdistdir}/doc/latex/auto-pst-pdf/example.tex

%files -n texlive-auto-pst-pdf
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/auto-pst-pdf/auto-pst-pdf.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-auto-pst-pdf-%{texlive_version}.%{texlive_noarch}.0.0.6svn52849-%{release}-zypper
%endif

%package -n texlive-auto-pst-pdf-lua
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn54779
Release:        0
Summary:        Using LuaLaTeX together with PostScript code
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires:       texlive-iftex >= %{texlive_version}
#!BuildIgnore: texlive-iftex
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-auto-pst-pdf-lua-doc >= %{texlive_version}
Provides:       tex(auto-pst-pdf-lua.sty)
Requires:       tex(ifluatex.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(pst-pdf.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source86:       auto-pst-pdf-lua.tar.xz
Source87:       auto-pst-pdf-lua.doc.tar.xz

%description -n texlive-auto-pst-pdf-lua
This package is a slightly modified version of auto-pst-pdf by
Will Robertson, which itself is a wrapper for pst-pdf by Rolf
Niepraschk. The package allows the use of LuaLaTeX together
with PostScript related code, eg. PSTricks. It depends on
ifpdf, ifluatex, ifplatform, and xkeyval.

%package -n texlive-auto-pst-pdf-lua-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.03svn54779
Release:        0
Summary:        Documentation for texlive-auto-pst-pdf-lua
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-auto-pst-pdf-lua-doc
This package includes the documentation for texlive-auto-pst-pdf-lua

%post -n texlive-auto-pst-pdf-lua
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-auto-pst-pdf-lua 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-auto-pst-pdf-lua
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-auto-pst-pdf-lua-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/auto-pst-pdf-lua/Changes
%{_texmfdistdir}/doc/latex/auto-pst-pdf-lua/README
%{_texmfdistdir}/doc/latex/auto-pst-pdf-lua/auto-pst-pdf-lua-doc.pdf
%{_texmfdistdir}/doc/latex/auto-pst-pdf-lua/auto-pst-pdf-lua-doc.tex

%files -n texlive-auto-pst-pdf-lua
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/auto-pst-pdf-lua/auto-pst-pdf-lua.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-auto-pst-pdf-lua-%{texlive_version}.%{texlive_noarch}.0.0.03svn54779-%{release}-zypper
%endif

%package -n texlive-autoaligne
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn49092
Release:        0
Summary:        Align terms and members in math expressions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-autoaligne-doc >= %{texlive_version}
Provides:       tex(autoaligne-fr.tex)
Provides:       tex(autoaligne.sty)
Provides:       tex(autoaligne.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source88:       autoaligne.tar.xz
Source89:       autoaligne.doc.tar.xz

%description -n texlive-autoaligne
This package allows to align terms and members between lines
containing math expressions.

%package -n texlive-autoaligne-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn49092
Release:        0
Summary:        Documentation for texlive-autoaligne
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-autoaligne-doc:fr)

%description -n texlive-autoaligne-doc
This package includes the documentation for texlive-autoaligne

%post -n texlive-autoaligne
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-autoaligne 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-autoaligne
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-autoaligne-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/autoaligne/README
%{_texmfdistdir}/doc/generic/autoaligne/autoaligne-fr.pdf

%files -n texlive-autoaligne
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/autoaligne/autoaligne-fr.tex
%{_texmfdistdir}/tex/generic/autoaligne/autoaligne.sty
%{_texmfdistdir}/tex/generic/autoaligne/autoaligne.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-autoaligne-%{texlive_version}.%{texlive_noarch}.1.4svn49092-%{release}-zypper
%endif

%package -n texlive-autoarea
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3asvn15878
Release:        0
Summary:        Automatic computation of bounding boxes with PiCTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-autoarea-doc >= %{texlive_version}
Provides:       tex(autoarea.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source90:       autoarea.tar.xz
Source91:       autoarea.doc.tar.xz

%description -n texlive-autoarea
This package makes PiCTeX recognize lines and arcs in
determining the "bounding box" of a picture. (PiCTeX so far
accounted for put commands only). The "bounding box" is
essential for proper placement of a picture between running
text and margins and for keeping the running text away.

%package -n texlive-autoarea-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3asvn15878
Release:        0
Summary:        Documentation for texlive-autoarea
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-autoarea-doc
This package includes the documentation for texlive-autoarea

%post -n texlive-autoarea
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-autoarea 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-autoarea
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-autoarea-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/autoarea/ANNOUNCE.txt
%{_texmfdistdir}/doc/latex/autoarea/README.aa
%{_texmfdistdir}/doc/latex/autoarea/autodemo/README.autodemo
%{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo+.log
%{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo+.pdf
%{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo+.tex
%{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo-.log
%{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo-.pdf
%{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo-.tex
%{_texmfdistdir}/doc/latex/autoarea/autodemo/autodemo.tex

%files -n texlive-autoarea
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/autoarea/autoarea.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-autoarea-%{texlive_version}.%{texlive_noarch}.0.0.3asvn15878-%{release}-zypper
%endif

%package -n texlive-autobreak
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn43337
Release:        0
Summary:        Simple line breaking of long formulae
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-autobreak-doc >= %{texlive_version}
Provides:       tex(autobreak.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(catchfile.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source92:       autobreak.tar.xz
Source93:       autobreak.doc.tar.xz

%description -n texlive-autobreak
This package implements a simple mechanism of line/page
breaking within the align environment of the amsmath package;
new line characters are considered as possible candidates for
the breaks and the package tries to put breaks at adequate
places. It is suitable for computer-generated long formulae
with many terms.

%package -n texlive-autobreak-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn43337
Release:        0
Summary:        Documentation for texlive-autobreak
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-autobreak-doc:en)

%description -n texlive-autobreak-doc
This package includes the documentation for texlive-autobreak

%post -n texlive-autobreak
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-autobreak 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-autobreak
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-autobreak-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/autobreak/README.md
%{_texmfdistdir}/doc/latex/autobreak/autobreak.pdf

%files -n texlive-autobreak
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/autobreak/autobreak.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-autobreak-%{texlive_version}.%{texlive_noarch}.0.0.3svn43337-%{release}-zypper
%endif

%package -n texlive-autofancyhdr
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn54049
Release:        0
Summary:        Automatically compute headlength for fancyhdr package
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-autofancyhdr-doc >= %{texlive_version}
Provides:       tex(autofancyhdr.sty)
Requires:       tex(biditools.sty)
Requires:       tex(fancyhdr.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source94:       autofancyhdr.tar.xz
Source95:       autofancyhdr.doc.tar.xz

%description -n texlive-autofancyhdr
The package automatically computes headlength for the fancyhdr
package

%package -n texlive-autofancyhdr-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn54049
Release:        0
Summary:        Documentation for texlive-autofancyhdr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-autofancyhdr-doc
This package includes the documentation for texlive-autofancyhdr

%post -n texlive-autofancyhdr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-autofancyhdr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-autofancyhdr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-autofancyhdr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/autofancyhdr/LICENSE
%{_texmfdistdir}/doc/latex/autofancyhdr/README.md

%files -n texlive-autofancyhdr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/autofancyhdr/autofancyhdr.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-autofancyhdr-%{texlive_version}.%{texlive_noarch}.0.0.1svn54049-%{release}-zypper
%endif

%package -n texlive-automata
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn19717
Release:        0
Summary:        Finite state machines, graphs and trees in MetaPost
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-automata-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source96:       automata.tar.xz
Source97:       automata.doc.tar.xz

%description -n texlive-automata
The package offers a collection of macros for MetaPost to make
easier to draw finite-state machines, automata, labelled
graphs, etc. The user defines nodes, which may be isolated or
arranged into matrices or trees; edges connect pairs of nodes
through arbitrary paths. Parameters, that specify the shapes of
nodes and the styles of edges, may be adjusted.

%package -n texlive-automata-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3svn19717
Release:        0
Summary:        Documentation for texlive-automata
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-automata-doc
This package includes the documentation for texlive-automata

%post -n texlive-automata
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-automata 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-automata
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-automata-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/automata/README
%{_texmfdistdir}/doc/metapost/automata/example.mp
%{_texmfdistdir}/doc/metapost/automata/example.pdf
%{_texmfdistdir}/doc/metapost/automata/example.tex

%files -n texlive-automata
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/automata/automata.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-automata-%{texlive_version}.%{texlive_noarch}.0.0.3svn19717-%{release}-zypper
%endif

%package -n texlive-autonum
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.11svn36084
Release:        0
Summary:        Automatic equation references
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-autonum-doc >= %{texlive_version}
Provides:       tex(autonum.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(etextools.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(textpos.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source98:       autonum.tar.xz
Source99:       autonum.doc.tar.xz

%description -n texlive-autonum
The package arranges that equation numbers are applied only to
those equations that are referenced. This operation is similar
to the showonlyrefs option of the package mathtools.

%package -n texlive-autonum-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.3.11svn36084
Release:        0
Summary:        Documentation for texlive-autonum
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-autonum-doc
This package includes the documentation for texlive-autonum

%post -n texlive-autonum
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-autonum 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-autonum
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-autonum-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/autonum/README
%{_texmfdistdir}/doc/latex/autonum/autonum.pdf
%{_texmfdistdir}/doc/latex/autonum/test-autonum.pdf
%{_texmfdistdir}/doc/latex/autonum/test-autonum.tex
%{_texmfdistdir}/doc/latex/autonum/test-freeze.tex

%files -n texlive-autonum
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/autonum/autonum.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-autonum-%{texlive_version}.%{texlive_noarch}.0.0.3.11svn36084-%{release}-zypper
%endif

%package -n texlive-autopdf
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32377
Release:        0
Summary:        Conversion of graphics to pdfLaTeX-compatible formats
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-autopdf-doc >= %{texlive_version}
Provides:       tex(autopdf.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifpdf.sty)
Requires:       tex(ifplatform.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(keyval.sty)
Requires:       tex(psfrag.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source100:      autopdf.tar.xz
Source101:      autopdf.doc.tar.xz

%description -n texlive-autopdf
The package facilitates the on-the-fly conversion of various
graphics formats to formats supported by pdfLaTeX (e.g. PDF).
It uses a range of external programs, and therefore requires
that the LaTeX run starts with write18 enabled.

%package -n texlive-autopdf-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn32377
Release:        0
Summary:        Documentation for texlive-autopdf
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-autopdf-doc
This package includes the documentation for texlive-autopdf

%post -n texlive-autopdf
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-autopdf 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-autopdf
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-autopdf-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/autopdf/README.txt
%{_texmfdistdir}/doc/latex/autopdf/autopdf.pdf

%files -n texlive-autopdf
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/autopdf/autopdf.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-autopdf-%{texlive_version}.%{texlive_noarch}.1.1svn32377-%{release}-zypper
%endif

%package -n texlive-autosp
Version:        %{texlive_version}.%{texlive_noarch}.svn54240
Release:        0
Summary:        A Preprocessor that generates note-spacing commands for MusiXTeX scores
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-autosp-bin >= %{texlive_version}
#!BuildIgnore: texlive-autosp-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Provides:       man(autosp.1)
Provides:       man(tex2aspc.1)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source102:      autosp.doc.tar.xz

%description -n texlive-autosp
This program simplifies the creation of MusiXTeX scores by
converting (non-standard) commands of the form \anotes ... \en
into one or more conventional note-spacing commands, as
determined by the note values themselves, with \sk spacing
commands inserted as necessary. The coding for an entire
measure can be entered one part at a time, without concern for
note-spacing changes within the part or spacing requirements of
other parts. For example, \anotes\qa J\qa K&\ca l\qa m\ca n\en
generates \Notes\qa J\sk\qa K\sk&\ca l\qa m\sk\ca n\en .
%post -n texlive-autosp
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-autosp 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-autosp
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-autosp
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/autosp/README
%{_texmfdistdir}/doc/generic/autosp/barsant2.aspc
%{_texmfdistdir}/doc/generic/autosp/barsant2.pdf
%{_texmfdistdir}/doc/generic/autosp/geminiani.aspc
%{_texmfdistdir}/doc/generic/autosp/geminiani.pdf
%{_texmfdistdir}/doc/generic/autosp/kinder2.aspc
%{_texmfdistdir}/doc/generic/autosp/kinder2.pdf
%{_texmfdistdir}/doc/generic/autosp/quod2.aspc
%{_texmfdistdir}/doc/generic/autosp/quod2.pdf
%{_texmfdistdir}/doc/generic/autosp/quod2A.aspc
%{_texmfdistdir}/doc/generic/autosp/quod2A.pdf
%{_texmfdistdir}/doc/generic/autosp/rebar.1
%{_texmfdistdir}/doc/generic/autosp/rebar.pdf
%{_mandir}/man1/autosp.1*
%{_mandir}/man1/tex2aspc.1*
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-autosp-%{texlive_version}.%{texlive_noarch}.svn54240-%{release}-zypper
%endif

%package -n texlive-auxhook
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn53173
Release:        0
Summary:        Hooks for auxiliary files
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-auxhook-doc >= %{texlive_version}
Provides:       tex(auxhook.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source103:      auxhook.tar.xz
Source104:      auxhook.doc.tar.xz

%description -n texlive-auxhook
This package auxhook provides hooks for adding stuff at the
begin of .aux files.

%package -n texlive-auxhook-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn53173
Release:        0
Summary:        Documentation for texlive-auxhook
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-auxhook-doc
This package includes the documentation for texlive-auxhook

%post -n texlive-auxhook
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-auxhook 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-auxhook
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-auxhook-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/auxhook/README.md
%{_texmfdistdir}/doc/latex/auxhook/auxhook.pdf

%files -n texlive-auxhook
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/auxhook/auxhook.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-auxhook-%{texlive_version}.%{texlive_noarch}.1.6svn53173-%{release}-zypper
%endif

%package -n texlive-avantgar
Version:        %{texlive_version}.%{texlive_noarch}.svn31835
Release:        0
Summary:        URW "Base 35" font pack for LaTeX
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-avantgar-fonts >= %{texlive_version}
Provides:       tex(8ruag.fd)
Provides:       tex(omluag.fd)
Provides:       tex(omsuag.fd)
Provides:       tex(ot1uag.fd)
Provides:       tex(pagd.tfm)
Provides:       tex(pagd.vf)
Provides:       tex(pagd7t.tfm)
Provides:       tex(pagd7t.vf)
Provides:       tex(pagd8c.tfm)
Provides:       tex(pagd8c.vf)
Provides:       tex(pagd8r.tfm)
Provides:       tex(pagd8t.tfm)
Provides:       tex(pagd8t.vf)
Provides:       tex(pagdc.tfm)
Provides:       tex(pagdc.vf)
Provides:       tex(pagdc7t.tfm)
Provides:       tex(pagdc7t.vf)
Provides:       tex(pagdc8t.tfm)
Provides:       tex(pagdc8t.vf)
Provides:       tex(pagdo.tfm)
Provides:       tex(pagdo.vf)
Provides:       tex(pagdo7t.tfm)
Provides:       tex(pagdo7t.vf)
Provides:       tex(pagdo8c.tfm)
Provides:       tex(pagdo8c.vf)
Provides:       tex(pagdo8r.tfm)
Provides:       tex(pagdo8t.tfm)
Provides:       tex(pagdo8t.vf)
Provides:       tex(pagk.tfm)
Provides:       tex(pagk.vf)
Provides:       tex(pagk7t.tfm)
Provides:       tex(pagk7t.vf)
Provides:       tex(pagk8c.tfm)
Provides:       tex(pagk8c.vf)
Provides:       tex(pagk8r.tfm)
Provides:       tex(pagk8t.tfm)
Provides:       tex(pagk8t.vf)
Provides:       tex(pagkc.tfm)
Provides:       tex(pagkc.vf)
Provides:       tex(pagkc7t.tfm)
Provides:       tex(pagkc7t.vf)
Provides:       tex(pagkc8t.tfm)
Provides:       tex(pagkc8t.vf)
Provides:       tex(pagko.tfm)
Provides:       tex(pagko.vf)
Provides:       tex(pagko7t.tfm)
Provides:       tex(pagko7t.vf)
Provides:       tex(pagko8c.tfm)
Provides:       tex(pagko8c.vf)
Provides:       tex(pagko8r.tfm)
Provides:       tex(pagko8t.tfm)
Provides:       tex(pagko8t.vf)
Provides:       tex(t1uag.fd)
Provides:       tex(ts1uag.fd)
Provides:       tex(uag.map)
Provides:       tex(uagb7t.tfm)
Provides:       tex(uagb7t.vf)
Provides:       tex(uagb8c.tfm)
Provides:       tex(uagb8c.vf)
Provides:       tex(uagb8r.tfm)
Provides:       tex(uagb8t.tfm)
Provides:       tex(uagb8t.vf)
Provides:       tex(uagbc7t.tfm)
Provides:       tex(uagbc7t.vf)
Provides:       tex(uagbc8t.tfm)
Provides:       tex(uagbc8t.vf)
Provides:       tex(uagbi7t.tfm)
Provides:       tex(uagbi7t.vf)
Provides:       tex(uagbi8c.tfm)
Provides:       tex(uagbi8c.vf)
Provides:       tex(uagbi8r.tfm)
Provides:       tex(uagbi8t.tfm)
Provides:       tex(uagbi8t.vf)
Provides:       tex(uagbo7t.tfm)
Provides:       tex(uagbo7t.vf)
Provides:       tex(uagbo8c.tfm)
Provides:       tex(uagbo8c.vf)
Provides:       tex(uagbo8r.tfm)
Provides:       tex(uagbo8t.tfm)
Provides:       tex(uagbo8t.vf)
Provides:       tex(uagd7t.tfm)
Provides:       tex(uagd7t.vf)
Provides:       tex(uagd8c.tfm)
Provides:       tex(uagd8c.vf)
Provides:       tex(uagd8r.tfm)
Provides:       tex(uagd8t.tfm)
Provides:       tex(uagd8t.vf)
Provides:       tex(uagdc7t.tfm)
Provides:       tex(uagdc7t.vf)
Provides:       tex(uagdc8t.tfm)
Provides:       tex(uagdc8t.vf)
Provides:       tex(uagdo7t.tfm)
Provides:       tex(uagdo7t.vf)
Provides:       tex(uagdo8c.tfm)
Provides:       tex(uagdo8c.vf)
Provides:       tex(uagdo8r.tfm)
Provides:       tex(uagdo8t.tfm)
Provides:       tex(uagdo8t.vf)
Provides:       tex(uagk7t.tfm)
Provides:       tex(uagk7t.vf)
Provides:       tex(uagk8c.tfm)
Provides:       tex(uagk8c.vf)
Provides:       tex(uagk8r.tfm)
Provides:       tex(uagk8t.tfm)
Provides:       tex(uagk8t.vf)
Provides:       tex(uagkc7t.tfm)
Provides:       tex(uagkc7t.vf)
Provides:       tex(uagkc8t.tfm)
Provides:       tex(uagkc8t.vf)
Provides:       tex(uagko7t.tfm)
Provides:       tex(uagko7t.vf)
Provides:       tex(uagko8c.tfm)
Provides:       tex(uagko8c.vf)
Provides:       tex(uagko8r.tfm)
Provides:       tex(uagko8t.tfm)
Provides:       tex(uagko8t.vf)
Provides:       tex(uagr7t.tfm)
Provides:       tex(uagr7t.vf)
Provides:       tex(uagr8c.tfm)
Provides:       tex(uagr8c.vf)
Provides:       tex(uagr8r.tfm)
Provides:       tex(uagr8t.tfm)
Provides:       tex(uagr8t.vf)
Provides:       tex(uagrc7t.tfm)
Provides:       tex(uagrc7t.vf)
Provides:       tex(uagrc8t.tfm)
Provides:       tex(uagrc8t.vf)
Provides:       tex(uagri7t.tfm)
Provides:       tex(uagri7t.vf)
Provides:       tex(uagri8c.tfm)
Provides:       tex(uagri8c.vf)
Provides:       tex(uagri8r.tfm)
Provides:       tex(uagri8t.tfm)
Provides:       tex(uagri8t.vf)
Provides:       tex(uagro7t.tfm)
Provides:       tex(uagro7t.vf)
Provides:       tex(uagro8c.tfm)
Provides:       tex(uagro8c.vf)
Provides:       tex(uagro8r.tfm)
Provides:       tex(uagro8t.tfm)
Provides:       tex(uagro8t.vf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source105:      avantgar.tar.xz

%description -n texlive-avantgar
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-avantgar-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn31835
Release:        0
Summary:        Severed fonts for texlive-avantgar
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-avantgar-fonts
The  separated fonts package for texlive-avantgar
%post -n texlive-avantgar
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap uag.map' >> /var/run/texlive/run-updmap

%postun -n texlive-avantgar 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap uag.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-avantgar
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-avantgar-fonts
%files -n texlive-avantgar
%defattr(-,root,root,755)
%{_texmfdistdir}/dvips/avantgar/config.uag
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagd8a.afm
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagdo8a.afm
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagk8a.afm
%{_texmfdistdir}/fonts/afm/adobe/avantgar/pagko8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagb8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagbi8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagd8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagdo8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagk8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagko8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagr8a.afm
%{_texmfdistdir}/fonts/afm/urw/avantgar/uagri8a.afm
%{_texmfdistdir}/fonts/map/dvips/avantgar/uag.map
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagd8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagdo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagk8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagkc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagkc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagkc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/avantgar/pagko8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagd8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagdo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagk8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagkc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagkc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagko8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/avantgar/uagro8t.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/avantgar/uagd8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagd8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/avantgar/uagdo8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagdo8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/avantgar/uagk8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagk8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/urw/avantgar/uagko8a.pfb
%{_texmfdistdir}/fonts/type1/urw/avantgar/uagko8a.pfm
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagd8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdc.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagdo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagk8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagkc.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagkc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagkc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko7t.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko8c.vf
%{_texmfdistdir}/fonts/vf/adobe/avantgar/pagko8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagd7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagd8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagd8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagdo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagk7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagk8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagk8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagkc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagkc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagko7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagko8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagko8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/avantgar/uagro8t.vf
%{_texmfdistdir}/tex/latex/avantgar/8ruag.fd
%{_texmfdistdir}/tex/latex/avantgar/omluag.fd
%{_texmfdistdir}/tex/latex/avantgar/omsuag.fd
%{_texmfdistdir}/tex/latex/avantgar/ot1uag.fd
%{_texmfdistdir}/tex/latex/avantgar/t1uag.fd
%{_texmfdistdir}/tex/latex/avantgar/ts1uag.fd

%files -n texlive-avantgar-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-avantgar
%{_datadir}/fontconfig/conf.avail/58-texlive-avantgar.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-avantgar/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-avantgar/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-avantgar/fonts.scale
%{_datadir}/fonts/texlive-avantgar/uagd8a.pfb
%{_datadir}/fonts/texlive-avantgar/uagdo8a.pfb
%{_datadir}/fonts/texlive-avantgar/uagk8a.pfb
%{_datadir}/fonts/texlive-avantgar/uagko8a.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-avantgar-fonts-%{texlive_version}.%{texlive_noarch}.svn31835-%{release}-zypper
%endif

%package -n texlive-avremu
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn35373
Release:        0
Summary:        An 8-Bit Microcontroller Simulator written in LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-avremu-doc >= %{texlive_version}
Provides:       tex(avr.binary.tex)
Provides:       tex(avr.bitops.tex)
Provides:       tex(avr.draw.tex)
Provides:       tex(avr.instr.tex)
Provides:       tex(avr.io.tex)
Provides:       tex(avr.memory.tex)
Provides:       tex(avr.numbers.tex)
Provides:       tex(avr.testsuite.tex)
Provides:       tex(avremu.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(kvoptions.sty)
Requires:       tex(tabularx.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source106:      avremu.tar.xz
Source107:      avremu.doc.tar.xz

%description -n texlive-avremu
A fully working package to simulate a Microprocessor in pure
LaTeX. The simulator is able to calculate complex pictures,
like Mandelbrot sets.

%package -n texlive-avremu-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.1svn35373
Release:        0
Summary:        Documentation for texlive-avremu
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-avremu-doc
This package includes the documentation for texlive-avremu

%post -n texlive-avremu
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-avremu 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-avremu
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-avremu-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/avremu/README
%{_texmfdistdir}/doc/latex/avremu/avremu.pdf

%files -n texlive-avremu
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/avremu/avr.binary.tex
%{_texmfdistdir}/tex/latex/avremu/avr.bitops.tex
%{_texmfdistdir}/tex/latex/avremu/avr.draw.tex
%{_texmfdistdir}/tex/latex/avremu/avr.instr.tex
%{_texmfdistdir}/tex/latex/avremu/avr.io.tex
%{_texmfdistdir}/tex/latex/avremu/avr.memory.tex
%{_texmfdistdir}/tex/latex/avremu/avr.numbers.tex
%{_texmfdistdir}/tex/latex/avremu/avr.testsuite.tex
%{_texmfdistdir}/tex/latex/avremu/avremu.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-avremu-%{texlive_version}.%{texlive_noarch}.0.0.1svn35373-%{release}-zypper
%endif

%package -n texlive-awesomebox
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn51776
Release:        0
Summary:        Draw admonition blocks in your documents, illustrated with FontAwesome icons
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-awesomebox-doc >= %{texlive_version}
Provides:       tex(awesomebox.sty)
Requires:       tex(array.sty)
Requires:       tex(fontawesome5.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source108:      awesomebox.tar.xz
Source109:      awesomebox.doc.tar.xz

%description -n texlive-awesomebox
Awesome Boxes is all about drawing admonition blocks around
text to inform or alert readers about something particular. The
specific aim of this package is to use FontAwesome icons to
ease the illustration of these blocks. The package depends on
fontawesome5, xcolor, array and xparse.

%package -n texlive-awesomebox-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.6svn51776
Release:        0
Summary:        Documentation for texlive-awesomebox
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-awesomebox-doc
This package includes the documentation for texlive-awesomebox

%post -n texlive-awesomebox
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-awesomebox 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-awesomebox
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-awesomebox-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/awesomebox/LICENSE
%{_texmfdistdir}/doc/latex/awesomebox/README.md
%{_texmfdistdir}/doc/latex/awesomebox/awesomebox.pdf
%{_texmfdistdir}/doc/latex/awesomebox/awesomebox.tex

%files -n texlive-awesomebox
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/awesomebox/awesomebox.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-awesomebox-%{texlive_version}.%{texlive_noarch}.0.0.6svn51776-%{release}-zypper
%endif

%package -n texlive-axessibility
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn54080
Release:        0
Summary:        Access to formulas in PDF files by assistive technologies
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-axessibility-doc >= %{texlive_version}
Provides:       tex(axessibility.sty)
Requires:       tex(accsupp.sty)
Requires:       tex(amsmath.sty)
Requires:       tex(amssymb.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(fontspec.sty)
Requires:       tex(luacode.sty)
Requires:       tex(tagpdf.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source110:      axessibility.tar.xz
Source111:      axessibility.doc.tar.xz

%description -n texlive-axessibility
PDF documents containing formulas generated by LaTeX are
usually not accessible by assistive technologies for visually
impaired people and people with special educational needs
(i.e., by screen readers and braille displays). The
axessibility package manages this issue, allowing to create a
PDF document where the formulas are read by these assistive
technologies, since it automatically generates hidden comments
in the PDF document (by means of the /ActualText attribute
and/or suitable tags) in correspondence to each formula.

%package -n texlive-axessibility-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0svn54080
Release:        0
Summary:        Documentation for texlive-axessibility
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-axessibility-doc
This package includes the documentation for texlive-axessibility

%post -n texlive-axessibility
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-axessibility 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-axessibility
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-axessibility-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/axessibility/README
%{_texmfdistdir}/doc/latex/axessibility/axessibility.lua
%{_texmfdistdir}/doc/latex/axessibility/axessibility.pdf
%{_texmfdistdir}/doc/latex/axessibility/axessibilityExampleAlignA.tex
%{_texmfdistdir}/doc/latex/axessibility/axessibilityExampleAlignT.tex
%{_texmfdistdir}/doc/latex/axessibility/axessibilityExampleSingleLineA.tex
%{_texmfdistdir}/doc/latex/axessibility/axessibilityExampleSingleLineT.tex

%files -n texlive-axessibility
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/axessibility/axessibility.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-axessibility-%{texlive_version}.%{texlive_noarch}.3.0svn54080-%{release}-zypper
%endif

%package -n texlive-axodraw2
Version:        %{texlive_version}.%{texlive_noarch}.2.1.1bsvn54055
Release:        0
Summary:        Feynman diagrams in a LaTeX document
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-axodraw2-bin >= %{texlive_version}
#!BuildIgnore: texlive-axodraw2-bin
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-axodraw2-doc >= %{texlive_version}
Provides:       tex(axodraw2.sty)
Requires:       tex(color.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(ifxetex.sty)
Requires:       tex(keyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source112:      axodraw2.tar.xz
Source113:      axodraw2.doc.tar.xz

%description -n texlive-axodraw2
This package defines macros for drawing Feynman graphs in LaTeX
documents. It is an important update of the axodraw package,
but since it is not completely backwards compatible, we have
given the style file a changed name. Many new features have
been added, with new types of line, and much more flexibility
in their properties. In addition, it is now possible to use
axodraw2 with pdfLaTeX, as well as with the LaTeX-dvips method.
However with pdfLaTeX (and also LuaLaTeX and XeLaTeX), an
external program, axohelp, is used to perform the geometrical
calculations needed for the pdf code inserted in the output
file. The processing involves a run of pdfLaTeX, a run of
axohelp, and then another run of pdfLaTeX.

%package -n texlive-axodraw2-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1.1bsvn54055
Release:        0
Summary:        Documentation for texlive-axodraw2
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       man(axohelp.1)

%description -n texlive-axodraw2-doc
This package includes the documentation for texlive-axodraw2

%post -n texlive-axodraw2
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-axodraw2 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-axodraw2
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-axodraw2-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/axodraw2/AUTHORS
%{_texmfdistdir}/doc/latex/axodraw2/COPYING
%{_texmfdistdir}/doc/latex/axodraw2/ChangeLog
%{_texmfdistdir}/doc/latex/axodraw2/INSTALL
%{_texmfdistdir}/doc/latex/axodraw2/README
%{_texmfdistdir}/doc/latex/axodraw2/axodraw2-man.pdf
%{_texmfdistdir}/doc/latex/axodraw2/axodraw2-man.tex
%{_texmfdistdir}/doc/latex/axodraw2/example.tex
%{_mandir}/man1/axohelp.1*

%files -n texlive-axodraw2
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/axodraw2/axodraw2.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-axodraw2-%{texlive_version}.%{texlive_noarch}.2.1.1bsvn54055-%{release}-zypper
%endif

%package -n texlive-b1encoding
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21271
Release:        0
Summary:        LaTeX encoding tools for Bookhands fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-b1encoding-doc >= %{texlive_version}
Provides:       tex(TeXB1.enc)
Provides:       tex(b1cmr.fd)
Provides:       tex(b1enc.def)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source114:      b1encoding.tar.xz
Source115:      b1encoding.doc.tar.xz

%description -n texlive-b1encoding
The package characterises and defines the author's B1 encoding
for use with LaTeX when typesetting things using his Bookhands
fonts.

%package -n texlive-b1encoding-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn21271
Release:        0
Summary:        Documentation for texlive-b1encoding
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-b1encoding-doc
This package includes the documentation for texlive-b1encoding

%post -n texlive-b1encoding
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-b1encoding 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-b1encoding
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-b1encoding-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/b1encoding/README
%{_texmfdistdir}/doc/latex/b1encoding/b1encoding.pdf

%files -n texlive-b1encoding
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/b1encoding/TeXB1.enc
%{_texmfdistdir}/tex/latex/b1encoding/b1cmr.fd
%{_texmfdistdir}/tex/latex/b1encoding/b1enc.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-b1encoding-%{texlive_version}.%{texlive_noarch}.1.0svn21271-%{release}-zypper
%endif

%package -n texlive-babel
Version:        %{texlive_version}.%{texlive_noarch}.3.42svn54487
Release:        0
Summary:        Multilingual support for Plain TeX or LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-doc >= %{texlive_version}
Provides:       tex(UKenglish.sty)
Provides:       tex(USenglish.sty)
Provides:       tex(afrikaans.sty)
Provides:       tex(albanian.sty)
Provides:       tex(american.sty)
Provides:       tex(austrian.sty)
Provides:       tex(babel-afrikaans.tex)
Provides:       tex(babel-aghem.tex)
Provides:       tex(babel-akan.tex)
Provides:       tex(babel-albanian.tex)
Provides:       tex(babel-american.tex)
Provides:       tex(babel-amharic.tex)
Provides:       tex(babel-ancientgreek.tex)
Provides:       tex(babel-arabic-algeria.tex)
Provides:       tex(babel-arabic-dz.tex)
Provides:       tex(babel-arabic-ma.tex)
Provides:       tex(babel-arabic-morocco.tex)
Provides:       tex(babel-arabic-sy.tex)
Provides:       tex(babel-arabic-syria.tex)
Provides:       tex(babel-arabic.tex)
Provides:       tex(babel-armenian.tex)
Provides:       tex(babel-assamese.tex)
Provides:       tex(babel-asturian.tex)
Provides:       tex(babel-asu.tex)
Provides:       tex(babel-australian.tex)
Provides:       tex(babel-austrian.tex)
Provides:       tex(babel-azerbaijani-cyrillic.tex)
Provides:       tex(babel-azerbaijani-cyrl.tex)
Provides:       tex(babel-azerbaijani-latin.tex)
Provides:       tex(babel-azerbaijani-latn.tex)
Provides:       tex(babel-azerbaijani.tex)
Provides:       tex(babel-bafia.tex)
Provides:       tex(babel-bambara.tex)
Provides:       tex(babel-basaa.tex)
Provides:       tex(babel-basque.tex)
Provides:       tex(babel-belarusian.tex)
Provides:       tex(babel-bemba.tex)
Provides:       tex(babel-bena.tex)
Provides:       tex(babel-bengali.tex)
Provides:       tex(babel-bodo.tex)
Provides:       tex(babel-bosnian-cyrillic.tex)
Provides:       tex(babel-bosnian-cyrl.tex)
Provides:       tex(babel-bosnian-latin.tex)
Provides:       tex(babel-bosnian-latn.tex)
Provides:       tex(babel-bosnian.tex)
Provides:       tex(babel-brazilian.tex)
Provides:       tex(babel-breton.tex)
Provides:       tex(babel-british.tex)
Provides:       tex(babel-bulgarian.tex)
Provides:       tex(babel-burmese.tex)
Provides:       tex(babel-canadian.tex)
Provides:       tex(babel-cantonese.tex)
Provides:       tex(babel-catalan.tex)
Provides:       tex(babel-centralatlastamazight.tex)
Provides:       tex(babel-centralkurdish.tex)
Provides:       tex(babel-chechen.tex)
Provides:       tex(babel-cherokee.tex)
Provides:       tex(babel-chiga.tex)
Provides:       tex(babel-chinese-hans-hk.tex)
Provides:       tex(babel-chinese-hans-mo.tex)
Provides:       tex(babel-chinese-hans-sg.tex)
Provides:       tex(babel-chinese-hans.tex)
Provides:       tex(babel-chinese-hant-hk.tex)
Provides:       tex(babel-chinese-hant-mo.tex)
Provides:       tex(babel-chinese-hant.tex)
Provides:       tex(babel-chinese-simplified-hongkongsarchina.tex)
Provides:       tex(babel-chinese-simplified-macausarchina.tex)
Provides:       tex(babel-chinese-simplified-singapore.tex)
Provides:       tex(babel-chinese-simplified.tex)
Provides:       tex(babel-chinese-traditional-hongkongsarchina.tex)
Provides:       tex(babel-chinese-traditional-macausarchina.tex)
Provides:       tex(babel-chinese-traditional.tex)
Provides:       tex(babel-chinese.tex)
Provides:       tex(babel-churchslavic-cyrs.tex)
Provides:       tex(babel-churchslavic-glag.tex)
Provides:       tex(babel-churchslavic-glagolitic.tex)
Provides:       tex(babel-churchslavic-oldcyrillic.tex)
Provides:       tex(babel-churchslavic.tex)
Provides:       tex(babel-churchslavonic.tex)
Provides:       tex(babel-classiclatin.tex)
Provides:       tex(babel-colognian.tex)
Provides:       tex(babel-coptic.tex)
Provides:       tex(babel-cornish.tex)
Provides:       tex(babel-croatian.tex)
Provides:       tex(babel-czech.tex)
Provides:       tex(babel-danish.tex)
Provides:       tex(babel-duala.tex)
Provides:       tex(babel-dutch.tex)
Provides:       tex(babel-dzongkha.tex)
Provides:       tex(babel-ecclesiasticlatin.tex)
Provides:       tex(babel-embu.tex)
Provides:       tex(babel-english-au.tex)
Provides:       tex(babel-english-australia.tex)
Provides:       tex(babel-english-ca.tex)
Provides:       tex(babel-english-canada.tex)
Provides:       tex(babel-english-gb.tex)
Provides:       tex(babel-english-newzealand.tex)
Provides:       tex(babel-english-nz.tex)
Provides:       tex(babel-english-unitedkingdom.tex)
Provides:       tex(babel-english-unitedstates.tex)
Provides:       tex(babel-english-us.tex)
Provides:       tex(babel-english.tex)
Provides:       tex(babel-esperanto.tex)
Provides:       tex(babel-estonian.tex)
Provides:       tex(babel-ewe.tex)
Provides:       tex(babel-ewondo.tex)
Provides:       tex(babel-faroese.tex)
Provides:       tex(babel-filipino.tex)
Provides:       tex(babel-finnish.tex)
Provides:       tex(babel-french-be.tex)
Provides:       tex(babel-french-belgium.tex)
Provides:       tex(babel-french-ca.tex)
Provides:       tex(babel-french-canada.tex)
Provides:       tex(babel-french-ch.tex)
Provides:       tex(babel-french-lu.tex)
Provides:       tex(babel-french-luxembourg.tex)
Provides:       tex(babel-french-switzerland.tex)
Provides:       tex(babel-french.tex)
Provides:       tex(babel-friulian.tex)
Provides:       tex(babel-fulah.tex)
Provides:       tex(babel-galician.tex)
Provides:       tex(babel-ganda.tex)
Provides:       tex(babel-georgian.tex)
Provides:       tex(babel-german-at.tex)
Provides:       tex(babel-german-austria-traditional.tex)
Provides:       tex(babel-german-austria.tex)
Provides:       tex(babel-german-ch.tex)
Provides:       tex(babel-german-switzerland-traditional.tex)
Provides:       tex(babel-german-switzerland.tex)
Provides:       tex(babel-german-traditional.tex)
Provides:       tex(babel-german.tex)
Provides:       tex(babel-greek.tex)
Provides:       tex(babel-gujarati.tex)
Provides:       tex(babel-gusii.tex)
Provides:       tex(babel-hausa-gh.tex)
Provides:       tex(babel-hausa-ghana.tex)
Provides:       tex(babel-hausa-ne.tex)
Provides:       tex(babel-hausa-niger.tex)
Provides:       tex(babel-hausa.tex)
Provides:       tex(babel-hawaiian.tex)
Provides:       tex(babel-hebrew.tex)
Provides:       tex(babel-hindi.tex)
Provides:       tex(babel-hungarian.tex)
Provides:       tex(babel-icelandic.tex)
Provides:       tex(babel-igbo.tex)
Provides:       tex(babel-inarisami.tex)
Provides:       tex(babel-indonesian.tex)
Provides:       tex(babel-interlingua.tex)
Provides:       tex(babel-irish.tex)
Provides:       tex(babel-italian.tex)
Provides:       tex(babel-japanese.tex)
Provides:       tex(babel-jolafonyi.tex)
Provides:       tex(babel-kabuverdianu.tex)
Provides:       tex(babel-kabyle.tex)
Provides:       tex(babel-kako.tex)
Provides:       tex(babel-kalaallisut.tex)
Provides:       tex(babel-kalenjin.tex)
Provides:       tex(babel-kamba.tex)
Provides:       tex(babel-kannada.tex)
Provides:       tex(babel-kashmiri.tex)
Provides:       tex(babel-kazakh.tex)
Provides:       tex(babel-khmer.tex)
Provides:       tex(babel-kikuyu.tex)
Provides:       tex(babel-kinyarwanda.tex)
Provides:       tex(babel-konkani.tex)
Provides:       tex(babel-korean.tex)
Provides:       tex(babel-koyraborosenni.tex)
Provides:       tex(babel-koyrachiini.tex)
Provides:       tex(babel-kwasio.tex)
Provides:       tex(babel-kyrgyz.tex)
Provides:       tex(babel-lakota.tex)
Provides:       tex(babel-langi.tex)
Provides:       tex(babel-lao.tex)
Provides:       tex(babel-latin.tex)
Provides:       tex(babel-latvian.tex)
Provides:       tex(babel-lingala.tex)
Provides:       tex(babel-lithuanian.tex)
Provides:       tex(babel-lowersorbian.tex)
Provides:       tex(babel-lsorbian.tex)
Provides:       tex(babel-lubakatanga.tex)
Provides:       tex(babel-luo.tex)
Provides:       tex(babel-luxembourgish.tex)
Provides:       tex(babel-luyia.tex)
Provides:       tex(babel-macedonian.tex)
Provides:       tex(babel-machame.tex)
Provides:       tex(babel-makhuwameetto.tex)
Provides:       tex(babel-makonde.tex)
Provides:       tex(babel-malagasy.tex)
Provides:       tex(babel-malay-bn.tex)
Provides:       tex(babel-malay-brunei.tex)
Provides:       tex(babel-malay-sg.tex)
Provides:       tex(babel-malay-singapore.tex)
Provides:       tex(babel-malay.tex)
Provides:       tex(babel-malayalam.tex)
Provides:       tex(babel-maltese.tex)
Provides:       tex(babel-manx.tex)
Provides:       tex(babel-marathi.tex)
Provides:       tex(babel-masai.tex)
Provides:       tex(babel-mazanderani.tex)
Provides:       tex(babel-medievallatin.tex)
Provides:       tex(babel-meru.tex)
Provides:       tex(babel-meta.tex)
Provides:       tex(babel-mexican.tex)
Provides:       tex(babel-mongolian.tex)
Provides:       tex(babel-monotonicgreek.tex)
Provides:       tex(babel-morisyen.tex)
Provides:       tex(babel-mundang.tex)
Provides:       tex(babel-nama.tex)
Provides:       tex(babel-naustrian.tex)
Provides:       tex(babel-nepali.tex)
Provides:       tex(babel-newzealand.tex)
Provides:       tex(babel-ngerman.tex)
Provides:       tex(babel-ngiemboon.tex)
Provides:       tex(babel-ngomba.tex)
Provides:       tex(babel-norsk.tex)
Provides:       tex(babel-northernluri.tex)
Provides:       tex(babel-northernsami.tex)
Provides:       tex(babel-northndebele.tex)
Provides:       tex(babel-norwegianbokmal.tex)
Provides:       tex(babel-norwegiannynorsk.tex)
Provides:       tex(babel-nswissgerman.tex)
Provides:       tex(babel-nuer.tex)
Provides:       tex(babel-nyankole.tex)
Provides:       tex(babel-nynorsk.tex)
Provides:       tex(babel-occitan.tex)
Provides:       tex(babel-oriya.tex)
Provides:       tex(babel-oromo.tex)
Provides:       tex(babel-ossetic.tex)
Provides:       tex(babel-pashto.tex)
Provides:       tex(babel-persian.tex)
Provides:       tex(babel-piedmontese.tex)
Provides:       tex(babel-polish.tex)
Provides:       tex(babel-polytonicgreek.tex)
Provides:       tex(babel-portuguese-br.tex)
Provides:       tex(babel-portuguese-brazil.tex)
Provides:       tex(babel-portuguese-portugal.tex)
Provides:       tex(babel-portuguese-pt.tex)
Provides:       tex(babel-portuguese.tex)
Provides:       tex(babel-punjabi-arab.tex)
Provides:       tex(babel-punjabi-arabic.tex)
Provides:       tex(babel-punjabi-gurmukhi.tex)
Provides:       tex(babel-punjabi-guru.tex)
Provides:       tex(babel-punjabi.tex)
Provides:       tex(babel-quechua.tex)
Provides:       tex(babel-romanian.tex)
Provides:       tex(babel-romansh.tex)
Provides:       tex(babel-rombo.tex)
Provides:       tex(babel-rundi.tex)
Provides:       tex(babel-russian.tex)
Provides:       tex(babel-rwa.tex)
Provides:       tex(babel-sakha.tex)
Provides:       tex(babel-samburu.tex)
Provides:       tex(babel-samin.tex)
Provides:       tex(babel-sango.tex)
Provides:       tex(babel-sangu.tex)
Provides:       tex(babel-sanskrit-beng.tex)
Provides:       tex(babel-sanskrit-bengali.tex)
Provides:       tex(babel-sanskrit-deva.tex)
Provides:       tex(babel-sanskrit-devanagari.tex)
Provides:       tex(babel-sanskrit-gujarati.tex)
Provides:       tex(babel-sanskrit-gujr.tex)
Provides:       tex(babel-sanskrit-kannada.tex)
Provides:       tex(babel-sanskrit-knda.tex)
Provides:       tex(babel-sanskrit-malayalam.tex)
Provides:       tex(babel-sanskrit-mlym.tex)
Provides:       tex(babel-sanskrit-telu.tex)
Provides:       tex(babel-sanskrit-telugu.tex)
Provides:       tex(babel-sanskrit.tex)
Provides:       tex(babel-scottishgaelic.tex)
Provides:       tex(babel-sena.tex)
Provides:       tex(babel-serbian-cyrillic-bosniaherzegovina.tex)
Provides:       tex(babel-serbian-cyrillic-kosovo.tex)
Provides:       tex(babel-serbian-cyrillic-montenegro.tex)
Provides:       tex(babel-serbian-cyrillic.tex)
Provides:       tex(babel-serbian-cyrl-ba.tex)
Provides:       tex(babel-serbian-cyrl-me.tex)
Provides:       tex(babel-serbian-cyrl-xk.tex)
Provides:       tex(babel-serbian-cyrl.tex)
Provides:       tex(babel-serbian-latin-bosniaherzegovina.tex)
Provides:       tex(babel-serbian-latin-kosovo.tex)
Provides:       tex(babel-serbian-latin-montenegro.tex)
Provides:       tex(babel-serbian-latin.tex)
Provides:       tex(babel-serbian-latn-ba.tex)
Provides:       tex(babel-serbian-latn-me.tex)
Provides:       tex(babel-serbian-latn-xk.tex)
Provides:       tex(babel-serbian-latn.tex)
Provides:       tex(babel-serbian.tex)
Provides:       tex(babel-shambala.tex)
Provides:       tex(babel-shona.tex)
Provides:       tex(babel-sichuanyi.tex)
Provides:       tex(babel-sinhala.tex)
Provides:       tex(babel-slovak.tex)
Provides:       tex(babel-slovene.tex)
Provides:       tex(babel-slovenian.tex)
Provides:       tex(babel-soga.tex)
Provides:       tex(babel-somali.tex)
Provides:       tex(babel-spanish-mexico.tex)
Provides:       tex(babel-spanish-mx.tex)
Provides:       tex(babel-spanish.tex)
Provides:       tex(babel-standardmoroccantamazight.tex)
Provides:       tex(babel-swahili.tex)
Provides:       tex(babel-swedish.tex)
Provides:       tex(babel-swissgerman.tex)
Provides:       tex(babel-syriac.tex)
Provides:       tex(babel-tachelhit-latin.tex)
Provides:       tex(babel-tachelhit-latn.tex)
Provides:       tex(babel-tachelhit-tfng.tex)
Provides:       tex(babel-tachelhit-tifinagh.tex)
Provides:       tex(babel-tachelhit.tex)
Provides:       tex(babel-taita.tex)
Provides:       tex(babel-tamil.tex)
Provides:       tex(babel-tasawaq.tex)
Provides:       tex(babel-telugu.tex)
Provides:       tex(babel-teso.tex)
Provides:       tex(babel-thai.tex)
Provides:       tex(babel-tibetan.tex)
Provides:       tex(babel-tigrinya.tex)
Provides:       tex(babel-tongan.tex)
Provides:       tex(babel-turkish.tex)
Provides:       tex(babel-turkmen.tex)
Provides:       tex(babel-ukenglish.tex)
Provides:       tex(babel-ukrainian.tex)
Provides:       tex(babel-uppersorbian.tex)
Provides:       tex(babel-urdu.tex)
Provides:       tex(babel-usenglish.tex)
Provides:       tex(babel-usorbian.tex)
Provides:       tex(babel-uyghur.tex)
Provides:       tex(babel-uzbek-arab.tex)
Provides:       tex(babel-uzbek-arabic.tex)
Provides:       tex(babel-uzbek-cyrillic.tex)
Provides:       tex(babel-uzbek-cyrl.tex)
Provides:       tex(babel-uzbek-latin.tex)
Provides:       tex(babel-uzbek-latn.tex)
Provides:       tex(babel-uzbek.tex)
Provides:       tex(babel-vai-latin.tex)
Provides:       tex(babel-vai-latn.tex)
Provides:       tex(babel-vai-vai.tex)
Provides:       tex(babel-vai-vaii.tex)
Provides:       tex(babel-vai.tex)
Provides:       tex(babel-vietnam.tex)
Provides:       tex(babel-vietnamese.tex)
Provides:       tex(babel-vunjo.tex)
Provides:       tex(babel-walser.tex)
Provides:       tex(babel-welsh.tex)
Provides:       tex(babel-westernfrisian.tex)
Provides:       tex(babel-yangben.tex)
Provides:       tex(babel-yiddish.tex)
Provides:       tex(babel-yoruba.tex)
Provides:       tex(babel-zarma.tex)
Provides:       tex(babel-zulu.tex)
Provides:       tex(babel.def)
Provides:       tex(babel.sty)
Provides:       tex(bahasa.sty)
Provides:       tex(bahasam.sty)
Provides:       tex(basque.sty)
Provides:       tex(blplain.tex)
Provides:       tex(bplain.tex)
Provides:       tex(breton.sty)
Provides:       tex(british.sty)
Provides:       tex(bulgarian.sty)
Provides:       tex(catalan.sty)
Provides:       tex(croatian.sty)
Provides:       tex(czech.sty)
Provides:       tex(danish.sty)
Provides:       tex(dutch.sty)
Provides:       tex(english.sty)
Provides:       tex(esperanto.sty)
Provides:       tex(estonian.sty)
Provides:       tex(finnish.sty)
Provides:       tex(francais.sty)
Provides:       tex(galician.sty)
Provides:       tex(germanb.sty)
Provides:       tex(greek.sty)
Provides:       tex(hebrew.sty)
Provides:       tex(hyphen.cfg)
Provides:       tex(icelandic.sty)
Provides:       tex(interlingua.sty)
Provides:       tex(irish.sty)
Provides:       tex(italian.sty)
Provides:       tex(latin.sty)
Provides:       tex(lsorbian.sty)
Provides:       tex(luababel.def)
Provides:       tex(magyar.sty)
Provides:       tex(naustrian.sty)
Provides:       tex(ngermanb.sty)
Provides:       tex(nil.ldf)
Provides:       tex(norsk.sty)
Provides:       tex(plain.def)
Provides:       tex(polish.sty)
Provides:       tex(portuges.sty)
Provides:       tex(romanian.sty)
Provides:       tex(russianb.sty)
Provides:       tex(samin.sty)
Provides:       tex(scottish.sty)
Provides:       tex(serbian.sty)
Provides:       tex(slovak.sty)
Provides:       tex(slovene.sty)
Provides:       tex(spanish.sty)
Provides:       tex(swedish.sty)
Provides:       tex(switch.def)
Provides:       tex(turkish.sty)
Provides:       tex(txtbabel.def)
Provides:       tex(ukraineb.sty)
Provides:       tex(usorbian.sty)
Provides:       tex(welsh.sty)
Provides:       tex(xebabel.def)
Requires:       tex(fontspec.sty)
Requires:       tex(language.def)
Requires:       tex(luatexbase.sty)
Requires:       tex(rlbabel.def)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source116:      babel.tar.xz
Source117:      babel.doc.tar.xz

%description -n texlive-babel
This package manages culturally-determined typographical (and
other) rules for a wide range of languages. A document may
select a single language to be supported, or it may select
several, in which case the document may switch from one
language to another in a variety of ways. Babel uses
contributed configuration files that provide the detail of what
has to be done for each language. Included is also a set of ini
files for about 200 languages. Many language styles work with
pdfLaTeX, as well as with XeLaTeX and LuaLaTeX, out of the box.
A few even work with plain formats.

%package -n texlive-babel-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.42svn54487
Release:        0
Summary:        Documentation for texlive-babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-doc
This package includes the documentation for texlive-babel

%post -n texlive-babel
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/babel/README.md
%{_texmfdistdir}/doc/latex/babel/babel.pdf

%files -n texlive-babel
%defattr(-,root,root,755)
%{_texmfdistdir}/makeindex/babel/bbglo.ist
%{_texmfdistdir}/makeindex/babel/bbind.ist
%{_texmfdistdir}/tex/generic/babel/UKenglish.sty
%{_texmfdistdir}/tex/generic/babel/USenglish.sty
%{_texmfdistdir}/tex/generic/babel/afrikaans.sty
%{_texmfdistdir}/tex/generic/babel/albanian.sty
%{_texmfdistdir}/tex/generic/babel/american.sty
%{_texmfdistdir}/tex/generic/babel/austrian.sty
%{_texmfdistdir}/tex/generic/babel/babel-bidi-basic-r.lua
%{_texmfdistdir}/tex/generic/babel/babel-bidi-basic.lua
%{_texmfdistdir}/tex/generic/babel/babel-data-bidi.lua
%{_texmfdistdir}/tex/generic/babel/babel-data-cjk.lua
%{_texmfdistdir}/tex/generic/babel/babel.def
%{_texmfdistdir}/tex/generic/babel/babel.sty
%{_texmfdistdir}/tex/generic/babel/bahasa.sty
%{_texmfdistdir}/tex/generic/babel/bahasam.sty
%{_texmfdistdir}/tex/generic/babel/basque.sty
%{_texmfdistdir}/tex/generic/babel/blplain.tex
%{_texmfdistdir}/tex/generic/babel/bplain.tex
%{_texmfdistdir}/tex/generic/babel/breton.sty
%{_texmfdistdir}/tex/generic/babel/british.sty
%{_texmfdistdir}/tex/generic/babel/bulgarian.sty
%{_texmfdistdir}/tex/generic/babel/catalan.sty
%{_texmfdistdir}/tex/generic/babel/croatian.sty
%{_texmfdistdir}/tex/generic/babel/czech.sty
%{_texmfdistdir}/tex/generic/babel/danish.sty
%{_texmfdistdir}/tex/generic/babel/dutch.sty
%{_texmfdistdir}/tex/generic/babel/english.sty
%{_texmfdistdir}/tex/generic/babel/esperanto.sty
%{_texmfdistdir}/tex/generic/babel/estonian.sty
%{_texmfdistdir}/tex/generic/babel/finnish.sty
%{_texmfdistdir}/tex/generic/babel/francais.sty
%{_texmfdistdir}/tex/generic/babel/galician.sty
%{_texmfdistdir}/tex/generic/babel/germanb.sty
%{_texmfdistdir}/tex/generic/babel/greek.sty
%{_texmfdistdir}/tex/generic/babel/hebrew.sty
%{_texmfdistdir}/tex/generic/babel/hyphen.cfg
%{_texmfdistdir}/tex/generic/babel/icelandic.sty
%{_texmfdistdir}/tex/generic/babel/interlingua.sty
%{_texmfdistdir}/tex/generic/babel/irish.sty
%{_texmfdistdir}/tex/generic/babel/italian.sty
%{_texmfdistdir}/tex/generic/babel/latin.sty
%{_texmfdistdir}/tex/generic/babel/locale/af/babel-af.ini
%{_texmfdistdir}/tex/generic/babel/locale/af/babel-afrikaans.tex
%{_texmfdistdir}/tex/generic/babel/locale/agq/babel-aghem.tex
%{_texmfdistdir}/tex/generic/babel/locale/agq/babel-agq.ini
%{_texmfdistdir}/tex/generic/babel/locale/ak/babel-ak.ini
%{_texmfdistdir}/tex/generic/babel/locale/ak/babel-akan.tex
%{_texmfdistdir}/tex/generic/babel/locale/am/babel-am.ini
%{_texmfdistdir}/tex/generic/babel/locale/am/babel-amharic.tex
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-ar-DZ.ini
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-ar-MA.ini
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-ar-SY.ini
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-ar.ini
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-arabic-algeria.tex
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-arabic-dz.tex
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-arabic-ma.tex
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-arabic-morocco.tex
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-arabic-sy.tex
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-arabic-syria.tex
%{_texmfdistdir}/tex/generic/babel/locale/ar/babel-arabic.tex
%{_texmfdistdir}/tex/generic/babel/locale/as/babel-as.ini
%{_texmfdistdir}/tex/generic/babel/locale/as/babel-assamese.tex
%{_texmfdistdir}/tex/generic/babel/locale/asa/babel-asa.ini
%{_texmfdistdir}/tex/generic/babel/locale/asa/babel-asu.tex
%{_texmfdistdir}/tex/generic/babel/locale/ast/babel-ast.ini
%{_texmfdistdir}/tex/generic/babel/locale/ast/babel-asturian.tex
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-az-Cyrl.ini
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-az-Latn.ini
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-az.ini
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-azerbaijani-cyrillic.tex
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-azerbaijani-cyrl.tex
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-azerbaijani-latin.tex
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-azerbaijani-latn.tex
%{_texmfdistdir}/tex/generic/babel/locale/az/babel-azerbaijani.tex
%{_texmfdistdir}/tex/generic/babel/locale/bas/babel-bas.ini
%{_texmfdistdir}/tex/generic/babel/locale/bas/babel-basaa.tex
%{_texmfdistdir}/tex/generic/babel/locale/be/babel-be.ini
%{_texmfdistdir}/tex/generic/babel/locale/be/babel-belarusian.tex
%{_texmfdistdir}/tex/generic/babel/locale/bem/babel-bem.ini
%{_texmfdistdir}/tex/generic/babel/locale/bem/babel-bemba.tex
%{_texmfdistdir}/tex/generic/babel/locale/bez/babel-bena.tex
%{_texmfdistdir}/tex/generic/babel/locale/bez/babel-bez.ini
%{_texmfdistdir}/tex/generic/babel/locale/bg/babel-bg.ini
%{_texmfdistdir}/tex/generic/babel/locale/bg/babel-bulgarian.tex
%{_texmfdistdir}/tex/generic/babel/locale/bm/babel-bambara.tex
%{_texmfdistdir}/tex/generic/babel/locale/bm/babel-bm.ini
%{_texmfdistdir}/tex/generic/babel/locale/bn/babel-bengali.tex
%{_texmfdistdir}/tex/generic/babel/locale/bn/babel-bn.ini
%{_texmfdistdir}/tex/generic/babel/locale/bo/babel-bo.ini
%{_texmfdistdir}/tex/generic/babel/locale/bo/babel-tibetan.tex
%{_texmfdistdir}/tex/generic/babel/locale/br/babel-br.ini
%{_texmfdistdir}/tex/generic/babel/locale/br/babel-breton.tex
%{_texmfdistdir}/tex/generic/babel/locale/brx/babel-bodo.tex
%{_texmfdistdir}/tex/generic/babel/locale/brx/babel-brx.ini
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bosnian-cyrillic.tex
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bosnian-cyrl.tex
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bosnian-latin.tex
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bosnian-latn.tex
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bosnian.tex
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bs-Cyrl.ini
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bs-Latn.ini
%{_texmfdistdir}/tex/generic/babel/locale/bs/babel-bs.ini
%{_texmfdistdir}/tex/generic/babel/locale/ca/babel-ca.ini
%{_texmfdistdir}/tex/generic/babel/locale/ca/babel-catalan.tex
%{_texmfdistdir}/tex/generic/babel/locale/ce/babel-ce.ini
%{_texmfdistdir}/tex/generic/babel/locale/ce/babel-chechen.tex
%{_texmfdistdir}/tex/generic/babel/locale/cgg/babel-cgg.ini
%{_texmfdistdir}/tex/generic/babel/locale/cgg/babel-chiga.tex
%{_texmfdistdir}/tex/generic/babel/locale/chr/babel-cherokee.tex
%{_texmfdistdir}/tex/generic/babel/locale/chr/babel-chr.ini
%{_texmfdistdir}/tex/generic/babel/locale/ckb/babel-centralkurdish.tex
%{_texmfdistdir}/tex/generic/babel/locale/ckb/babel-ckb.ini
%{_texmfdistdir}/tex/generic/babel/locale/cop/babel-cop.ini
%{_texmfdistdir}/tex/generic/babel/locale/cop/babel-coptic.tex
%{_texmfdistdir}/tex/generic/babel/locale/cs/babel-cs.ini
%{_texmfdistdir}/tex/generic/babel/locale/cs/babel-czech.tex
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-churchslavic-cyrs.tex
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-churchslavic-glag.tex
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-churchslavic-glagolitic.tex
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-churchslavic-oldcyrillic.tex
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-churchslavic.tex
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-churchslavonic.tex
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-cu-Cyrs.ini
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-cu-Glag.ini
%{_texmfdistdir}/tex/generic/babel/locale/cu/babel-cu.ini
%{_texmfdistdir}/tex/generic/babel/locale/cy/babel-cy.ini
%{_texmfdistdir}/tex/generic/babel/locale/cy/babel-welsh.tex
%{_texmfdistdir}/tex/generic/babel/locale/da/babel-da.ini
%{_texmfdistdir}/tex/generic/babel/locale/da/babel-danish.tex
%{_texmfdistdir}/tex/generic/babel/locale/dav/babel-dav.ini
%{_texmfdistdir}/tex/generic/babel/locale/dav/babel-taita.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-austrian.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-1901.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-1996.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-AT-1901.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-AT-1996.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-AT.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-CH-1901.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-CH-1996.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de-CH.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-de.ini
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german-at.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german-austria-traditional.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german-austria.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german-ch.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german-switzerland-traditional.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german-switzerland.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german-traditional.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-german.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-naustrian.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-ngerman.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-nswissgerman.tex
%{_texmfdistdir}/tex/generic/babel/locale/de/babel-swissgerman.tex
%{_texmfdistdir}/tex/generic/babel/locale/dje/babel-dje.ini
%{_texmfdistdir}/tex/generic/babel/locale/dje/babel-zarma.tex
%{_texmfdistdir}/tex/generic/babel/locale/dsb/babel-dsb.ini
%{_texmfdistdir}/tex/generic/babel/locale/dsb/babel-lowersorbian.tex
%{_texmfdistdir}/tex/generic/babel/locale/dsb/babel-lsorbian.tex
%{_texmfdistdir}/tex/generic/babel/locale/dua/babel-dua.ini
%{_texmfdistdir}/tex/generic/babel/locale/dua/babel-duala.tex
%{_texmfdistdir}/tex/generic/babel/locale/dyo/babel-dyo.ini
%{_texmfdistdir}/tex/generic/babel/locale/dyo/babel-jolafonyi.tex
%{_texmfdistdir}/tex/generic/babel/locale/dz/babel-dz.ini
%{_texmfdistdir}/tex/generic/babel/locale/dz/babel-dzongkha.tex
%{_texmfdistdir}/tex/generic/babel/locale/ebu/babel-ebu.ini
%{_texmfdistdir}/tex/generic/babel/locale/ebu/babel-embu.tex
%{_texmfdistdir}/tex/generic/babel/locale/ee/babel-ee.ini
%{_texmfdistdir}/tex/generic/babel/locale/ee/babel-ewe.tex
%{_texmfdistdir}/tex/generic/babel/locale/el/babel-el-polyton.ini
%{_texmfdistdir}/tex/generic/babel/locale/el/babel-el.ini
%{_texmfdistdir}/tex/generic/babel/locale/el/babel-greek.tex
%{_texmfdistdir}/tex/generic/babel/locale/el/babel-monotonicgreek.tex
%{_texmfdistdir}/tex/generic/babel/locale/el/babel-polytonicgreek.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-american.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-australian.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-british.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-canadian.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-en-AU.ini
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-en-CA.ini
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-en-GB.ini
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-en-NZ.ini
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-en-US.ini
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-en.ini
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-au.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-australia.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-ca.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-canada.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-gb.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-newzealand.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-nz.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-unitedkingdom.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-unitedstates.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english-us.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-english.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-newzealand.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-ukenglish.tex
%{_texmfdistdir}/tex/generic/babel/locale/en/babel-usenglish.tex
%{_texmfdistdir}/tex/generic/babel/locale/eo/babel-eo.ini
%{_texmfdistdir}/tex/generic/babel/locale/eo/babel-esperanto.tex
%{_texmfdistdir}/tex/generic/babel/locale/es/babel-es-MX.ini
%{_texmfdistdir}/tex/generic/babel/locale/es/babel-es.ini
%{_texmfdistdir}/tex/generic/babel/locale/es/babel-mexican.tex
%{_texmfdistdir}/tex/generic/babel/locale/es/babel-spanish-mexico.tex
%{_texmfdistdir}/tex/generic/babel/locale/es/babel-spanish-mx.tex
%{_texmfdistdir}/tex/generic/babel/locale/es/babel-spanish.tex
%{_texmfdistdir}/tex/generic/babel/locale/et/babel-estonian.tex
%{_texmfdistdir}/tex/generic/babel/locale/et/babel-et.ini
%{_texmfdistdir}/tex/generic/babel/locale/eu/babel-basque.tex
%{_texmfdistdir}/tex/generic/babel/locale/eu/babel-eu.ini
%{_texmfdistdir}/tex/generic/babel/locale/ewo/babel-ewo.ini
%{_texmfdistdir}/tex/generic/babel/locale/ewo/babel-ewondo.tex
%{_texmfdistdir}/tex/generic/babel/locale/fa/babel-fa.ini
%{_texmfdistdir}/tex/generic/babel/locale/fa/babel-persian.tex
%{_texmfdistdir}/tex/generic/babel/locale/ff/babel-ff.ini
%{_texmfdistdir}/tex/generic/babel/locale/ff/babel-fulah.tex
%{_texmfdistdir}/tex/generic/babel/locale/fi/babel-fi.ini
%{_texmfdistdir}/tex/generic/babel/locale/fi/babel-finnish.tex
%{_texmfdistdir}/tex/generic/babel/locale/fil/babel-fil.ini
%{_texmfdistdir}/tex/generic/babel/locale/fil/babel-filipino.tex
%{_texmfdistdir}/tex/generic/babel/locale/fo/babel-faroese.tex
%{_texmfdistdir}/tex/generic/babel/locale/fo/babel-fo.ini
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-fr-BE.ini
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-fr-CA.ini
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-fr-CH.ini
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-fr-LU.ini
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-fr.ini
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-be.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-belgium.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-ca.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-canada.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-ch.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-lu.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-luxembourg.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french-switzerland.tex
%{_texmfdistdir}/tex/generic/babel/locale/fr/babel-french.tex
%{_texmfdistdir}/tex/generic/babel/locale/fur/babel-friulian.tex
%{_texmfdistdir}/tex/generic/babel/locale/fur/babel-fur.ini
%{_texmfdistdir}/tex/generic/babel/locale/fy/babel-fy.ini
%{_texmfdistdir}/tex/generic/babel/locale/fy/babel-westernfrisian.tex
%{_texmfdistdir}/tex/generic/babel/locale/ga/babel-ga.ini
%{_texmfdistdir}/tex/generic/babel/locale/ga/babel-irish.tex
%{_texmfdistdir}/tex/generic/babel/locale/gd/babel-gd.ini
%{_texmfdistdir}/tex/generic/babel/locale/gd/babel-scottishgaelic.tex
%{_texmfdistdir}/tex/generic/babel/locale/gl/babel-galician.tex
%{_texmfdistdir}/tex/generic/babel/locale/gl/babel-gl.ini
%{_texmfdistdir}/tex/generic/babel/locale/grc/babel-ancientgreek.tex
%{_texmfdistdir}/tex/generic/babel/locale/grc/babel-grc.ini
%{_texmfdistdir}/tex/generic/babel/locale/gsw/babel-gsw.ini
%{_texmfdistdir}/tex/generic/babel/locale/gu/babel-gu.ini
%{_texmfdistdir}/tex/generic/babel/locale/gu/babel-gujarati.tex
%{_texmfdistdir}/tex/generic/babel/locale/guz/babel-gusii.tex
%{_texmfdistdir}/tex/generic/babel/locale/guz/babel-guz.ini
%{_texmfdistdir}/tex/generic/babel/locale/gv/babel-gv.ini
%{_texmfdistdir}/tex/generic/babel/locale/gv/babel-manx.tex
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-ha-GH.ini
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-ha-NE.ini
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-ha.ini
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-hausa-gh.tex
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-hausa-ghana.tex
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-hausa-ne.tex
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-hausa-niger.tex
%{_texmfdistdir}/tex/generic/babel/locale/ha/babel-hausa.tex
%{_texmfdistdir}/tex/generic/babel/locale/haw/babel-haw.ini
%{_texmfdistdir}/tex/generic/babel/locale/haw/babel-hawaiian.tex
%{_texmfdistdir}/tex/generic/babel/locale/he/babel-he.ini
%{_texmfdistdir}/tex/generic/babel/locale/he/babel-hebrew.tex
%{_texmfdistdir}/tex/generic/babel/locale/hi/babel-hi.ini
%{_texmfdistdir}/tex/generic/babel/locale/hi/babel-hindi.tex
%{_texmfdistdir}/tex/generic/babel/locale/hr/babel-croatian.tex
%{_texmfdistdir}/tex/generic/babel/locale/hr/babel-hr.ini
%{_texmfdistdir}/tex/generic/babel/locale/hsb/babel-hsb.ini
%{_texmfdistdir}/tex/generic/babel/locale/hsb/babel-uppersorbian.tex
%{_texmfdistdir}/tex/generic/babel/locale/hsb/babel-usorbian.tex
%{_texmfdistdir}/tex/generic/babel/locale/hu/babel-hu.ini
%{_texmfdistdir}/tex/generic/babel/locale/hu/babel-hungarian.tex
%{_texmfdistdir}/tex/generic/babel/locale/hy/babel-armenian.tex
%{_texmfdistdir}/tex/generic/babel/locale/hy/babel-hy.ini
%{_texmfdistdir}/tex/generic/babel/locale/ia/babel-ia.ini
%{_texmfdistdir}/tex/generic/babel/locale/ia/babel-interlingua.tex
%{_texmfdistdir}/tex/generic/babel/locale/id/babel-id.ini
%{_texmfdistdir}/tex/generic/babel/locale/id/babel-indonesian.tex
%{_texmfdistdir}/tex/generic/babel/locale/ig/babel-ig.ini
%{_texmfdistdir}/tex/generic/babel/locale/ig/babel-igbo.tex
%{_texmfdistdir}/tex/generic/babel/locale/ii/babel-ii.ini
%{_texmfdistdir}/tex/generic/babel/locale/ii/babel-sichuanyi.tex
%{_texmfdistdir}/tex/generic/babel/locale/is/babel-icelandic.tex
%{_texmfdistdir}/tex/generic/babel/locale/is/babel-is.ini
%{_texmfdistdir}/tex/generic/babel/locale/it/babel-it.ini
%{_texmfdistdir}/tex/generic/babel/locale/it/babel-italian.tex
%{_texmfdistdir}/tex/generic/babel/locale/ja/babel-ja.ini
%{_texmfdistdir}/tex/generic/babel/locale/ja/babel-japanese.tex
%{_texmfdistdir}/tex/generic/babel/locale/jgo/babel-jgo.ini
%{_texmfdistdir}/tex/generic/babel/locale/jgo/babel-ngomba.tex
%{_texmfdistdir}/tex/generic/babel/locale/jmc/babel-jmc.ini
%{_texmfdistdir}/tex/generic/babel/locale/jmc/babel-machame.tex
%{_texmfdistdir}/tex/generic/babel/locale/ka/babel-georgian.tex
%{_texmfdistdir}/tex/generic/babel/locale/ka/babel-ka.ini
%{_texmfdistdir}/tex/generic/babel/locale/kab/babel-kab.ini
%{_texmfdistdir}/tex/generic/babel/locale/kab/babel-kabyle.tex
%{_texmfdistdir}/tex/generic/babel/locale/kam/babel-kam.ini
%{_texmfdistdir}/tex/generic/babel/locale/kam/babel-kamba.tex
%{_texmfdistdir}/tex/generic/babel/locale/kde/babel-kde.ini
%{_texmfdistdir}/tex/generic/babel/locale/kde/babel-makonde.tex
%{_texmfdistdir}/tex/generic/babel/locale/kea/babel-kabuverdianu.tex
%{_texmfdistdir}/tex/generic/babel/locale/kea/babel-kea.ini
%{_texmfdistdir}/tex/generic/babel/locale/khq/babel-khq.ini
%{_texmfdistdir}/tex/generic/babel/locale/khq/babel-koyrachiini.tex
%{_texmfdistdir}/tex/generic/babel/locale/ki/babel-ki.ini
%{_texmfdistdir}/tex/generic/babel/locale/ki/babel-kikuyu.tex
%{_texmfdistdir}/tex/generic/babel/locale/kk/babel-kazakh.tex
%{_texmfdistdir}/tex/generic/babel/locale/kk/babel-kk.ini
%{_texmfdistdir}/tex/generic/babel/locale/kkj/babel-kako.tex
%{_texmfdistdir}/tex/generic/babel/locale/kkj/babel-kkj.ini
%{_texmfdistdir}/tex/generic/babel/locale/kl/babel-kalaallisut.tex
%{_texmfdistdir}/tex/generic/babel/locale/kl/babel-kl.ini
%{_texmfdistdir}/tex/generic/babel/locale/kln/babel-kalenjin.tex
%{_texmfdistdir}/tex/generic/babel/locale/kln/babel-kln.ini
%{_texmfdistdir}/tex/generic/babel/locale/km/babel-khmer.tex
%{_texmfdistdir}/tex/generic/babel/locale/km/babel-km.ini
%{_texmfdistdir}/tex/generic/babel/locale/kn/babel-kannada.tex
%{_texmfdistdir}/tex/generic/babel/locale/kn/babel-kn.ini
%{_texmfdistdir}/tex/generic/babel/locale/ko/babel-ko.ini
%{_texmfdistdir}/tex/generic/babel/locale/ko/babel-korean.tex
%{_texmfdistdir}/tex/generic/babel/locale/kok/babel-kok.ini
%{_texmfdistdir}/tex/generic/babel/locale/kok/babel-konkani.tex
%{_texmfdistdir}/tex/generic/babel/locale/ks/babel-kashmiri.tex
%{_texmfdistdir}/tex/generic/babel/locale/ks/babel-ks.ini
%{_texmfdistdir}/tex/generic/babel/locale/ksb/babel-ksb.ini
%{_texmfdistdir}/tex/generic/babel/locale/ksb/babel-shambala.tex
%{_texmfdistdir}/tex/generic/babel/locale/ksf/babel-bafia.tex
%{_texmfdistdir}/tex/generic/babel/locale/ksf/babel-ksf.ini
%{_texmfdistdir}/tex/generic/babel/locale/ksh/babel-colognian.tex
%{_texmfdistdir}/tex/generic/babel/locale/ksh/babel-ksh.ini
%{_texmfdistdir}/tex/generic/babel/locale/kw/babel-cornish.tex
%{_texmfdistdir}/tex/generic/babel/locale/kw/babel-kw.ini
%{_texmfdistdir}/tex/generic/babel/locale/ky/babel-ky.ini
%{_texmfdistdir}/tex/generic/babel/locale/ky/babel-kyrgyz.tex
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-classiclatin.tex
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-ecclesiasticlatin.tex
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-la-x-classic.ini
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-la-x-ecclesia.ini
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-la-x-medieval.ini
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-la.ini
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-latin.tex
%{_texmfdistdir}/tex/generic/babel/locale/la/babel-medievallatin.tex
%{_texmfdistdir}/tex/generic/babel/locale/lag/babel-lag.ini
%{_texmfdistdir}/tex/generic/babel/locale/lag/babel-langi.tex
%{_texmfdistdir}/tex/generic/babel/locale/lb/babel-lb.ini
%{_texmfdistdir}/tex/generic/babel/locale/lb/babel-luxembourgish.tex
%{_texmfdistdir}/tex/generic/babel/locale/lg/babel-ganda.tex
%{_texmfdistdir}/tex/generic/babel/locale/lg/babel-lg.ini
%{_texmfdistdir}/tex/generic/babel/locale/lkt/babel-lakota.tex
%{_texmfdistdir}/tex/generic/babel/locale/lkt/babel-lkt.ini
%{_texmfdistdir}/tex/generic/babel/locale/ln/babel-lingala.tex
%{_texmfdistdir}/tex/generic/babel/locale/ln/babel-ln.ini
%{_texmfdistdir}/tex/generic/babel/locale/lo/babel-lao.tex
%{_texmfdistdir}/tex/generic/babel/locale/lo/babel-lo.ini
%{_texmfdistdir}/tex/generic/babel/locale/lrc/babel-lrc.ini
%{_texmfdistdir}/tex/generic/babel/locale/lrc/babel-northernluri.tex
%{_texmfdistdir}/tex/generic/babel/locale/lt/babel-lithuanian.tex
%{_texmfdistdir}/tex/generic/babel/locale/lt/babel-lt.ini
%{_texmfdistdir}/tex/generic/babel/locale/lu/babel-lu.ini
%{_texmfdistdir}/tex/generic/babel/locale/lu/babel-lubakatanga.tex
%{_texmfdistdir}/tex/generic/babel/locale/luo/babel-luo.ini
%{_texmfdistdir}/tex/generic/babel/locale/luo/babel-luo.tex
%{_texmfdistdir}/tex/generic/babel/locale/luy/babel-luy.ini
%{_texmfdistdir}/tex/generic/babel/locale/luy/babel-luyia.tex
%{_texmfdistdir}/tex/generic/babel/locale/lv/babel-latvian.tex
%{_texmfdistdir}/tex/generic/babel/locale/lv/babel-lv.ini
%{_texmfdistdir}/tex/generic/babel/locale/mas/babel-mas.ini
%{_texmfdistdir}/tex/generic/babel/locale/mas/babel-masai.tex
%{_texmfdistdir}/tex/generic/babel/locale/mer/babel-mer.ini
%{_texmfdistdir}/tex/generic/babel/locale/mer/babel-meru.tex
%{_texmfdistdir}/tex/generic/babel/locale/mfe/babel-mfe.ini
%{_texmfdistdir}/tex/generic/babel/locale/mfe/babel-morisyen.tex
%{_texmfdistdir}/tex/generic/babel/locale/mg/babel-malagasy.tex
%{_texmfdistdir}/tex/generic/babel/locale/mg/babel-mg.ini
%{_texmfdistdir}/tex/generic/babel/locale/mgh/babel-makhuwameetto.tex
%{_texmfdistdir}/tex/generic/babel/locale/mgh/babel-mgh.ini
%{_texmfdistdir}/tex/generic/babel/locale/mgo/babel-meta.tex
%{_texmfdistdir}/tex/generic/babel/locale/mgo/babel-mgo.ini
%{_texmfdistdir}/tex/generic/babel/locale/mk/babel-macedonian.tex
%{_texmfdistdir}/tex/generic/babel/locale/mk/babel-mk.ini
%{_texmfdistdir}/tex/generic/babel/locale/ml/babel-malayalam.tex
%{_texmfdistdir}/tex/generic/babel/locale/ml/babel-ml.ini
%{_texmfdistdir}/tex/generic/babel/locale/mn/babel-mn.ini
%{_texmfdistdir}/tex/generic/babel/locale/mn/babel-mongolian.tex
%{_texmfdistdir}/tex/generic/babel/locale/mr/babel-marathi.tex
%{_texmfdistdir}/tex/generic/babel/locale/mr/babel-mr.ini
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-malay-bn.tex
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-malay-brunei.tex
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-malay-sg.tex
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-malay-singapore.tex
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-malay.tex
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-ms-BN.ini
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-ms-SG.ini
%{_texmfdistdir}/tex/generic/babel/locale/ms/babel-ms.ini
%{_texmfdistdir}/tex/generic/babel/locale/mt/babel-maltese.tex
%{_texmfdistdir}/tex/generic/babel/locale/mt/babel-mt.ini
%{_texmfdistdir}/tex/generic/babel/locale/mua/babel-mua.ini
%{_texmfdistdir}/tex/generic/babel/locale/mua/babel-mundang.tex
%{_texmfdistdir}/tex/generic/babel/locale/my/babel-burmese.tex
%{_texmfdistdir}/tex/generic/babel/locale/my/babel-my.ini
%{_texmfdistdir}/tex/generic/babel/locale/mzn/babel-mazanderani.tex
%{_texmfdistdir}/tex/generic/babel/locale/mzn/babel-mzn.ini
%{_texmfdistdir}/tex/generic/babel/locale/naq/babel-nama.tex
%{_texmfdistdir}/tex/generic/babel/locale/naq/babel-naq.ini
%{_texmfdistdir}/tex/generic/babel/locale/nb/babel-nb.ini
%{_texmfdistdir}/tex/generic/babel/locale/nb/babel-norsk.tex
%{_texmfdistdir}/tex/generic/babel/locale/nb/babel-norwegianbokmal.tex
%{_texmfdistdir}/tex/generic/babel/locale/nd/babel-nd.ini
%{_texmfdistdir}/tex/generic/babel/locale/nd/babel-northndebele.tex
%{_texmfdistdir}/tex/generic/babel/locale/ne/babel-ne.ini
%{_texmfdistdir}/tex/generic/babel/locale/ne/babel-nepali.tex
%{_texmfdistdir}/tex/generic/babel/locale/nl/babel-dutch.tex
%{_texmfdistdir}/tex/generic/babel/locale/nl/babel-nl.ini
%{_texmfdistdir}/tex/generic/babel/locale/nmg/babel-kwasio.tex
%{_texmfdistdir}/tex/generic/babel/locale/nmg/babel-nmg.ini
%{_texmfdistdir}/tex/generic/babel/locale/nn/babel-nn.ini
%{_texmfdistdir}/tex/generic/babel/locale/nn/babel-norwegiannynorsk.tex
%{_texmfdistdir}/tex/generic/babel/locale/nn/babel-nynorsk.tex
%{_texmfdistdir}/tex/generic/babel/locale/nnh/babel-ngiemboon.tex
%{_texmfdistdir}/tex/generic/babel/locale/nnh/babel-nnh.ini
%{_texmfdistdir}/tex/generic/babel/locale/nus/babel-nuer.tex
%{_texmfdistdir}/tex/generic/babel/locale/nus/babel-nus.ini
%{_texmfdistdir}/tex/generic/babel/locale/nyn/babel-nyankole.tex
%{_texmfdistdir}/tex/generic/babel/locale/nyn/babel-nyn.ini
%{_texmfdistdir}/tex/generic/babel/locale/oc/babel-oc.ini
%{_texmfdistdir}/tex/generic/babel/locale/oc/babel-occitan.tex
%{_texmfdistdir}/tex/generic/babel/locale/om/babel-om.ini
%{_texmfdistdir}/tex/generic/babel/locale/om/babel-oromo.tex
%{_texmfdistdir}/tex/generic/babel/locale/or/babel-or.ini
%{_texmfdistdir}/tex/generic/babel/locale/or/babel-oriya.tex
%{_texmfdistdir}/tex/generic/babel/locale/os/babel-os.ini
%{_texmfdistdir}/tex/generic/babel/locale/os/babel-ossetic.tex
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-pa-Arab.ini
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-pa-Guru.ini
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-pa.ini
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-punjabi-arab.tex
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-punjabi-arabic.tex
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-punjabi-gurmukhi.tex
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-punjabi-guru.tex
%{_texmfdistdir}/tex/generic/babel/locale/pa/babel-punjabi.tex
%{_texmfdistdir}/tex/generic/babel/locale/pl/babel-pl.ini
%{_texmfdistdir}/tex/generic/babel/locale/pl/babel-polish.tex
%{_texmfdistdir}/tex/generic/babel/locale/pms/babel-piedmontese.tex
%{_texmfdistdir}/tex/generic/babel/locale/pms/babel-pms.ini
%{_texmfdistdir}/tex/generic/babel/locale/ps/babel-pashto.tex
%{_texmfdistdir}/tex/generic/babel/locale/ps/babel-ps.ini
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-brazilian.tex
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-portuguese-br.tex
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-portuguese-brazil.tex
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-portuguese-portugal.tex
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-portuguese-pt.tex
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-portuguese.tex
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-pt-BR.ini
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-pt-PT.ini
%{_texmfdistdir}/tex/generic/babel/locale/pt/babel-pt.ini
%{_texmfdistdir}/tex/generic/babel/locale/qu/babel-qu.ini
%{_texmfdistdir}/tex/generic/babel/locale/qu/babel-quechua.tex
%{_texmfdistdir}/tex/generic/babel/locale/rm/babel-rm.ini
%{_texmfdistdir}/tex/generic/babel/locale/rm/babel-romansh.tex
%{_texmfdistdir}/tex/generic/babel/locale/rn/babel-rn.ini
%{_texmfdistdir}/tex/generic/babel/locale/rn/babel-rundi.tex
%{_texmfdistdir}/tex/generic/babel/locale/ro/babel-ro.ini
%{_texmfdistdir}/tex/generic/babel/locale/ro/babel-romanian.tex
%{_texmfdistdir}/tex/generic/babel/locale/rof/babel-rof.ini
%{_texmfdistdir}/tex/generic/babel/locale/rof/babel-rombo.tex
%{_texmfdistdir}/tex/generic/babel/locale/ru/babel-ru.ini
%{_texmfdistdir}/tex/generic/babel/locale/ru/babel-russian.tex
%{_texmfdistdir}/tex/generic/babel/locale/rw/babel-kinyarwanda.tex
%{_texmfdistdir}/tex/generic/babel/locale/rw/babel-rw.ini
%{_texmfdistdir}/tex/generic/babel/locale/rwk/babel-rwa.tex
%{_texmfdistdir}/tex/generic/babel/locale/rwk/babel-rwk.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sa-Beng.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sa-Deva.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sa-Gujr.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sa-Knda.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sa-Mlym.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sa-Telu.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sa.ini
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-beng.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-bengali.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-deva.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-devanagari.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-gujarati.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-gujr.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-kannada.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-knda.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-malayalam.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-mlym.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-telu.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit-telugu.tex
%{_texmfdistdir}/tex/generic/babel/locale/sa/babel-sanskrit.tex
%{_texmfdistdir}/tex/generic/babel/locale/sah/babel-sah.ini
%{_texmfdistdir}/tex/generic/babel/locale/sah/babel-sakha.tex
%{_texmfdistdir}/tex/generic/babel/locale/saq/babel-samburu.tex
%{_texmfdistdir}/tex/generic/babel/locale/saq/babel-saq.ini
%{_texmfdistdir}/tex/generic/babel/locale/sbp/babel-sangu.tex
%{_texmfdistdir}/tex/generic/babel/locale/sbp/babel-sbp.ini
%{_texmfdistdir}/tex/generic/babel/locale/se/babel-northernsami.tex
%{_texmfdistdir}/tex/generic/babel/locale/se/babel-samin.tex
%{_texmfdistdir}/tex/generic/babel/locale/se/babel-se.ini
%{_texmfdistdir}/tex/generic/babel/locale/seh/babel-seh.ini
%{_texmfdistdir}/tex/generic/babel/locale/seh/babel-sena.tex
%{_texmfdistdir}/tex/generic/babel/locale/ses/babel-koyraborosenni.tex
%{_texmfdistdir}/tex/generic/babel/locale/ses/babel-ses.ini
%{_texmfdistdir}/tex/generic/babel/locale/sg/babel-sango.tex
%{_texmfdistdir}/tex/generic/babel/locale/sg/babel-sg.ini
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-shi-Latn.ini
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-shi-Tfng.ini
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-shi.ini
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-tachelhit-latin.tex
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-tachelhit-latn.tex
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-tachelhit-tfng.tex
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-tachelhit-tifinagh.tex
%{_texmfdistdir}/tex/generic/babel/locale/shi/babel-tachelhit.tex
%{_texmfdistdir}/tex/generic/babel/locale/si/babel-si.ini
%{_texmfdistdir}/tex/generic/babel/locale/si/babel-sinhala.tex
%{_texmfdistdir}/tex/generic/babel/locale/sk/babel-sk.ini
%{_texmfdistdir}/tex/generic/babel/locale/sk/babel-slovak.tex
%{_texmfdistdir}/tex/generic/babel/locale/sl/babel-sl.ini
%{_texmfdistdir}/tex/generic/babel/locale/sl/babel-slovene.tex
%{_texmfdistdir}/tex/generic/babel/locale/sl/babel-slovenian.tex
%{_texmfdistdir}/tex/generic/babel/locale/smn/babel-inarisami.tex
%{_texmfdistdir}/tex/generic/babel/locale/smn/babel-smn.ini
%{_texmfdistdir}/tex/generic/babel/locale/sn/babel-shona.tex
%{_texmfdistdir}/tex/generic/babel/locale/sn/babel-sn.ini
%{_texmfdistdir}/tex/generic/babel/locale/so/babel-so.ini
%{_texmfdistdir}/tex/generic/babel/locale/so/babel-somali.tex
%{_texmfdistdir}/tex/generic/babel/locale/sq/babel-albanian.tex
%{_texmfdistdir}/tex/generic/babel/locale/sq/babel-sq.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrillic-bosniaherzegovina.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrillic-kosovo.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrillic-montenegro.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrillic.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrl-ba.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrl-me.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrl-xk.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-cyrl.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latin-bosniaherzegovina.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latin-kosovo.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latin-montenegro.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latin.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latn-ba.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latn-me.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latn-xk.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian-latn.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-serbian.tex
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Cyrl-BA.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Cyrl-ME.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Cyrl-XK.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Cyrl.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Latn-BA.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Latn-ME.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Latn-XK.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr-Latn.ini
%{_texmfdistdir}/tex/generic/babel/locale/sr/babel-sr.ini
%{_texmfdistdir}/tex/generic/babel/locale/sv/babel-sv.ini
%{_texmfdistdir}/tex/generic/babel/locale/sv/babel-swedish.tex
%{_texmfdistdir}/tex/generic/babel/locale/sw/babel-sw.ini
%{_texmfdistdir}/tex/generic/babel/locale/sw/babel-swahili.tex
%{_texmfdistdir}/tex/generic/babel/locale/syr/babel-syr.ini
%{_texmfdistdir}/tex/generic/babel/locale/syr/babel-syriac.tex
%{_texmfdistdir}/tex/generic/babel/locale/ta/babel-ta.ini
%{_texmfdistdir}/tex/generic/babel/locale/ta/babel-tamil.tex
%{_texmfdistdir}/tex/generic/babel/locale/te/babel-te.ini
%{_texmfdistdir}/tex/generic/babel/locale/te/babel-telugu.tex
%{_texmfdistdir}/tex/generic/babel/locale/teo/babel-teo.ini
%{_texmfdistdir}/tex/generic/babel/locale/teo/babel-teso.tex
%{_texmfdistdir}/tex/generic/babel/locale/th/babel-th.ini
%{_texmfdistdir}/tex/generic/babel/locale/th/babel-thai.tex
%{_texmfdistdir}/tex/generic/babel/locale/ti/babel-ti.ini
%{_texmfdistdir}/tex/generic/babel/locale/ti/babel-tigrinya.tex
%{_texmfdistdir}/tex/generic/babel/locale/tk/babel-tk.ini
%{_texmfdistdir}/tex/generic/babel/locale/tk/babel-turkmen.tex
%{_texmfdistdir}/tex/generic/babel/locale/to/babel-to.ini
%{_texmfdistdir}/tex/generic/babel/locale/to/babel-tongan.tex
%{_texmfdistdir}/tex/generic/babel/locale/tr/babel-tr.ini
%{_texmfdistdir}/tex/generic/babel/locale/tr/babel-turkish.tex
%{_texmfdistdir}/tex/generic/babel/locale/twq/babel-tasawaq.tex
%{_texmfdistdir}/tex/generic/babel/locale/twq/babel-twq.ini
%{_texmfdistdir}/tex/generic/babel/locale/tzm/babel-centralatlastamazight.tex
%{_texmfdistdir}/tex/generic/babel/locale/tzm/babel-tzm.ini
%{_texmfdistdir}/tex/generic/babel/locale/ug/babel-ug.ini
%{_texmfdistdir}/tex/generic/babel/locale/ug/babel-uyghur.tex
%{_texmfdistdir}/tex/generic/babel/locale/uk/babel-uk.ini
%{_texmfdistdir}/tex/generic/babel/locale/uk/babel-ukrainian.tex
%{_texmfdistdir}/tex/generic/babel/locale/ur/babel-ur.ini
%{_texmfdistdir}/tex/generic/babel/locale/ur/babel-urdu.tex
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uz-Arab.ini
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uz-Cyrl.ini
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uz-Latn.ini
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uz.ini
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uzbek-arab.tex
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uzbek-arabic.tex
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uzbek-cyrillic.tex
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uzbek-cyrl.tex
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uzbek-latin.tex
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uzbek-latn.tex
%{_texmfdistdir}/tex/generic/babel/locale/uz/babel-uzbek.tex
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai-Latn.ini
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai-Vaii.ini
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai-latin.tex
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai-latn.tex
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai-vai.tex
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai-vaii.tex
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai.ini
%{_texmfdistdir}/tex/generic/babel/locale/vai/babel-vai.tex
%{_texmfdistdir}/tex/generic/babel/locale/vi/babel-vi.ini
%{_texmfdistdir}/tex/generic/babel/locale/vi/babel-vietnam.tex
%{_texmfdistdir}/tex/generic/babel/locale/vi/babel-vietnamese.tex
%{_texmfdistdir}/tex/generic/babel/locale/vun/babel-vun.ini
%{_texmfdistdir}/tex/generic/babel/locale/vun/babel-vunjo.tex
%{_texmfdistdir}/tex/generic/babel/locale/wae/babel-wae.ini
%{_texmfdistdir}/tex/generic/babel/locale/wae/babel-walser.tex
%{_texmfdistdir}/tex/generic/babel/locale/xog/babel-soga.tex
%{_texmfdistdir}/tex/generic/babel/locale/xog/babel-xog.ini
%{_texmfdistdir}/tex/generic/babel/locale/yav/babel-yangben.tex
%{_texmfdistdir}/tex/generic/babel/locale/yav/babel-yav.ini
%{_texmfdistdir}/tex/generic/babel/locale/yi/babel-yi.ini
%{_texmfdistdir}/tex/generic/babel/locale/yi/babel-yiddish.tex
%{_texmfdistdir}/tex/generic/babel/locale/yo/babel-yo.ini
%{_texmfdistdir}/tex/generic/babel/locale/yo/babel-yoruba.tex
%{_texmfdistdir}/tex/generic/babel/locale/yue/babel-cantonese.tex
%{_texmfdistdir}/tex/generic/babel/locale/yue/babel-yue.ini
%{_texmfdistdir}/tex/generic/babel/locale/zgh/babel-standardmoroccantamazight.tex
%{_texmfdistdir}/tex/generic/babel/locale/zgh/babel-zgh.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-hans-hk.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-hans-mo.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-hans-sg.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-hans.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-hant-hk.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-hant-mo.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-hant.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-simplified-hongkongsarchina.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-simplified-macausarchina.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-simplified-singapore.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-simplified.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-traditional-hongkongsarchina.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-traditional-macausarchina.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese-traditional.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-chinese.tex
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh-Hans-HK.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh-Hans-MO.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh-Hans-SG.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh-Hans.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh-Hant-HK.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh-Hant-MO.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh-Hant.ini
%{_texmfdistdir}/tex/generic/babel/locale/zh/babel-zh.ini
%{_texmfdistdir}/tex/generic/babel/locale/zu/babel-zu.ini
%{_texmfdistdir}/tex/generic/babel/locale/zu/babel-zulu.tex
%{_texmfdistdir}/tex/generic/babel/lsorbian.sty
%{_texmfdistdir}/tex/generic/babel/luababel.def
%{_texmfdistdir}/tex/generic/babel/magyar.sty
%{_texmfdistdir}/tex/generic/babel/naustrian.sty
%{_texmfdistdir}/tex/generic/babel/ngermanb.sty
%{_texmfdistdir}/tex/generic/babel/nil.ldf
%{_texmfdistdir}/tex/generic/babel/norsk.sty
%{_texmfdistdir}/tex/generic/babel/plain.def
%{_texmfdistdir}/tex/generic/babel/polish.sty
%{_texmfdistdir}/tex/generic/babel/portuges.sty
%{_texmfdistdir}/tex/generic/babel/romanian.sty
%{_texmfdistdir}/tex/generic/babel/russianb.sty
%{_texmfdistdir}/tex/generic/babel/samin.sty
%{_texmfdistdir}/tex/generic/babel/scottish.sty
%{_texmfdistdir}/tex/generic/babel/serbian.sty
%{_texmfdistdir}/tex/generic/babel/slovak.sty
%{_texmfdistdir}/tex/generic/babel/slovene.sty
%{_texmfdistdir}/tex/generic/babel/spanish.sty
%{_texmfdistdir}/tex/generic/babel/swedish.sty
%{_texmfdistdir}/tex/generic/babel/switch.def
%{_texmfdistdir}/tex/generic/babel/turkish.sty
%{_texmfdistdir}/tex/generic/babel/txtbabel.def
%{_texmfdistdir}/tex/generic/babel/ukraineb.sty
%{_texmfdistdir}/tex/generic/babel/usorbian.sty
%{_texmfdistdir}/tex/generic/babel/welsh.sty
%{_texmfdistdir}/tex/generic/babel/xebabel.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-%{texlive_version}.%{texlive_noarch}.3.42svn54487-%{release}-zypper
%endif

%package -n texlive-babel-albanian
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn30254
Release:        0
Summary:        Support for Albanian within babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-albanian-doc >= %{texlive_version}
Provides:       tex(albanian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source118:      babel-albanian.tar.xz
Source119:      babel-albanian.doc.tar.xz

%description -n texlive-babel-albanian
The package provides support for typesetting Albanian (as part
of the babel system).

%package -n texlive-babel-albanian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn30254
Release:        0
Summary:        Documentation for texlive-babel-albanian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-albanian-doc
This package includes the documentation for texlive-babel-albanian

%post -n texlive-babel-albanian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-albanian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-albanian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-albanian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-albanian/albanian.pdf

%files -n texlive-babel-albanian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-albanian/albanian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-albanian-%{texlive_version}.%{texlive_noarch}.1.0csvn30254-%{release}-zypper
%endif

%package -n texlive-babel-azerbaijani
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn44197
Release:        0
Summary:        Support for Azerbaijani within babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-azerbaijani-doc >= %{texlive_version}
Provides:       tex(azerbaijani.ldf)
Recommends:     texlive-hyphen-turkish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source120:      babel-azerbaijani.tar.xz
Source121:      babel-azerbaijani.doc.tar.xz

%description -n texlive-babel-azerbaijani
This is the babel style for Azerbaijani. This language poses
special challenges because no "traditional" font encoding
contains the full character set, and therefore a mixture must
be used (e.g., T2A and T1). This package is compatible with
Unicode engines (LuaTeX, XeTeX), which are very likely the most
convenient way to write Azerbaijani documents.

%package -n texlive-babel-azerbaijani-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0asvn44197
Release:        0
Summary:        Documentation for texlive-babel-azerbaijani
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-azerbaijani-doc
This package includes the documentation for texlive-babel-azerbaijani

%post -n texlive-babel-azerbaijani
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-azerbaijani 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-azerbaijani
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-azerbaijani-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-azerbaijani/README
%{_texmfdistdir}/doc/generic/babel-azerbaijani/azerbaijani.pdf

%files -n texlive-babel-azerbaijani
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-azerbaijani/azerbaijani.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-azerbaijani-%{texlive_version}.%{texlive_noarch}.1.0asvn44197-%{release}-zypper
%endif

%package -n texlive-babel-basque
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn30256
Release:        0
Summary:        Babel contributed support for Basque
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-basque-doc >= %{texlive_version}
Provides:       tex(basque.ldf)
Recommends:     texlive-hyphen-basque
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source122:      babel-basque.tar.xz
Source123:      babel-basque.doc.tar.xz

%description -n texlive-babel-basque
The package establishes Basque conventions in a document.

%package -n texlive-babel-basque-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0fsvn30256
Release:        0
Summary:        Documentation for texlive-babel-basque
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-basque-doc
This package includes the documentation for texlive-babel-basque

%post -n texlive-babel-basque
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-basque 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-basque
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-basque-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-basque/basque.pdf

%files -n texlive-babel-basque
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-basque/basque.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-basque-%{texlive_version}.%{texlive_noarch}.1.0fsvn30256-%{release}-zypper
%endif

%package -n texlive-babel-belarusian
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn49022
Release:        0
Summary:        Babel support for Belarusian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-belarusian-doc >= %{texlive_version}
Provides:       tex(belarusian.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source124:      babel-belarusian.tar.xz
Source125:      babel-belarusian.doc.tar.xz

%description -n texlive-babel-belarusian
The package provides support for use of Babel in documents
written in Belarusian.

%package -n texlive-babel-belarusian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5svn49022
Release:        0
Summary:        Documentation for texlive-babel-belarusian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-belarusian-doc
This package includes the documentation for texlive-babel-belarusian

%post -n texlive-babel-belarusian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-belarusian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-belarusian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-belarusian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-belarusian/README.md
%{_texmfdistdir}/doc/generic/babel-belarusian/belarusian.pdf

%files -n texlive-babel-belarusian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-belarusian/belarusian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-belarusian-%{texlive_version}.%{texlive_noarch}.1.5svn49022-%{release}-zypper
%endif

%package -n texlive-babel-bosnian
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn38174
Release:        0
Summary:        Babel contrib support for Bosnian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-bosnian-doc >= %{texlive_version}
Provides:       tex(bosnian.ldf)
Recommends:     texlive-hyphen-churchslavonic
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source126:      babel-bosnian.tar.xz
Source127:      babel-bosnian.doc.tar.xz

%description -n texlive-babel-bosnian
The package provides a language definition file that enables
support of Bosnian with babel.

%package -n texlive-babel-bosnian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn38174
Release:        0
Summary:        Documentation for texlive-babel-bosnian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-bosnian-doc
This package includes the documentation for texlive-babel-bosnian

%post -n texlive-babel-bosnian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-bosnian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-bosnian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-bosnian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-bosnian/README
%{_texmfdistdir}/doc/generic/babel-bosnian/bosnian.pdf

%files -n texlive-babel-bosnian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-bosnian/bosnian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-bosnian-%{texlive_version}.%{texlive_noarch}.1.1svn38174-%{release}-zypper
%endif

%package -n texlive-babel-breton
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn30257
Release:        0
Summary:        Babel contributed support for Breton
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-breton-doc >= %{texlive_version}
Provides:       tex(breton.ldf)
Recommends:     texlive-hyphen-galician
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source128:      babel-breton.tar.xz
Source129:      babel-breton.doc.tar.xz

%description -n texlive-babel-breton
Breton (being, principally, a spoken language) does not have
typographic rules of its own; this package provides an
"appropriate" selection of French and British typographic
rules.

%package -n texlive-babel-breton-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn30257
Release:        0
Summary:        Documentation for texlive-babel-breton
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-breton-doc
This package includes the documentation for texlive-babel-breton

%post -n texlive-babel-breton
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-breton 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-breton
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-breton-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-breton/breton.pdf

%files -n texlive-babel-breton
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-breton/breton.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-breton-%{texlive_version}.%{texlive_noarch}.1.0hsvn30257-%{release}-zypper
%endif

%package -n texlive-babel-bulgarian
Version:        %{texlive_version}.%{texlive_noarch}.1.2gsvn31902
Release:        0
Summary:        Babel contributed support for Bulgarian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-bulgarian-doc >= %{texlive_version}
Provides:       tex(bulgarian.ldf)
Recommends:     texlive-hyphen-bulgarian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source130:      babel-bulgarian.tar.xz
Source131:      babel-bulgarian.doc.tar.xz

%description -n texlive-babel-bulgarian
The package provides support for documents in Bulgarian (or
simply containing some Bulgarian text).

%package -n texlive-babel-bulgarian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2gsvn31902
Release:        0
Summary:        Documentation for texlive-babel-bulgarian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-bulgarian-doc
This package includes the documentation for texlive-babel-bulgarian

%post -n texlive-babel-bulgarian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-bulgarian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-bulgarian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-bulgarian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-bulgarian/README
%{_texmfdistdir}/doc/generic/babel-bulgarian/bulgarian.pdf

%files -n texlive-babel-bulgarian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-bulgarian/bulgarian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-bulgarian-%{texlive_version}.%{texlive_noarch}.1.2gsvn31902-%{release}-zypper
%endif

%package -n texlive-babel-catalan
Version:        %{texlive_version}.%{texlive_noarch}.2.2psvn30259
Release:        0
Summary:        Babel contributed support for Catalan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-catalan-doc >= %{texlive_version}
Provides:       tex(catalan.ldf)
Recommends:     texlive-hyphen-catalan
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source132:      babel-catalan.tar.xz
Source133:      babel-catalan.doc.tar.xz

%description -n texlive-babel-catalan
The package establishes Catalan conventions in a document (or a
subset of the conventions, if Catalan is not the main language
of the document).

%package -n texlive-babel-catalan-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2psvn30259
Release:        0
Summary:        Documentation for texlive-babel-catalan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-catalan-doc
This package includes the documentation for texlive-babel-catalan

%post -n texlive-babel-catalan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-catalan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-catalan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-catalan-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-catalan/catalan.pdf

%files -n texlive-babel-catalan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-catalan/catalan.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-catalan-%{texlive_version}.%{texlive_noarch}.2.2psvn30259-%{release}-zypper
%endif

%package -n texlive-babel-croatian
Version:        %{texlive_version}.%{texlive_noarch}.1.3lsvn35198
Release:        0
Summary:        Babel contributed support for Croatian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-croatian-doc >= %{texlive_version}
Provides:       tex(croatian.ldf)
Recommends:     texlive-hyphen-croatian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source134:      babel-croatian.tar.xz
Source135:      babel-croatian.doc.tar.xz

%description -n texlive-babel-croatian
The package establishes Croatian conventions in a document (or
a subset of the conventions, if Croatian is not the main
language of the document).

%package -n texlive-babel-croatian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3lsvn35198
Release:        0
Summary:        Documentation for texlive-babel-croatian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-croatian-doc
This package includes the documentation for texlive-babel-croatian

%post -n texlive-babel-croatian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-croatian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-croatian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-croatian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-croatian/croatian.pdf

%files -n texlive-babel-croatian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-croatian/croatian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-croatian-%{texlive_version}.%{texlive_noarch}.1.3lsvn35198-%{release}-zypper
%endif

%package -n texlive-babel-czech
Version:        %{texlive_version}.%{texlive_noarch}.3.1asvn30261
Release:        0
Summary:        Babel support for Czech
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-czech-doc >= %{texlive_version}
Provides:       tex(czech.ldf)
Recommends:     texlive-hyphen-czech
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source136:      babel-czech.tar.xz
Source137:      babel-czech.doc.tar.xz

%description -n texlive-babel-czech
The package provides the language definition file for support
of Czech in babel. Some shortcuts are defined, as well as
translations to Czech of standard "LaTeX names".

%package -n texlive-babel-czech-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1asvn30261
Release:        0
Summary:        Documentation for texlive-babel-czech
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-czech-doc
This package includes the documentation for texlive-babel-czech

%post -n texlive-babel-czech
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-czech 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-czech
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-czech-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-czech/czech.pdf

%files -n texlive-babel-czech
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-czech/czech.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-czech-%{texlive_version}.%{texlive_noarch}.3.1asvn30261-%{release}-zypper
%endif

%package -n texlive-babel-danish
Version:        %{texlive_version}.%{texlive_noarch}.1.3rsvn30262
Release:        0
Summary:        Babel contributed support for Danish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-danish-doc >= %{texlive_version}
Provides:       tex(danish.ldf)
Recommends:     texlive-hyphen-danish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source138:      babel-danish.tar.xz
Source139:      babel-danish.doc.tar.xz

%description -n texlive-babel-danish
The package provides a language definition, file for use with
babel, which establishes Danish conventions in a document (or a
subset of the conventions, if Danish is not the main language
of the document).

%package -n texlive-babel-danish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3rsvn30262
Release:        0
Summary:        Documentation for texlive-babel-danish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-danish-doc
This package includes the documentation for texlive-babel-danish

%post -n texlive-babel-danish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-danish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-danish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-danish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-danish/danish.pdf

%files -n texlive-babel-danish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-danish/danish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-danish-%{texlive_version}.%{texlive_noarch}.1.3rsvn30262-%{release}-zypper
%endif

%package -n texlive-babel-dutch
Version:        %{texlive_version}.%{texlive_noarch}.3.8isvn30263
Release:        0
Summary:        Babel contributed support for Dutch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-dutch-doc >= %{texlive_version}
Provides:       tex(dutch.ldf)
Recommends:     texlive-hyphen-dutch
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source140:      babel-dutch.tar.xz
Source141:      babel-dutch.doc.tar.xz

%description -n texlive-babel-dutch
The package provides a language definition, file for use with
babel, which establishes Dutch conventions in a document (or a
subset of the conventions, if Dutch is not the main language of
the document).

%package -n texlive-babel-dutch-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.8isvn30263
Release:        0
Summary:        Documentation for texlive-babel-dutch
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-dutch-doc
This package includes the documentation for texlive-babel-dutch

%post -n texlive-babel-dutch
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-dutch 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-dutch
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-dutch-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-dutch/dutch.pdf

%files -n texlive-babel-dutch
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-dutch/dutch.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-dutch-%{texlive_version}.%{texlive_noarch}.3.8isvn30263-%{release}-zypper
%endif

%package -n texlive-babel-english
Version:        %{texlive_version}.%{texlive_noarch}.3.3rsvn44495
Release:        0
Summary:        Babel support for English
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-english-doc >= %{texlive_version}
Provides:       tex(UKenglish.ldf)
Provides:       tex(USenglish.ldf)
Provides:       tex(american.ldf)
Provides:       tex(australian.ldf)
Provides:       tex(british.ldf)
Provides:       tex(canadian.ldf)
Provides:       tex(english.ldf)
Provides:       tex(newzealand.ldf)
Recommends:     texlive-hyphen-english
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source142:      babel-english.tar.xz
Source143:      babel-english.doc.tar.xz

%description -n texlive-babel-english
The package provides the language definition file for support
of English in babel. Care is taken to select british
hyphenation patterns for British English and Australian text,
and default ('american') patterns for Canadian and USA text.

%package -n texlive-babel-english-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.3rsvn44495
Release:        0
Summary:        Documentation for texlive-babel-english
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-english-doc
This package includes the documentation for texlive-babel-english

%post -n texlive-babel-english
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-english 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-english
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-english-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-english/README
%{_texmfdistdir}/doc/generic/babel-english/english.pdf

%files -n texlive-babel-english
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-english/UKenglish.ldf
%{_texmfdistdir}/tex/generic/babel-english/USenglish.ldf
%{_texmfdistdir}/tex/generic/babel-english/american.ldf
%{_texmfdistdir}/tex/generic/babel-english/australian.ldf
%{_texmfdistdir}/tex/generic/babel-english/british.ldf
%{_texmfdistdir}/tex/generic/babel-english/canadian.ldf
%{_texmfdistdir}/tex/generic/babel-english/english.ldf
%{_texmfdistdir}/tex/generic/babel-english/newzealand.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-english-%{texlive_version}.%{texlive_noarch}.3.3rsvn44495-%{release}-zypper
%endif

%package -n texlive-babel-esperanto
Version:        %{texlive_version}.%{texlive_noarch}.1.4tsvn30265
Release:        0
Summary:        Babel support for Esperanto
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-esperanto-doc >= %{texlive_version}
Provides:       tex(esperanto.ldf)
Recommends:     texlive-hyphen-esperanto
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source144:      babel-esperanto.tar.xz
Source145:      babel-esperanto.doc.tar.xz

%description -n texlive-babel-esperanto
The package provides the language definition file for support
of Esperanto in babel. Some shortcuts are defined, as well as
translations to Esperanto of standard "LaTeX names".

%package -n texlive-babel-esperanto-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4tsvn30265
Release:        0
Summary:        Documentation for texlive-babel-esperanto
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-esperanto-doc
This package includes the documentation for texlive-babel-esperanto

%post -n texlive-babel-esperanto
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-esperanto 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-esperanto
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-esperanto-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-esperanto/esperanto.pdf

%files -n texlive-babel-esperanto
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-esperanto/esperanto.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-esperanto-%{texlive_version}.%{texlive_noarch}.1.4tsvn30265-%{release}-zypper
%endif

%package -n texlive-babel-estonian
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn38064
Release:        0
Summary:        Babel support for Estonian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-estonian-doc >= %{texlive_version}
Provides:       tex(estonian.ldf)
Recommends:     texlive-hyphen-estonian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source146:      babel-estonian.tar.xz
Source147:      babel-estonian.doc.tar.xz

%description -n texlive-babel-estonian
The package provides the language definition file for support
of Estonian in babel. Some shortcuts are defined, as well as
translations to Estonian of standard "LaTeX names".

%package -n texlive-babel-estonian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn38064
Release:        0
Summary:        Documentation for texlive-babel-estonian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-estonian-doc
This package includes the documentation for texlive-babel-estonian

%post -n texlive-babel-estonian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-estonian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-estonian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-estonian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-estonian/README.txt
%{_texmfdistdir}/doc/generic/babel-estonian/estonian.pdf

%files -n texlive-babel-estonian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-estonian/estonian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-estonian-%{texlive_version}.%{texlive_noarch}.1.1asvn38064-%{release}-zypper
%endif

%package -n texlive-babel-finnish
Version:        %{texlive_version}.%{texlive_noarch}.1.3rsvn54771
Release:        0
Summary:        Babel support for Finnish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-finnish-doc >= %{texlive_version}
Provides:       tex(finnish.ldf)
Recommends:     texlive-hyphen-finnish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source148:      babel-finnish.tar.xz
Source149:      babel-finnish.doc.tar.xz

%description -n texlive-babel-finnish
The package provides a language description file that enables
support of Finnish with babel.

%package -n texlive-babel-finnish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3rsvn54771
Release:        0
Summary:        Documentation for texlive-babel-finnish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-finnish-doc
This package includes the documentation for texlive-babel-finnish

%post -n texlive-babel-finnish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-finnish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-finnish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-finnish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-finnish/README.md
%{_texmfdistdir}/doc/generic/babel-finnish/finnish.pdf

%files -n texlive-babel-finnish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-finnish/finnish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-finnish-%{texlive_version}.%{texlive_noarch}.1.3rsvn54771-%{release}-zypper
%endif

%package -n texlive-babel-french
Version:        %{texlive_version}.%{texlive_noarch}.3.5hsvn54787
Release:        0
Summary:        Babel contributed support for French
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-french-doc >= %{texlive_version}
Provides:       tex(acadian.ldf)
Provides:       tex(canadien.ldf)
Provides:       tex(francais.ldf)
Provides:       tex(french.ldf)
Provides:       tex(frenchb.ldf)
Recommends:     texlive-hyphen-french
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source150:      babel-french.tar.xz
Source151:      babel-french.doc.tar.xz

%description -n texlive-babel-french
The package, formerly known as frenchb, establishes French
conventions in a document (or a subset of the conventions, if
French is not the main language of the document).

%package -n texlive-babel-french-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.5hsvn54787
Release:        0
Summary:        Documentation for texlive-babel-french
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-babel-french-doc:fr)

%description -n texlive-babel-french-doc
This package includes the documentation for texlive-babel-french

%post -n texlive-babel-french
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-french 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-french
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-french-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-french/README.md
%{_texmfdistdir}/doc/generic/babel-french/frenchb-doc.pdf
%{_texmfdistdir}/doc/generic/babel-french/frenchb-doc.tex
%{_texmfdistdir}/doc/generic/babel-french/frenchb.pdf

%files -n texlive-babel-french
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-french/acadian.ldf
%{_texmfdistdir}/tex/generic/babel-french/canadien.ldf
%{_texmfdistdir}/tex/generic/babel-french/francais.ldf
%{_texmfdistdir}/tex/generic/babel-french/french.ldf
%{_texmfdistdir}/tex/generic/babel-french/frenchb.ldf
%{_texmfdistdir}/tex/generic/babel-french/frenchb.lua
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-french-%{texlive_version}.%{texlive_noarch}.3.5hsvn54787-%{release}-zypper
%endif

%package -n texlive-babel-friulan
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn39861
Release:        0
Summary:        Babel/Polyglossia support for Friulan(Furlan)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-friulan-doc >= %{texlive_version}
Provides:       tex(friulan.ldf)
Recommends:     texlive-hyphen-friulan
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source152:      babel-friulan.tar.xz
Source153:      babel-friulan.doc.tar.xz

%description -n texlive-babel-friulan
The package provides a language description file that enables
support of Friulan either with babel or with polyglossia.

%package -n texlive-babel-friulan-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn39861
Release:        0
Summary:        Documentation for texlive-babel-friulan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-friulan-doc
This package includes the documentation for texlive-babel-friulan

%post -n texlive-babel-friulan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-friulan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-friulan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-friulan-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-friulan/README.txt
%{_texmfdistdir}/doc/generic/babel-friulan/friulan.pdf

%files -n texlive-babel-friulan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-friulan/friulan.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-friulan-%{texlive_version}.%{texlive_noarch}.1.3svn39861-%{release}-zypper
%endif

%package -n texlive-babel-galician
Version:        %{texlive_version}.%{texlive_noarch}.4.3csvn30270
Release:        0
Summary:        Babel/Polyglossia support for Galician
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-galician-doc >= %{texlive_version}
Provides:       tex(galician.ldf)
Recommends:     texlive-hyphen-galician
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source154:      babel-galician.tar.xz
Source155:      babel-galician.doc.tar.xz

%description -n texlive-babel-galician
The package provides a language description file that enables
support of Galician either with babel or with polyglossia.

%package -n texlive-babel-galician-doc
Version:        %{texlive_version}.%{texlive_noarch}.4.3csvn30270
Release:        0
Summary:        Documentation for texlive-babel-galician
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-galician-doc
This package includes the documentation for texlive-babel-galician

%post -n texlive-babel-galician
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-galician 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-galician
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-galician-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-galician/galician.pdf
%{_texmfdistdir}/doc/generic/babel-galician/glbst.tex
%{_texmfdistdir}/doc/generic/babel-galician/glromidx.tex

%files -n texlive-babel-galician
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-galician/galician.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-galician-%{texlive_version}.%{texlive_noarch}.4.3csvn30270-%{release}-zypper
%endif

%package -n texlive-babel-georgian
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn45864
Release:        0
Summary:        Babel support for Georgian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-georgian-doc >= %{texlive_version}
Provides:       tex(georgian.ldf)
Provides:       tex(georgian.sty)
Provides:       tex(georgiancaps.tex)
Recommends:     texlive-hyphen-georgian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source156:      babel-georgian.tar.xz
Source157:      babel-georgian.doc.tar.xz

%description -n texlive-babel-georgian
The package provides support for use of Babel in documents
written in Georgian. The package is adapted for use both under
'traditional' TeX engines, and under XeTeX and LuaTeX.

%package -n texlive-babel-georgian-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn45864
Release:        0
Summary:        Documentation for texlive-babel-georgian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-georgian-doc
This package includes the documentation for texlive-babel-georgian

%post -n texlive-babel-georgian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-georgian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-georgian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-georgian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-georgian/README

%files -n texlive-babel-georgian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-georgian/georgian.ldf
%{_texmfdistdir}/tex/generic/babel-georgian/georgian.sty
%{_texmfdistdir}/tex/generic/babel-georgian/georgiancaps.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-georgian-%{texlive_version}.%{texlive_noarch}.2.2svn45864-%{release}-zypper
%endif

%package -n texlive-babel-german
Version:        %{texlive_version}.%{texlive_noarch}.2.11svn49391
Release:        0
Summary:        Babel support for documents written in German
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-german-doc >= %{texlive_version}
Provides:       tex(austrian.ldf)
Provides:       tex(german.ldf)
Provides:       tex(germanb.ldf)
Provides:       tex(naustrian.ldf)
Provides:       tex(ngerman.ldf)
Provides:       tex(ngermanb.ldf)
Provides:       tex(nswissgerman.ldf)
Provides:       tex(swissgerman.ldf)
Recommends:     texlive-hyphen-german
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source158:      babel-german.tar.xz
Source159:      babel-german.doc.tar.xz

%description -n texlive-babel-german
This bundle is an extension to the babel package for
multilingual typesetting. It provides all the necessary macros,
definitions and settings to typeset German documents. The
bundle includes support for the traditional and reformed German
orthography as well as for the Austrian and Swiss varieties of
German.

%package -n texlive-babel-german-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.11svn49391
Release:        0
Summary:        Documentation for texlive-babel-german
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-german-doc
This package includes the documentation for texlive-babel-german

%post -n texlive-babel-german
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-german 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-german
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-german-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-german/README
%{_texmfdistdir}/doc/generic/babel-german/germanb.pdf
%{_texmfdistdir}/doc/generic/babel-german/ngermanb.pdf

%files -n texlive-babel-german
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-german/austrian.ldf
%{_texmfdistdir}/tex/generic/babel-german/german.ldf
%{_texmfdistdir}/tex/generic/babel-german/germanb.ldf
%{_texmfdistdir}/tex/generic/babel-german/naustrian.ldf
%{_texmfdistdir}/tex/generic/babel-german/ngerman.ldf
%{_texmfdistdir}/tex/generic/babel-german/ngermanb.ldf
%{_texmfdistdir}/tex/generic/babel-german/nswissgerman.ldf
%{_texmfdistdir}/tex/generic/babel-german/swissgerman.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-german-%{texlive_version}.%{texlive_noarch}.2.11svn49391-%{release}-zypper
%endif

%package -n texlive-babel-greek
Version:        %{texlive_version}.%{texlive_noarch}.1.9jsvn54512
Release:        0
Summary:        Babel support for documents written in Greek
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-greek-doc >= %{texlive_version}
Provides:       tex(athnum.sty)
Provides:       tex(greek.ldf)
Provides:       tex(grmath.sty)
Recommends:     texlive-hyphen-greek
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source160:      babel-greek.tar.xz
Source161:      babel-greek.doc.tar.xz

%description -n texlive-babel-greek
The file provides modes for monotonic (single-diacritic) and
polytonic (multiple-diacritic) modes of writing. Provision is
made for Greek function names in mathematics, and for
classical-era symbols.

%package -n texlive-babel-greek-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.9jsvn54512
Release:        0
Summary:        Documentation for texlive-babel-greek
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-greek-doc
This package includes the documentation for texlive-babel-greek

%post -n texlive-babel-greek
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-greek 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-greek
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-greek-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-greek/README
%{_texmfdistdir}/doc/generic/babel-greek/README.html
%{_texmfdistdir}/doc/generic/babel-greek/athnum.pdf
%{_texmfdistdir}/doc/generic/babel-greek/babel-greek.pdf
%{_texmfdistdir}/doc/generic/babel-greek/grmath.pdf
%{_texmfdistdir}/doc/generic/babel-greek/test-greek.pdf
%{_texmfdistdir}/doc/generic/babel-greek/test-greek.tex
%{_texmfdistdir}/doc/generic/babel-greek/test-unicode-greek.pdf
%{_texmfdistdir}/doc/generic/babel-greek/test-unicode-greek.tex
%{_texmfdistdir}/doc/generic/babel-greek/test-unicode-lgr.pdf
%{_texmfdistdir}/doc/generic/babel-greek/test-unicode-lgr.tex
%{_texmfdistdir}/doc/generic/babel-greek/usage.pdf
%{_texmfdistdir}/doc/generic/babel-greek/usage.tex

%files -n texlive-babel-greek
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-greek/athnum.sty
%{_texmfdistdir}/tex/generic/babel-greek/greek.ldf
%{_texmfdistdir}/tex/generic/babel-greek/grmath.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-greek-%{texlive_version}.%{texlive_noarch}.1.9jsvn54512-%{release}-zypper
%endif

%package -n texlive-babel-hebrew
Version:        %{texlive_version}.%{texlive_noarch}.2.3hsvn30273
Release:        0
Summary:        Babel support for Hebrew
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-hebrew-doc >= %{texlive_version}
Provides:       tex(8859-8.def)
Provides:       tex(cp1255.def)
Provides:       tex(cp862.def)
Provides:       tex(he8OmegaHebrew.fd)
Provides:       tex(he8aharoni.fd)
Provides:       tex(he8cmr.fd)
Provides:       tex(he8cmss.fd)
Provides:       tex(he8cmtt.fd)
Provides:       tex(he8david.fd)
Provides:       tex(he8drugulin.fd)
Provides:       tex(he8enc.def)
Provides:       tex(he8frankruehl.fd)
Provides:       tex(he8miriam.fd)
Provides:       tex(he8nachlieli.fd)
Provides:       tex(he8yad.fd)
Provides:       tex(hebcal.sty)
Provides:       tex(hebfont.sty)
Provides:       tex(hebrew.ldf)
Provides:       tex(hebrew_newcode.sty)
Provides:       tex(hebrew_oldcode.sty)
Provides:       tex(hebrew_p.sty)
Provides:       tex(lheclas.fd)
Provides:       tex(lhecmr.fd)
Provides:       tex(lhecmss.fd)
Provides:       tex(lhecmtt.fd)
Provides:       tex(lhecrml.fd)
Provides:       tex(lheenc.def)
Provides:       tex(lhefr.fd)
Provides:       tex(lheredis.fd)
Provides:       tex(lheshold.fd)
Provides:       tex(lheshscr.fd)
Provides:       tex(lheshstk.fd)
Provides:       tex(rlbabel.def)
Provides:       tex(si960.def)
Requires:       tex(babel.sty)
Requires:       tex(inputenc.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source162:      babel-hebrew.tar.xz
Source163:      babel-hebrew.doc.tar.xz

%description -n texlive-babel-hebrew
The package provides the language definition file for support
of Hebrew in babel. Macros to control the use of text direction
control of TeX--XeT and e-TeX are provided (and may be used
elsewhere). Some shortcuts are defined, as well as translations
to Hebrew of standard "LaTeX names".

%package -n texlive-babel-hebrew-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3hsvn30273
Release:        0
Summary:        Documentation for texlive-babel-hebrew
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-hebrew-doc
This package includes the documentation for texlive-babel-hebrew

%post -n texlive-babel-hebrew
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-hebrew 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-hebrew
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-hebrew-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-hebrew/00readme.heb
%{_texmfdistdir}/doc/generic/babel-hebrew/heb209.pdf
%{_texmfdistdir}/doc/generic/babel-hebrew/hebinp.pdf
%{_texmfdistdir}/doc/generic/babel-hebrew/hebrew.pdf

%files -n texlive-babel-hebrew
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-hebrew/8859-8.def
%{_texmfdistdir}/tex/generic/babel-hebrew/cp1255.def
%{_texmfdistdir}/tex/generic/babel-hebrew/cp862.def
%{_texmfdistdir}/tex/generic/babel-hebrew/he8OmegaHebrew.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8aharoni.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8cmr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8cmss.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8cmtt.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8david.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8drugulin.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8enc.def
%{_texmfdistdir}/tex/generic/babel-hebrew/he8frankruehl.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8miriam.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8nachlieli.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/he8yad.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/hebcal.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebfont.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew.ldf
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew_newcode.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew_oldcode.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/hebrew_p.sty
%{_texmfdistdir}/tex/generic/babel-hebrew/lheclas.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecmr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecmss.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecmtt.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lhecrml.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheenc.def
%{_texmfdistdir}/tex/generic/babel-hebrew/lhefr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheredis.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheshold.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheshscr.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/lheshstk.fd
%{_texmfdistdir}/tex/generic/babel-hebrew/rlbabel.def
%{_texmfdistdir}/tex/generic/babel-hebrew/si960.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-hebrew-%{texlive_version}.%{texlive_noarch}.2.3hsvn30273-%{release}-zypper
%endif

%package -n texlive-babel-hungarian
Version:        %{texlive_version}.%{texlive_noarch}.1.5csvn49701
Release:        0
Summary:        Babel support for Hungarian (Magyar)
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-hungarian-doc >= %{texlive_version}
Provides:       tex(magyar.ldf)
Recommends:     texlive-hyphen-hungarian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source164:      babel-hungarian.tar.xz
Source165:      babel-hungarian.doc.tar.xz

%description -n texlive-babel-hungarian
The package provides a language definition file that enables
support of Magyar (Hungarian) with babel.

%package -n texlive-babel-hungarian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5csvn49701
Release:        0
Summary:        Documentation for texlive-babel-hungarian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-hungarian-doc
This package includes the documentation for texlive-babel-hungarian

%post -n texlive-babel-hungarian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-hungarian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-hungarian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-hungarian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-hungarian/README

%files -n texlive-babel-hungarian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-hungarian/magyar.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-hungarian-%{texlive_version}.%{texlive_noarch}.1.5csvn49701-%{release}-zypper
%endif

%package -n texlive-babel-icelandic
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn51551
Release:        0
Summary:        Babel support for Icelandic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-icelandic-doc >= %{texlive_version}
Provides:       tex(icelandic.ldf)
Recommends:     texlive-hyphen-icelandic
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source166:      babel-icelandic.tar.xz
Source167:      babel-icelandic.doc.tar.xz

%description -n texlive-babel-icelandic
The package provides the language definition file for support
of Icelandic in babel. Some shortcuts are defined, as well as
translations to Icelandic of standard "LaTeX names".

%package -n texlive-babel-icelandic-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3svn51551
Release:        0
Summary:        Documentation for texlive-babel-icelandic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-icelandic-doc
This package includes the documentation for texlive-babel-icelandic

%post -n texlive-babel-icelandic
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-icelandic 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-icelandic
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-icelandic-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-icelandic/README.md
%{_texmfdistdir}/doc/generic/babel-icelandic/icelandic.pdf

%files -n texlive-babel-icelandic
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-icelandic/icelandic.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-icelandic-%{texlive_version}.%{texlive_noarch}.1.3svn51551-%{release}-zypper
%endif

%package -n texlive-babel-indonesian
Version:        %{texlive_version}.%{texlive_noarch}.1.0msvn43235
Release:        0
Summary:        Support for Indonesian within babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-indonesian-doc >= %{texlive_version}
Provides:       tex(bahasa.ldf)
Provides:       tex(bahasai.ldf)
Provides:       tex(indon.ldf)
Provides:       tex(indonesian.ldf)
Recommends:     texlive-hyphen-indonesian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source168:      babel-indonesian.tar.xz
Source169:      babel-indonesian.doc.tar.xz

%description -n texlive-babel-indonesian
This is the babel style for Indonesian.

%package -n texlive-babel-indonesian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0msvn43235
Release:        0
Summary:        Documentation for texlive-babel-indonesian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-indonesian-doc
This package includes the documentation for texlive-babel-indonesian

%post -n texlive-babel-indonesian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-indonesian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-indonesian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-indonesian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-indonesian/README
%{_texmfdistdir}/doc/generic/babel-indonesian/indonesian.pdf

%files -n texlive-babel-indonesian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-indonesian/bahasa.ldf
%{_texmfdistdir}/tex/generic/babel-indonesian/bahasai.ldf
%{_texmfdistdir}/tex/generic/babel-indonesian/indon.ldf
%{_texmfdistdir}/tex/generic/babel-indonesian/indonesian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-indonesian-%{texlive_version}.%{texlive_noarch}.1.0msvn43235-%{release}-zypper
%endif

%package -n texlive-babel-interlingua
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn30276
Release:        0
Summary:        Babel support for Interlingua
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-interlingua-doc >= %{texlive_version}
Provides:       tex(interlingua.ldf)
Recommends:     texlive-hyphen-interlingua
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source170:      babel-interlingua.tar.xz
Source171:      babel-interlingua.doc.tar.xz

%description -n texlive-babel-interlingua
The package provides the language definition file for support
of Interlingua in babel. Translations to Interlingua of
standard "LaTeX names" (no shortcuts are provided). Interlingua
itself is an auxiliary language, built from the common
vocabulary of Spanish/Portuguese, English, Italian and French,
with some normalisation of spelling.

%package -n texlive-babel-interlingua-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.6svn30276
Release:        0
Summary:        Documentation for texlive-babel-interlingua
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-interlingua-doc
This package includes the documentation for texlive-babel-interlingua

%post -n texlive-babel-interlingua
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-interlingua 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-interlingua
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-interlingua-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-interlingua/interlingua.pdf

%files -n texlive-babel-interlingua
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-interlingua/interlingua.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-interlingua-%{texlive_version}.%{texlive_noarch}.1.6svn30276-%{release}-zypper
%endif

%package -n texlive-babel-irish
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn30277
Release:        0
Summary:        Babel support for Irish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-irish-doc >= %{texlive_version}
Provides:       tex(irish.ldf)
Recommends:     texlive-hyphen-irish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source172:      babel-irish.tar.xz
Source173:      babel-irish.doc.tar.xz

%description -n texlive-babel-irish
The package provides the language definition file for support
of Irish Gaelic in babel. The principal content is translations
to Irish of standard "LaTeX names". (No shortcuts are defined.)

%package -n texlive-babel-irish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0hsvn30277
Release:        0
Summary:        Documentation for texlive-babel-irish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-irish-doc
This package includes the documentation for texlive-babel-irish

%post -n texlive-babel-irish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-irish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-irish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-irish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-irish/irish.pdf

%files -n texlive-babel-irish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-irish/irish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-irish-%{texlive_version}.%{texlive_noarch}.1.0hsvn30277-%{release}-zypper
%endif

%package -n texlive-babel-italian
Version:        %{texlive_version}.%{texlive_noarch}.1.4.03svn53019
Release:        0
Summary:        Babel support for Italian text
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-italian-doc >= %{texlive_version}
Provides:       tex(italian.ldf)
Recommends:     texlive-hyphen-italian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source174:      babel-italian.tar.xz
Source175:      babel-italian.doc.tar.xz

%description -n texlive-babel-italian
The package provides language definitions for use in babel.

%package -n texlive-babel-italian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4.03svn53019
Release:        0
Summary:        Documentation for texlive-babel-italian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-italian-doc
This package includes the documentation for texlive-babel-italian

%post -n texlive-babel-italian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-italian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-italian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-italian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-italian/README.txt
%{_texmfdistdir}/doc/generic/babel-italian/italian.pdf

%files -n texlive-babel-italian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-italian/italian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-italian-%{texlive_version}.%{texlive_noarch}.1.4.03svn53019-%{release}-zypper
%endif

%package -n texlive-babel-japanese
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn50735
Release:        0
Summary:        Babel support for Japanese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-japanese-doc >= %{texlive_version}
Provides:       tex(japanese.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source176:      babel-japanese.tar.xz
Source177:      babel-japanese.doc.tar.xz

%description -n texlive-babel-japanese
This package provides a japanese option for the babel package.
It defines all the language definition macros in Japanese.
Currently this package works with pLaTeX, upLaTeX, XeLaTeX and
LuaLaTeX.

%package -n texlive-babel-japanese-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn50735
Release:        0
Summary:        Documentation for texlive-babel-japanese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-babel-japanese-doc:ja)

%description -n texlive-babel-japanese-doc
This package includes the documentation for texlive-babel-japanese

%post -n texlive-babel-japanese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-japanese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-japanese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-japanese-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-japanese/README.md
%{_texmfdistdir}/doc/generic/babel-japanese/japanese-sample.pdf
%{_texmfdistdir}/doc/generic/babel-japanese/japanese-sample.tex
%{_texmfdistdir}/doc/generic/babel-japanese/japanese.pdf

%files -n texlive-babel-japanese
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-japanese/japanese.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-japanese-%{texlive_version}.%{texlive_noarch}.2.2svn50735-%{release}-zypper
%endif

%package -n texlive-babel-kurmanji
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn30279
Release:        0
Summary:        Babel support for Kurmanji
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-kurmanji-doc >= %{texlive_version}
Provides:       tex(kurmanji.ldf)
Recommends:     texlive-hyphen-kurmanji
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source178:      babel-kurmanji.tar.xz
Source179:      babel-kurmanji.doc.tar.xz

%description -n texlive-babel-kurmanji
The package provides the language definition file for support
of Kurmanji in babel. Kurmanji belongs to the family of Kurdish
languages. Some shortcuts are defined, as well as translations
to Kurmanji of standard "LaTeX names". Note that the package is
dealing with 'Northern' Kurdish, written using a Latin-based
alphabet. The arabxetex package offers support for Kurdish
written in Arabic script.

%package -n texlive-babel-kurmanji-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn30279
Release:        0
Summary:        Documentation for texlive-babel-kurmanji
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-kurmanji-doc
This package includes the documentation for texlive-babel-kurmanji

%post -n texlive-babel-kurmanji
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-kurmanji 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-kurmanji
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-kurmanji-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-kurmanji/kurmanji.pdf

%files -n texlive-babel-kurmanji
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-kurmanji/kurmanji.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-kurmanji-%{texlive_version}.%{texlive_noarch}.1.1svn30279-%{release}-zypper
%endif

%package -n texlive-babel-latin
Version:        %{texlive_version}.%{texlive_noarch}.3.5svn38173
Release:        0
Summary:        Babel support for Latin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-latin-doc >= %{texlive_version}
Provides:       tex(latin.ldf)
Recommends:     texlive-hyphen-latin
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source180:      babel-latin.tar.xz
Source181:      babel-latin.doc.tar.xz

%description -n texlive-babel-latin
The package provides the language definition file for support
of Latin in babel. Translations to Latin (in both modern and
medieval spelling) of standard "LaTeX names", and some
shortcuts, are provided. Apart from the modern vs. medieval
setting, a further switch permits addition of prosodic marks.

%package -n texlive-babel-latin-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.5svn38173
Release:        0
Summary:        Documentation for texlive-babel-latin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-latin-doc
This package includes the documentation for texlive-babel-latin

%post -n texlive-babel-latin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-latin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-latin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-latin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-latin/latin.pdf

%files -n texlive-babel-latin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-latin/latin.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-latin-%{texlive_version}.%{texlive_noarch}.3.5svn38173-%{release}-zypper
%endif

%package -n texlive-babel-latvian
Version:        %{texlive_version}.%{texlive_noarch}.2.0bsvn46681
Release:        0
Summary:        Babel support for Latvian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-latvian-doc >= %{texlive_version}
Provides:       tex(latvian.ldf)
Recommends:     texlive-hyphen-latvian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source182:      babel-latvian.tar.xz
Source183:      babel-latvian.doc.tar.xz

%description -n texlive-babel-latvian
The package provides the language definition file for support
of Latvian in babel.

%package -n texlive-babel-latvian-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0bsvn46681
Release:        0
Summary:        Documentation for texlive-babel-latvian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-latvian-doc
This package includes the documentation for texlive-babel-latvian

%post -n texlive-babel-latvian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-latvian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-latvian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-latvian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-latvian/README.md
%{_texmfdistdir}/doc/generic/babel-latvian/latvian.pdf

%files -n texlive-babel-latvian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-latvian/latvian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-latvian-%{texlive_version}.%{texlive_noarch}.2.0bsvn46681-%{release}-zypper
%endif

%package -n texlive-babel-macedonian
Version:        %{texlive_version}.%{texlive_noarch}.svn39587
Release:        0
Summary:        Babel module to support Macedonian Cyrillic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-macedonian-doc >= %{texlive_version}
Provides:       tex(macedonian.ldf)
Recommends:     texlive-hyphen-churchslavonic
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source184:      babel-macedonian.tar.xz
Source185:      babel-macedonian.doc.tar.xz

%description -n texlive-babel-macedonian
The package provides support for Macedonian documents written
in Cyrillic, in babel.

%package -n texlive-babel-macedonian-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn39587
Release:        0
Summary:        Documentation for texlive-babel-macedonian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-macedonian-doc
This package includes the documentation for texlive-babel-macedonian

%post -n texlive-babel-macedonian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-macedonian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-macedonian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-macedonian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-macedonian/README.md
%{_texmfdistdir}/doc/generic/babel-macedonian/macedonian.pdf

%files -n texlive-babel-macedonian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-macedonian/macedonian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-macedonian-%{texlive_version}.%{texlive_noarch}.svn39587-%{release}-zypper
%endif

%package -n texlive-babel-malay
Version:        %{texlive_version}.%{texlive_noarch}.1.0msvn43234
Release:        0
Summary:        Support for Malay within babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-malay-doc >= %{texlive_version}
Provides:       tex(bahasam.ldf)
Provides:       tex(malay.ldf)
Provides:       tex(melayu.ldf)
Provides:       tex(meyalu.ldf)
Recommends:     texlive-hyphen-indic
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source186:      babel-malay.tar.xz
Source187:      babel-malay.doc.tar.xz

%description -n texlive-babel-malay
This is the babel style for Malay.

%package -n texlive-babel-malay-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0msvn43234
Release:        0
Summary:        Documentation for texlive-babel-malay
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-malay-doc
This package includes the documentation for texlive-babel-malay

%post -n texlive-babel-malay
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-malay 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-malay
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-malay-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-malay/README
%{_texmfdistdir}/doc/generic/babel-malay/malay.pdf

%files -n texlive-babel-malay
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-malay/bahasam.ldf
%{_texmfdistdir}/tex/generic/babel-malay/malay.ldf
%{_texmfdistdir}/tex/generic/babel-malay/melayu.ldf
%{_texmfdistdir}/tex/generic/babel-malay/meyalu.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-malay-%{texlive_version}.%{texlive_noarch}.1.0msvn43234-%{release}-zypper
%endif

%package -n texlive-babel-norsk
Version:        %{texlive_version}.%{texlive_noarch}.2.0isvn30281
Release:        0
Summary:        Babel support for Norwegian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-norsk-doc >= %{texlive_version}
Provides:       tex(norsk.ldf)
Recommends:     texlive-hyphen-norwegian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source188:      babel-norsk.tar.xz
Source189:      babel-norsk.doc.tar.xz

%description -n texlive-babel-norsk
The package provides the language definition file for support
of Norwegian in babel. Some shortcuts are defined, as well as
translations to Norsk of standard "LaTeX names".

%package -n texlive-babel-norsk-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0isvn30281
Release:        0
Summary:        Documentation for texlive-babel-norsk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-norsk-doc
This package includes the documentation for texlive-babel-norsk

%post -n texlive-babel-norsk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-norsk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-norsk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-norsk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-norsk/norsk.pdf

%files -n texlive-babel-norsk
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-norsk/norsk.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-norsk-%{texlive_version}.%{texlive_noarch}.2.0isvn30281-%{release}-zypper
%endif

%package -n texlive-babel-occitan
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn39608
Release:        0
Summary:        Babel support for Occitan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-occitan-doc >= %{texlive_version}
Provides:       tex(occitan.ldf)
Recommends:     texlive-hyphen-occitan
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source190:      babel-occitan.tar.xz
Source191:      babel-occitan.doc.tar.xz

%description -n texlive-babel-occitan
Occitan language description file with usage instructions.

%package -n texlive-babel-occitan-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.2svn39608
Release:        0
Summary:        Documentation for texlive-babel-occitan
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-occitan-doc
This package includes the documentation for texlive-babel-occitan

%post -n texlive-babel-occitan
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-occitan 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-occitan
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-occitan-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-occitan/README
%{_texmfdistdir}/doc/generic/babel-occitan/occitan.pdf

%files -n texlive-babel-occitan
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-occitan/occitan.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-occitan-%{texlive_version}.%{texlive_noarch}.0.0.2svn39608-%{release}-zypper
%endif

%package -n texlive-babel-piedmontese
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn30282
Release:        0
Summary:        Babel support for Piedmontese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-piedmontese-doc >= %{texlive_version}
Provides:       tex(piedmontese.ldf)
Recommends:     texlive-hyphen-piedmontese
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source192:      babel-piedmontese.tar.xz
Source193:      babel-piedmontese.doc.tar.xz

%description -n texlive-babel-piedmontese
The package provides the language definition file for support
of Piedmontese in babel. Some shortcuts are defined, as well as
translations to Piedmontese of standard "LaTeX names".

%package -n texlive-babel-piedmontese-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0svn30282
Release:        0
Summary:        Documentation for texlive-babel-piedmontese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-piedmontese-doc
This package includes the documentation for texlive-babel-piedmontese

%post -n texlive-babel-piedmontese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-piedmontese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-piedmontese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-piedmontese-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-piedmontese/piedmontese.pdf

%files -n texlive-babel-piedmontese
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-piedmontese/piedmontese.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-piedmontese-%{texlive_version}.%{texlive_noarch}.1.0svn30282-%{release}-zypper
%endif

%package -n texlive-babel-polish
Version:        %{texlive_version}.%{texlive_noarch}.1.2lsvn30283
Release:        0
Summary:        Babel support for Polish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-polish-doc >= %{texlive_version}
Provides:       tex(polish.ldf)
Recommends:     texlive-hyphen-polish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source194:      babel-polish.tar.xz
Source195:      babel-polish.doc.tar.xz

%description -n texlive-babel-polish
The package provides the language definition file for support
of Polish in babel. Some shortcuts are defined, as well as
translations to Polish of standard "LaTeX names".

%package -n texlive-babel-polish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2lsvn30283
Release:        0
Summary:        Documentation for texlive-babel-polish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-polish-doc
This package includes the documentation for texlive-babel-polish

%post -n texlive-babel-polish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-polish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-polish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-polish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-polish/polish.pdf

%files -n texlive-babel-polish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-polish/polish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-polish-%{texlive_version}.%{texlive_noarch}.1.2lsvn30283-%{release}-zypper
%endif

%package -n texlive-babel-portuges
Version:        %{texlive_version}.%{texlive_noarch}.1.2qsvn30284
Release:        0
Summary:        Babel support for Portuges
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-portuges-doc >= %{texlive_version}
Provides:       tex(portuges.ldf)
Recommends:     texlive-hyphen-portuguese
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source196:      babel-portuges.tar.xz
Source197:      babel-portuges.doc.tar.xz

%description -n texlive-babel-portuges
The package provides the language definition file for support
of Portuguese and Brazilian Portuguese in babel. Some shortcuts
are defined, as well as translations to Portuguese of standard
"LaTeX names".

%package -n texlive-babel-portuges-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2qsvn30284
Release:        0
Summary:        Documentation for texlive-babel-portuges
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-portuges-doc
This package includes the documentation for texlive-babel-portuges

%post -n texlive-babel-portuges
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-portuges 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-portuges
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-portuges-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-portuges/portuges.pdf

%files -n texlive-babel-portuges
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-portuges/portuges.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-portuges-%{texlive_version}.%{texlive_noarch}.1.2qsvn30284-%{release}-zypper
%endif

%package -n texlive-babel-romanian
Version:        %{texlive_version}.%{texlive_noarch}.1.2lsvn30285
Release:        0
Summary:        Babel support for Romanian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-romanian-doc >= %{texlive_version}
Provides:       tex(romanian.ldf)
Recommends:     texlive-hyphen-romanian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source198:      babel-romanian.tar.xz
Source199:      babel-romanian.doc.tar.xz

%description -n texlive-babel-romanian
The package provides the language definition file for support
of Romanian in babel. Translations to Romanian of standard
"LaTeX names" are provided.

%package -n texlive-babel-romanian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2lsvn30285
Release:        0
Summary:        Documentation for texlive-babel-romanian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-romanian-doc
This package includes the documentation for texlive-babel-romanian

%post -n texlive-babel-romanian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-romanian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-romanian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-romanian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-romanian/romanian.pdf

%files -n texlive-babel-romanian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-romanian/romanian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-romanian-%{texlive_version}.%{texlive_noarch}.1.2lsvn30285-%{release}-zypper
%endif

%package -n texlive-babel-romansh
Version:        %{texlive_version}.%{texlive_noarch}.svn30286
Release:        0
Summary:        Babel/Polyglossia support for the Romansh language
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-romansh-doc >= %{texlive_version}
Provides:       tex(romansh.ldf)
Recommends:     texlive-hyphen-romansh
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source200:      babel-romansh.tar.xz
Source201:      babel-romansh.doc.tar.xz

%description -n texlive-babel-romansh
The package provides a language description file that enables
support of Romansh either with babel or with polyglossia.

%package -n texlive-babel-romansh-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn30286
Release:        0
Summary:        Documentation for texlive-babel-romansh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-romansh-doc
This package includes the documentation for texlive-babel-romansh

%post -n texlive-babel-romansh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-romansh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-romansh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-romansh-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-romansh/romansh.pdf

%files -n texlive-babel-romansh
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-romansh/romansh.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-romansh-%{texlive_version}.%{texlive_noarch}.svn30286-%{release}-zypper
%endif

%package -n texlive-babel-russian
Version:        %{texlive_version}.%{texlive_noarch}.1.3jsvn45007
Release:        0
Summary:        Russian language module for Babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-russian-doc >= %{texlive_version}
Provides:       tex(russianb.ldf)
Recommends:     texlive-hyphen-russian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source202:      babel-russian.tar.xz
Source203:      babel-russian.doc.tar.xz

%description -n texlive-babel-russian
The package provides support for use of Babel in documents
written in Russian (in both "traditional" and modern forms).
The support is adapted for use both under 'traditional' TeX
engines, and under XeTeX and LuaTeX.

%package -n texlive-babel-russian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.3jsvn45007
Release:        0
Summary:        Documentation for texlive-babel-russian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-russian-doc
This package includes the documentation for texlive-babel-russian

%post -n texlive-babel-russian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-russian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-russian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-russian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-russian/README
%{_texmfdistdir}/doc/generic/babel-russian/russianb.pdf

%files -n texlive-babel-russian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-russian/russianb.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-russian-%{texlive_version}.%{texlive_noarch}.1.3jsvn45007-%{release}-zypper
%endif

%package -n texlive-babel-samin
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn30288
Release:        0
Summary:        Babel support for Samin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-samin-doc >= %{texlive_version}
Provides:       tex(samin.ldf)
Recommends:     texlive-hyphen-norwegian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source204:      babel-samin.tar.xz
Source205:      babel-samin.doc.tar.xz

%description -n texlive-babel-samin
The package provides the language definition file for support
of North Sami in babel. (Several Sami dialects/languages are
spoken in Finland, Norway, Sweden and on the Kola Peninsula of
Russia). Not all use the same alphabet, and no attempt is made
to support any other than North Sami here. Some shortcuts are
defined, as well as translations to Norsk of standard "LaTeX
names".

%package -n texlive-babel-samin-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0csvn30288
Release:        0
Summary:        Documentation for texlive-babel-samin
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-samin-doc
This package includes the documentation for texlive-babel-samin

%post -n texlive-babel-samin
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-samin 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-samin
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-samin-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-samin/samin.pdf

%files -n texlive-babel-samin
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-samin/samin.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-samin-%{texlive_version}.%{texlive_noarch}.1.0csvn30288-%{release}-zypper
%endif

%package -n texlive-babel-scottish
Version:        %{texlive_version}.%{texlive_noarch}.1.0gsvn30289
Release:        0
Summary:        Babel support for Scottish Gaelic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-scottish-doc >= %{texlive_version}
Provides:       tex(scottish.ldf)
Recommends:     texlive-hyphen-galician
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source206:      babel-scottish.tar.xz
Source207:      babel-scottish.doc.tar.xz

%description -n texlive-babel-scottish
The package provides the language definition file for support
of Gaidhlig (Scottish Gaelic) in babel. Some shortcuts are
defined, as well as translations of standard "LaTeX names".

%package -n texlive-babel-scottish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0gsvn30289
Release:        0
Summary:        Documentation for texlive-babel-scottish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-scottish-doc
This package includes the documentation for texlive-babel-scottish

%post -n texlive-babel-scottish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-scottish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-scottish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-scottish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-scottish/scottish.pdf

%files -n texlive-babel-scottish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-scottish/scottish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-scottish-%{texlive_version}.%{texlive_noarch}.1.0gsvn30289-%{release}-zypper
%endif

%package -n texlive-babel-serbian
Version:        %{texlive_version}.%{texlive_noarch}.2.0asvn53140
Release:        0
Summary:        Babel/Polyglossia support for Serbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-serbian-doc >= %{texlive_version}
Provides:       tex(serbian.ldf)
Recommends:     texlive-hyphen-serbian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source208:      babel-serbian.tar.xz
Source209:      babel-serbian.doc.tar.xz

%description -n texlive-babel-serbian
The package provides support for Serbian documents written in
Latin, in babel.

%package -n texlive-babel-serbian-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.0asvn53140
Release:        0
Summary:        Documentation for texlive-babel-serbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-serbian-doc
This package includes the documentation for texlive-babel-serbian

%post -n texlive-babel-serbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-serbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-serbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-serbian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-serbian/README.md
%{_texmfdistdir}/doc/generic/babel-serbian/serbian.pdf

%files -n texlive-babel-serbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-serbian/serbian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-serbian-%{texlive_version}.%{texlive_noarch}.2.0asvn53140-%{release}-zypper
%endif

%package -n texlive-babel-serbianc
Version:        %{texlive_version}.%{texlive_noarch}.3.0asvn53139
Release:        0
Summary:        Babel module to support Serbian Cyrillic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-serbianc-doc >= %{texlive_version}
Provides:       tex(serbianc.ldf)
Recommends:     texlive-hyphen-serbian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source210:      babel-serbianc.tar.xz
Source211:      babel-serbianc.doc.tar.xz

%description -n texlive-babel-serbianc
The package provides support for Serbian documents written in
Cyrillic, in babel.

%package -n texlive-babel-serbianc-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.0asvn53139
Release:        0
Summary:        Documentation for texlive-babel-serbianc
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-serbianc-doc
This package includes the documentation for texlive-babel-serbianc

%post -n texlive-babel-serbianc
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-serbianc 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-serbianc
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-serbianc-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-serbianc/README.md
%{_texmfdistdir}/doc/generic/babel-serbianc/serbianc.pdf

%files -n texlive-babel-serbianc
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-serbianc/serbianc.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-serbianc-%{texlive_version}.%{texlive_noarch}.3.0asvn53139-%{release}-zypper
%endif

%package -n texlive-babel-slovak
Version:        %{texlive_version}.%{texlive_noarch}.3.1asvn30292
Release:        0
Summary:        Babel support for typesetting Slovak
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-slovak-doc >= %{texlive_version}
Provides:       tex(slovak.ldf)
Recommends:     texlive-hyphen-slovak
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source212:      babel-slovak.tar.xz
Source213:      babel-slovak.doc.tar.xz

%description -n texlive-babel-slovak
The package provides the language definition file for support
of Slovak in babel, including Slovak variants of LaTeX
built-in-names. Shortcuts are also defined.

%package -n texlive-babel-slovak-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1asvn30292
Release:        0
Summary:        Documentation for texlive-babel-slovak
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-slovak-doc
This package includes the documentation for texlive-babel-slovak

%post -n texlive-babel-slovak
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-slovak 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-slovak
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-slovak-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-slovak/slovak.pdf

%files -n texlive-babel-slovak
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-slovak/slovak.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-slovak-%{texlive_version}.%{texlive_noarch}.3.1asvn30292-%{release}-zypper
%endif

%package -n texlive-babel-slovenian
Version:        %{texlive_version}.%{texlive_noarch}.1.2isvn30351
Release:        0
Summary:        Babel support for typesetting Slovenian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-slovenian-doc >= %{texlive_version}
Provides:       tex(slovene.ldf)
Recommends:     texlive-hyphen-slovenian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source214:      babel-slovenian.tar.xz
Source215:      babel-slovenian.doc.tar.xz

%description -n texlive-babel-slovenian
The package provides the language definition file for support
of Slovenian in babel. Several shortcuts are defined, as well
as translations to Slovenian of standard "LaTeX names".

%package -n texlive-babel-slovenian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.2isvn30351
Release:        0
Summary:        Documentation for texlive-babel-slovenian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-slovenian-doc
This package includes the documentation for texlive-babel-slovenian

%post -n texlive-babel-slovenian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-slovenian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-slovenian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-slovenian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-slovenian/slovene.pdf

%files -n texlive-babel-slovenian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-slovenian/slovene.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-slovenian-%{texlive_version}.%{texlive_noarch}.1.2isvn30351-%{release}-zypper
%endif

%package -n texlive-babel-sorbian
Version:        %{texlive_version}.%{texlive_noarch}.lower_sorbian_1.0g._upper_1.0ksvn30294
Release:        0
Summary:        Babel support for Upper and Lower Sorbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-sorbian-doc >= %{texlive_version}
Provides:       tex(lsorbian.ldf)
Provides:       tex(usorbian.ldf)
Recommends:     texlive-hyphen-uppersorbian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source216:      babel-sorbian.tar.xz
Source217:      babel-sorbian.doc.tar.xz

%description -n texlive-babel-sorbian
The package provides language definitions file for support of
both Upper and Lower Sorbian, in babel. Some shortcuts are
defined, as well as translations to the relevant language of
standard "LaTeX names".

%package -n texlive-babel-sorbian-doc
Version:        %{texlive_version}.%{texlive_noarch}.lower_sorbian_1.0g._upper_1.0ksvn30294
Release:        0
Summary:        Documentation for texlive-babel-sorbian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-sorbian-doc
This package includes the documentation for texlive-babel-sorbian

%post -n texlive-babel-sorbian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-sorbian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-sorbian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-sorbian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-sorbian/lsorbian.pdf
%{_texmfdistdir}/doc/generic/babel-sorbian/usorbian.pdf

%files -n texlive-babel-sorbian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-sorbian/lsorbian.ldf
%{_texmfdistdir}/tex/generic/babel-sorbian/usorbian.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-sorbian-%{texlive_version}.%{texlive_noarch}.lower_sorbian_1.0g._upper_1.0ksvn30294-%{release}-zypper
%endif

%package -n texlive-babel-spanish
Version:        %{texlive_version}.%{texlive_noarch}.5.0psvn54080
Release:        0
Summary:        Babel support for Spanish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-spanish-doc >= %{texlive_version}
Provides:       tex(romanidx.sty)
Provides:       tex(spanish.ldf)
Recommends:     texlive-hyphen-spanish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source218:      babel-spanish.tar.xz
Source219:      babel-spanish.doc.tar.xz

%description -n texlive-babel-spanish
This bundle provides the means to typeset Spanish text, with
the support provided by the LaTeX standard package babel. Note
that separate support is provided for those who wish to typeset
Spanish as written in Mexico.

%package -n texlive-babel-spanish-doc
Version:        %{texlive_version}.%{texlive_noarch}.5.0psvn54080
Release:        0
Summary:        Documentation for texlive-babel-spanish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-babel-spanish-doc:es)

%description -n texlive-babel-spanish-doc
This package includes the documentation for texlive-babel-spanish

%post -n texlive-babel-spanish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-spanish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-spanish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-spanish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-spanish/README.md
%{_texmfdistdir}/doc/generic/babel-spanish/spanish.pdf

%files -n texlive-babel-spanish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-spanish/romanidx.sty
%{_texmfdistdir}/tex/generic/babel-spanish/spanish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-spanish-%{texlive_version}.%{texlive_noarch}.5.0psvn54080-%{release}-zypper
%endif

%package -n texlive-babel-swedish
Version:        %{texlive_version}.%{texlive_noarch}.2.3dsvn30296
Release:        0
Summary:        Babel support for typesetting Swedish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-swedish-doc >= %{texlive_version}
Provides:       tex(swedish.ldf)
Recommends:     texlive-hyphen-swedish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source220:      babel-swedish.tar.xz
Source221:      babel-swedish.doc.tar.xz

%description -n texlive-babel-swedish
The package provides the language definition file for Swedish.

%package -n texlive-babel-swedish-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.3dsvn30296
Release:        0
Summary:        Documentation for texlive-babel-swedish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-swedish-doc
This package includes the documentation for texlive-babel-swedish

%post -n texlive-babel-swedish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-swedish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-swedish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-swedish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-swedish/swedish.pdf

%files -n texlive-babel-swedish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-swedish/swedish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-swedish-%{texlive_version}.%{texlive_noarch}.2.3dsvn30296-%{release}-zypper
%endif

%package -n texlive-babel-thai
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn30564
Release:        0
Summary:        Support for Thai within babel
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-thai-doc >= %{texlive_version}
Provides:       tex(lthenc.def)
Provides:       tex(thai.ldf)
Provides:       tex(tis620.def)
Recommends:     texlive-hyphen-thai
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source222:      babel-thai.tar.xz
Source223:      babel-thai.doc.tar.xz

%description -n texlive-babel-thai
The package provides support for typesetting Thai text. within
the babel system.

%package -n texlive-babel-thai-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.0.0svn30564
Release:        0
Summary:        Documentation for texlive-babel-thai
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-thai-doc
This package includes the documentation for texlive-babel-thai

%post -n texlive-babel-thai
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-thai 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-thai
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-thai-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-thai/thai.pdf

%files -n texlive-babel-thai
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-thai/lthenc.def
%{_texmfdistdir}/tex/generic/babel-thai/thai.ldf
%{_texmfdistdir}/tex/generic/babel-thai/tis620.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-thai-%{texlive_version}.%{texlive_noarch}.1.0.0svn30564-%{release}-zypper
%endif

%package -n texlive-babel-turkish
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51560
Release:        0
Summary:        Babel support for Turkish documents
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-turkish-doc >= %{texlive_version}
Provides:       tex(turkish.ldf)
Recommends:     texlive-hyphen-turkish
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source224:      babel-turkish.tar.xz
Source225:      babel-turkish.doc.tar.xz

%description -n texlive-babel-turkish
The package provides support, within babel, of the Turkish
language.

%package -n texlive-babel-turkish-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn51560
Release:        0
Summary:        Documentation for texlive-babel-turkish
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-turkish-doc
This package includes the documentation for texlive-babel-turkish

%post -n texlive-babel-turkish
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-turkish 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-turkish
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-turkish-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-turkish/README.md
%{_texmfdistdir}/doc/generic/babel-turkish/turkish.pdf

%files -n texlive-babel-turkish
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-turkish/turkish.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-turkish-%{texlive_version}.%{texlive_noarch}.1.4svn51560-%{release}-zypper
%endif

%package -n texlive-babel-ukrainian
Version:        %{texlive_version}.%{texlive_noarch}.1.4csvn47585
Release:        0
Summary:        Babel support for Ukrainian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-ukrainian-doc >= %{texlive_version}
Provides:       tex(ukraineb.ldf)
Recommends:     texlive-hyphen-ukrainian
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source226:      babel-ukrainian.tar.xz
Source227:      babel-ukrainian.doc.tar.xz

%description -n texlive-babel-ukrainian
The package provides support for use of babel in documents
written in Ukrainian. The support is adapted for use under
legacy TeX engines as well as XeTeX and LuaTeX.

%package -n texlive-babel-ukrainian-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4csvn47585
Release:        0
Summary:        Documentation for texlive-babel-ukrainian
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-ukrainian-doc
This package includes the documentation for texlive-babel-ukrainian

%post -n texlive-babel-ukrainian
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-ukrainian 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-ukrainian
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-ukrainian-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-ukrainian/README.md
%{_texmfdistdir}/doc/generic/babel-ukrainian/ukraineb.pdf

%files -n texlive-babel-ukrainian
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-ukrainian/ukraineb.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-ukrainian-%{texlive_version}.%{texlive_noarch}.1.4csvn47585-%{release}-zypper
%endif

%package -n texlive-babel-vietnamese
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn39246
Release:        0
Summary:        Babel support for typesetting Vietnamese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-vietnamese-doc >= %{texlive_version}
Provides:       tex(vietnamese.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source228:      babel-vietnamese.tar.xz
Source229:      babel-vietnamese.doc.tar.xz

%description -n texlive-babel-vietnamese
The package provides the language definition file for support
of Vietnamese in babel.

%package -n texlive-babel-vietnamese-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4svn39246
Release:        0
Summary:        Documentation for texlive-babel-vietnamese
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-vietnamese-doc
This package includes the documentation for texlive-babel-vietnamese

%post -n texlive-babel-vietnamese
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-vietnamese 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-vietnamese
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-vietnamese-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-vietnamese/README
%{_texmfdistdir}/doc/generic/babel-vietnamese/uvnenc.tex
%{_texmfdistdir}/doc/generic/babel-vietnamese/vietnamese.pdf

%files -n texlive-babel-vietnamese
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-vietnamese/vietnamese.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-vietnamese-%{texlive_version}.%{texlive_noarch}.1.4svn39246-%{release}-zypper
%endif

%package -n texlive-babel-welsh
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn38372
Release:        0
Summary:        Babel support for Welsh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babel-welsh-doc >= %{texlive_version}
Provides:       tex(welsh.ldf)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source230:      babel-welsh.tar.xz
Source231:      babel-welsh.doc.tar.xz

%description -n texlive-babel-welsh
The package provides the language definition file for Welsh.
(Mostly Welsh-language versions of the standard names in a
LaTeX file.)

%package -n texlive-babel-welsh-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1asvn38372
Release:        0
Summary:        Documentation for texlive-babel-welsh
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babel-welsh-doc
This package includes the documentation for texlive-babel-welsh

%post -n texlive-babel-welsh
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babel-welsh 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babel-welsh
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babel-welsh-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/babel-welsh/README
%{_texmfdistdir}/doc/generic/babel-welsh/welsh.pdf

%files -n texlive-babel-welsh
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/babel-welsh/welsh.ldf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babel-welsh-%{texlive_version}.%{texlive_noarch}.1.1asvn38372-%{release}-zypper
%endif

%package -n texlive-babelbib
Version:        %{texlive_version}.%{texlive_noarch}.1.32svn50354
Release:        0
Summary:        Multilingual bibliographies
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-babelbib-doc >= %{texlive_version}
Provides:       tex(babelbib.sty)
Requires:       tex(babel.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source232:      babelbib.tar.xz
Source233:      babelbib.doc.tar.xz

%description -n texlive-babelbib
This package enables the user to generate multilingual
bibliographies in cooperation with babel. Two approaches are
possible: Each citation may be written in another language, or
the whole bibliography can be typeset in a language chosen by
the user. In addition, the package supports commands to change
the typography of the bibliographies.

%package -n texlive-babelbib-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.32svn50354
Release:        0
Summary:        Documentation for texlive-babelbib
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-babelbib-doc
This package includes the documentation for texlive-babelbib

%post -n texlive-babelbib
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-babelbib 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-babelbib
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-babelbib-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/babelbib/ChangeLog
%{_texmfdistdir}/doc/bibtex/babelbib/Makefile
%{_texmfdistdir}/doc/bibtex/babelbib/README
%{_texmfdistdir}/doc/bibtex/babelbib/babelbib.dtx
%{_texmfdistdir}/doc/bibtex/babelbib/babelbib.ins
%{_texmfdistdir}/doc/bibtex/babelbib/babelbib.pdf
%{_texmfdistdir}/doc/bibtex/babelbib/babelbibtest.bib
%{_texmfdistdir}/doc/bibtex/babelbib/babelbibtest.tex
%{_texmfdistdir}/doc/bibtex/babelbib/getversion.tex
%{_texmfdistdir}/doc/bibtex/babelbib/tugboat-babelbib.pdf

%files -n texlive-babelbib
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/babelbib/bababbr3-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbr3-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbr3.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbrv-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbrv-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/bababbrv.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babalpha-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babalpha-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babalpha.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babamspl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplai3-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplai3-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplai3.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babplain.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babunsrt-fl.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babunsrt-lf.bst
%{_texmfdistdir}/bibtex/bst/babelbib/babunsrt.bst
%{_texmfdistdir}/tex/latex/babelbib/afrikaans.bdf
%{_texmfdistdir}/tex/latex/babelbib/babelbib.sty
%{_texmfdistdir}/tex/latex/babelbib/bahasa.bdf
%{_texmfdistdir}/tex/latex/babelbib/catalan.bdf
%{_texmfdistdir}/tex/latex/babelbib/croatian.bdf
%{_texmfdistdir}/tex/latex/babelbib/czech.bdf
%{_texmfdistdir}/tex/latex/babelbib/danish.bdf
%{_texmfdistdir}/tex/latex/babelbib/dutch.bdf
%{_texmfdistdir}/tex/latex/babelbib/english.bdf
%{_texmfdistdir}/tex/latex/babelbib/esperanto.bdf
%{_texmfdistdir}/tex/latex/babelbib/finnish.bdf
%{_texmfdistdir}/tex/latex/babelbib/french.bdf
%{_texmfdistdir}/tex/latex/babelbib/galician.bdf
%{_texmfdistdir}/tex/latex/babelbib/german.bdf
%{_texmfdistdir}/tex/latex/babelbib/greek.bdf
%{_texmfdistdir}/tex/latex/babelbib/italian.bdf
%{_texmfdistdir}/tex/latex/babelbib/norsk.bdf
%{_texmfdistdir}/tex/latex/babelbib/portuguese.bdf
%{_texmfdistdir}/tex/latex/babelbib/romanian.bdf
%{_texmfdistdir}/tex/latex/babelbib/russian.bdf
%{_texmfdistdir}/tex/latex/babelbib/serbian.bdf
%{_texmfdistdir}/tex/latex/babelbib/spanish.bdf
%{_texmfdistdir}/tex/latex/babelbib/swedish.bdf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-babelbib-%{texlive_version}.%{texlive_noarch}.1.32svn50354-%{release}-zypper
%endif

%package -n texlive-background
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn42428
Release:        0
Summary:        Placement of background material on pages of a document
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-background-doc >= %{texlive_version}
Provides:       tex(background.sty)
Requires:       tex(afterpage.sty)
Requires:       tex(everypage.sty)
Requires:       tex(tikz.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source234:      background.tar.xz
Source235:      background.doc.tar.xz

%description -n texlive-background
The package offers the placement of background material on the
pages of a document. The user can control many aspects
(contents, position, color, opacity) of the background material
that will be displayed; all placement and attribute settings
are controlled by setting key values. The package makes use of
the everypage package, and uses pgf/tikz for attribute control.

%package -n texlive-background-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.1svn42428
Release:        0
Summary:        Documentation for texlive-background
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-background-doc
This package includes the documentation for texlive-background

%post -n texlive-background
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-background 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-background
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-background-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/background/README
%{_texmfdistdir}/doc/latex/background/background.pdf

%files -n texlive-background
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/background/background.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-background-%{texlive_version}.%{texlive_noarch}.2.1svn42428-%{release}-zypper
%endif

%package -n texlive-backnaur
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn54080
Release:        0
Summary:        Typeset Backus Naur Form definitions
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-backnaur-doc >= %{texlive_version}
Provides:       tex(backnaur.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source236:      backnaur.tar.xz
Source237:      backnaur.doc.tar.xz

%description -n texlive-backnaur
The package typesets Backus-Naur Form (BNF) definitions. It
prints formatted lists of productions, with numbers if
required. It can also print in-line BNF expressions using math
mode.

%package -n texlive-backnaur-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.1svn54080
Release:        0
Summary:        Documentation for texlive-backnaur
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-backnaur-doc
This package includes the documentation for texlive-backnaur

%post -n texlive-backnaur
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-backnaur 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-backnaur
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-backnaur-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/backnaur/README
%{_texmfdistdir}/doc/latex/backnaur/backnaur.pdf

%files -n texlive-backnaur
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/backnaur/backnaur.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-backnaur-%{texlive_version}.%{texlive_noarch}.3.1svn54080-%{release}-zypper
%endif

%package -n texlive-baekmuk
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn42106
Release:        0
Summary:        Baekmuk Korean TrueType fonts
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-baekmuk-fonts >= %{texlive_version}
Recommends:     texlive-baekmuk-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source238:      baekmuk.tar.xz
Source239:      baekmuk.doc.tar.xz

%description -n texlive-baekmuk
Baekmuk TrueType fonts (Korean) These fonts were retrieved from
http://kldp.net/baekmuk/

%package -n texlive-baekmuk-doc
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn42106
Release:        0
Summary:        Documentation for texlive-baekmuk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-baekmuk-doc
This package includes the documentation for texlive-baekmuk


%package -n texlive-baekmuk-fonts
Version:        %{texlive_version}.%{texlive_noarch}.2.2svn42106
Release:        0
Summary:        Severed fonts for texlive-baekmuk
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-baekmuk-fonts
The  separated fonts package for texlive-baekmuk
%post -n texlive-baekmuk
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-baekmuk 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-baekmuk
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-baekmuk-fonts
%files -n texlive-baekmuk-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/baekmuk/COPYRIGHT
%{_texmfdistdir}/doc/fonts/baekmuk/COPYRIGHT.ks
%{_texmfdistdir}/doc/fonts/baekmuk/README.md
%{_texmfdistdir}/doc/fonts/baekmuk/README_original

%files -n texlive-baekmuk
%defattr(-,root,root,755)
%verify(link) %{_texmfdistdir}/fonts/truetype/public/baekmuk/batang.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/baekmuk/dotum.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/baekmuk/gulim.ttf
%verify(link) %{_texmfdistdir}/fonts/truetype/public/baekmuk/hline.ttf

%files -n texlive-baekmuk-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-baekmuk
%{_datadir}/fontconfig/conf.avail/58-texlive-baekmuk.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baekmuk/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baekmuk/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baekmuk/fonts.scale
%{_datadir}/fonts/texlive-baekmuk/batang.ttf
%{_datadir}/fonts/texlive-baekmuk/dotum.ttf
%{_datadir}/fonts/texlive-baekmuk/gulim.ttf
%{_datadir}/fonts/texlive-baekmuk/hline.ttf
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-baekmuk-fonts-%{texlive_version}.%{texlive_noarch}.2.2svn42106-%{release}-zypper
%endif

%package -n texlive-bagpipe
Version:        %{texlive_version}.%{texlive_noarch}.3.02svn34393
Release:        0
Summary:        Support for typesetting bagpipe music
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bagpipe-doc >= %{texlive_version}
Provides:       tex(bagpipe.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source240:      bagpipe.tar.xz
Source241:      bagpipe.doc.tar.xz

%description -n texlive-bagpipe
Typesetting bagpipe music in MusixTeX is needlessly tedious.
This package provides specialized and re-defined macros to
simplify this task.

%package -n texlive-bagpipe-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.02svn34393
Release:        0
Summary:        Documentation for texlive-bagpipe
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bagpipe-doc
This package includes the documentation for texlive-bagpipe

%post -n texlive-bagpipe
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bagpipe 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bagpipe
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bagpipe-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/bagpipe/BlackDonald.pdf
%{_texmfdistdir}/doc/generic/bagpipe/BlackDonald.tex
%{_texmfdistdir}/doc/generic/bagpipe/Bonnets.pdf
%{_texmfdistdir}/doc/generic/bagpipe/Bonnets.tex
%{_texmfdistdir}/doc/generic/bagpipe/Green.pdf
%{_texmfdistdir}/doc/generic/bagpipe/Green.tex
%{_texmfdistdir}/doc/generic/bagpipe/GreenTwo.pdf
%{_texmfdistdir}/doc/generic/bagpipe/GreenTwo.tex
%{_texmfdistdir}/doc/generic/bagpipe/README
%{_texmfdistdir}/doc/generic/bagpipe/Washer.pdf
%{_texmfdistdir}/doc/generic/bagpipe/Washer.tex
%{_texmfdistdir}/doc/generic/bagpipe/bagdoc.pdf
%{_texmfdistdir}/doc/generic/bagpipe/bagdoc.tex
%{_texmfdistdir}/doc/generic/bagpipe/quickref.pdf
%{_texmfdistdir}/doc/generic/bagpipe/quickref.tex

%files -n texlive-bagpipe
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/bagpipe/bagpipe.ini
%{_texmfdistdir}/tex/generic/bagpipe/bagpipe.tex
%{_texmfdistdir}/tex/generic/bagpipe/bagpipex.ini
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bagpipe-%{texlive_version}.%{texlive_noarch}.3.02svn34393-%{release}-zypper
%endif

%package -n texlive-bangorcsthesis
Version:        %{texlive_version}.%{texlive_noarch}.1.5.3svn48834
Release:        0
Summary:        Typeset a thesis at Bangor University
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bangorcsthesis-doc >= %{texlive_version}
Provides:       tex(bangorcsthesis.cls)
Requires:       tex(amsmath.sty)
Requires:       tex(babel.sty)
Requires:       tex(berasans.sty)
Requires:       tex(cleveref.sty)
Requires:       tex(csquotes.sty)
Requires:       tex(draftwatermark.sty)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyhdr.sty)
Requires:       tex(fifo-stack.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(forloop.sty)
Requires:       tex(framed.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(hyperref.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(indentfirst.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(isodate.sty)
Requires:       tex(microtype.sty)
Requires:       tex(newtxmath.sty)
Requires:       tex(newtxtext.sty)
Requires:       tex(parskip.sty)
Requires:       tex(report.cls)
Requires:       tex(setspace.sty)
Requires:       tex(tikz.sty)
Requires:       tex(titlesec.sty)
Requires:       tex(tocloft.sty)
Requires:       tex(totalcount.sty)
Requires:       tex(url.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xparse.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source242:      bangorcsthesis.tar.xz
Source243:      bangorcsthesis.doc.tar.xz

%description -n texlive-bangorcsthesis
The class typesets thesis/dissertation documents for all levels
(i.e., both undergraduate and graduate students may use the
class). It also provides macros designed to optimise the
process of producing a thesis.

%package -n texlive-bangorcsthesis-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.5.3svn48834
Release:        0
Summary:        Documentation for texlive-bangorcsthesis
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bangorcsthesis-doc
This package includes the documentation for texlive-bangorcsthesis

%post -n texlive-bangorcsthesis
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bangorcsthesis 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bangorcsthesis
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bangorcsthesis-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/bangorcsthesis/README
%{_texmfdistdir}/doc/latex/bangorcsthesis/bangorcsthesis.pdf

%files -n texlive-bangorcsthesis
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/bangorcsthesis/bangorcsthesis.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bangorcsthesis-%{texlive_version}.%{texlive_noarch}.1.5.3svn48834-%{release}-zypper
%endif

%package -n texlive-bangorexam
Version:        %{texlive_version}.%{texlive_noarch}.1.4.0svn46626
Release:        0
Summary:        Typeset an examination at Bangor University
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bangorexam-doc >= %{texlive_version}
Provides:       tex(bangorexam.cls)
Requires:       tex(array.sty)
Requires:       tex(babel.sty)
Requires:       tex(color.sty)
Requires:       tex(courier.sty)
Requires:       tex(etoolbox.sty)
Requires:       tex(exam.cls)
Requires:       tex(fontenc.sty)
Requires:       tex(forloop.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(inputenc.sty)
Requires:       tex(isodate.sty)
Requires:       tex(letltxmacro.sty)
Requires:       tex(newpxmath.sty)
Requires:       tex(newpxtext.sty)
Requires:       tex(tikz.sty)
Requires:       tex(totcount.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source244:      bangorexam.tar.xz
Source245:      bangorexam.doc.tar.xz

%description -n texlive-bangorexam
The package allows typesetting of Bangor Univesity's exam
style. It currently supports a standard A/B choice, A-only
compulsory and 'n' from 'm' exam styles. Marks are totalled and
checked automatically.

%package -n texlive-bangorexam-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.4.0svn46626
Release:        0
Summary:        Documentation for texlive-bangorexam
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bangorexam-doc
This package includes the documentation for texlive-bangorexam

%post -n texlive-bangorexam
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bangorexam 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bangorexam
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bangorexam-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/bangorexam/README.txt
%{_texmfdistdir}/doc/latex/bangorexam/bangorexam.pdf

%files -n texlive-bangorexam
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/bangorexam/bangorexam.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bangorexam-%{texlive_version}.%{texlive_noarch}.1.4.0svn46626-%{release}-zypper
%endif

%package -n texlive-bangtex
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Writing Bangla and Assamese with LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bangtex-doc >= %{texlive_version}
Provides:       tex(bang10.tfm)
Provides:       tex(bangfont.tex)
Provides:       tex(bangsl10.tfm)
Provides:       tex(bangwd10.tfm)
Provides:       tex(barticle.cls)
Provides:       tex(bbk10.clo)
Provides:       tex(bbk11.clo)
Provides:       tex(bbk12.clo)
Provides:       tex(bbook.cls)
Provides:       tex(bletter.cls)
Provides:       tex(bsize10.clo)
Provides:       tex(bsize11.clo)
Provides:       tex(bsize12.clo)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source246:      bangtex.tar.xz
Source247:      bangtex.doc.tar.xz

%description -n texlive-bangtex
The bundle provides class files for writing Bangla and Assamese
with LaTeX, and Metafont sources for fonts.

%package -n texlive-bangtex-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-bangtex
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bangtex-doc
This package includes the documentation for texlive-bangtex

%post -n texlive-bangtex
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bangtex 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bangtex
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bangtex-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/bangtex/README.bangtex
%{_texmfdistdir}/doc/latex/bangtex/manual.tex
%{_texmfdistdir}/doc/latex/bangtex/samplett.tex
%{_texmfdistdir}/doc/latex/bangtex/samptex.tex

%files -n texlive-bangtex
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/bangtex/bang10.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangbase.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangconso.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangdefs.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangfala.mf
%{_texmfdistdir}/fonts/source/public/bangtex/banghalf.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangjuk.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangkaar.mf
%{_texmfdistdir}/fonts/source/public/bangtex/banglig.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangmac.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangnum.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangpunc.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangsl10.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangvow.mf
%{_texmfdistdir}/fonts/source/public/bangtex/bangwd10.mf
%{_texmfdistdir}/fonts/tfm/public/bangtex/bang10.tfm
%{_texmfdistdir}/fonts/tfm/public/bangtex/bangsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bangtex/bangwd10.tfm
%{_texmfdistdir}/tex/latex/bangtex/bangfont.tex
%{_texmfdistdir}/tex/latex/bangtex/barticle.cls
%{_texmfdistdir}/tex/latex/bangtex/bbk10.clo
%{_texmfdistdir}/tex/latex/bangtex/bbk11.clo
%{_texmfdistdir}/tex/latex/bangtex/bbk12.clo
%{_texmfdistdir}/tex/latex/bangtex/bbook.cls
%{_texmfdistdir}/tex/latex/bangtex/bletter.cls
%{_texmfdistdir}/tex/latex/bangtex/bsize10.clo
%{_texmfdistdir}/tex/latex/bangtex/bsize11.clo
%{_texmfdistdir}/tex/latex/bangtex/bsize12.clo
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bangtex-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-bankstatement
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.2svn38857
Release:        0
Summary:        A LaTeX class for bank statements based on csv data
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bankstatement-doc >= %{texlive_version}
Provides:       tex(bankstatement.cls)
Provides:       tex(csv-camt.def)
Provides:       tex(csv-mt940.def)
Provides:       tex(csv-standard-bank-na.def)
Provides:       tex(stmenglish.def)
Provides:       tex(stmgerman.def)
Provides:       tex(stmnamibian.def)
Requires:       tex(article.cls)
Requires:       tex(booktabs.sty)
Requires:       tex(calc.sty)
Requires:       tex(datatool.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(longtable.sty)
Requires:       tex(siunitx.sty)
Requires:       tex(tabularx.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
Requires:       tex(xkvltxp.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source248:      bankstatement.tar.xz
Source249:      bankstatement.doc.tar.xz

%description -n texlive-bankstatement
More and more banks allow their customers to download posting
records in various formats. By using the bankstatement class,
you can create bank statements, as long as a csv format is
available. At the moment, the csv-mt940 and csv-camt formats --
used by many german Sparkassen -- are supported. You can quite
easily add support for other csv formats. Simply define the
order of the keys in the csv data file and how to use them. The
terminology in this class -- such as BIC (Business Identifier
Code) or IBAN (International Bank Account Number) -- is based
on usage in the SEPA (Single Euro Payments Area). The user may
adjust the terminology to suit local needs.

%package -n texlive-bankstatement-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.9.2svn38857
Release:        0
Summary:        Documentation for texlive-bankstatement
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bankstatement-doc
This package includes the documentation for texlive-bankstatement

%post -n texlive-bankstatement
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bankstatement 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bankstatement
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bankstatement-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/bankstatement/201412.csv
%{_texmfdistdir}/doc/latex/bankstatement/README.md
%{_texmfdistdir}/doc/latex/bankstatement/bankstatement-example.pdf
%{_texmfdistdir}/doc/latex/bankstatement/bankstatement-example.tex
%{_texmfdistdir}/doc/latex/bankstatement/bankstatement.dtx
%{_texmfdistdir}/doc/latex/bankstatement/bankstatement.pdf
%{_texmfdistdir}/doc/latex/bankstatement/makefile
%{_texmfdistdir}/doc/latex/bankstatement/stmlogo.jpg

%files -n texlive-bankstatement
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/bankstatement/bankstatement.cls
%{_texmfdistdir}/tex/latex/bankstatement/csv-camt.def
%{_texmfdistdir}/tex/latex/bankstatement/csv-mt940.def
%{_texmfdistdir}/tex/latex/bankstatement/csv-standard-bank-na.def
%{_texmfdistdir}/tex/latex/bankstatement/stmenglish.def
%{_texmfdistdir}/tex/latex/bankstatement/stmgerman.def
%{_texmfdistdir}/tex/latex/bankstatement/stmnamibian.def
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bankstatement-%{texlive_version}.%{texlive_noarch}.0.0.9.2svn38857-%{release}-zypper
%endif

%package -n texlive-barcodes
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Fonts for making barcodes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-barcodes-doc >= %{texlive_version}
Provides:       tex(barcodes.sty)
Provides:       tex(wlc11.tfm)
Provides:       tex(wlc128.tfm)
Provides:       tex(wlc39.tfm)
Provides:       tex(wlc93.tfm)
Provides:       tex(wlcr39.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source250:      barcodes.tar.xz
Source251:      barcodes.doc.tar.xz

%description -n texlive-barcodes
The package deals with EAN barcodes; Metafont sources for fonts
are provided, and a set of examples; for some codes, a small
Perl script is needed.

%package -n texlive-barcodes-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn15878
Release:        0
Summary:        Documentation for texlive-barcodes
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-barcodes-doc
This package includes the documentation for texlive-barcodes

%post -n texlive-barcodes
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-barcodes 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-barcodes
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-barcodes-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/barcodes/README
%{_texmfdistdir}/doc/latex/barcodes/bcfaq.tex
%{_texmfdistdir}/doc/latex/barcodes/changes
%{_texmfdistdir}/doc/latex/barcodes/code39.tex
%{_texmfdistdir}/doc/latex/barcodes/codean.pl
%{_texmfdistdir}/doc/latex/barcodes/eandoc.pdf
%{_texmfdistdir}/doc/latex/barcodes/eandoc.tex
%{_texmfdistdir}/doc/latex/barcodes/examples.tex
%{_texmfdistdir}/doc/latex/barcodes/wlcdb.vpl
%{_texmfdistdir}/doc/latex/barcodes/wlcf39.vpl
%{_texmfdistdir}/doc/latex/barcodes/wlitf.vpl

%files -n texlive-barcodes
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/barcodes/wlc11.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlc128.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlc39.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlc93.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlcr39.mf
%{_texmfdistdir}/fonts/source/public/barcodes/wlean.mf
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc11.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc128.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc39.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlc93.tfm
%{_texmfdistdir}/fonts/tfm/public/barcodes/wlcr39.tfm
%{_texmfdistdir}/tex/latex/barcodes/barcodes.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-barcodes-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif

%package -n texlive-bardiag
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn22013
Release:        0
Summary:        LaTeX package for drawing bar diagrams
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bardiag-doc >= %{texlive_version}
Provides:       tex(barddoc.sty)
Provides:       tex(bardiag.cfg)
Provides:       tex(bardiag.sty)
Provides:       tex(pstfp.sty)
Requires:       tex(calc.sty)
Requires:       tex(fp-snap.sty)
Requires:       tex(geometry.sty)
Requires:       tex(graphicx.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(listings.sty)
Requires:       tex(makeidx.sty)
Requires:       tex(multido.sty)
Requires:       tex(pst-grad.sty)
Requires:       tex(pstcol.sty)
Requires:       tex(pstricks.sty)
Requires:       tex(subfigure.sty)
Requires:       tex(verbatim.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source252:      bardiag.tar.xz
Source253:      bardiag.doc.tar.xz

%description -n texlive-bardiag
The main purpose of the package is to make the drawing of bar
diagrams possible and easy in LaTeX. The BarDiag package is
inspired by and based on PSTricks.

%package -n texlive-bardiag-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.4asvn22013
Release:        0
Summary:        Documentation for texlive-bardiag
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bardiag-doc
This package includes the documentation for texlive-bardiag

%post -n texlive-bardiag
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bardiag 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bardiag
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bardiag-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/bardiag/README
%{_texmfdistdir}/doc/latex/bardiag/bardiag.pdf
%{_texmfdistdir}/doc/latex/bardiag/bardiag.tex
%{_texmfdistdir}/doc/latex/bardiag/bardiag1.pdf
%{_texmfdistdir}/doc/latex/bardiag/bardiag1.tex
%{_texmfdistdir}/doc/latex/bardiag/bardiag2.pdf
%{_texmfdistdir}/doc/latex/bardiag/bardiag2.tex
%{_texmfdistdir}/doc/latex/bardiag/example/altdiags.ps
%{_texmfdistdir}/doc/latex/bardiag/example/altdiags.tex
%{_texmfdistdir}/doc/latex/bardiag/example/compile.all
%{_texmfdistdir}/doc/latex/bardiag/example/diagrams.dvi
%{_texmfdistdir}/doc/latex/bardiag/example/diagrams.ps
%{_texmfdistdir}/doc/latex/bardiag/example/diagrams.tex
%{_texmfdistdir}/doc/latex/bardiag/example/diagramsbw.ps
%{_texmfdistdir}/doc/latex/bardiag/example/diagramsbw.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/10.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/1a.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/1b.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/2a.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/2b.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/3.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/4.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/5.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/6.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/7.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/8.tex
%{_texmfdistdir}/doc/latex/bardiag/example/src/9.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/diag.eps
%{_texmfdistdir}/doc/latex/bardiag/figs/diagleg.eps
%{_texmfdistdir}/doc/latex/bardiag/figs/examp1.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp1a.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp1b.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp2.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp2er.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp3.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp4.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp5.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/examp6.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/exampcr.tex
%{_texmfdistdir}/doc/latex/bardiag/figs/tddiag.eps
%{_texmfdistdir}/doc/latex/bardiag/src/10.tex
%{_texmfdistdir}/doc/latex/bardiag/src/1a.tex
%{_texmfdistdir}/doc/latex/bardiag/src/1b.tex
%{_texmfdistdir}/doc/latex/bardiag/src/2a.tex
%{_texmfdistdir}/doc/latex/bardiag/src/2b.tex
%{_texmfdistdir}/doc/latex/bardiag/src/3.tex
%{_texmfdistdir}/doc/latex/bardiag/src/4.tex
%{_texmfdistdir}/doc/latex/bardiag/src/5.tex
%{_texmfdistdir}/doc/latex/bardiag/src/6.tex
%{_texmfdistdir}/doc/latex/bardiag/src/7.tex
%{_texmfdistdir}/doc/latex/bardiag/src/8.tex
%{_texmfdistdir}/doc/latex/bardiag/src/9.tex

%files -n texlive-bardiag
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/bardiag/barddoc.sty
%{_texmfdistdir}/tex/latex/bardiag/bardiag.bar
%{_texmfdistdir}/tex/latex/bardiag/bardiag.cfg
%{_texmfdistdir}/tex/latex/bardiag/bardiag.sty
%{_texmfdistdir}/tex/latex/bardiag/pstfp.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bardiag-%{texlive_version}.%{texlive_noarch}.0.0.4asvn22013-%{release}-zypper
%endif

%package -n texlive-barr
Version:        %{texlive_version}.%{texlive_noarch}.svn38479
Release:        0
Summary:        Diagram macros by Michael Barr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-barr-doc >= %{texlive_version}
Provides:       tex(diagxy.tex)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source254:      barr.tar.xz
Source255:      barr.doc.tar.xz

%description -n texlive-barr
Diagxy is a general diagramming package, useful for diagrams in
a number of mathematical disciplines. Diagxy is a development
of an earlier (successful) package to use the facilities of the
xypic bundle.

%package -n texlive-barr-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn38479
Release:        0
Summary:        Documentation for texlive-barr
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-barr-doc
This package includes the documentation for texlive-barr

%post -n texlive-barr
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-barr 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-barr
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-barr-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/generic/barr/README
%{_texmfdistdir}/doc/generic/barr/diaxydoc.pdf
%{_texmfdistdir}/doc/generic/barr/diaxydoc.tex

%files -n texlive-barr
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/generic/barr/diagxy.tex
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-barr-%{texlive_version}.%{texlive_noarch}.svn38479-%{release}-zypper
%endif

%package -n texlive-barracuda
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.10svn53683
Release:        0
Summary:        Draw barcodes with Lua
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-barracuda-doc >= %{texlive_version}
Provides:       tex(barracuda.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source256:      barracuda.tar.xz
Source257:      barracuda.doc.tar.xz

%description -n texlive-barracuda
The barracuda library is a modular Lua package for drawing
barcode symbols. It provides modules for writing barcodes from
a LuaTeX document. It is also possible to use Barracuda with a
standalone Lua interpreter to draw barcodes in different
graphic formats like SVG.

%package -n texlive-barracuda-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.0.10svn53683
Release:        0
Summary:        Documentation for texlive-barracuda
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-barracuda-doc
This package includes the documentation for texlive-barracuda

%post -n texlive-barracuda
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-barracuda 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-barracuda
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-barracuda-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/luatex/barracuda/INSTALL.txt
%{_texmfdistdir}/doc/luatex/barracuda/LICENSE.txt
%{_texmfdistdir}/doc/luatex/barracuda/PLANNER.txt
%{_texmfdistdir}/doc/luatex/barracuda/README.md
%{_texmfdistdir}/doc/luatex/barracuda/doc/barracuda-ga-asm.pdf
%{_texmfdistdir}/doc/luatex/barracuda/doc/barracuda-ga-asm.tex
%{_texmfdistdir}/doc/luatex/barracuda/doc/barracuda-manual-tool.tex
%{_texmfdistdir}/doc/luatex/barracuda/doc/barracuda.pdf
%{_texmfdistdir}/doc/luatex/barracuda/doc/barracuda.tex
%{_texmfdistdir}/doc/luatex/barracuda/doc/image/8006194056290.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-barracuda-package/01-barracuda-latex-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-barracuda-package/01-barracuda-latex-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-barracuda-package/02-ord_iter-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code128/001-code128-test.lua
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code128/002-code128-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code128/002-code128-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code128/02-05-pdfliteral.txt
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code128/c128-123.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/001-code39-test.lua
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/002-code39-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/002-code39-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/003-code39-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/003-code39-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/004-code39-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/004-code39-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/005-code39-test.lua
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/006-code39-test.lua
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/006-six.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-code39/my_barcode.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/001-13-ean-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/001-13-ean-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/002-ean-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/002-ean-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/003-ean-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/003-ean-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/004-ean-test.lua
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/005-isbn-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/005-isbn-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/006-issn-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/006-issn-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/8006194056290.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ean/ars.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ga-pdfliteral/001-ga-pdfliteral-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ga-pdfliteral/001-ga-pdfliteral-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ga-svg/001-ga-svg-test.lua
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ga-svg/002-ga-svg-test.lua
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ga-svg/test-01.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ga-svg/test-02.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-ga-svg/test-code39.svg
%{_texmfdistdir}/doc/luatex/barracuda/test/test-i2of5/001-i2of5-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-i2of5/001-i2of5-test.tex
%{_texmfdistdir}/doc/luatex/barracuda/test/test-i2of5/002-ITF14-test.pdf
%{_texmfdistdir}/doc/luatex/barracuda/test/test-i2of5/002-ITF14-test.tex

%files -n texlive-barracuda
%defattr(-,root,root,755)
%{_texmfdistdir}/scripts/barracuda/barracuda.lua
%{_texmfdistdir}/scripts/barracuda/lib-barcode/brcd-barcode.lua
%{_texmfdistdir}/scripts/barracuda/lib-barcode/brcd-code128.lua
%{_texmfdistdir}/scripts/barracuda/lib-barcode/brcd-code39.lua
%{_texmfdistdir}/scripts/barracuda/lib-barcode/brcd-ean.lua
%{_texmfdistdir}/scripts/barracuda/lib-barcode/brcd-i2of5.lua
%{_texmfdistdir}/scripts/barracuda/lib-driver/brcd-driver.lua
%{_texmfdistdir}/scripts/barracuda/lib-driver/brcd-drv-pdfliteral.lua
%{_texmfdistdir}/scripts/barracuda/lib-driver/brcd-drv-svg.lua
%{_texmfdistdir}/scripts/barracuda/lib-geo/brcd-gacanvas.lua
%{_texmfdistdir}/scripts/barracuda/lib-geo/brcd-libgeo.lua
%{_texmfdistdir}/tex/luatex/barracuda/barracuda.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-barracuda-%{texlive_version}.%{texlive_noarch}.0.0.0.10svn53683-%{release}-zypper
%endif

%package -n texlive-bartel-chess-fonts
Version:        %{texlive_version}.%{texlive_noarch}.svn20619
Release:        0
Summary:        A set of fonts supporting chess diagrams
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bartel-chess-fonts-doc >= %{texlive_version}
Provides:       tex(fselch10.tfm)
Provides:       tex(fselch11.tfm)
Provides:       tex(fselch12.tfm)
Provides:       tex(fselch13.tfm)
Provides:       tex(fselch14.tfm)
Provides:       tex(fselch16.tfm)
Provides:       tex(fselch17.tfm)
Provides:       tex(fselch20.tfm)
Provides:       tex(fselch24.tfm)
Provides:       tex(fselch32.tfm)
Provides:       tex(fselch36.tfm)
Provides:       tex(fselch6.tfm)
Provides:       tex(fselch7.tfm)
Provides:       tex(fselch8.tfm)
Provides:       tex(fselch9.tfm)
Provides:       tex(pkelch10.tfm)
Provides:       tex(pkelch11.tfm)
Provides:       tex(pkelch12.tfm)
Provides:       tex(pkelch14.tfm)
Provides:       tex(pkelch16.tfm)
Provides:       tex(pkelch8.tfm)
Provides:       tex(pkelch9.tfm)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source258:      bartel-chess-fonts.tar.xz
Source259:      bartel-chess-fonts.doc.tar.xz

%description -n texlive-bartel-chess-fonts
The fonts are provided as Metafont source.

%package -n texlive-bartel-chess-fonts-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn20619
Release:        0
Summary:        Documentation for texlive-bartel-chess-fonts
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bartel-chess-fonts-doc
This package includes the documentation for texlive-bartel-chess-fonts

%post -n texlive-bartel-chess-fonts
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bartel-chess-fonts 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bartel-chess-fonts
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bartel-chess-fonts-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/README
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/CGA.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/agfa.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/amiga-PAL.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/amiga.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/chess.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch15.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch30.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch34.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/fselch5mm.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkelch.mfj
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkfootbows.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkmakeneutral.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkparallel.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkscreengrid.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/pkshorten.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px150.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px17.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px20.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px21.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px23.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px25.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px29.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px31.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px33.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px41.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px45.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px49.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px53.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px57.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px63.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px700.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px71.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px72.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px79.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/px9.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/scan.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/screengrid.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/tt.mf
%{_texmfdistdir}/doc/fonts/bartel-chess-fonts/other-sources/turnboard.mf

%files -n texlive-bartel-chess-fonts
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-bishop.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-blackfield.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-chbase.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-equi.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-geo.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-king.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-knight.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-pawn.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-queen.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/elch-rook.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch10.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch11.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch12.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch13.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch14.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch16.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch17.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch20.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch24.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch32.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch36.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch6.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch7.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch8.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/fselch9.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkbase.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkbishop.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkblackfield.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch10.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch11.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch12.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch14.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch16.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch8.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkelch9.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkgeo.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkking.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkknight.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkpawn.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkqueen.mf
%{_texmfdistdir}/fonts/source/public/bartel-chess-fonts/pkrook.mf
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch10.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch11.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch12.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch13.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch14.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch16.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch17.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch20.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch24.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch32.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch36.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch6.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch7.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch8.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/fselch9.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch10.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch11.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch12.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch14.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch16.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch8.tfm
%{_texmfdistdir}/fonts/tfm/public/bartel-chess-fonts/pkelch9.tfm
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bartel-chess-fonts-%{texlive_version}.%{texlive_noarch}.svn20619-%{release}-zypper
%endif

%package -n texlive-bashful
Version:        %{texlive_version}.%{texlive_noarch}.0.0.93svn25597
Release:        0
Summary:        Invoke bash commands from within LaTeX
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bashful-doc >= %{texlive_version}
Provides:       tex(bashful.sty)
Requires:       tex(catchfile.sty)
Requires:       tex(listings.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xcolor.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source260:      bashful.tar.xz
Source261:      bashful.doc.tar.xz

%description -n texlive-bashful
The package makes it possible to execute Unix bash shell
scripts from within LaTeX. The main application is in writing
computer-science texts, in which you want to make sure the
programs listed in the document are executed directly from the
input. The package may use other Unix shells than bash, but
does not work without modification in a Windows environment.
The package requires the -shell-escape flag when LaTeX is
processing your document.

%package -n texlive-bashful-doc
Version:        %{texlive_version}.%{texlive_noarch}.0.0.93svn25597
Release:        0
Summary:        Documentation for texlive-bashful
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bashful-doc
This package includes the documentation for texlive-bashful

%post -n texlive-bashful
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bashful 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bashful
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bashful-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/bashful/Makefile
%{_texmfdistdir}/doc/latex/bashful/README
%{_texmfdistdir}/doc/latex/bashful/bashful.pdf
%{_texmfdistdir}/doc/latex/bashful/bashful.tex

%files -n texlive-bashful
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/bashful/bashful.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bashful-%{texlive_version}.%{texlive_noarch}.0.0.93svn25597-%{release}-zypper
%endif

%package -n texlive-basicarith
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn35460
Release:        0
Summary:        Macros for typesetting basic arithmetic
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-basicarith-doc >= %{texlive_version}
Provides:       tex(basicarith.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source262:      basicarith.tar.xz
Source263:      basicarith.doc.tar.xz

%description -n texlive-basicarith
The package provides macros for typesetting basic arithmetic,
in the style typically found in textbooks. It focuses on the
American style of performing these algorithms. It is written
mostly in low-level TeX, with the goal that it should run in
either plain TeX or LaTeX, but there are two constructions that
currently prevent this. It is highly configurable, with macros
and lengths described in the documentation.

%package -n texlive-basicarith-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.1svn35460
Release:        0
Summary:        Documentation for texlive-basicarith
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-basicarith-doc
This package includes the documentation for texlive-basicarith

%post -n texlive-basicarith
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-basicarith 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-basicarith
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-basicarith-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/basicarith/CHANGES
%{_texmfdistdir}/doc/latex/basicarith/README
%{_texmfdistdir}/doc/latex/basicarith/basicarith.pdf
%{_texmfdistdir}/doc/latex/basicarith/lppl.txt

%files -n texlive-basicarith
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/basicarith/basicarith.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-basicarith-%{texlive_version}.%{texlive_noarch}.1.1svn35460-%{release}-zypper
%endif

%package -n texlive-baskervald
Version:        %{texlive_version}.%{texlive_noarch}.1.016svn19490
Release:        0
Summary:        Baskervald ADF fonts collection with TeX/LaTeX support
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-baskervald-fonts >= %{texlive_version}
Recommends:     texlive-baskervald-doc >= %{texlive_version}
Provides:       tex(baskervald.sty)
Provides:       tex(supp-ybv.enc)
Provides:       tex(t1ybv.fd)
Provides:       tex(t1ybvw.fd)
Provides:       tex(ts1ybv.fd)
Provides:       tex(ts1ybvw.fd)
Provides:       tex(ybv.map)
Provides:       tex(ybvb8c.tfm)
Provides:       tex(ybvb8c.vf)
Provides:       tex(ybvb8r.tfm)
Provides:       tex(ybvb8s.tfm)
Provides:       tex(ybvb8t.tfm)
Provides:       tex(ybvb8t.vf)
Provides:       tex(ybvbi8c.tfm)
Provides:       tex(ybvbi8c.vf)
Provides:       tex(ybvbi8r.tfm)
Provides:       tex(ybvbi8s.tfm)
Provides:       tex(ybvbi8t.tfm)
Provides:       tex(ybvbi8t.vf)
Provides:       tex(ybvbiw8t.tfm)
Provides:       tex(ybvbiw8t.vf)
Provides:       tex(ybvbw8t.tfm)
Provides:       tex(ybvbw8t.vf)
Provides:       tex(ybvh8c.tfm)
Provides:       tex(ybvh8c.vf)
Provides:       tex(ybvh8r.tfm)
Provides:       tex(ybvh8s.tfm)
Provides:       tex(ybvh8t.tfm)
Provides:       tex(ybvh8t.vf)
Provides:       tex(ybvho8c.tfm)
Provides:       tex(ybvho8c.vf)
Provides:       tex(ybvho8r.tfm)
Provides:       tex(ybvho8s.tfm)
Provides:       tex(ybvho8t.tfm)
Provides:       tex(ybvho8t.vf)
Provides:       tex(ybvhow8t.tfm)
Provides:       tex(ybvhow8t.vf)
Provides:       tex(ybvhw8t.tfm)
Provides:       tex(ybvhw8t.vf)
Provides:       tex(ybvr8c.tfm)
Provides:       tex(ybvr8c.vf)
Provides:       tex(ybvr8r.tfm)
Provides:       tex(ybvr8s.tfm)
Provides:       tex(ybvr8t.tfm)
Provides:       tex(ybvr8t.vf)
Provides:       tex(ybvri8c.tfm)
Provides:       tex(ybvri8c.vf)
Provides:       tex(ybvri8r.tfm)
Provides:       tex(ybvri8s.tfm)
Provides:       tex(ybvri8t.tfm)
Provides:       tex(ybvri8t.vf)
Provides:       tex(ybvriw8t.tfm)
Provides:       tex(ybvriw8t.vf)
Provides:       tex(ybvrw8t.tfm)
Provides:       tex(ybvrw8t.vf)
Requires:       tex(fontenc.sty)
Requires:       tex(nfssext-cfr.sty)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source264:      baskervald.tar.xz
Source265:      baskervald.doc.tar.xz

%description -n texlive-baskervald
Baskervald ADF is a serif family with lining figures designed
as a substitute for Baskerville. The family currently includes
upright and italic or oblique shapes in each of regular, bold
and heavy weights. All fonts include the slashed zero and
additional non-standard ligatures. The support package renames
them according to the Karl Berry fontname scheme and defines
two families. One of these primarily provides access to the
"standard" or default characters while the other supports
additional ligatures. The included package files provide access
to these features in LaTeX.

%package -n texlive-baskervald-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.016svn19490
Release:        0
Summary:        Documentation for texlive-baskervald
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-baskervald-doc
This package includes the documentation for texlive-baskervald


%package -n texlive-baskervald-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.016svn19490
Release:        0
Summary:        Severed fonts for texlive-baskervald
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-baskervald-fonts
The  separated fonts package for texlive-baskervald
%post -n texlive-baskervald
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap ybv.map' >> /var/run/texlive/run-updmap

%postun -n texlive-baskervald 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap ybv.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-baskervald
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-baskervald-fonts
%files -n texlive-baskervald-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/baskervald/COPYING
%{_texmfdistdir}/doc/fonts/baskervald/NOTICE.txt
%{_texmfdistdir}/doc/fonts/baskervald/README
%{_texmfdistdir}/doc/fonts/baskervald/baskervaldadf.pdf
%{_texmfdistdir}/doc/fonts/baskervald/baskervaldadf.tex
%{_texmfdistdir}/doc/fonts/baskervald/manifest.txt

%files -n texlive-baskervald
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvb8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvbi8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvh8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvho8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvr8a.afm
%{_texmfdistdir}/fonts/afm/arkandis/baskervald/ybvri8a.afm
%{_texmfdistdir}/fonts/enc/dvips/baskervald/supp-ybv.enc
%{_texmfdistdir}/fonts/map/dvips/baskervald/ybv.map
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvb8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbi8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbiw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvbw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvh8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvho8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvhow8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvhw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvr8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8c.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8r.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8s.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvri8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvriw8t.tfm
%{_texmfdistdir}/fonts/tfm/arkandis/baskervald/ybvrw8t.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvb8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvb8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvbi8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvbi8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvh8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvh8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvho8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvho8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvr8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvr8a.pfm
%verify(link) %{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvri8a.pfb
%{_texmfdistdir}/fonts/type1/arkandis/baskervald/ybvri8a.pfm
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvb8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvb8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbi8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbi8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbiw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvbw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvh8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvh8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvho8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvho8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvhow8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvhw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvr8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvr8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvri8c.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvri8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvriw8t.vf
%{_texmfdistdir}/fonts/vf/arkandis/baskervald/ybvrw8t.vf
%{_texmfdistdir}/tex/latex/baskervald/baskervald.sty
%{_texmfdistdir}/tex/latex/baskervald/t1ybv.fd
%{_texmfdistdir}/tex/latex/baskervald/t1ybvw.fd
%{_texmfdistdir}/tex/latex/baskervald/ts1ybv.fd
%{_texmfdistdir}/tex/latex/baskervald/ts1ybvw.fd

%files -n texlive-baskervald-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-baskervald
%{_datadir}/fontconfig/conf.avail/58-texlive-baskervald.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervald/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervald/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervald/fonts.scale
%{_datadir}/fonts/texlive-baskervald/ybvb8a.pfb
%{_datadir}/fonts/texlive-baskervald/ybvbi8a.pfb
%{_datadir}/fonts/texlive-baskervald/ybvh8a.pfb
%{_datadir}/fonts/texlive-baskervald/ybvho8a.pfb
%{_datadir}/fonts/texlive-baskervald/ybvr8a.pfb
%{_datadir}/fonts/texlive-baskervald/ybvri8a.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-baskervald-fonts-%{texlive_version}.%{texlive_noarch}.1.016svn19490-%{release}-zypper
%endif

%package -n texlive-baskervaldx
Version:        %{texlive_version}.%{texlive_noarch}.1.073svn54512
Release:        0
Summary:        Extension and modification of BaskervaldADF with LaTeX support
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-baskervaldx-fonts >= %{texlive_version}
Recommends:     texlive-baskervaldx-doc >= %{texlive_version}
Provides:       tex(Baskervaldx-Bol-lf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-lf-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-lf-ly1.vf)
Provides:       tex(Baskervaldx-Bol-lf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-lf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-lf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Bol-lf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-lf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Bol-lf-sc-t1.vf)
Provides:       tex(Baskervaldx-Bol-lf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-lf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-lf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Bol-lf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-lf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Bol-lf-swash-t1.vf)
Provides:       tex(Baskervaldx-Bol-lf-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-lf-t1.tfm)
Provides:       tex(Baskervaldx-Bol-lf-t1.vf)
Provides:       tex(Baskervaldx-Bol-lf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Bol-lf-ts1.tfm)
Provides:       tex(Baskervaldx-Bol-lf-ts1.vf)
Provides:       tex(Baskervaldx-Bol-osf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-osf-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-osf-ly1.vf)
Provides:       tex(Baskervaldx-Bol-osf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-osf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-osf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Bol-osf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-osf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Bol-osf-sc-t1.vf)
Provides:       tex(Baskervaldx-Bol-osf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-osf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-osf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Bol-osf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-osf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Bol-osf-swash-t1.vf)
Provides:       tex(Baskervaldx-Bol-osf-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-osf-t1.tfm)
Provides:       tex(Baskervaldx-Bol-osf-t1.vf)
Provides:       tex(Baskervaldx-Bol-osf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Bol-osf-ts1.tfm)
Provides:       tex(Baskervaldx-Bol-osf-ts1.vf)
Provides:       tex(Baskervaldx-Bol-osf.tfm)
Provides:       tex(Baskervaldx-Bol-sup-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-sup-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-sup-ly1.vf)
Provides:       tex(Baskervaldx-Bol-sup-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-sup-t1.tfm)
Provides:       tex(Baskervaldx-Bol-sup-t1.vf)
Provides:       tex(Baskervaldx-Bol-tlf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-ly1.vf)
Provides:       tex(Baskervaldx-Bol-tlf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Bol-tlf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-sc-t1.vf)
Provides:       tex(Baskervaldx-Bol-tlf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Bol-tlf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-swash-t1.vf)
Provides:       tex(Baskervaldx-Bol-tlf-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-t1.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-t1.vf)
Provides:       tex(Baskervaldx-Bol-tlf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-ts1.tfm)
Provides:       tex(Baskervaldx-Bol-tlf-ts1.vf)
Provides:       tex(Baskervaldx-Bol-tosf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-ly1.vf)
Provides:       tex(Baskervaldx-Bol-tosf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Bol-tosf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-sc-t1.vf)
Provides:       tex(Baskervaldx-Bol-tosf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Bol-tosf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-swash-t1.vf)
Provides:       tex(Baskervaldx-Bol-tosf-t1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-t1.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-t1.vf)
Provides:       tex(Baskervaldx-Bol-tosf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-ts1.tfm)
Provides:       tex(Baskervaldx-Bol-tosf-ts1.vf)
Provides:       tex(Baskervaldx-BolIta-alph.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-lf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-sc-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-lf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-sc-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-sc-t1.vf)
Provides:       tex(Baskervaldx-BolIta-lf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-swash-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-lf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-swash-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-swash-t1.vf)
Provides:       tex(Baskervaldx-BolIta-lf-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-t1.vf)
Provides:       tex(Baskervaldx-BolIta-lf-ts1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-ts1.tfm)
Provides:       tex(Baskervaldx-BolIta-lf-ts1.vf)
Provides:       tex(Baskervaldx-BolIta-osf-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-osf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-sc-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-osf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-sc-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-sc-t1.vf)
Provides:       tex(Baskervaldx-BolIta-osf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-swash-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-osf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-swash-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-swash-t1.vf)
Provides:       tex(Baskervaldx-BolIta-osf-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-t1.vf)
Provides:       tex(Baskervaldx-BolIta-osf-ts1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-ts1.tfm)
Provides:       tex(Baskervaldx-BolIta-osf-ts1.vf)
Provides:       tex(Baskervaldx-BolIta-sup-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-sup-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-sup-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-sup-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-sup-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-sup-t1.vf)
Provides:       tex(Baskervaldx-BolIta-tlf-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-tlf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-sc-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-tlf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-sc-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-sc-t1.vf)
Provides:       tex(Baskervaldx-BolIta-tlf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-swash-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-tlf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-swash-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-swash-t1.vf)
Provides:       tex(Baskervaldx-BolIta-tlf-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-t1.vf)
Provides:       tex(Baskervaldx-BolIta-tlf-ts1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-ts1.tfm)
Provides:       tex(Baskervaldx-BolIta-tlf-ts1.vf)
Provides:       tex(Baskervaldx-BolIta-tosf-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-tosf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-sc-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-tosf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-sc-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-sc-t1.vf)
Provides:       tex(Baskervaldx-BolIta-tosf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-swash-ly1.vf)
Provides:       tex(Baskervaldx-BolIta-tosf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-swash-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-swash-t1.vf)
Provides:       tex(Baskervaldx-BolIta-tosf-t1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-t1.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-t1.vf)
Provides:       tex(Baskervaldx-BolIta-tosf-ts1--base.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-ts1.tfm)
Provides:       tex(Baskervaldx-BolIta-tosf-ts1.vf)
Provides:       tex(Baskervaldx-Ita-alph.tfm)
Provides:       tex(Baskervaldx-Ita-lf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-lf-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-lf-ly1.vf)
Provides:       tex(Baskervaldx-Ita-lf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-lf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-lf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Ita-lf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-lf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Ita-lf-sc-t1.vf)
Provides:       tex(Baskervaldx-Ita-lf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-lf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-lf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Ita-lf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-lf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Ita-lf-swash-t1.vf)
Provides:       tex(Baskervaldx-Ita-lf-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-lf-t1.tfm)
Provides:       tex(Baskervaldx-Ita-lf-t1.vf)
Provides:       tex(Baskervaldx-Ita-lf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Ita-lf-ts1.tfm)
Provides:       tex(Baskervaldx-Ita-lf-ts1.vf)
Provides:       tex(Baskervaldx-Ita-osf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-osf-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-osf-ly1.vf)
Provides:       tex(Baskervaldx-Ita-osf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-osf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-osf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Ita-osf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-osf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Ita-osf-sc-t1.vf)
Provides:       tex(Baskervaldx-Ita-osf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-osf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-osf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Ita-osf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-osf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Ita-osf-swash-t1.vf)
Provides:       tex(Baskervaldx-Ita-osf-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-osf-t1.tfm)
Provides:       tex(Baskervaldx-Ita-osf-t1.vf)
Provides:       tex(Baskervaldx-Ita-osf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Ita-osf-ts1.tfm)
Provides:       tex(Baskervaldx-Ita-osf-ts1.vf)
Provides:       tex(Baskervaldx-Ita-sup-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-sup-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-sup-ly1.vf)
Provides:       tex(Baskervaldx-Ita-sup-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-sup-t1.tfm)
Provides:       tex(Baskervaldx-Ita-sup-t1.vf)
Provides:       tex(Baskervaldx-Ita-tlf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-ly1.vf)
Provides:       tex(Baskervaldx-Ita-tlf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Ita-tlf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-sc-t1.vf)
Provides:       tex(Baskervaldx-Ita-tlf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Ita-tlf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-swash-t1.vf)
Provides:       tex(Baskervaldx-Ita-tlf-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-t1.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-t1.vf)
Provides:       tex(Baskervaldx-Ita-tlf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-ts1.tfm)
Provides:       tex(Baskervaldx-Ita-tlf-ts1.vf)
Provides:       tex(Baskervaldx-Ita-tosf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-ly1.vf)
Provides:       tex(Baskervaldx-Ita-tosf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Ita-tosf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-sc-t1.vf)
Provides:       tex(Baskervaldx-Ita-tosf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Ita-tosf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-swash-t1.vf)
Provides:       tex(Baskervaldx-Ita-tosf-t1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-t1.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-t1.vf)
Provides:       tex(Baskervaldx-Ita-tosf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-ts1.tfm)
Provides:       tex(Baskervaldx-Ita-tosf-ts1.vf)
Provides:       tex(Baskervaldx-Reg-lf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-lf-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-lf-ly1.vf)
Provides:       tex(Baskervaldx-Reg-lf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-lf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-lf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Reg-lf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-lf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Reg-lf-sc-t1.vf)
Provides:       tex(Baskervaldx-Reg-lf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-lf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-lf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Reg-lf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-lf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Reg-lf-swash-t1.vf)
Provides:       tex(Baskervaldx-Reg-lf-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-lf-t1.tfm)
Provides:       tex(Baskervaldx-Reg-lf-t1.vf)
Provides:       tex(Baskervaldx-Reg-lf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Reg-lf-ts1.tfm)
Provides:       tex(Baskervaldx-Reg-lf-ts1.vf)
Provides:       tex(Baskervaldx-Reg-osf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-osf-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-osf-ly1.vf)
Provides:       tex(Baskervaldx-Reg-osf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-osf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-osf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Reg-osf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-osf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Reg-osf-sc-t1.vf)
Provides:       tex(Baskervaldx-Reg-osf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-osf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-osf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Reg-osf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-osf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Reg-osf-swash-t1.vf)
Provides:       tex(Baskervaldx-Reg-osf-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-osf-t1.tfm)
Provides:       tex(Baskervaldx-Reg-osf-t1.vf)
Provides:       tex(Baskervaldx-Reg-osf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Reg-osf-ts1.tfm)
Provides:       tex(Baskervaldx-Reg-osf-ts1.vf)
Provides:       tex(Baskervaldx-Reg-sup-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-sup-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-sup-ly1.vf)
Provides:       tex(Baskervaldx-Reg-sup-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-sup-t1.tfm)
Provides:       tex(Baskervaldx-Reg-sup-t1.vf)
Provides:       tex(Baskervaldx-Reg-tlf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-ly1.vf)
Provides:       tex(Baskervaldx-Reg-tlf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Reg-tlf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-sc-t1.vf)
Provides:       tex(Baskervaldx-Reg-tlf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Reg-tlf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-swash-t1.vf)
Provides:       tex(Baskervaldx-Reg-tlf-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-t1.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-t1.vf)
Provides:       tex(Baskervaldx-Reg-tlf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-ts1.tfm)
Provides:       tex(Baskervaldx-Reg-tlf-ts1.vf)
Provides:       tex(Baskervaldx-Reg-tosf-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-ly1.vf)
Provides:       tex(Baskervaldx-Reg-tosf-sc-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-sc-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-sc-ly1.vf)
Provides:       tex(Baskervaldx-Reg-tosf-sc-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-sc-t1.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-sc-t1.vf)
Provides:       tex(Baskervaldx-Reg-tosf-swash-ly1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-swash-ly1.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-swash-ly1.vf)
Provides:       tex(Baskervaldx-Reg-tosf-swash-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-swash-t1.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-swash-t1.vf)
Provides:       tex(Baskervaldx-Reg-tosf-t1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-t1.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-t1.vf)
Provides:       tex(Baskervaldx-Reg-tosf-ts1--base.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-ts1.tfm)
Provides:       tex(Baskervaldx-Reg-tosf-ts1.vf)
Provides:       tex(Baskervaldx-osf.tfm)
Provides:       tex(Baskervaldx.sty)
Provides:       tex(LY1Baskervaldx-LF.fd)
Provides:       tex(LY1Baskervaldx-OsF.fd)
Provides:       tex(LY1Baskervaldx-Sup.fd)
Provides:       tex(LY1Baskervaldx-TLF.fd)
Provides:       tex(LY1Baskervaldx-TOsF.fd)
Provides:       tex(T1Baskervaldx-LF.fd)
Provides:       tex(T1Baskervaldx-OsF.fd)
Provides:       tex(T1Baskervaldx-Sup.fd)
Provides:       tex(T1Baskervaldx-TLF.fd)
Provides:       tex(T1Baskervaldx-TOsF.fd)
Provides:       tex(TS1Baskervaldx-LF.fd)
Provides:       tex(TS1Baskervaldx-OsF.fd)
Provides:       tex(TS1Baskervaldx-TLF.fd)
Provides:       tex(TS1Baskervaldx-TOsF.fd)
Provides:       tex(baskervaldx.map)
Provides:       tex(bvalph.enc)
Provides:       tex(bvtabosf.enc)
Provides:       tex(zbv_2bp5ef.enc)
Provides:       tex(zbv_2n2qka.enc)
Provides:       tex(zbv_2sm4i7.enc)
Provides:       tex(zbv_3lvabu.enc)
Provides:       tex(zbv_3omoui.enc)
Provides:       tex(zbv_4f5bev.enc)
Provides:       tex(zbv_4kmser.enc)
Provides:       tex(zbv_4ksy5y.enc)
Provides:       tex(zbv_537kn6.enc)
Provides:       tex(zbv_5zt4ml.enc)
Provides:       tex(zbv_67xtiz.enc)
Provides:       tex(zbv_6mioll.enc)
Provides:       tex(zbv_6rdtju.enc)
Provides:       tex(zbv_6rwo65.enc)
Provides:       tex(zbv_6tdhgo.enc)
Provides:       tex(zbv_7453eo.enc)
Provides:       tex(zbv_7nnme4.enc)
Provides:       tex(zbv_7qmldf.enc)
Provides:       tex(zbv_awcfcx.enc)
Provides:       tex(zbv_bgypte.enc)
Provides:       tex(zbv_bs5d7e.enc)
Provides:       tex(zbv_caye23.enc)
Provides:       tex(zbv_cgzxx6.enc)
Provides:       tex(zbv_ck4t6h.enc)
Provides:       tex(zbv_coqtyh.enc)
Provides:       tex(zbv_e3qxqg.enc)
Provides:       tex(zbv_ea64ih.enc)
Provides:       tex(zbv_gar3zb.enc)
Provides:       tex(zbv_gjwmpg.enc)
Provides:       tex(zbv_go57dj.enc)
Provides:       tex(zbv_gsgxts.enc)
Provides:       tex(zbv_h4nqsn.enc)
Provides:       tex(zbv_hg6ru4.enc)
Provides:       tex(zbv_hkyy53.enc)
Provides:       tex(zbv_igsfta.enc)
Provides:       tex(zbv_ik76ei.enc)
Provides:       tex(zbv_ilkd46.enc)
Provides:       tex(zbv_jd6ty7.enc)
Provides:       tex(zbv_jmvj36.enc)
Provides:       tex(zbv_jwmruw.enc)
Provides:       tex(zbv_k3ascw.enc)
Provides:       tex(zbv_k6hbcl.enc)
Provides:       tex(zbv_krjs6b.enc)
Provides:       tex(zbv_l7sulo.enc)
Provides:       tex(zbv_lewyuf.enc)
Provides:       tex(zbv_mvsyl4.enc)
Provides:       tex(zbv_n3xo7h.enc)
Provides:       tex(zbv_n57xi2.enc)
Provides:       tex(zbv_nak3zo.enc)
Provides:       tex(zbv_ne5zxs.enc)
Provides:       tex(zbv_nq5ldf.enc)
Provides:       tex(zbv_oue4qy.enc)
Provides:       tex(zbv_riybhr.enc)
Provides:       tex(zbv_rtdlfq.enc)
Provides:       tex(zbv_rzwiio.enc)
Provides:       tex(zbv_shb4ap.enc)
Provides:       tex(zbv_uhxou6.enc)
Provides:       tex(zbv_untte3.enc)
Provides:       tex(zbv_upsxpb.enc)
Provides:       tex(zbv_wvrs5w.enc)
Provides:       tex(zbv_wy43ep.enc)
Provides:       tex(zbv_xbckbj.enc)
Provides:       tex(zbv_xjuza2.enc)
Provides:       tex(zbv_xsxsev.enc)
Provides:       tex(zbv_xyk42r.enc)
Provides:       tex(zbv_ymibyh.enc)
Provides:       tex(zbvbmi.tfm)
Provides:       tex(zbvbmi.vf)
Provides:       tex(zbvmi.tfm)
Provides:       tex(zbvmi.vf)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(mweights.sty)
Requires:       tex(ntxbmi.tfm)
Requires:       tex(ntxmi.tfm)
Requires:       tex(textcomp.sty)
Requires:       tex(xkeyval.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source266:      baskervaldx.tar.xz
Source267:      baskervaldx.doc.tar.xz

%description -n texlive-baskervaldx
Extends and modifies the BaskervaldADF font (a Baskerville
substitute) with more accented glyphs, with small caps and
oldstyle figures in all shapes. Includes OpenType and
PostScript fonts, as well as LaTeX support files.

%package -n texlive-baskervaldx-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.073svn54512
Release:        0
Summary:        Documentation for texlive-baskervaldx
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-baskervaldx-doc
This package includes the documentation for texlive-baskervaldx


%package -n texlive-baskervaldx-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.073svn54512
Release:        0
Summary:        Severed fonts for texlive-baskervaldx
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-baskervaldx-fonts
The  separated fonts package for texlive-baskervaldx
%post -n texlive-baskervaldx
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap baskervaldx.map' >> /var/run/texlive/run-updmap

%postun -n texlive-baskervaldx 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap baskervaldx.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-baskervaldx
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-baskervaldx-fonts
%files -n texlive-baskervaldx-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/baskervaldx/COPYING
%{_texmfdistdir}/doc/fonts/baskervaldx/NOTICE.txt
%{_texmfdistdir}/doc/fonts/baskervaldx/README
%{_texmfdistdir}/doc/fonts/baskervaldx/baskervaldx-doc.pdf
%{_texmfdistdir}/doc/fonts/baskervaldx/baskervaldx-doc.tex
%{_texmfdistdir}/doc/fonts/baskervaldx/baskervaldxmatheg-crop.pdf

%files -n texlive-baskervaldx
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/afm/public/baskervaldx/Baskervaldx-Bol.afm
%{_texmfdistdir}/fonts/afm/public/baskervaldx/Baskervaldx-BolIta.afm
%{_texmfdistdir}/fonts/afm/public/baskervaldx/Baskervaldx-Ita.afm
%{_texmfdistdir}/fonts/afm/public/baskervaldx/Baskervaldx-Reg.afm
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/bvalph.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/bvtabosf.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_2bp5ef.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_2n2qka.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_2sm4i7.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_3lvabu.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_3omoui.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_4f5bev.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_4kmser.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_4ksy5y.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_537kn6.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_5zt4ml.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_67xtiz.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_6mioll.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_6rdtju.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_6rwo65.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_6tdhgo.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_7453eo.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_7nnme4.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_7qmldf.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_awcfcx.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_bgypte.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_bs5d7e.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_caye23.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_cgzxx6.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_ck4t6h.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_coqtyh.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_e3qxqg.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_ea64ih.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_gar3zb.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_gjwmpg.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_go57dj.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_gsgxts.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_h4nqsn.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_hg6ru4.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_hkyy53.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_igsfta.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_ik76ei.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_ilkd46.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_jd6ty7.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_jmvj36.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_jwmruw.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_k3ascw.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_k6hbcl.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_krjs6b.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_l7sulo.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_lewyuf.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_mvsyl4.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_n3xo7h.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_n57xi2.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_nak3zo.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_ne5zxs.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_nq5ldf.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_oue4qy.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_riybhr.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_rtdlfq.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_rzwiio.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_shb4ap.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_uhxou6.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_untte3.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_upsxpb.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_wvrs5w.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_wy43ep.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_xbckbj.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_xjuza2.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_xsxsev.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_xyk42r.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervaldx/zbv_ymibyh.enc
%{_texmfdistdir}/fonts/map/dvips/baskervaldx/baskervaldx.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervaldx/Baskervaldx-Bol.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervaldx/Baskervaldx-BolIta.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervaldx/Baskervaldx-Ita.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervaldx/Baskervaldx-Reg.otf
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Bol-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-alph.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-BolIta-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-alph.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Ita-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-Reg-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/Baskervaldx-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/zbvbmi.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervaldx/zbvmi.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervaldx/Baskervaldx-Bol.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervaldx/Baskervaldx-BolIta.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervaldx/Baskervaldx-Ita.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervaldx/Baskervaldx-Reg.pfb
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Bol-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-BolIta-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Ita-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/Baskervaldx-Reg-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/zbvbmi.vf
%{_texmfdistdir}/fonts/vf/public/baskervaldx/zbvmi.vf
%{_texmfdistdir}/tex/latex/baskervaldx/Baskervaldx.sty
%{_texmfdistdir}/tex/latex/baskervaldx/LY1Baskervaldx-LF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/LY1Baskervaldx-OsF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/LY1Baskervaldx-Sup.fd
%{_texmfdistdir}/tex/latex/baskervaldx/LY1Baskervaldx-TLF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/LY1Baskervaldx-TOsF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/T1Baskervaldx-LF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/T1Baskervaldx-OsF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/T1Baskervaldx-Sup.fd
%{_texmfdistdir}/tex/latex/baskervaldx/T1Baskervaldx-TLF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/T1Baskervaldx-TOsF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/TS1Baskervaldx-LF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/TS1Baskervaldx-OsF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/TS1Baskervaldx-TLF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/TS1Baskervaldx-TOsF.fd
%{_texmfdistdir}/tex/latex/baskervaldx/baskervaldx.fontspec

%files -n texlive-baskervaldx-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-baskervaldx
%{_datadir}/fontconfig/conf.avail/58-texlive-baskervaldx.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-baskervaldx.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-baskervaldx.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervaldx/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervaldx/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervaldx/fonts.scale
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-Bol.otf
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-BolIta.otf
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-Ita.otf
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-Reg.otf
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-Bol.pfb
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-BolIta.pfb
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-Ita.pfb
%{_datadir}/fonts/texlive-baskervaldx/Baskervaldx-Reg.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-baskervaldx-fonts-%{texlive_version}.%{texlive_noarch}.1.073svn54512-%{release}-zypper
%endif

%package -n texlive-baskervillef
Version:        %{texlive_version}.%{texlive_noarch}.1.050svn54512
Release:        0
Summary:        Fry's Baskerville look-alike, with math support
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(post): findutils
Requires(post): grep
Requires(post): sed
Requires(post): texlive >= %{texlive_version}
Requires(post): tex(updmap.cfg)
#!BuildIgnore:  tex(updmap.cfg)
Requires(postun): findutils
Requires(postun): grep
Requires(postun): sed
Requires(postun): texlive >= %{texlive_version}
Requires(postun): tex(updmap.cfg)
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Requires:       texlive-baskervillef-fonts >= %{texlive_version}
Recommends:     texlive-baskervillef-doc >= %{texlive_version}
Provides:       tex(BaskervilleF-Bold-lf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-ly1.vf)
Provides:       tex(BaskervilleF-Bold-lf-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Bold-lf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Bold-lf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-sc-t1.vf)
Provides:       tex(BaskervilleF-Bold-lf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Bold-lf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-swash-t1.vf)
Provides:       tex(BaskervilleF-Bold-lf-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-t1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-t1.vf)
Provides:       tex(BaskervilleF-Bold-lf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Bold-lf-ts1.tfm)
Provides:       tex(BaskervilleF-Bold-lf-ts1.vf)
Provides:       tex(BaskervilleF-Bold-osf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-ly1.vf)
Provides:       tex(BaskervilleF-Bold-osf-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Bold-osf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Bold-osf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-sc-t1.vf)
Provides:       tex(BaskervilleF-Bold-osf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Bold-osf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-swash-t1.vf)
Provides:       tex(BaskervilleF-Bold-osf-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-t1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-t1.vf)
Provides:       tex(BaskervilleF-Bold-osf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Bold-osf-ts1.tfm)
Provides:       tex(BaskervilleF-Bold-osf-ts1.vf)
Provides:       tex(BaskervilleF-Bold-osf.tfm)
Provides:       tex(BaskervilleF-Bold-sup-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-sup-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-sup-ly1.vf)
Provides:       tex(BaskervilleF-Bold-sup-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-sup-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-sup-t1.tfm)
Provides:       tex(BaskervilleF-Bold-sup-t1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-ly1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-ot1G.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-ot1G.vf)
Provides:       tex(BaskervilleF-Bold-tlf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-sc-t1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-swash-t1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-t1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-t1.vf)
Provides:       tex(BaskervilleF-Bold-tlf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-ts1.tfm)
Provides:       tex(BaskervilleF-Bold-tlf-ts1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-ly1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-sc-t1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-swash-t1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-t1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-t1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-t1.vf)
Provides:       tex(BaskervilleF-Bold-tosf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-ts1.tfm)
Provides:       tex(BaskervilleF-Bold-tosf-ts1.vf)
Provides:       tex(BaskervilleF-Bold.tfm)
Provides:       tex(BaskervilleF-BoldItalic-alph.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-lf-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-ot1.vf)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-sc-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-swash-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-lf-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-lf-ts1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-ts1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-lf-ts1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-ot1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-sc-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-swash-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf-ts1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-ts1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-osf-ts1.vf)
Provides:       tex(BaskervilleF-BoldItalic-osf.tfm)
Provides:       tex(BaskervilleF-BoldItalic-sup-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-sup-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-sup-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-sup-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-sup-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-sup-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-sup-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ot1G.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ot1G.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-ot1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-sc-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-swash-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ts1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ts1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tlf-ts1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-ot1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-sc-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ly1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-swash-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-t1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-t1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-t1.vf)
Provides:       tex(BaskervilleF-BoldItalic-tosf-ts1--base.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-ts1.tfm)
Provides:       tex(BaskervilleF-BoldItalic-tosf-ts1.vf)
Provides:       tex(BaskervilleF-BoldItalic.tfm)
Provides:       tex(BaskervilleF-Italic-alph.tfm)
Provides:       tex(BaskervilleF-Italic-dnom-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-dnom-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-dnom-ly1.vf)
Provides:       tex(BaskervilleF-Italic-dnom-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-dnom-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-dnom-t1.tfm)
Provides:       tex(BaskervilleF-Italic-dnom-t1.vf)
Provides:       tex(BaskervilleF-Italic-lf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-ly1.vf)
Provides:       tex(BaskervilleF-Italic-lf-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Italic-lf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Italic-lf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-sc-t1.vf)
Provides:       tex(BaskervilleF-Italic-lf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Italic-lf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-swash-t1.vf)
Provides:       tex(BaskervilleF-Italic-lf-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-t1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-t1.vf)
Provides:       tex(BaskervilleF-Italic-lf-th-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-th-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-th-ly1.vf)
Provides:       tex(BaskervilleF-Italic-lf-th-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-th-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-th-t1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-th-t1.vf)
Provides:       tex(BaskervilleF-Italic-lf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Italic-lf-ts1.tfm)
Provides:       tex(BaskervilleF-Italic-lf-ts1.vf)
Provides:       tex(BaskervilleF-Italic-osf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-ly1.vf)
Provides:       tex(BaskervilleF-Italic-osf-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Italic-osf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Italic-osf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-sc-t1.vf)
Provides:       tex(BaskervilleF-Italic-osf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Italic-osf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-swash-t1.vf)
Provides:       tex(BaskervilleF-Italic-osf-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-t1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-t1.vf)
Provides:       tex(BaskervilleF-Italic-osf-th-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-th-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-th-ly1.vf)
Provides:       tex(BaskervilleF-Italic-osf-th-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-th-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-th-t1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-th-t1.vf)
Provides:       tex(BaskervilleF-Italic-osf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Italic-osf-ts1.tfm)
Provides:       tex(BaskervilleF-Italic-osf-ts1.vf)
Provides:       tex(BaskervilleF-Italic-osf.tfm)
Provides:       tex(BaskervilleF-Italic-sup-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-sup-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-sup-ly1.vf)
Provides:       tex(BaskervilleF-Italic-sup-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-sup-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-sup-t1.tfm)
Provides:       tex(BaskervilleF-Italic-sup-t1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-ot1G.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-ot1G.vf)
Provides:       tex(BaskervilleF-Italic-tlf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-sc-t1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-swash-t1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-t1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-th-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-th-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-th-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-th-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-th-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-th-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-th-t1.vf)
Provides:       tex(BaskervilleF-Italic-tlf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-ts1.tfm)
Provides:       tex(BaskervilleF-Italic-tlf-ts1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-sc-t1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-swash-t1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-t1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-th-ly1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-th-ly1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-th-ly1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-th-ot1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-th-t1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-th-t1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-th-t1.vf)
Provides:       tex(BaskervilleF-Italic-tosf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-ts1.tfm)
Provides:       tex(BaskervilleF-Italic-tosf-ts1.vf)
Provides:       tex(BaskervilleF-Italic.tfm)
Provides:       tex(BaskervilleF-Regular-dnom-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-dnom-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-dnom-ly1.vf)
Provides:       tex(BaskervilleF-Regular-dnom-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-dnom-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-dnom-t1.tfm)
Provides:       tex(BaskervilleF-Regular-dnom-t1.vf)
Provides:       tex(BaskervilleF-Regular-lf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-ly1.vf)
Provides:       tex(BaskervilleF-Regular-lf-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Regular-lf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Regular-lf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-sc-t1.vf)
Provides:       tex(BaskervilleF-Regular-lf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Regular-lf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-swash-t1.vf)
Provides:       tex(BaskervilleF-Regular-lf-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-t1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-t1.vf)
Provides:       tex(BaskervilleF-Regular-lf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Regular-lf-ts1.tfm)
Provides:       tex(BaskervilleF-Regular-lf-ts1.vf)
Provides:       tex(BaskervilleF-Regular-osf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-ly1.vf)
Provides:       tex(BaskervilleF-Regular-osf-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Regular-osf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Regular-osf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-sc-t1.vf)
Provides:       tex(BaskervilleF-Regular-osf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Regular-osf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-swash-t1.vf)
Provides:       tex(BaskervilleF-Regular-osf-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-t1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-t1.vf)
Provides:       tex(BaskervilleF-Regular-osf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Regular-osf-ts1.tfm)
Provides:       tex(BaskervilleF-Regular-osf-ts1.vf)
Provides:       tex(BaskervilleF-Regular-osf.tfm)
Provides:       tex(BaskervilleF-Regular-sup-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-sup-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-sup-ly1.vf)
Provides:       tex(BaskervilleF-Regular-sup-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-sup-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-sup-t1.tfm)
Provides:       tex(BaskervilleF-Regular-sup-t1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-ly1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-ot1G.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-ot1G.vf)
Provides:       tex(BaskervilleF-Regular-tlf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-sc-t1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-swash-t1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-t1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-t1.vf)
Provides:       tex(BaskervilleF-Regular-tlf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-ts1.tfm)
Provides:       tex(BaskervilleF-Regular-tlf-ts1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-ly1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-sc-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-sc-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-sc-ly1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-sc-ot1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-sc-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-sc-ot1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-sc-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-sc-t1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-sc-t1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-swash-ly1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-swash-ly1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-swash-ly1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-swash-ot1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-swash-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-swash-t1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-swash-t1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-t1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-t1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-t1.vf)
Provides:       tex(BaskervilleF-Regular-tosf-ts1--base.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-ts1.tfm)
Provides:       tex(BaskervilleF-Regular-tosf-ts1.vf)
Provides:       tex(BaskervilleF-Regular.tfm)
Provides:       tex(BaskervilleF.map)
Provides:       tex(LY1BaskervilleF-Dnom.fd)
Provides:       tex(LY1BaskervilleF-LF.fd)
Provides:       tex(LY1BaskervilleF-OsF.fd)
Provides:       tex(LY1BaskervilleF-Sup.fd)
Provides:       tex(LY1BaskervilleF-TLF.fd)
Provides:       tex(LY1BaskervilleF-TOsF.fd)
Provides:       tex(OT1BaskervilleF-Dnom.fd)
Provides:       tex(OT1BaskervilleF-LF.fd)
Provides:       tex(OT1BaskervilleF-OsF.fd)
Provides:       tex(OT1BaskervilleF-Sup.fd)
Provides:       tex(OT1BaskervilleF-TLF.fd)
Provides:       tex(OT1BaskervilleF-TOsF.fd)
Provides:       tex(T1BaskervilleF-Dnom.fd)
Provides:       tex(T1BaskervilleF-LF.fd)
Provides:       tex(T1BaskervilleF-OsF.fd)
Provides:       tex(T1BaskervilleF-Sup.fd)
Provides:       tex(T1BaskervilleF-TLF.fd)
Provides:       tex(T1BaskervilleF-TOsF.fd)
Provides:       tex(TS1BaskervilleF-LF.fd)
Provides:       tex(TS1BaskervilleF-OsF.fd)
Provides:       tex(TS1BaskervilleF-TLF.fd)
Provides:       tex(TS1BaskervilleF-TOsF.fd)
Provides:       tex(baskervillef.sty)
Provides:       tex(omlzbami.fd)
Provides:       tex(zba_3oppw2.enc)
Provides:       tex(zba_4scfns.enc)
Provides:       tex(zba_523v7l.enc)
Provides:       tex(zba_66iezk.enc)
Provides:       tex(zba_6emqgt.enc)
Provides:       tex(zba_6mhi2z.enc)
Provides:       tex(zba_77ryg7.enc)
Provides:       tex(zba_7yyqda.enc)
Provides:       tex(zba_a6zfty.enc)
Provides:       tex(zba_adnnkl.enc)
Provides:       tex(zba_ahcsm7.enc)
Provides:       tex(zba_b5lrlg.enc)
Provides:       tex(zba_bnmcfu.enc)
Provides:       tex(zba_bue3wb.enc)
Provides:       tex(zba_bvbtx2.enc)
Provides:       tex(zba_cgvvj5.enc)
Provides:       tex(zba_csuamn.enc)
Provides:       tex(zba_cvjygd.enc)
Provides:       tex(zba_cyyuxb.enc)
Provides:       tex(zba_dzrx7a.enc)
Provides:       tex(zba_e3xw3x.enc)
Provides:       tex(zba_e6c7a3.enc)
Provides:       tex(zba_eurn55.enc)
Provides:       tex(zba_evqzha.enc)
Provides:       tex(zba_fj77ru.enc)
Provides:       tex(zba_hkkd2g.enc)
Provides:       tex(zba_hljrbf.enc)
Provides:       tex(zba_i3q27v.enc)
Provides:       tex(zba_i5fury.enc)
Provides:       tex(zba_igqvi4.enc)
Provides:       tex(zba_invrxa.enc)
Provides:       tex(zba_iqxfxn.enc)
Provides:       tex(zba_iy3fha.enc)
Provides:       tex(zba_iy3qnl.enc)
Provides:       tex(zba_jayro7.enc)
Provides:       tex(zba_jesydd.enc)
Provides:       tex(zba_kb3ura.enc)
Provides:       tex(zba_kodzea.enc)
Provides:       tex(zba_koujiy.enc)
Provides:       tex(zba_kqfmr4.enc)
Provides:       tex(zba_kragcu.enc)
Provides:       tex(zba_kua26b.enc)
Provides:       tex(zba_kuzvvg.enc)
Provides:       tex(zba_ljx3jq.enc)
Provides:       tex(zba_lwrbox.enc)
Provides:       tex(zba_m3z5kj.enc)
Provides:       tex(zba_mebvzg.enc)
Provides:       tex(zba_mevjdz.enc)
Provides:       tex(zba_n43ddx.enc)
Provides:       tex(zba_n4mxmz.enc)
Provides:       tex(zba_nvjtae.enc)
Provides:       tex(zba_o2tifi.enc)
Provides:       tex(zba_o6dtj2.enc)
Provides:       tex(zba_owa6ha.enc)
Provides:       tex(zba_owjda7.enc)
Provides:       tex(zba_oxcsv2.enc)
Provides:       tex(zba_oyegn6.enc)
Provides:       tex(zba_p3pzma.enc)
Provides:       tex(zba_pjh6nq.enc)
Provides:       tex(zba_pqfamk.enc)
Provides:       tex(zba_q37ime.enc)
Provides:       tex(zba_qleltn.enc)
Provides:       tex(zba_qptswd.enc)
Provides:       tex(zba_qycpdj.enc)
Provides:       tex(zba_rqwz3b.enc)
Provides:       tex(zba_s6fzkp.enc)
Provides:       tex(zba_sb5wfb.enc)
Provides:       tex(zba_sqc4ly.enc)
Provides:       tex(zba_t5goht.enc)
Provides:       tex(zba_t7zhq6.enc)
Provides:       tex(zba_taxp3x.enc)
Provides:       tex(zba_tjuaha.enc)
Provides:       tex(zba_tqvuvp.enc)
Provides:       tex(zba_twn2qn.enc)
Provides:       tex(zba_u24co6.enc)
Provides:       tex(zba_uf7ozb.enc)
Provides:       tex(zba_vaofbk.enc)
Provides:       tex(zba_ve4agh.enc)
Provides:       tex(zba_vezlo5.enc)
Provides:       tex(zba_vunabj.enc)
Provides:       tex(zba_wcz3px.enc)
Provides:       tex(zba_wdfmp4.enc)
Provides:       tex(zba_xlbenp.enc)
Provides:       tex(zba_xt7x67.enc)
Provides:       tex(zba_xucdkt.enc)
Provides:       tex(zba_z5rfyo.enc)
Provides:       tex(zba_zfeutd.enc)
Provides:       tex(zba_zn4iv3.enc)
Provides:       tex(zba_zptsj3.enc)
Provides:       tex(zba_zygn7r.enc)
Provides:       tex(zbabmi.tfm)
Provides:       tex(zbabmi.vf)
Provides:       tex(zbami.tfm)
Provides:       tex(zbami.vf)
Requires:       tex(etoolbox.sty)
Requires:       tex(fontaxes.sty)
Requires:       tex(fontenc.sty)
Requires:       tex(ifthen.sty)
Requires:       tex(mweights.sty)
Requires:       tex(ntxbmi.tfm)
Requires:       tex(ntxmi.tfm)
Requires:       tex(rtxbmi.tfm)
Requires:       tex(rtxmi.tfm)
Requires:       tex(textcomp.sty)
Requires:       tex(txbmia.tfm)
Requires:       tex(txmia.tfm)
Requires:       tex(xkeyval.sty)
Requires:       tex(xstring.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source268:      baskervillef.tar.xz
Source269:      baskervillef.doc.tar.xz

%description -n texlive-baskervillef
BaskervilleF is a fork from the Libre Baskerville fonts (Roman,
Italic, Bold only) released under the OFL by Paolo Impallari
and Rodrigo Fuenzalida. Their fonts are optimized for web
usage, while BaskervilleF is optimized for traditional TeX
usage, normally destined for production of pdf files. A bold
italic style was added and mathematical support is offered as
an option to newtxmath.

%package -n texlive-baskervillef-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.050svn54512
Release:        0
Summary:        Documentation for texlive-baskervillef
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-baskervillef-doc
This package includes the documentation for texlive-baskervillef


%package -n texlive-baskervillef-fonts
Version:        %{texlive_version}.%{texlive_noarch}.1.050svn54512
Release:        0
Summary:        Severed fonts for texlive-baskervillef
License:        OFL-1.1
Group:          Productivity/Publishing/TeX/Fonts
URL:            http://www.tug.org/texlive/
%reconfigure_fonts_prereq
Requires(posttrans): fontconfig
Requires(posttrans): ghostscript-fonts-std
Requires(posttrans): mkfontdir
Requires(posttrans): mkfontscale
Requires(posttrans): xorg-x11-fonts-core

%description -n texlive-baskervillef-fonts
The  separated fonts package for texlive-baskervillef
%post -n texlive-baskervillef
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
echo 'addMap BaskervilleF.map' >> /var/run/texlive/run-updmap

%postun -n texlive-baskervillef 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    echo 'deleteMap BaskervilleF.map' >> /var/run/texlive/run-updmap
    exit 0
fi

%posttrans -n texlive-baskervillef
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%reconfigure_fonts_scriptlets -n texlive-baskervillef-fonts
%files -n texlive-baskervillef-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/fonts/baskervillef/FONTLOG.txt
%{_texmfdistdir}/doc/fonts/baskervillef/OFL-FAQ.txt
%{_texmfdistdir}/doc/fonts/baskervillef/OFL.txt
%{_texmfdistdir}/doc/fonts/baskervillef/README
%{_texmfdistdir}/doc/fonts/baskervillef/baskervillef-doc.pdf
%{_texmfdistdir}/doc/fonts/baskervillef/baskervillef-doc.tex

%files -n texlive-baskervillef
%defattr(-,root,root,755)
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_3oppw2.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_4scfns.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_523v7l.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_66iezk.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_6emqgt.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_6mhi2z.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_77ryg7.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_7yyqda.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_a6zfty.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_adnnkl.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_ahcsm7.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_b5lrlg.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_bnmcfu.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_bue3wb.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_bvbtx2.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_cgvvj5.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_csuamn.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_cvjygd.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_cyyuxb.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_dzrx7a.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_e3xw3x.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_e6c7a3.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_eurn55.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_evqzha.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_fj77ru.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_hkkd2g.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_hljrbf.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_i3q27v.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_i5fury.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_igqvi4.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_invrxa.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_iqxfxn.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_iy3fha.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_iy3qnl.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_jayro7.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_jesydd.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_kb3ura.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_kodzea.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_koujiy.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_kqfmr4.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_kragcu.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_kua26b.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_kuzvvg.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_ljx3jq.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_lwrbox.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_m3z5kj.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_mebvzg.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_mevjdz.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_n43ddx.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_n4mxmz.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_nvjtae.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_o2tifi.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_o6dtj2.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_owa6ha.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_owjda7.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_oxcsv2.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_oyegn6.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_p3pzma.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_pjh6nq.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_pqfamk.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_q37ime.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_qleltn.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_qptswd.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_qycpdj.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_rqwz3b.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_s6fzkp.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_sb5wfb.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_sqc4ly.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_t5goht.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_t7zhq6.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_taxp3x.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_tjuaha.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_tqvuvp.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_twn2qn.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_u24co6.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_uf7ozb.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_vaofbk.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_ve4agh.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_vezlo5.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_vunabj.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_wcz3px.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_wdfmp4.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_xlbenp.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_xt7x67.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_xucdkt.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_z5rfyo.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_zfeutd.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_zn4iv3.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_zptsj3.enc
%{_texmfdistdir}/fonts/enc/dvips/baskervillef/zba_zygn7r.enc
%{_texmfdistdir}/fonts/map/dvips/baskervillef/BaskervilleF.map
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervillef/BaskervilleF-Bold.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervillef/BaskervilleF-BoldItalic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervillef/BaskervilleF-Italic.otf
%verify(link) %{_texmfdistdir}/fonts/opentype/public/baskervillef/BaskervilleF-Regular.otf
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ot1G.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Bold.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-alph.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ot1G.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-BoldItalic.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-alph.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-dnom-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-th-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-th-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ot1G.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-th-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-th-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Italic.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-dnom-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-lf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-osf.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-sup-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ot1G.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tlf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ot1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-sc-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-swash-ly1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-swash-ly1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-swash-ot1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-swash-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-swash-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-t1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-t1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ts1--base.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular-tosf-ts1.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/BaskervilleF-Regular.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/zbabmi.tfm
%{_texmfdistdir}/fonts/tfm/public/baskervillef/zbami.tfm
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervillef/BaskervilleF-Bold.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervillef/BaskervilleF-BoldItalic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervillef/BaskervilleF-Italic.pfb
%verify(link) %{_texmfdistdir}/fonts/type1/public/baskervillef/BaskervilleF-Regular.pfb
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-ot1G.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Bold-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-ot1G.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-BoldItalic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-dnom-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-dnom-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-th-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-th-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-th-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-th-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-ot1G.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-th-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-th-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-th-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-th-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Italic-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-dnom-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-dnom-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-lf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-osf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-sup-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-sup-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-ot1G.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tlf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-sc-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-sc-ot1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-sc-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-swash-ly1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-swash-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-t1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/BaskervilleF-Regular-tosf-ts1.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/zbabmi.vf
%{_texmfdistdir}/fonts/vf/public/baskervillef/zbami.vf
%{_texmfdistdir}/tex/latex/baskervillef/LY1BaskervilleF-Dnom.fd
%{_texmfdistdir}/tex/latex/baskervillef/LY1BaskervilleF-LF.fd
%{_texmfdistdir}/tex/latex/baskervillef/LY1BaskervilleF-OsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/LY1BaskervilleF-Sup.fd
%{_texmfdistdir}/tex/latex/baskervillef/LY1BaskervilleF-TLF.fd
%{_texmfdistdir}/tex/latex/baskervillef/LY1BaskervilleF-TOsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/OT1BaskervilleF-Dnom.fd
%{_texmfdistdir}/tex/latex/baskervillef/OT1BaskervilleF-LF.fd
%{_texmfdistdir}/tex/latex/baskervillef/OT1BaskervilleF-OsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/OT1BaskervilleF-Sup.fd
%{_texmfdistdir}/tex/latex/baskervillef/OT1BaskervilleF-TLF.fd
%{_texmfdistdir}/tex/latex/baskervillef/OT1BaskervilleF-TOsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/T1BaskervilleF-Dnom.fd
%{_texmfdistdir}/tex/latex/baskervillef/T1BaskervilleF-LF.fd
%{_texmfdistdir}/tex/latex/baskervillef/T1BaskervilleF-OsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/T1BaskervilleF-Sup.fd
%{_texmfdistdir}/tex/latex/baskervillef/T1BaskervilleF-TLF.fd
%{_texmfdistdir}/tex/latex/baskervillef/T1BaskervilleF-TOsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/TS1BaskervilleF-LF.fd
%{_texmfdistdir}/tex/latex/baskervillef/TS1BaskervilleF-OsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/TS1BaskervilleF-TLF.fd
%{_texmfdistdir}/tex/latex/baskervillef/TS1BaskervilleF-TOsF.fd
%{_texmfdistdir}/tex/latex/baskervillef/baskervillef.fontspec
%{_texmfdistdir}/tex/latex/baskervillef/baskervillef.sty
%{_texmfdistdir}/tex/latex/baskervillef/omlzbami.fd

%files -n texlive-baskervillef-fonts
%defattr(-,root,root,755)
%dir %{_datadir}/fonts/texlive-baskervillef
%{_datadir}/fontconfig/conf.avail/58-texlive-baskervillef.conf
%{_datadir}/fontconfig/conf.avail/55-texlive-baskervillef.conf
%config %{_sysconfdir}/fonts/conf.d/55-texlive-baskervillef.conf
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervillef/encodings.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervillef/fonts.dir
%ghost %verify(not md5 size mtime) %{_datadir}/fonts/texlive-baskervillef/fonts.scale
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-Bold.otf
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-BoldItalic.otf
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-Italic.otf
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-Regular.otf
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-Bold.pfb
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-BoldItalic.pfb
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-Italic.pfb
%{_datadir}/fonts/texlive-baskervillef/BaskervilleF-Regular.pfb
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-baskervillef-fonts-%{texlive_version}.%{texlive_noarch}.1.050svn54512-%{release}-zypper
%endif

%package -n texlive-basque-book
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn32924
Release:        0
Summary:        Class for book-type documents written in Basque
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-basque-book-doc >= %{texlive_version}
Provides:       tex(basque-book.cls)
Requires:       tex(basque-date.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source270:      basque-book.tar.xz
Source271:      basque-book.doc.tar.xz

%description -n texlive-basque-book
The class is derived from the LaTeX book class. The extensions
solve grammatical and numeration issues that occur when
book-type documents are written in Basque. The class is useful
for writing books, PhD and Master Theses, etc., in Basque.

%package -n texlive-basque-book-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.20svn32924
Release:        0
Summary:        Documentation for texlive-basque-book
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Provides:       locale(texlive-basque-book-doc:en;eu)

%description -n texlive-basque-book-doc
This package includes the documentation for texlive-basque-book

%post -n texlive-basque-book
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-basque-book 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-basque-book
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-basque-book-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/basque-book/README
%{_texmfdistdir}/doc/latex/basque-book/basque-book.pdf
%{_texmfdistdir}/doc/latex/basque-book/basque-book_EUS.pdf
%{_texmfdistdir}/doc/latex/basque-book/basque-book_EUS.tex

%files -n texlive-basque-book
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/basque-book/basque-book.cls
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-basque-book-%{texlive_version}.%{texlive_noarch}.1.20svn32924-%{release}-zypper
%endif

%package -n texlive-basque-date
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn26477
Release:        0
Summary:        Print the date in Basque
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-basque-date-doc >= %{texlive_version}
Provides:       tex(basque-date.sty)
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source272:      basque-date.tar.xz
Source273:      basque-date.doc.tar.xz

%description -n texlive-basque-date
The package provides two LaTeX commands to print the current
date in Basque according to the correct forms ruled by The
Basque Language Academy (Euskaltzaindia). The commands
automatically solve the complex declination issues of numbers
in Basque.

%package -n texlive-basque-date-doc
Version:        %{texlive_version}.%{texlive_noarch}.1.05svn26477
Release:        0
Summary:        Documentation for texlive-basque-date
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-basque-date-doc
This package includes the documentation for texlive-basque-date

%post -n texlive-basque-date
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-basque-date 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-basque-date
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-basque-date-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/latex/basque-date/README
%{_texmfdistdir}/doc/latex/basque-date/basque-date.pdf

%files -n texlive-basque-date
%defattr(-,root,root,755)
%{_texmfdistdir}/tex/latex/basque-date/basque-date.sty
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-basque-date-%{texlive_version}.%{texlive_noarch}.1.05svn26477-%{release}-zypper
%endif

%package -n texlive-bath-bst
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn53422
Release:        0
Summary:        Harvard referencing style as recommended by the University of Bath Library
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bath-bst-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source274:      bath-bst.tar.xz
Source275:      bath-bst.doc.tar.xz

%description -n texlive-bath-bst
This package provides a BibTeX style to format reference lists
in the Harvard style recommended by the University of Bath
Library. It should be used in conjunction with natbib for
citations.

%package -n texlive-bath-bst-doc
Version:        %{texlive_version}.%{texlive_noarch}.3.2svn53422
Release:        0
Summary:        Documentation for texlive-bath-bst
License:        LPPL-1.0
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bath-bst-doc
This package includes the documentation for texlive-bath-bst

%post -n texlive-bath-bst
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bath-bst 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bath-bst
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bath-bst-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/bibtex/bath-bst/README.md
%{_texmfdistdir}/doc/bibtex/bath-bst/bath-bst-v1.bib
%{_texmfdistdir}/doc/bibtex/bath-bst/bath-bst-v1.pdf
%{_texmfdistdir}/doc/bibtex/bath-bst/bath-bst-v1.tex
%{_texmfdistdir}/doc/bibtex/bath-bst/bath-bst.bib
%{_texmfdistdir}/doc/bibtex/bath-bst/bath-bst.pdf

%files -n texlive-bath-bst
%defattr(-,root,root,755)
%{_texmfdistdir}/bibtex/bst/bath-bst/bath.bst
%{_texmfdistdir}/bibtex/bst/bath-bst/bathx.bst
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bath-bst-%{texlive_version}.%{texlive_noarch}.3.2svn53422-%{release}-zypper
%endif

%package -n texlive-bbcard
Version:        %{texlive_version}.%{texlive_noarch}.svn19440
Release:        0
Summary:        Bullshit bingo, calendar and baseball-score cards
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/
Requires(pre): texlive-filesystem >= %{texlive_version}
Requires(post): coreutils
Requires(postun): coreutils
Requires(postun): texlive >= %{texlive_version}
Requires(postun): texlive-filesystem >= %{texlive_version}
Requires(postun): texlive-kpathsea-bin >= %{texlive_version}
Requires(postun): texlive-kpathsea >= %{texlive_version}
Requires(postun): texlive-scripts-bin >= %{texlive_version}
Requires(postun): texlive-scripts >= %{texlive_version}
Requires(posttrans): coreutils
Requires(posttrans): ed
Requires(posttrans): findutils
Requires(posttrans): grep
Requires(posttrans): sed
Requires(posttrans): texlive >= %{texlive_version}
Requires(posttrans): texlive-filesystem >= %{texlive_version}
Requires(posttrans): texlive-kpathsea-bin >= %{texlive_version}
Requires(posttrans): texlive-kpathsea >= %{texlive_version}
Requires(posttrans): texlive-scripts-bin >= %{texlive_version}
Requires(posttrans): texlive-scripts >= %{texlive_version}
Recommends:     texlive-bbcard-doc >= %{texlive_version}
# Download at ftp://ftp://ftp.tug.org/texlive/tlpretest/archive/
# from 20200327
Source276:      bbcard.tar.xz
Source277:      bbcard.doc.tar.xz

%description -n texlive-bbcard
Three jiffy packages for creating cards of various sorts with
MetaPost.

%package -n texlive-bbcard-doc
Version:        %{texlive_version}.%{texlive_noarch}.svn19440
Release:        0
Summary:        Documentation for texlive-bbcard
License:        SUSE-Public-Domain
Group:          Productivity/Publishing/TeX/Base
URL:            http://www.tug.org/texlive/

%description -n texlive-bbcard-doc
This package includes the documentation for texlive-bbcard

%post -n texlive-bbcard
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update

%postun -n texlive-bbcard 
mkdir -p /var/run/texlive
> /var/run/texlive/run-mktexlsr
> /var/run/texlive/run-update
if test $1 = 0; then
    exit 0
fi

%posttrans -n texlive-bbcard
%if %{with zypper_posttrans}
test -z "$ZYPP_IS_RUNNING" || exit 0
%endif
test -d /var/run/texlive || exit 0
VERBOSE=false %{_texmfdistdir}/texconfig/update || :

%files -n texlive-bbcard-doc
%defattr(-,root,root,755)
%{_texmfdistdir}/doc/metapost/bbcard/README.TEXLIVE
%{_texmfdistdir}/doc/metapost/bbcard/README.bbcard
%{_texmfdistdir}/doc/metapost/bbcard/README.calendar
%{_texmfdistdir}/doc/metapost/bbcard/README.scorecard

%files -n texlive-bbcard
%defattr(-,root,root,755)
%{_texmfdistdir}/metapost/bbcard/bbcard.mp
%{_texmfdistdir}/metapost/bbcard/breakwidth.mp
%{_texmfdistdir}/metapost/bbcard/calendar.mp
%{_texmfdistdir}/metapost/bbcard/scorecard.mp
%if %{with zypper_posttrans}
/var/adm/update-scripts/texlive-bbcard-%{texlive_version}.%{texlive_noarch}.svn19440-%{release}-zypper
%endif

%prep
%setup -q -c -T

%build

%install
    rm -rf %{buildroot}
    mkdir -p %{buildroot}%{_texmfdistdir}
    mkdir -p %{buildroot}%{_texmfmaindir}/tlpkg/tlpostcode
    mkdir -p %{buildroot}%{_datadir}/texlive/tlpkg
    mkdir -p %{buildroot}/var/adm/update-scripts
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf-dist
    ln -sf ../../share/texmf        %{buildroot}%{_datadir}/texlive/texmf
    ln -sf ../../../share/texmf/tlpkg/tlpostcode \
                                    %{buildroot}%{_datadir}/texlive/tlpkg/tlpostcode
    ln -sf tlpkg/tlpostcode         %{buildroot}%{_texmfmaindir}/tlpostcode
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-around-the-bend-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:1} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-arphic-fonts-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:2} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:3} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-arphic
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/arphic/bkaiu/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/arphic/bsmiu/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/arphic/gbsnu/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/arphic/gkaiu/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-arphic
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-arphic/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-arphic/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-arphic/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-arphic/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-arphic.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-arphic    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-arphic/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-arphic-ttf-fonts-%{texlive_version}.%{texlive_noarch}.svn42675-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:4} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:5} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-arphic-ttf
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/arphic-ttf/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-arphic-ttf
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-arphic-ttf/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-arphic-ttf/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-arphic-ttf/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-arphic-ttf/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-arphic-ttf.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-arphic-ttf    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-arphic-ttf/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-arraycols-%{texlive_version}.%{texlive_noarch}.1.0svn51491-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:6} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:7} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-arrayjobx-%{texlive_version}.%{texlive_noarch}.1.04svn18125-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:8} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:9} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-arraysort-%{texlive_version}.%{texlive_noarch}.1.0svn31576-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:10} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:11} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-arsclassica-%{texlive_version}.%{texlive_noarch}.svn45656-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:12} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:13} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-articleingud-%{texlive_version}.%{texlive_noarch}.0.0.3svn38741-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:14} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:15} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-arydshln-%{texlive_version}.%{texlive_noarch}.1.76svn50084-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:16} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:17} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asaetr-%{texlive_version}.%{texlive_noarch}.1.0asvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:18} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:19} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asapsym-fonts-%{texlive_version}.%{texlive_noarch}.1.0svn40201-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:20} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:21} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-asapsym
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/omnibus-type/asapsym/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-asapsym
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-asapsym/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-asapsym/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-asapsym/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-asapsym/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-asapsym.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-asapsym    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-asapsym/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ascelike-%{texlive_version}.%{texlive_noarch}.2.3svn29129-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:22} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:23} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ascii-chart-%{texlive_version}.%{texlive_noarch}.svn20536-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:24} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ascii-font-fonts-%{texlive_version}.%{texlive_noarch}.2.0svn29989-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:25} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:26} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-ascii-font
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/ascii-font/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-ascii-font
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-ascii-font/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-ascii-font/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-ascii-font/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-ascii-font/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-ascii-font.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-ascii-font    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-ascii-font/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asciilist-%{texlive_version}.%{texlive_noarch}.2.2bsvn49060-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:27} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:28} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-ascmac-fonts-%{texlive_version}.%{texlive_noarch}.2.1svn53411-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:29} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:30} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-ascmac
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/ascmac/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-ascmac
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-ascmac/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-ascmac/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-ascmac/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-ascmac/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-ascmac.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-ascmac    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-ascmac/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-askinclude-%{texlive_version}.%{texlive_noarch}.2.7svn54725-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:31} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:32} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-askmaps-%{texlive_version}.%{texlive_noarch}.0.0.1svn32320-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:33} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:34} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asmeconf-%{texlive_version}.%{texlive_noarch}.1.18svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:35} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:36} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asmejour-%{texlive_version}.%{texlive_noarch}.1.12svn54758-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:37} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:38} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-aspectratio-fonts-%{texlive_version}.%{texlive_noarch}.2.0svn25243-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:39} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:40} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-aspectratio
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/aspectratio/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-aspectratio
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-aspectratio/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-aspectratio/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-aspectratio/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-aspectratio/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-aspectratio.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-aspectratio    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-aspectratio/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-assignment-%{texlive_version}.%{texlive_noarch}.svn20431-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:41} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:42} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-assoccnt-%{texlive_version}.%{texlive_noarch}.0.0.8svn38497-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:43} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:44} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-astro-%{texlive_version}.%{texlive_noarch}.2.20svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:45} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:46} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asyfig-%{texlive_version}.%{texlive_noarch}.0.0.1csvn17512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:47} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:48} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asymptote-%{texlive_version}.%{texlive_noarch}.2.65svn54567-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:49} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:50} -C %{buildroot}%{_datadir}/texlive
    # Correct wrong python scripts if any
    for scr in %{_texmfdistdir}/asymptote/GUI/icons_rc.py
    do
        test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		i
		#! /usr/bin/python
		.
		w
		q
	EOF
    done
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/asymptote/asy-kate.sh \
	       %{_texmfdistdir}/asymptote/asymptote.py
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/asymptote/GUI/CustMatTransform.py \
	       %{_texmfdistdir}/asymptote/GUI/DebugFlags.py \
	       %{_texmfdistdir}/asymptote/GUI/GuidesManager.py \
	       %{_texmfdistdir}/asymptote/GUI/InplaceAddObj.py \
	       %{_texmfdistdir}/asymptote/GUI/PrimitiveShape.py \
	       %{_texmfdistdir}/asymptote/GUI/SetCustomAnchor.py \
	       %{_texmfdistdir}/asymptote/GUI/UndoRedoStack.py \
	       %{_texmfdistdir}/asymptote/GUI/Widg_addLabel.py \
	       %{_texmfdistdir}/asymptote/GUI/Widg_addPolyOpt.py \
	       %{_texmfdistdir}/asymptote/GUI/Widg_editBezier.py \
	       %{_texmfdistdir}/asymptote/GUI/Window1.py \
	       %{_texmfdistdir}/asymptote/GUI/__init__.py \
	       %{_texmfdistdir}/asymptote/GUI/labelEditor.py \
	       %{_texmfdistdir}/asymptote/GUI/setup.py \
	       %{_texmfdistdir}/asymptote/GUI/xasy.py \
	       %{_texmfdistdir}/asymptote/GUI/xasy2asy.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyArgs.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyBezierInterface.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyFile.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyOptions.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyStrings.py \
	       %{_texmfdistdir}/asymptote/GUI/xasySvg.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyTransform.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyUtils.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyValidator.py \
	       %{_texmfdistdir}/asymptote/GUI/xasyVersion.py \
	       %{_texmfdistdir}/asymptote/asymptote.py
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
    # Strip executable bit from non-scripts
    for txt in %{_texmfdistdir}/asymptote/shaders/fragment.glsl \
	       %{_texmfdistdir}/asymptote/shaders/vertex.glsl
    do
	test -e %{buildroot}/$txt || continue
	chmod 0644 %{buildroot}/$txt
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asymptote-by-example-zh-cn-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:51} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/CLEAN.bat
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/MAKEPDF.bat
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/cleantmp \
	       %{_texmfdistdir}/doc/support/asymptote-by-example-zh-cn/src/makepdf
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asymptote-faq-zh-cn-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:52} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asymptote-manual-zh-cn-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:53} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/CLEAN.bat
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/MAKEPDF.bat
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/cleantmp \
	       %{_texmfdistdir}/doc/support/asymptote-manual-zh-cn/src/makepdf
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-asypictureb-%{texlive_version}.%{texlive_noarch}.0.0.3svn33490-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:54} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:55} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-atbegshi-%{texlive_version}.%{texlive_noarch}.1.19svn53051-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:56} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:57} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-atenddvi-%{texlive_version}.%{texlive_noarch}.1.4svn53107-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:58} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:59} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-attachfile-%{texlive_version}.%{texlive_noarch}.1.9svn42099-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:60} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:61} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-attachfile2-%{texlive_version}.%{texlive_noarch}.2.11svn52929-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:62} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:63} -C %{buildroot}%{_datadir}/texlive
    # Make possible scripts usable if any
    for scr in %{_texmfdistdir}/scripts/attachfile2/pdfatfi.pl
    do
	test -e %{buildroot}/$scr || continue
	chmod 0755 %{buildroot}/$scr
    done
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/attachfile2/pdfatfi.pl
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-atveryend-%{texlive_version}.%{texlive_noarch}.1.11svn53108-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:64} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:65} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-aucklandthesis-%{texlive_version}.%{texlive_noarch}.svn51323-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:66} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:67} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-augie-fonts-%{texlive_version}.%{texlive_noarch}.svn18948-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:68} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:69} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-augie
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/augie/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-augie
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-augie/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-augie/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-augie/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-augie/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-augie.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-augie    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-augie/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-auncial-new-fonts-%{texlive_version}.%{texlive_noarch}.2.0svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:70} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:71} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-auncial-new
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/auncial-new/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-auncial-new
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-auncial-new/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-auncial-new/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-auncial-new/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-auncial-new/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-auncial-new.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-auncial-new    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-auncial-new/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-aurical-fonts-%{texlive_version}.%{texlive_noarch}.1.5svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:72} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:73} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-aurical
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/public/aurical/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-aurical
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-aurical/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-aurical/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-aurical/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-aurical/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-aurical.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-aurical    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-aurical/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-aurl-%{texlive_version}.%{texlive_noarch}.svn41853-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:74} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:75} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-authoraftertitle-%{texlive_version}.%{texlive_noarch}.0.0.9svn24863-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:76} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:77} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-authorarchive-%{texlive_version}.%{texlive_noarch}.1.1.1svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:78} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:79} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-authordate-%{texlive_version}.%{texlive_noarch}.svn52564-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:80} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:81} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-authorindex-%{texlive_version}.%{texlive_noarch}.svn51757-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:82} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:83} -C %{buildroot}%{_datadir}/texlive
    # Avoid /usr/bin/env <prog>
    for scr in %{_texmfdistdir}/scripts/authorindex/authorindex
    do
	test -e %{buildroot}/$scr || continue
	ed %{buildroot}/${scr} <<-'EOF'
		1
		s@/env[[:blank:]]\+@/@
		.
		w
		q
	EOF
    done
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-auto-pst-pdf-%{texlive_version}.%{texlive_noarch}.0.0.6svn52849-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:84} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:85} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-auto-pst-pdf-lua-%{texlive_version}.%{texlive_noarch}.0.0.03svn54779-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:86} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:87} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-autoaligne-%{texlive_version}.%{texlive_noarch}.1.4svn49092-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:88} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:89} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-autoarea-%{texlive_version}.%{texlive_noarch}.0.0.3asvn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:90} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:91} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-autobreak-%{texlive_version}.%{texlive_noarch}.0.0.3svn43337-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:92} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:93} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-autofancyhdr-%{texlive_version}.%{texlive_noarch}.0.0.1svn54049-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:94} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:95} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-automata-%{texlive_version}.%{texlive_noarch}.0.0.3svn19717-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:96} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:97} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-autonum-%{texlive_version}.%{texlive_noarch}.0.0.3.11svn36084-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:98} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:99} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-autopdf-%{texlive_version}.%{texlive_noarch}.1.1svn32377-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:100} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:101} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-autosp-%{texlive_version}.%{texlive_noarch}.svn54240-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:102} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-auxhook-%{texlive_version}.%{texlive_noarch}.1.6svn53173-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:103} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:104} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-avantgar-fonts-%{texlive_version}.%{texlive_noarch}.svn31835-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:105} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-avantgar
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/urw/avantgar/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-avantgar
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-avantgar/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-avantgar/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-avantgar/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-avantgar/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-avantgar.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-avantgar    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-avantgar/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-avremu-%{texlive_version}.%{texlive_noarch}.0.0.1svn35373-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:106} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:107} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-awesomebox-%{texlive_version}.%{texlive_noarch}.0.0.6svn51776-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:108} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:109} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-axessibility-%{texlive_version}.%{texlive_noarch}.3.0svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:110} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:111} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-axodraw2-%{texlive_version}.%{texlive_noarch}.2.1.1bsvn54055-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:112} -C %{buildroot}%{_datadir}/texlive
    tar --use-compress-program=xz -xf %{S:113} -C %{buildroot}%{_datadir}/texlive
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-b1encoding-%{texlive_version}.%{texlive_noarch}.1.0svn21271-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:114} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:115} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-%{texlive_version}.%{texlive_noarch}.3.42svn54487-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:116} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:117} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-albanian-%{texlive_version}.%{texlive_noarch}.1.0csvn30254-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:118} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:119} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-azerbaijani-%{texlive_version}.%{texlive_noarch}.1.0asvn44197-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:120} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:121} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-basque-%{texlive_version}.%{texlive_noarch}.1.0fsvn30256-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:122} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:123} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-belarusian-%{texlive_version}.%{texlive_noarch}.1.5svn49022-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:124} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:125} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-bosnian-%{texlive_version}.%{texlive_noarch}.1.1svn38174-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:126} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:127} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-breton-%{texlive_version}.%{texlive_noarch}.1.0hsvn30257-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:128} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:129} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-bulgarian-%{texlive_version}.%{texlive_noarch}.1.2gsvn31902-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:130} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:131} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-catalan-%{texlive_version}.%{texlive_noarch}.2.2psvn30259-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:132} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:133} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-croatian-%{texlive_version}.%{texlive_noarch}.1.3lsvn35198-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:134} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:135} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-czech-%{texlive_version}.%{texlive_noarch}.3.1asvn30261-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:136} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:137} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-danish-%{texlive_version}.%{texlive_noarch}.1.3rsvn30262-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:138} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:139} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-dutch-%{texlive_version}.%{texlive_noarch}.3.8isvn30263-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:140} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:141} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-english-%{texlive_version}.%{texlive_noarch}.3.3rsvn44495-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:142} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:143} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-esperanto-%{texlive_version}.%{texlive_noarch}.1.4tsvn30265-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:144} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:145} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-estonian-%{texlive_version}.%{texlive_noarch}.1.1asvn38064-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:146} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:147} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-finnish-%{texlive_version}.%{texlive_noarch}.1.3rsvn54771-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:148} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:149} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-french-%{texlive_version}.%{texlive_noarch}.3.5hsvn54787-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:150} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:151} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-friulan-%{texlive_version}.%{texlive_noarch}.1.3svn39861-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:152} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:153} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-galician-%{texlive_version}.%{texlive_noarch}.4.3csvn30270-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:154} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:155} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-georgian-%{texlive_version}.%{texlive_noarch}.2.2svn45864-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:156} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:157} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-german-%{texlive_version}.%{texlive_noarch}.2.11svn49391-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:158} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:159} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-greek-%{texlive_version}.%{texlive_noarch}.1.9jsvn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:160} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:161} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-hebrew-%{texlive_version}.%{texlive_noarch}.2.3hsvn30273-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:162} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:163} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-hungarian-%{texlive_version}.%{texlive_noarch}.1.5csvn49701-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:164} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:165} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-icelandic-%{texlive_version}.%{texlive_noarch}.1.3svn51551-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:166} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:167} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-indonesian-%{texlive_version}.%{texlive_noarch}.1.0msvn43235-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:168} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:169} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-interlingua-%{texlive_version}.%{texlive_noarch}.1.6svn30276-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:170} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:171} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-irish-%{texlive_version}.%{texlive_noarch}.1.0hsvn30277-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:172} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:173} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-italian-%{texlive_version}.%{texlive_noarch}.1.4.03svn53019-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:174} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:175} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-japanese-%{texlive_version}.%{texlive_noarch}.2.2svn50735-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:176} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:177} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-kurmanji-%{texlive_version}.%{texlive_noarch}.1.1svn30279-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:178} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:179} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-latin-%{texlive_version}.%{texlive_noarch}.3.5svn38173-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:180} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:181} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-latvian-%{texlive_version}.%{texlive_noarch}.2.0bsvn46681-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:182} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:183} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-macedonian-%{texlive_version}.%{texlive_noarch}.svn39587-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:184} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:185} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-malay-%{texlive_version}.%{texlive_noarch}.1.0msvn43234-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:186} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:187} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-norsk-%{texlive_version}.%{texlive_noarch}.2.0isvn30281-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:188} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:189} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-occitan-%{texlive_version}.%{texlive_noarch}.0.0.2svn39608-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:190} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:191} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-piedmontese-%{texlive_version}.%{texlive_noarch}.1.0svn30282-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:192} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:193} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-polish-%{texlive_version}.%{texlive_noarch}.1.2lsvn30283-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:194} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:195} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-portuges-%{texlive_version}.%{texlive_noarch}.1.2qsvn30284-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:196} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:197} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-romanian-%{texlive_version}.%{texlive_noarch}.1.2lsvn30285-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:198} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:199} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-romansh-%{texlive_version}.%{texlive_noarch}.svn30286-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:200} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:201} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-russian-%{texlive_version}.%{texlive_noarch}.1.3jsvn45007-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:202} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:203} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-samin-%{texlive_version}.%{texlive_noarch}.1.0csvn30288-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:204} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:205} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-scottish-%{texlive_version}.%{texlive_noarch}.1.0gsvn30289-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:206} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:207} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-serbian-%{texlive_version}.%{texlive_noarch}.2.0asvn53140-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:208} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:209} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-serbianc-%{texlive_version}.%{texlive_noarch}.3.0asvn53139-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:210} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:211} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-slovak-%{texlive_version}.%{texlive_noarch}.3.1asvn30292-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:212} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:213} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-slovenian-%{texlive_version}.%{texlive_noarch}.1.2isvn30351-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:214} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:215} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-sorbian-%{texlive_version}.%{texlive_noarch}.lower_sorbian_1.0g._upper_1.0ksvn30294-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:216} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:217} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-spanish-%{texlive_version}.%{texlive_noarch}.5.0psvn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:218} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:219} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-swedish-%{texlive_version}.%{texlive_noarch}.2.3dsvn30296-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:220} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:221} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-thai-%{texlive_version}.%{texlive_noarch}.1.0.0svn30564-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:222} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:223} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-turkish-%{texlive_version}.%{texlive_noarch}.1.4svn51560-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:224} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:225} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-ukrainian-%{texlive_version}.%{texlive_noarch}.1.4csvn47585-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:226} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:227} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-vietnamese-%{texlive_version}.%{texlive_noarch}.1.4svn39246-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:228} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:229} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babel-welsh-%{texlive_version}.%{texlive_noarch}.1.1asvn38372-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:230} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:231} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-babelbib-%{texlive_version}.%{texlive_noarch}.1.32svn50354-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:232} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:233} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-background-%{texlive_version}.%{texlive_noarch}.2.1svn42428-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:234} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:235} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-backnaur-%{texlive_version}.%{texlive_noarch}.3.1svn54080-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:236} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:237} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-baekmuk-fonts-%{texlive_version}.%{texlive_noarch}.2.2svn42106-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:238} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:239} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-baekmuk
    for font in %{buildroot}/%{_texmfdistdir}/fonts/truetype/public/baekmuk/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-baekmuk
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-baekmuk/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-baekmuk/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baekmuk/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baekmuk/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-baekmuk.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-baekmuk    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-baekmuk/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bagpipe-%{texlive_version}.%{texlive_noarch}.3.02svn34393-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:240} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:241} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bangorcsthesis-%{texlive_version}.%{texlive_noarch}.1.5.3svn48834-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:242} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:243} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bangorexam-%{texlive_version}.%{texlive_noarch}.1.4.0svn46626-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:244} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:245} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bangtex-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:246} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:247} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bankstatement-%{texlive_version}.%{texlive_noarch}.0.0.9.2svn38857-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:248} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:249} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-barcodes-%{texlive_version}.%{texlive_noarch}.svn15878-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:250} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:251} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove files
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/latex/barcodes/install.bat
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bardiag-%{texlive_version}.%{texlive_noarch}.0.0.4asvn22013-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:252} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:253} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-barr-%{texlive_version}.%{texlive_noarch}.svn38479-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:254} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:255} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-barracuda-%{texlive_version}.%{texlive_noarch}.0.0.0.10svn53683-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:256} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:257} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bartel-chess-fonts-%{texlive_version}.%{texlive_noarch}.svn20619-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:258} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:259} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bashful-%{texlive_version}.%{texlive_noarch}.0.0.93svn25597-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:260} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:261} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-basicarith-%{texlive_version}.%{texlive_noarch}.1.1svn35460-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:262} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:263} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-baskervald-fonts-%{texlive_version}.%{texlive_noarch}.1.016svn19490-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:264} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:265} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-baskervald
    for font in %{buildroot}/%{_texmfdistdir}/fonts/type1/arkandis/baskervald/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-baskervald
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-baskervald/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervald/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervald/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervald/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-baskervald.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-baskervald    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-baskervald/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-baskervaldx-fonts-%{texlive_version}.%{texlive_noarch}.1.073svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:266} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:267} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-baskervaldx
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/baskervaldx/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/baskervaldx/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-baskervaldx
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-baskervaldx/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervaldx/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervaldx/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervaldx/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-baskervaldx.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-baskervaldx    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-baskervaldx/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-baskervaldx.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-baskervaldx/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-baskervaldx.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-baskervaldx.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-baskervillef-fonts-%{texlive_version}.%{texlive_noarch}.1.050svn54512-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:268} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:269} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Move font files
    mkdir -p %{buildroot}%{_datadir}/fonts/texlive-baskervillef
    for font in %{buildroot}/%{_texmfdistdir}/fonts/opentype/public/baskervillef/*.{pf[ab],[ot]tf} \
		%{buildroot}/%{_texmfdistdir}/fonts/type1/public/baskervillef/*.{pf[ab],[ot]tf}
    do
        test -e $font || continue
        mv -f $font %{buildroot}%{_datadir}/fonts/texlive-baskervillef
        base=${font##*/}
        ln -sf %{_datadir}/fonts/texlive-baskervillef/${base} ${font}
    done
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervillef/encodings.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervillef/fonts.dir
    >  %{buildroot}%{_datadir}/fonts/texlive-baskervillef/fonts.scale
    mkdir -p %{buildroot}%{_datadir}/fontconfig/conf.avail
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/58-texlive-baskervillef.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Use this to disable the TeX fonts of the package -->
	<!--    texlive-baskervillef    -->
	<!-- Be aware that the configurations in the files    -->
	<!-- 09-texlive*.conf will not be affected by this    -->
	<!-- ************************************************ -->

	<fontconfig>
	  <rejectfont>
	    <glob>%{_datadir}/fonts/texlive-baskervillef/*</glob>
	  </rejectfont>
	</fontconfig>
	EOF

    mkdir -p %{buildroot}%{_sysconfdir}/fonts/conf.d
    (cat > %{buildroot}%{_datadir}/fontconfig/conf.avail/55-texlive-baskervillef.conf)<<-'EOF'
	<?xml version="1.0"?>
	<!DOCTYPE fontconfig SYSTEM "fonts.dtd">

	<!-- ************************************************ -->
	<!-- Disable plain Type1 font to let fontconfig       -->
	<!-- prefere the OpenType and TrueType fonts          -->
	<!-- ************************************************ -->

	<fontconfig>
	  <selectfont>
	    <rejectfont>
	      <glob>%{_datadir}/fonts/texlive-baskervillef/*.pf*</glob>
	    </rejectfont>
	  </selectfont>
	</fontconfig>
	EOF
    ln -sf %{_datadir}/fontconfig/conf.avail/55-texlive-baskervillef.conf %{buildroot}%{_sysconfdir}/fonts/conf.d/55-texlive-baskervillef.conf
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-basque-book-%{texlive_version}.%{texlive_noarch}.1.20svn32924-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:270} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:271} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-basque-date-%{texlive_version}.%{texlive_noarch}.1.05svn26477-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:272} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:273} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bath-bst-%{texlive_version}.%{texlive_noarch}.3.2svn53422-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:274} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:275} -C %{buildroot}%{_datadir}/texlive/texmf-dist
%if %{with zypper_posttrans}
    ln -sf %{_texmfdistdir}/texconfig/zypper.py \
       %{buildroot}/var/adm/update-scripts/texlive-bbcard-%{texlive_version}.%{texlive_noarch}.svn19440-%{release}-zypper
%endif
    tar --use-compress-program=xz -xf %{S:276} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    tar --use-compress-program=xz -xf %{S:277} -C %{buildroot}%{_datadir}/texlive/texmf-dist
    # Remove this
    rm -vrf %{buildroot}%{_texmfdistdir}/tlpkg/tlpobj
    rm -vrf %{buildroot}%{_texmfmaindir}/tlpkg/tlpobj
    rm -v  %{buildroot}%{_datadir}/texlive/texmf
    rm -v  %{buildroot}%{_datadir}/texlive/texmf-dist
    rm -v  %{buildroot}%{_texmfmaindir}/tlpostcode
    rm -vr %{buildroot}%{_datadir}/texlive
    # Handle manual pages
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfmaindir}/doc/man/man*/*.pdf
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/Makefile
    rm -vf %{buildroot}%{_texmfdistdir}/doc/man/man*/*.pdf
    for path in %{buildroot}%{_texmfmaindir}/doc/man/man? \
               %{buildroot}%{_texmfdistdir}/doc/man/man?
    do
        test -d "$path" || continue
        sec=${path##*/}
        mkdir -p %{buildroot}%{_mandir}/${sec}
        for page in ${path}/*.*
        do
            test -e "$page" || continue
            mv -f $page %{buildroot}%{_mandir}/${sec}/
        done
    done
    rm -rf %{buildroot}%{_texmfmaindir}/doc/man
    rm -rf %{buildroot}%{_texmfdistdir}/doc/man
    # Handle info documents
    rm -vf  %{buildroot}%{_texmfmaindir}/doc/info/dir
    rm -vf  %{buildroot}%{_texmfdistdir}/doc/info/dir
    mkdir -p %{buildroot}%{_infodir}
    for inf in %{buildroot}%{_texmfmaindir}/doc/info/*.info \
               %{buildroot}%{_texmfdistdir}/doc/info/*.info
    do
        test -e "$inf" || continue
        mv -f $inf %{buildroot}%{_infodir}/
    done
    rm -rf %{buildroot}%{_texmfmaindir}/doc/info
    rm -rf %{buildroot}%{_texmfdistdir}/doc/info
    find %{buildroot}%{_texmfmaindir}/ %{buildroot}%{_texmfdistdir}/ \
        -type f -a -perm /g+w,o+w | xargs --no-run-if-empty chmod g-w,o-w

%changelog
