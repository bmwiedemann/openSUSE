#
# spec file for package efont-serif-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           efont-serif-fonts
Version:        20010312
Release:        0
Summary:        Free and Open Scalable Electronic Font
License:        GPL-2.0
Group:          System/X11/Fonts
Url:            http://openlab.ring.gr.jp/efont/
# downloaded from
# http://openlab.ring.gr.jp/efont/dist/serif/efont-serif-{version}-win.zip
# and converted to tar.bz2 to save a bit of space
Source0:        efont-serif-%{version}.tar.bz2
Source1:        fonts.scale.efont-serif-ttf
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
# Summary(ja):  真にフリーでオープンな電子書体です。
# %description -l ja
#
# 真にフリーでオープンな電子書体です。
#
#
# 例えば、再配布が自由な Omega Serif や URW Nimbus は、Adobe Times と字形
# が酷似しています。efont-serif は、アウトラインデータはもちろん、字形その
# ものも、著作権で保護されている他の書体を一切コピーしていません。
#
# Authors:
# --------
#
#     Kazuhiko Shiozaki <kazuhiko@ring.gr.jp>

%description
The efont-serif is a really free and open scalable electronic font.

The Omega Serif and URW Nimbus are also distributable. But their letter
forms are quite similar to Adobe Times. The efont-serif does not copy
the outlines or the letter forms of any copyrighted typefaces.

%prep
%setup -n efont-serif-%{version}-win

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}
install -c -m 644 $RPM_SOURCE_DIR/fonts.scale.efont-serif-ttf %{buildroot}%{_ttfontsdir}/
dos2unix GPL*
%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc GPL*
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*.ttf
%config %{_ttfontsdir}/fonts.scale.efont-serif-ttf

%changelog
