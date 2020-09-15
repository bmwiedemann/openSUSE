#
# spec file for package mozc
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


%define with_fcitx 1

%if %{with_fcitx}
%define fcitx_icon_dir %{_datadir}/fcitx/mozc/icon/
%define fcitx_addon_dir %{_datadir}/fcitx/addon/
%define fcitx_inputmethod_dir %{_datadir}/fcitx/inputmethod/
%define fcitx_lib_dir %{_libdir}/fcitx/
%endif

%define ibus_mozc_path %{_libdir}/ibus-mozc/ibus-engine-mozc
%define ibus_mozc_icon_path %{_datadir}/ibus-mozc/product_icon.png
%define document_dir %{_docdir}/ibus-mozc
%define zinnia_model_path %{_datadir}/zinnia/model/tomoe/handwriting-ja.model
%define use_libprotobuf 1

Name:           mozc
Version:        2.23.2815.102
Release:        0
Summary:        Mozc - Japanese Input Method for Chromium OS, Mac and Linux
License:        BSD-3-Clause AND SUSE-Public-Domain
Group:          System/I18n/Japanese
ExcludeArch:    ppc ppc64 s390 s390x
URL:            https://github.com/google/mozc
# Run ./make_archive.sh to make tar.xz removing third party files
Source0:        %{name}-%{version}.tar.xz
Source1:        README.SUSE

# gyp is not included from 1.11.1522.102
# License: BSD-3-Clause
# git clone https://chromium.googlesource.com/external/gyp
Source3:        gyp-e87d37d.tar.xz
#
Source4:        ibus-setup-mozc-jp.desktop.in
#
# svn export http://japanese-usage-dictionary.googlecode.com/svn/trunk/@r10
# japanese-usage-dictionary
# License: BSD-2-Clause
Source5:        japanese_usage_dictionary-r10.tar.xz
# protobuf
# License: BSD-3-Clause
#
# Use static protobuf, which is recommended when protobuf is used from a C++ application
# Using protobuf >= 3.6 requires to update Mozc source
# https://github.com/protocolbuffers/protobuf/archive/v3.5.2.tar.gz
Source6:        protobuf-v3.5.2.tar.gz
#
# jigyosyo.zip and ken_all.zip are zip-code--address data provided by
# Japan Post Co., Ltd.
# License: SUSE-Public-Domain
Source10:       jigyosyo.zip
Source11:       ken_all.zip
#
%if %{with_fcitx}
# add fcitx as mozc module
# License: BSD-3-Clause
Patch:          fcitx-mozc-2.23.2815.102.1.patch
Source21:       fcitx-mozc-icons.tar.gz
%endif
# A script for making a source tar.xz archive
Source99:       make_archive.sh

# PATCH-FEATURE-OPENSUSE ftake@geeko.jp
Patch1:         ibus-provide-layout-variations.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org
Patch2:         mozc-ninja-verbose-build.patch

# PATCH-FIX-OPENSUSE ftake@geeko.jp
# workaround for the Qt5 bug (boo#947013)
Patch6:         ibus-qt5-hide_preedit_text-workaround.patch

# PATCH-FIX-OPENSUSE mozc-build-gcc.patch bsc#990844 qzhao@suse.com -- Portng mozc-build-gcc.patch to force mozc build with gcc.
Patch7:         mozc-build-gcc.patch

# PATCH-FIX-UPSTREAM i@marguerite.su
# fix python import error
Patch8:         mozc-gen_zip_code_seed_py.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp
# fix build error with gcc 8.1
Patch9:         gcc-8.1-ZeroQueryDict-iterator.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp
Patch10:        add-Japanese-new-era-reiwa-to-dict.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp
Patch11:        add-Japanese-new-era-reiwa-to-date_rewriter.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp
Patch12:        add-Japanese-new-era-reiwa-ligature-to-dict.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp -- fix compile error caused by newer protobuf (from Gentoo)
# https://github.com/google/mozc/issues/460
Patch13:        mozc-2.23.2815.102-protobuf_generated_classes_no_inheritance.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp -- Use Python 3 to build Mozc
Patch14:        build-scripts-migration-to-python3.patch
# PATCH-FIX-UPSTREAM ftake@geeko.jp -- fix a bug of the Python3 patch
Patch15:        fix-zip-code-conversion-output.patch

BuildRequires:  ninja >= 1.4
%if %{use_libprotobuf}
BuildRequires:  protobuf-devel
%endif
BuildRequires:  python3
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mozc is a Japanese Input Method Editor (IME) designed for
multi-platform such as Chromium OS, Mac and Linux. This open-source
project originates from Google Japanese Input.

%package -n ibus-mozc
Summary:        The Mozc engine for IBus
Group:          System/I18n/Japanese
BuildRequires:  ibus-devel
Requires:       ibus >= 1.4.1
Requires:       mozc = %{version}
Requires:       mozc-gui-tools = %{version}
Recommends:     ibus-mozc-candidate-window
Provides:       locale(ibus:ja)

%description -n ibus-mozc
The Mozc engine for IBus provides a Japanese input method.

%package -n ibus-mozc-candidate-window
Summary:        An optional candidate window for ibus-mozc
Group:          System/I18n/Japanese
BuildRequires:  gtk2-devel
BuildRequires:  libglib-2_0-0
Requires:       ibus-mozc = %{version}
Provides:       locale(ibus:ja)

%description -n ibus-mozc-candidate-window
This package provides an advanced candidate window for IBus. The
window shows examples of selected words.

%if %{with_fcitx}
%package -n fcitx-mozc
Summary:        The Mozc backend for Fcitx
Group:          System/I18n/Japanese
BuildRequires:  fcitx-devel
Requires:       fcitx
Requires:       mozc = %{version}
Requires:       mozc-gui-tools = %{version}
Provides:       locale(fcitx:ja)

%description -n fcitx-mozc
The Mozc backend for Fcitx provides a Japanese input method.
%endif

%package gui-tools
Summary:        GUI tools for mozc
Group:          System/I18n/Japanese
BuildRequires:  zinnia-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       mozc = %{version}
Requires:       zinnia
Requires:       zinnia-tomoe

%description gui-tools
This package provides config, word-register, dictioaly,
character-palette, handwriting tools.

%prep
%setup -q

# extract fcitx-mozc
%if %{with_fcitx}
%patch -p1
%endif

%patch1 -p1
%patch2 -p1

cp %{SOURCE1} .

# install third_party files
cd src/third_party
# gyp
tar xvf %{SOURCE3}
# japanese_usage_dictionary
tar xvf %{SOURCE5}
# protobuf
%if ! %{use_libprotobuf}
mkdir protobuf
tar xvf %{SOURCE6} -C protobuf --strip-components 1
%endif
cd ../..

cd src
%patch6 -p1
%patch7 -p1
cd ..

%patch8 -p1

%patch9 -p1

# patches to support new Japanese era, Reiwa
%patch10 -p1
%patch11 -p1
cd src
%patch12 -p1
cd ..

%patch13 -p1
%patch14 -p1
%patch15 -p1

# Use python as python3
mkdir %{_builddir}/bin
ln -s /usr/bin/python3 %{_builddir}/bin/python
export PATH=%{_builddir}/bin:$PATH

# fix installation path
sed -e 's|@libdir@|%{_libdir}|g' %{SOURCE4} > ibus-setup-mozc-jp.desktop

# prepare zip code dictionary
cd src/data/dictionary_oss
unzip %{SOURCE10}
unzip %{SOURCE11}
python ../../dictionary/gen_zip_code_seed.py --zip_code=KEN_ALL.CSV --jigyosyo=JIGYOSYO.CSV >> dictionary09.txt
cd ../..

%build
%define target Release
export PATH=%{_builddir}/bin:$PATH
export QTDIR=%{_libdir}/qt5

# -Wall from RPM_OPT_FLAGS overrides -Wno-* options from gyp.
# gyp inserts -Wall to the head of release_extra_flags.
flags=${RPM_OPT_FLAGS/-Wall/}

# disable Fcitx5 for now
export GYP_DEFINES='ibus_mozc_path=%{ibus_mozc_path} ibus_mozc_icon_path=%{ibus_mozc_icon_path} use_libprotobuf=%{use_libprotobuf} use_libzinnia=1 document_dir=%{document_dir} zinnia_model_file=%{zinnia_model_path} release_extra_cflags="'$flags'" use_fcitx5=0'

cd src
python build_mozc.py gyp --server_dir=%{_libdir}/mozc
python build_mozc.py build -c %{target} \
	unix/ibus/ibus.gyp:ibus_mozc \
%if %{with_fcitx}
	unix/fcitx/fcitx.gyp:fcitx-mozc \
%endif
	server/server.gyp:mozc_server \
	unix/emacs/emacs.gyp:mozc_emacs_helper \
	gui/gui.gyp:mozc_tool \
	renderer/renderer.gyp:mozc_renderer

%define output_dir src/out_linux/%{target}

%install

install -m755 -d %{buildroot}%{_libdir}/ibus-mozc
install -m755 %{output_dir}/ibus_mozc %{buildroot}%{_libdir}/ibus-mozc/ibus-engine-mozc
install -m755 -d %{buildroot}%{_datadir}/ibus/component
install -m644 %{output_dir}/gen/unix/ibus/mozc.xml %{buildroot}%{_datadir}/ibus/component/mozc.xml
install -m755 -d %{buildroot}%{_datadir}/ibus-mozc
install -m644 src/data/images/unix/ime_product_icon_opensource-32.png %{buildroot}%{_datadir}/ibus-mozc/product_icon.png
install -m644 src/data/images/unix/ui-tool.png %{buildroot}%{_datadir}/ibus-mozc/tool.png
install -m644 src/data/images/unix/ui-properties.png %{buildroot}%{_datadir}/ibus-mozc/properties.png
install -m644 src/data/images/unix/ui-dictionary.png %{buildroot}%{_datadir}/ibus-mozc/dictionary.png
install -m644 src/data/images/unix/ui-direct.png %{buildroot}%{_datadir}/ibus-mozc/direct.png
install -m644 src/data/images/unix/ui-hiragana.png %{buildroot}%{_datadir}/ibus-mozc/hiragana.png
install -m644 src/data/images/unix/ui-katakana_half.png %{buildroot}%{_datadir}/ibus-mozc/katakana_half.png
install -m644 src/data/images/unix/ui-katakana_full.png %{buildroot}%{_datadir}/ibus-mozc/katakana_full.png
install -m644 src/data/images/unix/ui-alpha_half.png %{buildroot}%{_datadir}/ibus-mozc/alpha_half.png
install -m644 src/data/images/unix/ui-alpha_full.png %{buildroot}%{_datadir}/ibus-mozc/alpha_full.png

install -m755 -d %{buildroot}%{_datadir}/applications
install -m644 ibus-setup-mozc-jp.desktop %{buildroot}%{_datadir}/applications/ibus-setup-mozc-jp.desktop
%suse_update_desktop_file ibus-setup-mozc-jp System X-SuSE-Core-System

# for provide-layout-variations patch
ln -s ibus-setup-mozc-jp.desktop %{buildroot}%{_datadir}/applications/ibus-setup-mozc-jp-jp.desktop
%suse_update_desktop_file ibus-setup-mozc-jp-jp System X-SuSE-Core-System
ln -s ibus-setup-mozc-jp.desktop %{buildroot}%{_datadir}/applications/ibus-setup-mozc-us.desktop
%suse_update_desktop_file ibus-setup-mozc-us System X-SuSE-Core-System
ln -s ibus-setup-mozc-jp.desktop %{buildroot}%{_datadir}/applications/ibus-setup-mozc-dv.desktop
%suse_update_desktop_file ibus-setup-mozc-dv System X-SuSE-Core-System

%if %{with_fcitx}
# Install Fcitx module
for mofile in %{output_dir}/gen/unix/fcitx/po/*.mo
do
	filename=`basename $mofile`
	lang=${filename/.mo/}
	install -D -m 644 "$mofile" "%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/fcitx-mozc.mo"
done
install -m755 -d %{buildroot}%{fcitx_addon_dir}
install -m755 -d %{buildroot}%{fcitx_inputmethod_dir}
install -m755 -d %{buildroot}%{fcitx_icon_dir}
install -m755 -d %{buildroot}%{fcitx_lib_dir}
install -m 755 %{output_dir}/fcitx-mozc.so %{buildroot}%{fcitx_lib_dir}
install -m 644 src/unix/fcitx/fcitx-mozc.conf %{buildroot}%{fcitx_addon_dir}
install -m 644 src/unix/fcitx/mozc.conf %{buildroot}%{fcitx_inputmethod_dir}
install -m 644 src/data/images/product_icon_32bpp-128.png %{buildroot}%{fcitx_icon_dir}/mozc.png
install -m 644 src/data/images/unix/ui-alpha_full.png %{buildroot}%{fcitx_icon_dir}/mozc-alpha_full.png
install -m 644 src/data/images/unix/ui-alpha_half.png %{buildroot}%{fcitx_icon_dir}/mozc-alpha_half.png
install -m 644 src/data/images/unix/ui-direct.png %{buildroot}%{fcitx_icon_dir}/mozc-direct.png
install -m 644 src/data/images/unix/ui-hiragana.png %{buildroot}%{fcitx_icon_dir}/mozc-hiragana.png
install -m 644 src/data/images/unix/ui-katakana_full.png %{buildroot}%{fcitx_icon_dir}/mozc-katakana_full.png
install -m 644 src/data/images/unix/ui-katakana_half.png %{buildroot}%{fcitx_icon_dir}/mozc-katakana_half.png
install -m 644 src/data/images/unix/ui-dictionary.png %{buildroot}%{fcitx_icon_dir}/mozc-dictionary.png
install -m 644 src/data/images/unix/ui-properties.png %{buildroot}%{fcitx_icon_dir}/mozc-properties.png
install -m 644 src/data/images/unix/ui-tool.png %{buildroot}%{fcitx_icon_dir}/mozc-tool.png

# fix mozc icons. they're too ugly that even lose face for openSUSE.
cp -r %{SOURCE21} ./
tar -xzf fcitx-mozc-icons.tar.gz
cp -r fcitx-mozc-icons/* %{buildroot}%{fcitx_icon_dir}/
rm -rf fcitx-mozc-icons
rm -rf fcitx-mozc-icons.tar.gz

%endif

install -m755 -d %{buildroot}%{_libdir}/mozc
install -m755 %{output_dir}/mozc_server %{buildroot}%{_libdir}/mozc
install -m755 %{output_dir}/mozc_tool %{buildroot}%{_libdir}/mozc
install -m755 %{output_dir}/mozc_renderer %{buildroot}%{_libdir}/mozc

install -m755 -d %{buildroot}%{_bindir}
install -m755 %{output_dir}/mozc_emacs_helper %{buildroot}%{_bindir}
# install only for emacs since xemacs is not supported
install -m755 -d %{buildroot}%{_datadir}/emacs/site-lisp
install -m644 src/unix/emacs/mozc.el %{buildroot}%{_datadir}/emacs/site-lisp/

chmod 644 src/data/installer/credits_*.html

%if %{with_fcitx}
%find_lang fcitx-mozc %no_lang_C
%endif

%files
%defattr(-, root, root)
%doc src/data/installer/credits_en.html
%doc README.SUSE
%dir %{_libdir}/mozc
%{_libdir}/mozc/mozc_server
%{_bindir}/mozc_emacs_helper
%dir %{_datadir}/emacs/site-lisp/
%{_datadir}/emacs/site-lisp/mozc.el

%files gui-tools
%defattr(-, root, root)
%{_libdir}/mozc/mozc_tool

%files -n ibus-mozc
%defattr(-, root, root)
%dir %{_libdir}/ibus-mozc/
%{_libdir}/ibus-mozc/ibus-engine-mozc
%{_datadir}/applications/ibus-setup-mozc-jp.desktop
%{_datadir}/applications/ibus-setup-mozc-jp-jp.desktop
%{_datadir}/applications/ibus-setup-mozc-us.desktop
%{_datadir}/applications/ibus-setup-mozc-dv.desktop
%dir %{_datadir}/ibus/component/
%{_datadir}/ibus/component/mozc.xml
%dir %{_datadir}/ibus-mozc/
%{_datadir}/ibus-mozc/product_icon.png
%{_datadir}/ibus-mozc/tool.png
%{_datadir}/ibus-mozc/properties.png
%{_datadir}/ibus-mozc/dictionary.png
%{_datadir}/ibus-mozc/direct.png
%{_datadir}/ibus-mozc/hiragana.png
%{_datadir}/ibus-mozc/katakana_half.png
%{_datadir}/ibus-mozc/katakana_full.png
%{_datadir}/ibus-mozc/alpha_half.png
%{_datadir}/ibus-mozc/alpha_full.png

%files -n ibus-mozc-candidate-window
%defattr(-, root, root)
%{_libdir}/mozc/mozc_renderer

%if %{with_fcitx}
%files -n fcitx-mozc -f fcitx-mozc.lang
%defattr(-,root,root)

%{fcitx_lib_dir}/fcitx-mozc.so
%{fcitx_addon_dir}/fcitx-mozc.conf
%dir %{fcitx_inputmethod_dir}
%{fcitx_inputmethod_dir}/mozc.conf
%dir %{_datadir}/fcitx/mozc
%dir %{fcitx_icon_dir}
%{fcitx_icon_dir}/mozc.png
%{fcitx_icon_dir}/mozc-alpha_full.png
%{fcitx_icon_dir}/mozc-alpha_half.png
%{fcitx_icon_dir}/mozc-direct.png
%{fcitx_icon_dir}/mozc-hiragana.png
%{fcitx_icon_dir}/mozc-katakana_full.png
%{fcitx_icon_dir}/mozc-katakana_half.png
%{fcitx_icon_dir}/mozc-dictionary.png
%{fcitx_icon_dir}/mozc-properties.png
%{fcitx_icon_dir}/mozc-tool.png
%endif

%changelog
