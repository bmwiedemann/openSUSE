#
# spec file for package mozc
#
# Copyright (c) 2025 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%if 0%{?is_opensuse}
%if "%flavor" == "fcitx"
%define with_fcitx4 1
%define with_fcitx5 0
%define install_mozc 0
%else
%define with_fcitx4 0
%define with_fcitx5 1
%define install_mozc 1
%endif
%endif

%if !0%{?is_opensuse}
%if "%flavor" == "fcitx"
ExclusiveArch:  do_not_build
%else
%define with_fcitx4 0
%define with_fcitx5 0
%define install_mozc 1
%endif
%endif

%if %{with_fcitx4}
%define fcitx_icon_dir %{_datadir}/fcitx/mozc/icon/
%define fcitx_addon_dir %{_datadir}/fcitx/addon/
%define fcitx_inputmethod_dir %{_datadir}/fcitx/inputmethod/
%define fcitx_lib_dir %{_libdir}/fcitx/
%endif

%if %{with_fcitx5}
%define fcitx5_addon_dir %{_datadir}/fcitx5/addon/
%define fcitx5_inputmethod_dir %{_datadir}/fcitx5/inputmethod/
%define fcitx5_lib_dir %{_libdir}/fcitx5/
%endif

%define server_dir %{_libdir}/mozc
%define ibus_mozc_path %{_libdir}/ibus-mozc/ibus-engine-mozc
%define ibus_mozc_icon_path %{_datadir}/ibus-mozc/mozc.png
%define document_dir %{_docdir}/ibus-mozc

Name:           mozc
Version:        2.31.5810.102
Release:        0
Summary:        Mozc - Japanese Input Method for Chromium OS, Mac and Linux
License:        Apache-2.0 AND BSD-3-Clause AND SUSE-Public-Domain AND Zlib
Group:          System/I18n/Japanese
ExcludeArch:    ppc ppc64 s390 s390x %{ix86}
%if %{with_fcitx4} && 0%{?suse_version} == 1600 && 0%{?is_opensuse}
ExclusiveArch:  donotbuild
%endif
URL:            https://github.com/google/mozc
Source0:        %{name}-%{version}.tar.xz
Source1:        README.SUSE
# See dependencies.tar/sbom.json for license information
# License: Apache-2.0 AND BSD-3-Clause AND Zlib AND SUSE-Public-Domain
Source2:        dependencies.tar
# A Subset of Bazel Central Registry
# License: Apache-2.0
Source3:        bcr.tar.xz
Source4:        ibus-setup-mozc-jp.desktop.in
#
#
# add fcitx as mozc module
# License: BSD-3-Clause
# https://github.com/fcitx/mozc/tree/fcitx/src/unix/fcitx{,5}
# Run ./make_archive.sh to make tar.xz
%if %{with_fcitx4} || %{with_fcitx5}
Source20:       fcitx-mozc-cf70daeb.tar.xz
Source21:       fcitx-mozc-icons.tar.gz
Patch20:        fcitx-mozc-bazel-build.patch
%endif

# PATCH-FEATURE-OPENSUSE ftake@geeko.jp
Patch1:         ibus-provide-layout-variations.patch
# PATCH-FEATURE-OPENSUSE ftake@geeko.jp -- Use system python while building
Patch2:         use-system-python.patch
# PATCH-FEATURE-OPENSUSE ftake@geeko.jp -- Use system python while building (for Leap 15)
Patch3:         use-system-python-3.12.patch

BuildRequires:  bazel8
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
BuildRequires:  python312
%endif
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
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
Requires:       ibus-mozc = %{version}
Provides:       locale(ibus:ja)

%description -n ibus-mozc-candidate-window
This package provides an advanced candidate window for IBus. The
window shows examples of selected words.

%if %{with_fcitx4}
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

%if %{with_fcitx5}
%package -n fcitx5-mozc
Summary:        The Mozc backend for Fcitx 5
Group:          System/I18n/Japanese
BuildRequires:  fcitx5-devel
Requires:       fcitx5
Requires:       mozc = %{version}
Requires:       mozc-gui-tools = %{version}
Provides:       locale(fcitx5:ja)

%description -n fcitx5-mozc
The Mozc backend for Fcitx 5 provides a Japanese input method.
%endif

%package gui-tools
Summary:        GUI tools for mozc
Group:          System/I18n/Japanese
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
Requires:       mozc = %{version}

%description gui-tools
This package provides config, word-register, dictioaly,
character-palette tools.

%prep
%setup -q

# extract fcitx-mozc
%if %{with_fcitx4} || %{with_fcitx5}
tar xvf %{SOURCE20}
%patch -P 20 -p1
%endif

%patch -P 1 -p1

cp %{SOURCE1} .

%if 0%{?suse_version} == 1500
%patch -P 3 -p1
%else
%patch -P 2 -p1
%endif

# extract dependencies
tar xf %{SOURCE2}
tar xf %{SOURCE3}

# fix installation, library and header path
sed -e 's|@libdir@|%{_libdir}|g' %{SOURCE4} > ibus-setup-mozc-jp.desktop

sed -i -e 's|^\(LINUX_MOZC_DOCUMENT_DIR = \).*|\1 "%{_docdir}/%{name}"|' src/config.bzl
sed -i -e 's|^\(LINUX_MOZC_SERVER_DIR = \).*|\1 "%{_libdir}/mozc"|' src/config.bzl
sed -i -e 's|^\(IBUS_MOZC_PATH = \).*|\1 "%{_libdir}/ibus-mozc/ibus-engine-mozc"|' src/config.bzl
sed -i -e 's|^\(IBUS_MOZC_ICON_PATH = \).*|\1 "%{ibus_mozc_icon_path}"|' src/config.bzl

# set compile options from distribution
for f in %{optflags}; do
	case $f in
		*FORTIFY_SOURCE*) ;; # conflicts with opts (-DFORTIFY_SOURCE and -Werror) from source
		*) echo build --copt=$f >> src/.bazelrc
	esac
done

# The version of buil-in bazel module is different for each minor bazel versions
# Use build-in bazel modules from Bazel 8.4
# https://github.com/bazelbuild/bazel/blob/release-8.4.1/src/MODULE.tools
echo 'bazel_dep(name = "rules_java", version = "8.14.0")' >> src/MODULE.bazel
echo 'bazel_dep(name = "zlib", version = "1.3.1.bcr.5")' >> src/MODULE.bazel

%build

cd src

%if 0%{?suse_version} == 1500
export CC=gcc-10
export CXX=g++-10
%endif

# Be careful bazel cache is not cleared by `obs build`
# --output_base might help

bazel build package \
%if %{with_fcitx4}
	"//unix/fcitx:fcitx-mozc.so" \
%endif
%if %{with_fcitx5}
	"//unix/fcitx5:fcitx5-mozc.so" \
%endif
	--repository_cache=../dependencies \
	--registry=file:$(realpath ../bcr) \
	--config oss_linux \
	-c opt \
	--force_pic \
	$(echo %{?_smp_mflags} | sed 's/-j/--jobs /') \
	--strip=never \
	--sandbox_debug \
	--verbose_failures \
	-s

bazel shutdown

%define output_dir src/bazel-bin

%if %{with_fcitx4}
cd unix/fcitx
./gen_fcitx_mozc_i18n.sh ../../../%{output_dir}/unix/fcitx/po
%endif
%if %{with_fcitx5}
cd unix/fcitx5
../fcitx/gen_fcitx_mozc_i18n.sh ../../../%{output_dir}/unix/fcitx5/po
%endif

%install

%if %{install_mozc}
install -m755 -d %{buildroot}%{_libdir}/ibus-mozc
install -m755 %{output_dir}/unix/ibus/ibus_mozc %{buildroot}%{_libdir}/ibus-mozc/ibus-engine-mozc
install -m755 -d %{buildroot}%{_datadir}/ibus/component
install -m644 %{output_dir}/unix/ibus/mozc.xml %{buildroot}%{_datadir}/ibus/component/mozc.xml
install -m755 -d %{buildroot}%{_datadir}/ibus-mozc
unzip %{output_dir}/unix/icons.zip -d %{buildroot}%{_datadir}/ibus-mozc/

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
%endif

%if %{with_fcitx4}
# Install Fcitx module
for mofile in %{output_dir}/unix/fcitx/po/*.mo
do
	filename=`basename $mofile`
	lang=${filename/.mo/}
	install -D -m 644 "$mofile" "%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/fcitx-mozc.mo"
done
install -m755 -d %{buildroot}%{fcitx_addon_dir}
install -m755 -d %{buildroot}%{fcitx_inputmethod_dir}
install -m755 -d %{buildroot}%{fcitx_icon_dir}
install -m755 -d %{buildroot}%{fcitx_lib_dir}
install -m 755 %{output_dir}/unix/fcitx/fcitx-mozc.so %{buildroot}%{fcitx_lib_dir}/fcitx-mozc.so
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

%if %{with_fcitx5}
# Install Fcitx5 module
for mofile in %{output_dir}/unix/fcitx5/po/*.mo
do
	filename=`basename $mofile`
	lang=${filename/.mo/}
	install -D -m 644 "$mofile" "%{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/fcitx5-mozc.mo"
done
install -m755 -d %{buildroot}%{fcitx5_addon_dir}
install -m755 -d %{buildroot}%{fcitx5_inputmethod_dir}
install -m755 -d %{buildroot}%{fcitx5_lib_dir}
install -m 755 %{output_dir}/unix/fcitx5/fcitx5-mozc.so %{buildroot}%{fcitx5_lib_dir}/fcitx5-mozc.so
install -m 644 src/unix/fcitx5/mozc-addon.conf %{buildroot}%{fcitx5_addon_dir}/mozc.conf
install -m 644 src/unix/fcitx5/mozc.conf %{buildroot}%{fcitx5_inputmethod_dir}

unzip -d icons %{output_dir}/unix/icons.zip
install -D -m 644 src/data/images/product_icon_32bpp-128.png "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/org.fcitx.Fcitx5.fcitx_mozc.png"
install -D -m 644 src/data/images/unix/ime_product_icon_opensource-32.png "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/org.fcitx.Fcitx5.fcitx_mozc.png"
install -D -m 644 icons/mozc.svg "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.fcitx.Fcitx5.fcitx_mozc.svg"
install -D -m 644 icons/alpha_full.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_alpha_full.png"
install -D -m 644 icons/alpha_half.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_alpha_half.png"
install -D -m 644 icons/direct.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_direct.png"
install -D -m 644 icons/hiragana.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_hiragana.png"
install -D -m 644 icons/katakana_full.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_katakana_full.png"
install -D -m 644 icons/katakana_half.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_katakana_half.png"
install -D -m 644 icons/dictionary.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_dictionary.png"
install -D -m 644 icons/properties.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_properties.png"
install -D -m 644 icons/tool.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/org.fcitx.Fcitx5.fcitx_mozc_tool.png"

ln -sf org.fcitx.Fcitx5.fcitx_mozc.png "%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/fcitx_mozc.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc.png "%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/fcitx_mozc.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc.svg "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/fcitx_mozc.svg"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_alpha_full.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_alpha_full.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_alpha_half.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_alpha_half.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_direct.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_direct.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_hiragana.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_hiragana.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_katakana_full.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_katakana_full.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_katakana_half.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_katakana_half.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_dictionary.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_dictionary.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_properties.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_properties.png"
ln -sf org.fcitx.Fcitx5.fcitx_mozc_tool.png "%{buildroot}%{_datadir}/icons/hicolor/48x48/apps/fcitx_mozc_tool.png"
%endif

%if %{install_mozc}
install -m755 -d %{buildroot}%{server_dir}
install -m755 %{output_dir}/server/mozc_server %{buildroot}%{server_dir}
install -m755 %{output_dir}/gui/tool/mozc_tool %{buildroot}%{server_dir}
install -m755 %{output_dir}/renderer/qt/mozc_renderer %{buildroot}%{server_dir}

install -m755 -d %{buildroot}%{_bindir}
install -m755 %{output_dir}/unix/emacs/mozc_emacs_helper %{buildroot}%{_bindir}
# install only for emacs since xemacs is not supported
install -m755 -d %{buildroot}%{_datadir}/emacs/site-lisp
install -m644 src/unix/emacs/mozc.el %{buildroot}%{_datadir}/emacs/site-lisp/

chmod 644 src/data/installer/credits_*.html
%endif

%if %{with_fcitx4}
%find_lang fcitx-mozc %no_lang_C
%endif

%if %{with_fcitx5}
%find_lang fcitx5-mozc %no_lang_C
%endif

%if %{install_mozc}
%files
%defattr(-, root, root)
%doc src/data/installer/credits_en.html
%doc README.SUSE
%dir %{server_dir}
%{server_dir}/mozc_server
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
%{_datadir}/ibus-mozc/

%files -n ibus-mozc-candidate-window
%defattr(-, root, root)
%{_libdir}/mozc/mozc_renderer
%endif

%if %{with_fcitx4}
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

%if %{with_fcitx5}
%files -n fcitx5-mozc -f fcitx5-mozc.lang
%defattr(-,root,root)

%{fcitx5_lib_dir}/fcitx5-mozc.so
%{fcitx5_addon_dir}/mozc.conf
%dir %{fcitx5_inputmethod_dir}
%{fcitx5_inputmethod_dir}/mozc.conf
%{_datadir}/icons/hicolor/
%endif

%changelog
