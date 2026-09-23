#
# spec file for package libreoffice
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


%ifarch %{ix86}
# zstd payload compression OOMs on 32-bit during package creation
# use gzip level 1 (streaming, minimal memory footprint)
%define _binary_payload w1.gzdio
%endif

%{!?aarch64:%global aarch64 aarch64 arm64 armv8}
# Urls
%define external_url https://dev-www.libreoffice.org/src/
%define tarball_url  https://dev-builds.libreoffice.org/pre-releases/src/
# LTO needs newer toolchain stack only
%if 0%{?suse_version} >= 1500
%bcond_without lto
%else
%bcond_with lto
%endif

# When Tumbleweed or SLOF
# Enable QT6 support
%if 0%{?suse_version} >= 1600
%bcond_without qt
%bcond_without qt6
%bcond_with qt5
%else
# When Leap or SLE15-SP4 or newer
# Enable QT5 support
# Disable QT6 support
%if 0%{?is_opensuse} || 0%{?sle_version} >= 150400
%bcond_without qt
%bcond_without qt5
%bcond_with qt6
%else
# Disable QT5/QT6 support
%bcond_with qt
%bcond_with qt5
%bcond_with qt6
%endif
%endif

# When Leap 15.X or SLE15 (any service pack)
# Enable firebird support
%if 0%{?suse_version} >= 1500 && 0%{?suse_version} < 1600
%bcond_without firebird
%else
# Otherwise
# Disable Firebird support
%bcond_with firebird
%endif

# ============================================================================
# External library configuration
#
# Exactly one if/else per library, and it decides everything about that
# library:
#
#   %enable_X    1 = the library is built at all, 0 = --disable-X
#   %bundle_X    1 = build the external tarball, 0 = link the system copy
#   %support_X   the literal configure switch (may be %{nil})
#   %version_X   version download.lst would fetch, whatever %bundle_X says
#
# Everything further down is derived from these: the Source/Provides block
# after the patches keys off %bundle_X, and configure is handed %support_X.
# Do not add a system-vs-bundled decision anywhere else in this file.
#
# LibreOffice only has an --enable-X/--disable-X for a handful of these,
# and spells most of them differently from the library (libeot is
# --disable-eot, rhino is --disable-scripting-javascript, and so on). Where
# no such option exists the library is mandatory: %enable_X is pinned to 1
# and %support_X carries only the system-vs-bundled half. Never invent an
# --enable-X; autoconf accepts unknown ones, warns, and ignores them.
#
# Libraries that are only consumed by another one do not get their own
# distro test; they follow their driver's %bundle_X.
#
# %version_X is the version that goes into Provides: bundled(X). Source:
# lines use it when the tarball name contains it verbatim, and spell the
# name out otherwise.
# ============================================================================

# --- libraries with a real system-vs-bundled choice -------------------------

# ---- abseil (header-only; LibreOffice carries an internal copy, there is no tarball)
%global enable_abseil            1
%if 0%{?suse_version} < 1600
%global bundle_abseil            1
%global support_abseil           --without-system-abseil
%else
%global bundle_abseil            0
%global support_abseil           --with-system-abseil
%endif
# ---- afdko
%global version_afdko            4.0.3
%global enable_afdko             1
%global bundle_afdko             1
%global support_afdko            --without-system-afdko
# ---- argon2
%global version_argon2           20190702
%global enable_argon2            1
%if 0%{?suse_version} < 1500
%global bundle_argon2            1
%global support_argon2           --without-system-argon2
%else
%global bundle_argon2            0
%global support_argon2           --with-system-argon2
%endif
# ---- beanshell
%global enable_beanshell         1
%global bundle_beanshell         0
%global support_beanshell        --enable-scripting-beanshell --with-system-beanshell
# ---- boost
%global version_boost            1.89.0
%global enable_boost             1
%if 0%{?suse_version} < 1550
%global bundle_boost             1
%global support_boost            --without-system-boost
%else
%global bundle_boost             0
%global support_boost            --with-system-boost
%endif
# ---- box2d
%global enable_box2d             1
%global bundle_box2d             0
%global support_box2d            --with-system-box2d
# ---- cairo
%global enable_cairo             1
%global bundle_cairo             0
%global support_cairo            --with-system-cairo
# ---- clucene
%global enable_clucene           1
%global bundle_clucene           0
%global support_clucene          --with-system-clucene
# ---- cppunit
%global enable_cppunit           1
%global bundle_cppunit           0
%global support_cppunit          --with-system-cppunit
# ---- curl
%global version_curl             8.14.1
%global enable_curl              1
%if 0%{?suse_version} <= 1500
%global bundle_curl              1
%global support_curl             --without-system-curl
%else
%global bundle_curl              0
%global support_curl             --with-system-curl
%endif
# ---- dragonbox
%global enable_dragonbox         1
%global bundle_dragonbox         0
%global support_dragonbox        --with-system-dragonbox
# ---- epoxy
%global enable_epoxy             1
%global bundle_epoxy             0
%global support_epoxy            --with-system-epoxy
# ---- expat
%global enable_expat             1
%global bundle_expat             0
%global support_expat            --with-system-expat
# ---- fast_float
%global version_fast_float       8.2.10
%global enable_fast_float        1
%global bundle_fast_float        0
%global support_fast_float       --with-system-fast-float
# ---- fontconfig
%global version_fontconfig       2.17.1
%global enable_fontconfig        1
%if 0%{?suse_version} < 1500
%global bundle_fontconfig        1
%global support_fontconfig       --without-system-fontconfig
%else
%global bundle_fontconfig        0
%global support_fontconfig       --with-system-fontconfig
%endif
# ---- freetype
%global version_freetype         2.13.3
%global enable_freetype          1
%if 0%{?suse_version} < 1500
%global bundle_freetype          1
%global support_freetype         --without-system-freetype
%else
%global bundle_freetype          0
%global support_freetype         --with-system-freetype
%endif
# ---- frozen
%global version_frozen           1.2.0
%global enable_frozen            1
%global bundle_frozen            0
%global support_frozen           --with-system-frozen
# ---- glm
%global enable_glm               1
%global bundle_glm               0
%global support_glm              --with-system-glm
# ---- gpgme
%global version_gpgme            1.24.3
%global enable_gpgme             1
%if 0%{?suse_version} <= 1500
%global bundle_gpgme             1
%global support_gpgme            --enable-gpgmepp --without-system-gpgmepp
%else
%global bundle_gpgme             0
%global support_gpgme            --enable-gpgmepp --with-system-gpgmepp
%endif
# ---- harfbuzz
%global version_harfbuzz         11.4.3
%global enable_harfbuzz          1
%if 0%{?suse_version} < 1300
%global bundle_harfbuzz          1
%global support_harfbuzz         --without-system-harfbuzz
%else
%global bundle_harfbuzz          0
%global support_harfbuzz         --with-system-harfbuzz
%endif
# ---- graphite (graphite2 is only consumed by harfbuzz; it follows it)
%global version_graphite         1.3.14
%global enable_graphite          1
%if %{bundle_harfbuzz}
%global bundle_graphite          1
%global support_graphite         --without-system-graphite
%else
%global bundle_graphite          0
%global support_graphite         --with-system-graphite
%endif
# ---- hsqldb (the system version does not work with LibreOffice)
%global version_hsqldb           1.8.0
%global enable_hsqldb            1
%global bundle_hsqldb            1
%global support_hsqldb           --without-system-hsqldb
# ---- hunspell
%global enable_hunspell          1
%global bundle_hunspell          0
%global support_hunspell         --with-system-hunspell
# ---- icu
%global version_icu              77.1
%global enable_icu               1
%if 0%{?suse_version} < 1500
%global bundle_icu               1
%global support_icu              --without-system-icu
%else
%global bundle_icu               0
%global support_icu              --with-system-icu
%endif
# ---- java_websocket
%global version_java_websocket   1.6.0
%global enable_java_websocket    1
%global bundle_java_websocket    1
%global support_java_websocket   --without-system-java-websocket
# ---- jfreereport (eleven separate zips, see the derived Source block; bsc#1195634)
%global enable_jfreereport       1
%global bundle_jfreereport       1
%global support_jfreereport      --enable-report-builder --without-system-jfreereport
# ---- lcms2
%global enable_lcms2             1
%global bundle_lcms2             0
%global support_lcms2            --with-system-lcms2
# ---- libabw
%global enable_libabw            1
%global bundle_libabw            0
%global support_libabw           --with-system-libabw
# ---- libcdr
%global enable_libcdr            1
%global bundle_libcdr            0
%global support_libcdr           --with-system-libcdr
# ---- libcmis
%global version_libcmis          0.6.2
%global enable_libcmis           1
%if 0%{?suse_version} < 1550
%global bundle_libcmis           1
%global support_libcmis          --without-system-libcmis
%else
%global bundle_libcmis           0
%global support_libcmis          --with-system-libcmis
%endif
# ---- libebook
%global enable_libebook          1
%global bundle_libebook          0
%global support_libebook         --with-system-libebook
# ---- libeot
%global enable_libeot            1
%global bundle_libeot            0
%global support_libeot           --enable-eot --with-system-libeot
# ---- libepubgen
%global enable_libepubgen        1
%global bundle_libepubgen        0
%global support_libepubgen       --with-system-libepubgen
# ---- libetonyek
%global enable_libetonyek        1
%global bundle_libetonyek        0
%global support_libetonyek       --with-system-libetonyek
# ---- libexttextcat
%global enable_libexttextcat     1
%global bundle_libexttextcat     0
%global support_libexttextcat    --with-system-libexttextcat
# ---- libfixmath (no tarball in download.lst)
%global enable_libfixmath        1
%global bundle_libfixmath        0
%global support_libfixmath       --with-system-libfixmath
# ---- libfreehand
%global enable_libfreehand       1
%global bundle_libfreehand       0
%global support_libfreehand      --with-system-libfreehand
# ---- libjpeg (libjpeg-turbo)
%global enable_libjpeg           1
%global bundle_libjpeg           0
%global support_libjpeg          --with-system-jpeg
# ---- liblangtag
%global enable_liblangtag        1
%global bundle_liblangtag        0
%global support_liblangtag       --with-system-liblangtag
# ---- libnumbertext
%global enable_libnumbertext     1
%global bundle_libnumbertext     0
%global support_libnumbertext    --with-system-libnumbertext
# ---- libpng
%global enable_libpng            1
%global bundle_libpng            0
%global support_libpng           --with-system-libpng
# ---- libtiff
%global version_libtiff          4.7.0
%global enable_libtiff           1
%if 0%{?suse_version} < 1550
%global bundle_libtiff           1
%global support_libtiff          --without-system-libtiff
%else
%global bundle_libtiff           0
%global support_libtiff          --with-system-libtiff
%endif
# ---- libwebp
%global enable_libwebp           1
%global bundle_libwebp           0
%global support_libwebp          --with-system-libwebp
# ---- libxml (covers libxml2 and libxslt)
%global enable_libxml            1
%global bundle_libxml            0
%global support_libxml           --with-system-libxml
# ---- libzmf
%global enable_libzmf            1
%global bundle_libzmf            0
%global support_libzmf           --with-system-libzmf
# ---- lpsolve
%global enable_lpsolve           1
%global bundle_lpsolve           0
%global support_lpsolve          --enable-lpsolve --with-system-lpsolve
# ---- lzma (xz)
%global version_lzma             5.8.3
%global enable_lzma              1
%global bundle_lzma              0
%global support_lzma             --with-system-lzma
# ---- mariadb
%global enable_mariadb           1
%global bundle_mariadb           0
%global support_mariadb          --enable-mariadb-sdbc --with-system-mariadb
# ---- md4c
%global version_md4c             0.5.3
%global enable_md4c              1
%global bundle_md4c              0
%global support_md4c             --with-system-md4c
# ---- mdds
%global version_mdds             3.2.1
%global enable_mdds              1
%global bundle_mdds              0
%global support_mdds             --with-system-mdds
# ---- mspub
%global enable_mspub             1
%global bundle_mspub             0
%global support_mspub            --with-system-libmspub
# ---- mwaw
%global enable_mwaw              1
%global bundle_mwaw              0
%global support_mwaw             --with-system-libmwaw
# ---- mythes
%global enable_mythes            1
%global bundle_mythes            0
%global support_mythes           --with-system-mythes
# ---- nss
%global enable_nss               1
%global bundle_nss               0
%global support_nss              --enable-nss --with-system-nss
# ---- odfgen
%global enable_odfgen            1
%global bundle_odfgen            0
%global support_odfgen           --with-system-libodfgen
# ---- openjpeg (no tarball in download.lst; --without-system-openjpeg means no openjpeg at all)
%global enable_openjpeg          1
%if 0%{?suse_version} < 1500
%global bundle_openjpeg          1
%global support_openjpeg         --without-system-openjpeg
%else
%global bundle_openjpeg          0
%global support_openjpeg         --with-system-openjpeg
%endif
# ---- openldap
%global enable_openldap          1
%global bundle_openldap          0
%global support_openldap         --enable-ldap --with-system-openldap
# ---- openssl (curl >= 8.20 needs OpenSSL >= 3.0, which SLE-15 does not ship by default)
%global version_openssl          3.5.7
%global enable_openssl           1
%global bundle_openssl           0
%global support_openssl          --enable-openssl --with-system-openssl
# ---- orcus
%global version_orcus            0.21.0
%global enable_orcus             1
%global bundle_orcus             0
%global support_orcus            --with-system-orcus
# ---- pagemaker
%global enable_pagemaker         1
%global bundle_pagemaker         0
%global support_pagemaker        --with-system-libpagemaker
# ---- poppler
%global version_poppler          25.09.0
%global enable_poppler           1
%if 0%{?suse_version} < 1550
%global bundle_poppler           1
%global support_poppler          --enable-poppler --without-system-poppler
%else
%global bundle_poppler           0
%global support_poppler          --enable-poppler --with-system-poppler
%endif
# ---- postgresql
%global enable_postgresql        1
%global bundle_postgresql        0
%global support_postgresql       --enable-postgresql-sdbc --with-system-postgresql
# ---- qxp
%global enable_qxp               1
%global bundle_qxp               0
%global support_qxp              --with-system-libqxp
# ---- redland (covers raptor2 and rasqal)
%global enable_redland           1
%global bundle_redland           0
%global support_redland          --with-system-redland
# ---- revenge
%global enable_revenge           1
%global bundle_revenge           0
%global support_revenge          --with-system-librevenge
# ---- rhino
%global enable_rhino             1
%global bundle_rhino             0
%global support_rhino            --enable-scripting-javascript --with-system-rhino
# ---- sqlite3
%global version_sqlite3          3.53.4
%global enable_sqlite3           1
%global bundle_sqlite3           0
%global support_sqlite3          --with-system-sqlite3
# ---- staroffice
%global enable_staroffice        1
%global bundle_staroffice        0
%global support_staroffice       --with-system-libstaroffice
# ---- visio
%global enable_visio             1
%global bundle_visio             0
%global support_visio            --with-system-libvisio
# ---- wpd
%global enable_wpd               1
%global bundle_wpd               0
%global support_wpd              --with-system-libwpd
# ---- wpg
%global enable_wpg               1
%global bundle_wpg               0
%global support_wpg              --with-system-libwpg
# ---- wps
%global enable_wps               1
%global bundle_wps               0
%global support_wps              --with-system-libwps
# ---- xmlsec (SLE stages xmlsec1-1.3.12.tar.gz but builds against system xmlsec1-nss)
%global version_xmlsec           1.3.12
%global enable_xmlsec            1
%global bundle_xmlsec            0
%global support_xmlsec           --with-system-xmlsec
# ---- zlib
%global enable_zlib              1
%global bundle_zlib              0
%global support_zlib             --with-system-zlib
# ---- zstd
%global enable_zstd              1
%global bundle_zstd              0
%global support_zstd             --with-system-zstd
# ---- zxcvbn
%global enable_zxcvbn            1
%global bundle_zxcvbn            0
%global support_zxcvbn           --with-system-zxcvbn
# ---- zxing
%global enable_zxing             1
%global bundle_zxing             0
%global support_zxing            --enable-zxing --with-system-zxing

# --- python: the switch is --enable-python, not --with-system-python --------

# ---- python
%global version_python           3.13.15
%global enable_python            1
%global bundle_python            0
%global support_python           --enable-python=system

# --- always bundled: no --with-system-* option exists ------------------------

# ---- antlr4 (build dependency of afdko)
%global version_antlr4           4.13.2
%global enable_antlr4            1
%if %{bundle_afdko}
%global bundle_antlr4            1
%global support_antlr4           %{nil}
%else
%global bundle_antlr4            0
%global support_antlr4           %{nil}
%endif
# ---- icu_data
%global version_icu_data         77.1
%global enable_icu_data          1
%if %{bundle_icu}
%global bundle_icu_data          1
%global support_icu_data         %{nil}
%else
%global bundle_icu_data          0
%global support_icu_data         %{nil}
%endif
# ---- libassuan
%global version_libassuan        3.0.2
%global enable_libassuan         1
%if %{bundle_gpgme}
%global bundle_libassuan         1
%global support_libassuan        %{nil}
%else
%global bundle_libassuan         0
%global support_libassuan        %{nil}
%endif
# ---- libgpgerror
%global version_libgpgerror      1.55
%global enable_libgpgerror       1
%if %{bundle_gpgme}
%global bundle_libgpgerror       1
%global support_libgpgerror      %{nil}
%else
%global bundle_libgpgerror       0
%global support_libgpgerror      %{nil}
%endif
# ---- libffi (only needed by the internal Python)
%global version_libffi           3.5.2
%global enable_libffi            1
%if %{bundle_python}
%global bundle_libffi            1
%global support_libffi           %{nil}
%else
%global bundle_libffi            0
%global support_libffi           %{nil}
%endif
# ---- lxml (only needed by the internal Python)
%global version_lxml             6.1.1
%global enable_lxml              1
%if %{bundle_python}
%global bundle_lxml              1
%global support_lxml             %{nil}
%else
%global bundle_lxml              0
%global support_lxml             %{nil}
%endif
# ---- meson (build tool for the bundled harfbuzz / fontconfig / freetype)
%global version_meson            1.8.0
%global enable_meson             1
%if %{bundle_harfbuzz} || %{bundle_fontconfig} || %{bundle_freetype}
%global bundle_meson             1
%global support_meson            %{nil}
%else
%global bundle_meson             0
%global support_meson            %{nil}
%endif
# ---- odfvalidator (integration tests; inert while --without-export-validation is passed)
%global version_odfvalidator     0.9.0
%global enable_odfvalidator      1
%global bundle_odfvalidator      1
%global support_odfvalidator     %{nil}
# ---- officeotron (integration tests; inert while --without-export-validation is passed)
%global version_officeotron      0.7.4
%global enable_officeotron       1
%global bundle_officeotron       1
%global support_officeotron      %{nil}
# ---- pdfium (bundled everywhere)
%global version_pdfium           7681
%ifarch %{aarch64}
%if 0%{?suse_version} < 1550
%global enable_pdfium            0
%global support_pdfium           --disable-pdfium
%else
%global enable_pdfium            1
%global support_pdfium           --enable-pdfium
%endif
%else
%global enable_pdfium            1
%global support_pdfium           --enable-pdfium
%endif
%global bundle_pdfium            1
# ---- poppler_data
%global version_poppler_data     0.4.12
%global enable_poppler_data      1
%if %{bundle_poppler}
%global bundle_poppler_data      1
%global support_poppler_data     %{nil}
%else
%global bundle_poppler_data      0
%global support_poppler_data     %{nil}
%endif
# ---- skia (part of chromium; upstream ships it monorepo-style only)
%global version_skia             m147
%ifnarch s390x ppc64 ppc %{ix86}
%global enable_skia              1
%global support_skia             --enable-skia
%else
%global enable_skia              0
%global support_skia             --disable-skia
%endif
%global bundle_skia              1
# ---- xsltml (needed by wiki-publisher)
%global version_xsltml           2.1.2
%global enable_xsltml            1
%global bundle_xsltml            1
%global support_xsltml           %{nil}

# --- in download.lst but not reachable in this build -------------------------

# ---- breakpad: crash reporting is not enabled
%global enable_breakpad          0
%global bundle_breakpad          0
%global support_breakpad         --disable-breakpad
# ---- bzip2: only used by --enable-online-update-mar or the internal Python, and both take the system copy via --with-system-libs
%global enable_bzip2             0
%global bundle_bzip2             0
%global support_bzip2            %{nil}
# ---- coinmp: no coinmp packages to build against
%global enable_coinmp            0
%global bundle_coinmp            0
%global support_coinmp           --disable-coinmp
# ---- epm: LibreOffice's own packaging code, superfluous under rpmbuild
%global enable_epm               0
%global bundle_epm               0
%global support_epm              --disable-epm
# ---- firebird: follows the firebird bcond at the top of this file
%if %{with firebird}
%global enable_firebird          1
%global support_firebird         --enable-firebird-sdbc
%else
%global enable_firebird          0
%global support_firebird         --disable-firebird-sdbc
%endif
%global bundle_firebird          0
# ---- hyphen: --with-system-dicts plus --with-external-hyph-dir
%global enable_hyphen            0
%global bundle_hyphen            0
%global support_hyphen           %{nil}
# ---- iaccessible2: Windows only
%global enable_iaccessible2      0
%global bundle_iaccessible2      0
%global support_iaccessible2     %{nil}
# ---- langtagreg: only used with a bundled liblangtag
%global enable_langtagreg        0
%global bundle_langtagreg        0
%global support_langtagreg       %{nil}
# ---- libatomic_ops: only used by the internal firebird on non-Intel
%global enable_libatomic_ops     0
%global bundle_libatomic_ops     0
%global support_libatomic_ops    %{nil}
# ---- libtommath: only used by the internal firebird
%global enable_libtommath        0
%global bundle_libtommath        0
%global support_libtommath       %{nil}
# ---- mdnsresponder: Windows only
%global enable_mdnsresponder     0
%global bundle_mdnsresponder     0
%global support_mdnsresponder    %{nil}
# ---- onlineupdate: the distribution updates LibreOffice, not LibreOffice itself
%global enable_onlineupdate      0
%global bundle_onlineupdate      0
%global support_onlineupdate     --disable-online-update
# ---- pixman: only used with a bundled cairo
%global enable_pixman            0
%global bundle_pixman            0
%global support_pixman           %{nil}
# ---- python_bootstrap: Windows only
%global enable_python_bootstrap  0
%global bundle_python_bootstrap  0
%global support_python_bootstrap %{nil}
# ---- quickjs: experimental QuickJS scripting (LO 26.8 download.lst only)
%global enable_quickjs           0
%global bundle_quickjs           0
%global support_quickjs          --disable-quickjs
# ---- raptor: only used with a bundled redland
%global enable_raptor            0
%global bundle_raptor            0
%global support_raptor           %{nil}
# ---- rasqal: only used with a bundled redland
%global enable_rasqal            0
%global bundle_rasqal            0
%global support_rasqal           %{nil}
# ---- twain_dsm: Windows only
%global enable_twain_dsm         0
%global bundle_twain_dsm         0
%global support_twain_dsm        %{nil}
# ---- verapdf: --without-export-validation (LO 26.8 download.lst only)
%global enable_verapdf           0
%global bundle_verapdf           0
%global support_verapdf          %{nil}
# ---- yrs: --with-yrs is not passed
%global enable_yrs               0
%global bundle_yrs               0
%global support_yrs              %{nil}

# ---- fonts: --without-fonts, we use the distribution font packages
%global enable_font_agdasima     0
%global bundle_font_agdasima     0
%global support_font_agdasima    %{nil}
%global enable_font_alef         0
%global bundle_font_alef         0
%global support_font_alef        %{nil}
%global enable_font_amiri        0
%global bundle_font_amiri        0
%global support_font_amiri       %{nil}
%global enable_font_bacasime_antique 0
%global bundle_font_bacasime_antique 0
%global support_font_bacasime_antique %{nil}
%global enable_font_belanosima   0
%global bundle_font_belanosima   0
%global support_font_belanosima  %{nil}
%global enable_font_caladea      0
%global bundle_font_caladea      0
%global support_font_caladea     %{nil}
%global enable_font_caprasimo    0
%global bundle_font_caprasimo    0
%global support_font_caprasimo   %{nil}
%global enable_font_carlito      0
%global bundle_font_carlito      0
%global support_font_carlito     %{nil}
%global enable_font_culmus       0
%global bundle_font_culmus       0
%global support_font_culmus      %{nil}
%global enable_font_dejavu       0
%global bundle_font_dejavu       0
%global support_font_dejavu      %{nil}
%global enable_font_gentium      0
%global bundle_font_gentium      0
%global support_font_gentium     %{nil}
%global enable_font_liberation   0
%global bundle_font_liberation   0
%global support_font_liberation  %{nil}
%global enable_font_liberation_narrow 0
%global bundle_font_liberation_narrow 0
%global support_font_liberation_narrow %{nil}
%global enable_font_libre_hebrew 0
%global bundle_font_libre_hebrew 0
%global support_font_libre_hebrew %{nil}
%global enable_font_linlibertineg 0
%global bundle_font_linlibertineg 0
%global support_font_linlibertineg %{nil}
%global enable_font_lugrasimo    0
%global bundle_font_lugrasimo    0
%global support_font_lugrasimo   %{nil}
%global enable_font_lumanosimo   0
%global bundle_font_lumanosimo   0
%global support_font_lumanosimo  %{nil}
%global enable_font_lunasima     0
%global bundle_font_lunasima     0
%global support_font_lunasima    %{nil}
%global enable_font_noto_kufi_arabic 0
%global bundle_font_noto_kufi_arabic 0
%global support_font_noto_kufi_arabic %{nil}
%global enable_font_noto_naskh_arabic 0
%global bundle_font_noto_naskh_arabic 0
%global support_font_noto_naskh_arabic %{nil}
%global enable_font_noto_sans    0
%global bundle_font_noto_sans    0
%global support_font_noto_sans   %{nil}
%global enable_font_noto_sans_arabic 0
%global bundle_font_noto_sans_arabic 0
%global support_font_noto_sans_arabic %{nil}
%global enable_font_noto_sans_armenian 0
%global bundle_font_noto_sans_armenian 0
%global support_font_noto_sans_armenian %{nil}
%global enable_font_noto_sans_georgian 0
%global bundle_font_noto_sans_georgian 0
%global support_font_noto_sans_georgian %{nil}
%global enable_font_noto_sans_hebrew 0
%global bundle_font_noto_sans_hebrew 0
%global support_font_noto_sans_hebrew %{nil}
%global enable_font_noto_sans_lao 0
%global bundle_font_noto_sans_lao 0
%global support_font_noto_sans_lao %{nil}
%global enable_font_noto_sans_lisu 0
%global bundle_font_noto_sans_lisu 0
%global support_font_noto_sans_lisu %{nil}
%global enable_font_noto_serif   0
%global bundle_font_noto_serif   0
%global support_font_noto_serif  %{nil}
%global enable_font_noto_serif_armenian 0
%global bundle_font_noto_serif_armenian 0
%global support_font_noto_serif_armenian %{nil}
%global enable_font_noto_serif_georgian 0
%global bundle_font_noto_serif_georgian 0
%global support_font_noto_serif_georgian %{nil}
%global enable_font_noto_serif_hebrew 0
%global bundle_font_noto_serif_hebrew 0
%global support_font_noto_serif_hebrew %{nil}
%global enable_font_noto_serif_lao 0
%global bundle_font_noto_serif_lao 0
%global support_font_noto_serif_lao %{nil}
%global enable_font_reem         0
%global bundle_font_reem         0
%global support_font_reem        %{nil}
%global enable_font_scheherazade 0
%global bundle_font_scheherazade 0
%global support_font_scheherazade %{nil}

%if %{bundle_gpgme}
# Hack in the bundled libs to not pop up on requires/provides to avoid
# faking libreoffice provide some system packages
%global __provides_exclude_from ^%{_libdir}/libreoffice/program/lib(gpg|assuan).*\\.so.*$
%global __requires_exclude_from ^%{_libdir}/libreoffice/program/lib(gpg|assuan).*\\.so.*$
%global __requires_exclude ^libgpgmepp\\.so.*$
%endif
Name:           libreoffice
Version:        26.8.0.3
Release:        0
Summary:        A Free Office Suite (Framework)
License:        LGPL-3.0-or-later AND MPL-2.0+
Group:          Productivity/Office/Suite
URL:            https://www.documentfoundation.org/
Source0:        %{tarball_url}/libreoffice-%{version}.tar.xz
Source1:        %{tarball_url}/libreoffice-%{version}.tar.xz.asc
Source2:        %{tarball_url}/libreoffice-help-%{version}.tar.xz
Source3:        %{tarball_url}/libreoffice-help-%{version}.tar.xz.asc
Source4:        %{tarball_url}/libreoffice-translations-%{version}.tar.xz
Source5:        %{tarball_url}/libreoffice-translations-%{version}.tar.xz.asc
# SUSE color palette in year 2021: bsc#1181122 https://brand.suse.com/brand-system/color-palette
# SUSE color palette bsc#1045339 https://intra.microfocus.net/brandcentral/suse/identity.php#palette
Source6:        SUSE.soc
Source98:       %{name}.keyring
Source99:       %{name}-rpmlintrc
Source100:      %{name}.changes
# change user config dir name from ~/.libreoffice/3 to ~/.libreoffice/3-suse
# to avoid BerkleyDB incompatibility with the plain build
Patch1:         scp2-user-config-suse.diff
# do not use the broken help; unopkg complained about it when registering extensions
# FIXME: the right fix is to compile the help and produce the .db_, .ht_, and other files
Patch2:         nlpsolver-no-broken-help.diff
Patch3:         mediawiki-no-broken-help.diff
Patch4:         python-detection.patch
# PATCH-FIX-OPENSUSE boo#1186110 fix GCC 11 error
Patch6:         gcc11-fix-error.patch
Patch9:         fix_math_desktop_file.patch
Patch10:        fix_gtk_popover_on_3.20.patch
Patch11:        fix_webp_on_sle12_sp5.patch
# PATCH-FIX-SUSE Fix make distro-pack-install
Patch15:        fix-sdk-idl.patch
# PATCH-FIX-UPSTREAM detect system box2d without a pkg-config file
Patch16:        box2d-detection.patch
# PATCH-FIX-UPSTREAM do not crash in the Base wizard when Firebird is not built
Patch17:        dbaccess-no-firebird-default-crash.patch
# try to save space by using hardlinks
Patch990:       install-with-hardlinks.diff
# save time by relying on rpm check rather than doing stupid find+grep
Patch991:       libreoffice-no-destdircheck.patch
# Fix build on sle12
Patch992:       python34-no-f-strings.patch
# PATCH-FIX-OPENSUSE override date in clucene files (boo#1047218)
Patch995:       reproducible-clucene.patch
# Add .key (Apple Keynote) files to Bash completion (tdf#167995)
Patch996:       bash-completion-key.patch
# ============================================================================
# Derived from the external library configuration
#
# Every block here is guarded by a single %bundle_* macro from that region.
# Nothing here may test %suse_version to decide bundled-vs-system; the only
# distro tests left are about how a system package happens to be split up.
#
# Source numbers are historical and carry no meaning beyond uniqueness.
# ============================================================================
%if %{bundle_afdko}
Source403:      %{external_url}/afdko-%{version_afdko}.tar.gz
%endif
%if %{bundle_antlr4}
Source404:      %{external_url}/antlr4-cpp-runtime-%{version_antlr4}-source.zip
%endif
%if %{bundle_hsqldb}
Source2002:     %{external_url}/17410483b5b5f267aa18b7e00b65e6e0-hsqldb_1_8_0.zip
Provides:       bundled(hsqldb) = %{version_hsqldb}
%endif
%if %{bundle_xsltml}
Source2005:     %{external_url}/a7983f859eafb2677d7ff386a023bc40-xsltml_2.1.2.zip
%endif
%if %{bundle_officeotron}
Source2006:     https://dev-www.libreoffice.org/extern/8249374c274932a21846fa7629c2aa9b-officeotron-0.7.4-master.jar
%endif
%if %{bundle_odfvalidator}
Source2007:     https://dev-www.libreoffice.org/extern/odfvalidator-0.9.0-RC2-SNAPSHOT-jar-with-dependencies-2726ab578664434a545f8379a01a9faffac0ae73.jar
%endif
%if %{bundle_pdfium}
Source2008:     %{external_url}/pdfium-%{version_pdfium}.tar.bz2
%endif
%if %{bundle_skia}
Source2010:     %{external_url}/skia-m147-ad8ecedbfdef9f4ae4b1e73347b6dd56e6637d38.tar.xz
%endif
%if %{bundle_jfreereport}
Source2101:     %{external_url}/eeb2c7ddf0d302fba4bfc6e97eac9624-libbase-1.1.6.zip
Source2102:     %{external_url}/d8bd5eed178db6e2b18eeed243f85aa8-flute-1.1.6.zip
Source2103:     %{external_url}/97b2d4dba862397f446b217e2b623e71-libloader-1.1.6.zip
Source2104:     %{external_url}/ace6ab49184e329db254e454a010f56d-libxml-1.1.7.zip
Source2105:     %{external_url}/3404ab6b1792ae5f16bbd603bd1e1d03-libformula-1.1.7.zip
Source2106:     %{external_url}/3bdf40c0d199af31923e900d082ca2dd-libfonts-1.1.6.zip
Source2107:     %{external_url}/8ce2fcd72becf06c41f7201d15373ed9-librepository-1.1.6.zip
Source2108:     %{external_url}/f94d9870737518e3b597f9265f4e9803-libserializer-1.1.6.zip
Source2109:     %{external_url}/db60e4fde8dd6d6807523deb71ee34dc-liblayout-0.2.10.zip
Source2110:     %{external_url}/ba2930200c9f019c2d93a8c88c651a0f-flow-engine-0.9.4.zip
Source2111:     %{external_url}/39bb3fcea1514f1369fcfc87542390fd-sacjava-1.3.zip
%endif
%if %{bundle_curl}
Source2013:     %{external_url}/curl-%{version_curl}.tar.xz
Provides:       bundled(curl) = %{version_curl}
%else
BuildRequires:  curl-devel >= 7.68.0
%endif
# curl >= 8.20 requires OpenSSL >= 3.0 and SLE-15 only offers 1.1.1 by
# default, so build the bundled curl against a bundled OpenSSL too
%if %{bundle_boost}
Source2020:     %{external_url}/boost_1_89_0.tar.xz
Provides:       bundled(boost) = %{version_boost}
%else
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_locale-devel
# boost_system stopped being a separate library after 1.69
%if 0%{?suse_version} <= 1550
BuildRequires:  libboost_system-devel
%endif
%endif
%if %{bundle_icu}
Source2021:     %{external_url}/icu4c-77_1-src.tgz
Provides:       bundled(icu) = %{version_icu}
%else
# the genbrk binary is required
BuildRequires:  icu
BuildRequires:  pkgconfig(icu-i18n)
%endif
%if %{bundle_icu_data}
Source2022:     %{external_url}/icu4c-77_1-data.zip
%endif
%if %{bundle_poppler}
Source2023:     %{external_url}/poppler-%{version_poppler}.tar.xz
Provides:       bundled(poppler) = %{version_poppler}
%else
BuildRequires:  pkgconfig(poppler) >= 21.01.0
BuildRequires:  pkgconfig(poppler-cpp)
%endif
%if %{bundle_poppler_data}
Source2024:     %{external_url}/poppler-data-%{version_poppler_data}.tar.gz
Provides:       bundled(poppler-data) = %{version_poppler_data}
%endif
%if %{bundle_harfbuzz}
Source2025:     %{external_url}/harfbuzz-%{version_harfbuzz}.tar.xz
Provides:       bundled(harfbuzz) = %{version_harfbuzz}
%else
BuildRequires:  pkgconfig(harfbuzz) >= 5.1.0
BuildRequires:  pkgconfig(harfbuzz-icu) >= 5.1.0
%endif
%if %{bundle_graphite}
Source2026:     %{external_url}/graphite2-minimal-%{version_graphite}.tgz
Provides:       bundled(graphite2) = %{version_graphite}
%else
BuildRequires:  pkgconfig(graphite2) >= 0.9.3
%endif
%if %{bundle_argon2}
Source2027:     %{external_url}/phc-winner-argon2-%{version_argon2}.tar.gz
%else
BuildRequires:  argon2-devel
%endif
%if %{bundle_fontconfig}
Source2028:     %{external_url}/fontconfig-%{version_fontconfig}.tar.xz
%endif
%if %{bundle_freetype}
Source2029:     %{external_url}/freetype-%{version_freetype}.tar.xz
%endif
%if %{bundle_libtiff}
Source2030:     %{external_url}/tiff-%{version_libtiff}.tar.xz
Provides:       bundled(tiff) = %{version_libtiff}
%else
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.10
%endif
%if %{bundle_libcmis}
Source2031:     %{external_url}/libcmis-%{version_libcmis}.tar.xz
Provides:       bundled(libcmis) = %{version_libcmis}
%else
BuildRequires:  libcmis-devel
%endif
%if %{bundle_meson}
Source2032:     %{external_url}/meson-%{version_meson}.tar.gz
BuildRequires:  meson >= 0.55
BuildRequires:  ninja
%endif
%if %{bundle_gpgme}
Source1000:     %{external_url}/gpgme-%{version_gpgme}.tar.bz2
Provides:       bundled(gpgme) = %{version_gpgme}
%else
BuildRequires:  libgpgmepp-devel >= 1.14
%endif
%if %{bundle_libgpgerror}
Source1001:     %{external_url}/libgpg-error-%{version_libgpgerror}.tar.bz2
Provides:       bundled(libgpg-error) = %{version_libgpgerror}
%endif
%if %{bundle_libassuan}
Source1002:     %{external_url}/libassuan-%{version_libassuan}.tar.bz2
Provides:       bundled(libassuan) = %{version_libassuan}
%endif
%if %{bundle_java_websocket}
Source3000:     %{external_url}/Java-WebSocket-%{version_java_websocket}.tar.gz
%endif
BuildRequires:  fast_float-devel
BuildRequires:  md4c-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(liborcus-0.21) >= 0.21.0
BuildRequires:  pkgconfig(mdds-3.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xmlsec1-nss) >= 1.2.35
%if !%{bundle_openjpeg}
BuildRequires:  pkgconfig(libopenjp2)
%endif
%if !%{bundle_abseil}
BuildRequires:  abseil-cpp-devel
%endif
# ============================================================================
BuildRequires:  %{name}-share-linker
BuildRequires:  ant
BuildRequires:  autoconf
BuildRequires:  awk
BuildRequires:  bison
BuildRequires:  bsh2
BuildRequires:  cups-devel
BuildRequires:  fixmath-devel
BuildRequires:  libwebp-devel
%if 0%{?suse_version} > 1500
BuildRequires:  strip-nondeterminism
%endif
BuildRequires:  zlib-devel
BuildRequires:  zxcvbn-devel
# Needed for tests
BuildRequires:  dejavu-fonts
BuildRequires:  doxygen >= 1.8.4
BuildRequires:  dragonbox-devel
BuildRequires:  fdupes
BuildRequires:  flex >= 2.6.0
BuildRequires:  flute
BuildRequires:  fontforge
BuildRequires:  frozen-devel
BuildRequires:  glm-devel
BuildRequires:  google-carlito-fonts
BuildRequires:  gperf >= 3.1
BuildRequires:  graphviz
BuildRequires:  hyphen-devel
BuildRequires:  junit4
BuildRequires:  libbase
BuildRequires:  libcppunit-devel >= 1.14.0
BuildRequires:  liberation-fonts
BuildRequires:  libexif
BuildRequires:  libfonts
BuildRequires:  libformula
BuildRequires:  libjpeg-devel
BuildRequires:  liblayout
BuildRequires:  libloader
BuildRequires:  librepository
BuildRequires:  libserializer
BuildRequires:  libtool
BuildRequires:  libzstd-devel
BuildRequires:  lpsolve-devel
BuildRequires:  make
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  rhino
BuildRequires:  sac
BuildRequires:  ucpp
BuildRequires:  unixODBC-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xml-commons-apis
BuildRequires:  xz
BuildRequires:  zip
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(atk) >= 2.28
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1) >= 0.60
BuildRequires:  pkgconfig(epoxy) >= 1.2
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gssrpc)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(hunspell)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libabw-0.1)
BuildRequires:  pkgconfig(libcdr-0.1) >= 0.1
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(libe-book-0.1) >= 0.1.2
BuildRequires:  pkgconfig(libeot) >= 0.01
BuildRequires:  pkgconfig(libepubgen-0.1)
BuildRequires:  pkgconfig(libetonyek-0.1) >= 0.1.10
BuildRequires:  pkgconfig(libexttextcat) >= 3.4.1
BuildRequires:  pkgconfig(libfreehand-0.1)
BuildRequires:  pkgconfig(liblangtag)
BuildRequires:  pkgconfig(libmspub-0.1) >= 0.1
BuildRequires:  pkgconfig(libmwaw-0.3) >= 0.3.21
BuildRequires:  pkgconfig(libnumbertext) >= 1.0.6
BuildRequires:  pkgconfig(libodfgen-0.1) >= 0.1.4
BuildRequires:  pkgconfig(libpagemaker-0.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libqxp-0.0)
BuildRequires:  pkgconfig(librevenge-0.0) >= 0.0.1
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstaroffice-0.0) >= 0.0.7
BuildRequires:  pkgconfig(libvisio-0.1) >= 0.1
BuildRequires:  pkgconfig(libwpd-0.10) >= 0.10
BuildRequires:  pkgconfig(libwpg-0.3)
BuildRequires:  pkgconfig(libwps-0.4) >= 0.4.11
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libzmf-0.0)
BuildRequires:  pkgconfig(mythes)
BuildRequires:  pkgconfig(nspr) >= 4.8
BuildRequires:  pkgconfig(nss) >= 3.9.3
BuildRequires:  pkgconfig(redland)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zxing)
Requires:       liberation-fonts
Requires:       libreoffice-branding >= 6.0
Requires:       libreoffice-icon-themes = %{version}
# We need at least english to launch ourselves
Requires:       libreoffice-l10n-en = %{version}
Requires:       python3
Recommends:     dejavu-fonts
Recommends:     google-carlito-fonts
Provides:       %{name}-draw-extensions = %{version}
Obsoletes:      %{name}-draw-extensions < %{version}
Provides:       %{name}-impress-extensions = %{version}
Obsoletes:      %{name}-impress-extensions < %{version}
Provides:       %{name}-base-extensions = %{version}
Obsoletes:      %{name}-base-extensions < %{version}
Provides:       %{name}-kde = %{version}
Obsoletes:      %{name}-kde < %{version}
Provides:       %{name}-l10n-prebuild = %{version}
Obsoletes:      %{name}-l10n-prebuild < %{version}
Provides:       %{name}-mono = %{version}
Obsoletes:      %{name}-mono < %{version}
Provides:       %{name}-ure = %{version}
Obsoletes:      %{name}-ure < %{version}
Provides:       %{name}-icon-theme-crystal = %{version}
Obsoletes:      %{name}-icon-theme-crystal < %{version}
Provides:       %{name}-icon-theme-oxygen = %{version}
Obsoletes:      %{name}-icon-theme-oxygen < %{version}
# Not a bundling decision: these system packages were simply renamed/split.
%if 0%{?suse_version} < 1500
BuildRequires:  libBox2D-devel
BuildRequires:  libmysqlclient-devel
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%else
BuildRequires:  libbox2d-devel
BuildRequires:  libmariadb-devel
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1.8
%if 0%{?suse_version}
# needed by python3_sitelib
BuildRequires:  python-rpm-macros
%endif
%if %{with firebird}
BuildRequires:  pkgconfig(fbclient)
%endif
%if %{with qt5}
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb-icccm)
%else
Provides:       %{name}-kde4 = %{version}
Obsoletes:      %{name}-kde4 < %{version}
Provides:       %{name}-qt5 = %{version}
Obsoletes:      %{name}-qt5 < %{version}
%endif
%if %{with qt6}
BuildRequires:  qt6-base-common-devel
BuildRequires:  qt6-base-devel
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6MultimediaWidgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(xcb-icccm)
%else
Provides:       %{name}-qt6 = %{version}
Obsoletes:      %{name}-qt6 < %{version}
%endif

%description
LibreOffice is a comprehensive office package featuring a word
processor, a spreadsheet, a presentation program, and much more. This
package provides only the basic framework. You have to install the
additional modules to get the required functionality, see packages:

- libreoffice-base
- libreoffice-calc
- libreoffice-draw
- libreoffice-impress
- libreoffice-math
- libreoffice-writer

Some optional features are provided by extra packages, for example:

- libreoffice-mailmerge
- libreoffice-filters
- libreoffice-qt5
- libreoffice-qt6
- libreoffice-gnome

Non-English localizations are provided by extra packages as well, for
example:

- libreoffice-l10n-de
- libreoffice-l10n-fr
- libreoffice-l10n-it

%package branding-upstream
Summary:        Original Branding for LibreOffice
Group:          Productivity/Office/Suite
Supplements:    libreoffice
Conflicts:      libreoffice-branding
Provides:       libreoffice-branding = %{version}
Provides:       libreoffice-branding-openSUSE = 4.0.1
Obsoletes:      libreoffice-branding-openSUSE < 4.0.1
Provides:       libreoffice-branding-SLE = 4.0.1
Obsoletes:      libreoffice-branding-SLE < 4.0.1
%if 0%{suse_version} < 1500
Supplements:    packageand(libreoffice:branding-openSUSE)
%else
Supplements:    (libreoffice and branding-openSUSE)
%endif
BuildArch:      noarch

%description branding-upstream
This package includes the original branding for the LibreOffice office suite.

%package icon-themes
Summary:        LibreOffice Icon Themes
Group:          Productivity/Office/Suite
Requires(post): %{name}-share-linker
Requires(postun): %{name}-share-linker
Supplements:    libreoffice
Provides:       %{name}-icon-theme-breeze = %{version}
Obsoletes:      %{name}-icon-theme-breeze < %{version}
Provides:       %{name}-icon-theme-galaxy = %{version}
Obsoletes:      %{name}-icon-theme-galaxy < %{version}
Provides:       %{name}-icon-theme-hicontrast = %{version}
Obsoletes:      %{name}-icon-theme-hicontrast < %{version}
Provides:       %{name}-icon-theme-sifr = %{version}
Obsoletes:      %{name}-icon-theme-sifr < %{version}
Provides:       %{name}-icon-theme-tango = %{version}
Obsoletes:      %{name}-icon-theme-tango < %{version}
BuildArch:      noarch

%description icon-themes
This package provides all of the LibreOffice icon themes.

%package glade
Summary:        Support for creating LibreOffice dialogs in glade
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
BuildArch:      noarch

%description glade
%{name}-glade contains a catalog of LibreOffice-specific widgets for
glade and ui-previewer tool to check the visual appearance of dialogs.

%package gdb-pretty-printers
Summary:        Additional support for debugging with gdb
Group:          Productivity/Office/Suite
Requires:       gdb
Requires:       libreoffice = %{version}
Requires:       python3-six
Supplements:    libreoffice-debuginfo = %{version}
BuildArch:      noarch

%description gdb-pretty-printers
This package provides gdb pretty printers for package %{name}.

%package base
Summary:        LibreOffice Base
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Supplements:    %{name}
Obsoletes:      %{name}-base-drivers-mysql
# default database connector
%if %{with firebird}
Requires:       %{name}-base-drivers-firebird
%else
Requires:       jre >= 1.8
%endif

%description base
This module allows you to manage databases, create queries and reports
to track and manage your information by using LibreOffice office
suite.

%package calc
Summary:        LibreOffice Calc
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Supplements:    %{name}

%description  calc
This module allows you to perform calculation, analyze information and
manage lists in spreadsheets by using LibreOffice office suite.

%package draw
Summary:        LibreOffice Draw
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
# libreoffice-draw requires libreoffice-impress from 7.5 onwards, bsc#1215595
Requires:       %{name}-impress
Supplements:    %{name}

%description  draw
This module allows you to create and edit drawings, flow charts, and
logos by using LibreOffice office suite.

%package math
Summary:        LibreOffice Math
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Supplements:    %{name}

%description math
This module allows you to create and edit scientific formulas and
equations by using LibreOffice office suite.

%package impress
Summary:        LibreOffice Impress
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Supplements:    %{name}

%description impress
This module allows you to create and edit presentations for slideshows,
meeting and Web pages by using LibreOffice office suite.

%package writer
Summary:        LibreOffice Writer and Web
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Supplements:    %{name}

%description writer
This module allows you to create and edit text and graphics in letters,
reports, documents and Web pages by using LibreOffice office suite.

%package base-drivers-postgresql
Summary:        PostgreSQL Database Driver for LibreOffice
Group:          Productivity/Office/Suite
Requires:       postgresql

%description base-drivers-postgresql
This package allows to access PostgreSQL databases from LibreOffice Base.

%package base-drivers-firebird
Summary:        Firebird Database Driver for LibreOffice
Group:          Productivity/Office/Suite
Requires:       firebird

%description base-drivers-firebird
This package allows to access Firebird databeses from LibreOffice Base.

%package filters-optional
Summary:        Additional Import and Export Filters for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name}-calc = %{version}
Requires:       %{name}-draw = %{version}
Requires:       %{name}-impress = %{version}
Requires:       %{name}-math = %{version}
Requires:       %{name}-writer = %{version}
Supplements:    %{name}

%description filters-optional
This package includes some additional import and export filters for
LibreOffice:
- AportisDoc (Palm)
- Pocket Excel
- Pocket Word
- DocBook
- XHTML

%package mailmerge
Summary:        Mail Merge Functionality for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name}-pyuno = %{version}
Supplements:    %{name}

%description mailmerge
This module allows you to create form letters or send E-mail messages
to many recipients using LibreOffice office suite.

%package pyuno
Summary:        Python UNO Bridge for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Supplements:    %{name}

%description pyuno
The Python-UNO bridge allows to use the standard LibreOffice API
from the well known Python scripting language. It can be used to
develop UNO components in python, thus python UNO components may be run
within the LibreOffice process and can be called from Java, C++ or
the built in StarBasic scripting language. You can create and invoke
scripts with the office scripting framework (OOo 2.0 and later) with
it. For example, it is used for the mail merge functionality.

You can find the more information at
http://udk.openoffice.org/python/python-bridge.html

%package librelogo
Summary:        LibreLogo scripting language
Group:          Productivity/Office/Suite
Requires:       %{name}-pyuno = %{version}
Requires:       %{name}-writer = %{version}

%description librelogo
Enables LibreLogo scripting in Writer. LibreLogo is a Logo-like
programming language with interactive vectorgraphics for education and
DTP.

%package gnome
Summary:        GNOME Extensions for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}

%description gnome
This package contains some GNOME extensions and GTK2 interface for LibreOffice.

%package gtk3
Summary:        Gtk3 interface for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name}-gnome = %{version}
%if 0%{suse_version} < 1500
Supplements:    packageand(libreoffice:gnome-session)
Supplements:    packageand(libreoffice:mate-session-manager)
Supplements:    packageand(libreoffice:xfce4-session)
%if !%{with qt}
Supplements:    packageand(libreoffice:plasma5-workspace)
%endif
%else
Supplements:    (libreoffice and gnome-session)
Supplements:    (libreoffice and mate-session-manager)
Supplements:    (libreoffice and xfce4-session)
%if !%{with qt}
Supplements:    (libreoffice and plasma5-workspace)
%endif
%endif

%description gtk3
This package contains Gtk3 interface rendering option for LibreOffice.

%package qt5
Summary:        Qt5/KDE Frameworks interface for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
%if 0%{suse_version} < 1500
Supplements:    packageand(libreoffice:plasma5-workspace)
%else
Supplements:    (libreoffice and plasma5-workspace)
%endif
Provides:       %{name}-kde4 = %{version}
Obsoletes:      %{name}-kde4 < %{version}

%description qt5
This package contains Qt5/KDE Frameworks interface rendering options for LibreOffice.

%package qt6
Summary:        Qt6/KDE Frameworks interface for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
%if 0%{suse_version} < 1500
Supplements:    packageand(libreoffice:plasma6-workspace)
%else
Supplements:    (libreoffice and plasma6-workspace)
%endif

%description qt6
This package contains Qt6/KDE Frameworks interface rendering options for LibreOffice.

%package kdeintegration
Summary:        KDE integration support for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
BuildArch:      noarch

%description kdeintegration
This package contains the necessary files to enable proper KDE integration for LibreOffice.

%package sdk
Summary:        LibreOffice SDK
Group:          Documentation/HTML
Requires:       %{name} = %{version}
Requires:       gcc-c++
Requires:       make
Requires:       ucpp
Requires:       zip
Recommends:     java-devel >= 9.0
Provides:       libreoffice-ure-devel = %{version}
Obsoletes:      libreoffice-ure-devel < %{version}

%description sdk
This package contains the files needed to build plugins/add-ons for
LibreOffice. It includes header files, IDL files, needed build
tools, etc.

The documentation is in the package libreoffice-sdk-doc

%package sdk-doc
Summary:        LibreOffice SDK Documentation
Group:          Development/Libraries/Other
Suggests:       %{name}-sdk = %{version}
Enhances:       %{name}-sdk = %{version}
Provides:       libreoffice-ure-devel-doc = %{version}
Obsoletes:      libreoffice-ure-devel-doc < %{version}

%description sdk-doc
This package includes documentation and examples for the LibreOffice
Software Development Kit (SDK).

%package officebean
Summary:        OfficeBean Java Bean component for LibreOffice
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Requires:       jre >= 1.8

%description officebean
With the OfficeBean, a developer can easily write Java applications,
harnessing the power of LibreOffice. It encapsulates a connection to
a locally running LibreOffice process, and hides the complexity of
establishing and maintaining that connection from the developer.

It also allows embedding of LibreOffice documents within the Java
environment. It provides an interface the developer can use to obtain
Java AWT windows into which the backend LibreOffice process draws
its visual representation. These windows are then plugged into the UI
hierarchy of the hosting Java application. The embedded document is
controlled from the Java environment, since the OfficeBean allows
developers to access the complete LibreOffice API from their Java
environment giving them full control over the embedded document, its
appearance and behavior.

%package calc-extensions
Summary:        LibreOffice Calc Extensions
Group:          Productivity/Office/Suite
Requires:       libreoffice-calc = %{version}
# pyuno is needed for the numbertext extension
Requires:       libreoffice-pyuno = %{version}
Requires(pre):  libreoffice = %{version}
# the watchWindow extension is written in java
Requires:       jre >= 1.8

%description calc-extensions
This package provides extensions for LibreOffice Calc:

- Convert Text to Number
- New Functions NUMBERTEXT and MONEYTEXT
- Solver for Nonlinear Programming

%package writer-extensions
Summary:        LibreOffice Writer Extensions
Group:          Productivity/Office/Suite
Requires:       libreoffice-writer = %{version}
Requires(pre):  libreoffice = %{version}
# the wiki extension is written in java
Requires:       jre >= 1.8

%description writer-extensions
This package provides extensions for LibreOffice Writer:

- MediaWiki Publisher

%package -n libreofficekit
Summary:        A library providing access to LibreOffice functionality
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}

%description -n libreofficekit
LibreOfficeKit can be used to access LibreOffice functionality
through C/C++, without any need to use UNO.

%package -n libreofficekit-devel
Summary:        Development files for libreofficekit
Group:          Productivity/Office/Suite
Requires:       libreofficekit = %{version}

%description -n libreofficekit-devel
The libreofficekit-devel package contains libraries and header files for
developing applications that use libreofficekit.

# Symlink autocorr files for various conversion items
%define make_autocorr_aliases(l:) \
%{?-l: \
for lang in %{*}; do \
    ln -sf acor_%{-l*}.dat %{buildroot}%{_libdir}/%{name}/share/autocorr/acor_$lang.dat \
done \
} \
%{!?-l:%{error:-l must be present}}
# Symlinking macro for /usr/lib64 and /usr/share packing
# As argument takes name of the package
%define _link_noarch_files() \
%posttrans %{1} \
rpm -ql %{name}-%{1} > %{_datadir}/libreoffice/%{1}_list.txt || true \
if [ -f %{_datadir}/libreoffice/%{1}_list.txt ] ; then \
    %{_bindir}/libreoffice-share-linker %{_datadir}/libreoffice/%{1}_list.txt || true \
fi \
\
%postun %{1} \
if [ "$1" = "0" -a -f %{_datadir}/libreoffice/%{1}_list.txt -a -x %{_bindir}/libreoffice-share-linker ]; then \
    %{_bindir}/libreoffice-share-linker --unlink %{_datadir}/libreoffice/%{1}_list.txt || true \
    rm -f %{_datadir}/libreoffice/%{1}_list.txt 2> /dev/null || true \
fi \
%{nil}
# Crazy magic for the auto help/lang generating.
# Inspired and adjusted from Fedora spec.
%define _langpack_common(g:l:j:) \
%if "%{-l*}" != "en-US" \
%dir %{_datadir}/libreoffice/program/resource \
%dir %{_datadir}/libreoffice/program/resource/%{-g:%{-g*}}%{!-g:%{-l*}} \
%dir %{_datadir}/libreoffice/program/resource/%{-g:%{-g*}}%{!-g:%{-l*}}/LC_MESSAGES \
%{_datadir}/%{name}/program/resource/%{-g:%{-g*}}%{!-g:%{-l*}}/LC_MESSAGES/*.mo \
%endif \
%dir %{_datadir}/%{name}/share/registry \
%dir %{_datadir}/%{name}/share/registry/res \
%{_datadir}/%{name}/share/registry/Langpack-%{-l*}.xcd \
%if "%{-l*}" != "en-US" \
%{_datadir}/%{name}/share/registry/res/registry_%{-l*}.xcd \
%endif \
%{_datadir}/%{name}/share/registry/res/fcfg_langpack_%{-l*}.xcd \
%dir %{_datadir}/%{name}/share/wizards \
%{_datadir}/%{name}/share/wizards/resources_%{-j:%{-j*}}%{!-j:%{-l*}}.properties \
%{nil}
# Defines a language pack subpackage.
#
# It's necessary to define language code (-l) and language name (-n).
# Additionally, it's possible
# * to require autocorr, hunspell, hyphen or mythes package or font for
#   given language,
# * to obsolete openoffice.org-langpack package,
# * to provide libreoffice-langpack-loc package, where loc is glibc
#   locale--this is necessary for yum to pick it automatically,
# * to require other, unrelated, packages,
# * to specify file serving as file list.
# For these, lower case character argument takes an argument specifying
# language, upper case character argument uses language from -l.
#
# All remaining arguments are considered to be files and added to the file
# list.
#
# c:   additional config file (just the name stem)
# E    the package does not contain any files (i.e., has empty filelist)
# i:   additional language added to this package
# L:   internal (LibreOffice) language code, used in file names
# l:   language code, e.g., cs
# g:   glibc/java locale
# j:   java locale
# k:   glibc locale for the additional language -i
# o:   java locale for the additional language -i
# Mm:  myspell dependency
# n:   language name, e.g., Czech
# p:   Provides: of libreoffice-l10n
# q:   Provides: of libreoffice-l10n if one provide is not enough
# r:   comma-separated list of additional requires
# S:s: script classification (cjk, ctl). -S is only a marker, as it does
#      not add any .xcd into the package (the file does not exist for at
#      least one CTL-using locale, si)
# T    has help files
# Xx:  has autotext definitions
#
# Example:
# libreoffice-l10n-cs: langpack for Czech lang. Requiring myspell-cs_CZ:
# %%langpack -l cs -n Czech -m cs_CZ
%define langpack(c:Ei:g:j:k:L:l:Mm:n:o:p:q:r:S:s:TXx:) \
%define project LibreOffice \
%define lang %{-l:%{-l*}}%{!-l:%{error:Language code not defined}} \
%define _langpack_lang %{-L:%{-L*}}%{!-L:%{lang}} \
%define pkgname l10n-%{lang} \
%define langname %{-n:%{-n*}}%{!-n:%{error:Language name not defined}} \
\
%package %{pkgname} \
Summary:        %{langname} localization files for %{project} \
Group:          Productivity/Office/Suite \
Requires:       %{name} = %{version} \
Requires:       %{name}-share-linker \
Provides:       locale(libreoffice:%{lang}) \
BuildArch:      noarch \
%{-m:Requires: myspell-%{-m*}}%{!-m:%{-M:Requires: myspell-%{lang}}} \
%{-r:Requires: %{-r*}} \
%{-p: \
Provides: %{name}-l10n-%{-p*} = %{version} \
Obsoletes: %{name}-l10n-%{-p*} < %{version} \
} \
%{-q: \
Provides: %{name}-l10n-%{-q*} = %{version} \
Obsoletes: %{name}-l10n-%{-q*} < %{version} \
} \
Provides:       %{name}-help-%{lang} = %{version} \
Obsoletes:      %{name}-help-%{lang} < %{version} \
%{-L: \
Provides:       %{name}-help-%{-L*} = %{version} \
Obsoletes:      %{name}-help-%{-L*} < %{version} \
} \
%{-p: \
Provides:       %{name}-help-%{-p*} = %{version} \
Obsoletes:      %{name}-help-%{-p*} < %{version} \
} \
%{-q: \
Provides:       %{name}-help-%{-q*} = %{version} \
Obsoletes:      %{name}-help-%{-q*} < %{version} \
} \
\
%description %{pkgname} \
Provides %{langname} translations and additional resources (help files, etc.) for %{project}. \
\
%files %{pkgname} \
%{-T: \
%dir %{_datadir}/libreoffice/help/%{_langpack_lang} \
%{_datadir}/libreoffice/help/%{_langpack_lang}/* \
%if "%{-L*}" == "en-US" \
%{_datadir}/libreoffice/help/*.js \
%{_datadir}/libreoffice/help/*.css \
%{_datadir}/libreoffice/help/*.html \
%{_datadir}/libreoffice/help/media* \
%endif \
} \
%{!-E: \
%define autotextdir %{_datadir}/%{name}/share/autotext \
%dir %{autotextdir} \
%{expand:%%_langpack_common -l %{_langpack_lang} %{-g:-g %{-g*}} %{-j:-j %{-j*}}} \
%{-x:%{autotextdir}/%{-x*}}%{!-x:%{-X:%{autotextdir}/%{_langpack_lang}}} \
%{-c:%{_datadir}/%{name}/share/registry/%{-c*}.xcd} \
%{-s:%{_datadir}/%{name}/share/registry/%{-s*}_%{_langpack_lang}.xcd} \
%{-i:%{expand:%%_langpack_common -l %{-i*} %{-k:-g %{-k*}} %{-o:-j %{-o*}}}} \
} \
\
%{expand:%%_link_noarch_files %{pkgname}} \
%{nil}
%langpack -l ab -n Abkhazian -X
%langpack -l sat_Olck -n Santali -L sat-Olck -g sat_Olck -j sat_Olck -X
%langpack -l af -n Afrikaans -m af_ZA -X
%langpack -l am -n Amharic -T -X
%langpack -l ar -n Arabic -s ctl -m ar -T -X
%langpack -l as -n Assamese -X
%langpack -l ast -n Asturian -T -X
%langpack -l be -n Belarusian -m be_BY -X
%langpack -l bg -n Bulgarian -X -m bg_BG -T
%langpack -l bn -n Bengali -m bn_BD -T -X
%langpack -l bn_IN -n Bengali_India -T -p bn-IN -m bn_IN -L bn-IN -g bn_IN -j bn_IN -X
%langpack -l bo -n Tibetian -T -s ctl -m bo -X
%langpack -l br -n Breton -m br_FR -X
%langpack -l brx -n Bodo -X
%langpack -l bs -n Bosnian -T -X
%langpack -l ca -n Catalan -M -X -T
%langpack -l ca_valencia -n Valencian -m ca_ES_valencia -T -L ca-valencia -g ca@valencia -j ca_valencia -X
%langpack -l ckb -n Central_Kurdish
%langpack -l cs -n Czech -X -m cs_CZ -T
%langpack -l cy -n Welsh -X
%langpack -l da -n Danish -X -m da_DK -T
%langpack -l de -n German -X -M -T
%langpack -l dgo -n Dogri -X
%langpack -l dsb -n Lower_Sorbian -T -X
%langpack -l dz -n Dzongkha -s ctl -T -X
%langpack -l el -n Greek  -m el_GR -T -X
%langpack -l en -n English -L en-US -X -M -g en_US -T -j en_US
%langpack -l en_GB -n English_GB -M -T -X -L en-GB -g en_GB -j en_GB
%langpack -l en_ZA -n English_ZA -M -T -X -L en-ZA -g en_ZA -j en_ZA
%langpack -l eo -n Esperanto -T -X
%langpack -l es -n Spanish -M -X -T
%langpack -l et -n Estonian -m et_EE -T -X
%langpack -l eu -n Basque -T -X
%langpack -l fa -n Farsi -s ctl -X
%langpack -l fi -n Finnish -r libreoffice-voikko -X -T
%langpack -l fr -n French -X -m fr_FR -T
%langpack -l fur -n Friulian
%langpack -l fy -n Frisian -X
%langpack -l ga -n Irish -X
%langpack -l gd -n Gaelic -m gd_GB -X
%langpack -l gl -n Galician -M -T -X
%langpack -l gu -n Gujarati -s ctl -p gu-IN -m gu_IN -T -X
%langpack -l gug -n Paraguayan_Guaraní -M -X
%langpack -l he -n Hebrew -s ctl -m he_IL -T -X
%langpack -l hi -n Hindi -s ctl -p hi-IN -m hi_IN -T -X
%langpack -l hr -n Croatian -m hr_HR -X -T
%langpack -l hsb -n Upper_Sorbian -T -X
%langpack -l hu -n Hungarian -X -m hu_HU -T
%langpack -l hy -n Armenian
%langpack -l it -n Italian -X -m it_IT -T
%langpack -l id -n Indonesian -T -M -X
%langpack -l is -n Icelandic -T -X -M
%langpack -l ja -n Japanese -s cjk -X -T
%langpack -l ka -n Georgian -T -X
%langpack -l kab -n Kabyle -X
%langpack -l kk -n Kazakh -X
%langpack -l kn -n Kannada -X
%langpack -l km -n Khmer -T -X -s ctl -c ctlseqcheck_km
%langpack -l kmr_Latn -n Kurdish -M -g kmr@latin -L kmr-Latn -j kmr_Latn -X
%langpack -l ko -n Korean -s cjk -X -T
%langpack -l kok -n Konkani -X
%langpack -l ks -n Kashmiri -X
%langpack -l lb -n Luxembourgish -X
%langpack -l lo -n Lao -T -s ctl -m lo_LA -c ctlseqcheck_lo -X
%langpack -l lt -n Lithuanian -m lt_LT -X -T
%langpack -l lv -n Latvian -m lv_LV -T -X
%langpack -l mai -n Maithili -X
%langpack -l mk -n Macedonian -T -X
%langpack -l ml -n Malayalam -X
%langpack -l mn -n Monglolian -X
%langpack -l mni -n Manipuri -X
%langpack -l mr -n Marathi -X
%langpack -l my -n Burnese -s ctl -X
%langpack -l nb -n Bokmal -M -m no -T -X
%langpack -l ne -n Nepali -T -s ctl -m ne_NP -X
%langpack -l nl -n Dutch -X -m nl_NL -T
%langpack -l nn -n Nynorsk -m nn_NO -T -X
%langpack -l nr -n Southern_Ndebele -X
%langpack -l nso -n Northern_Sotho -X
%langpack -l oc -n Occitan -m oc_FR -X
%langpack -l om -n Oromo -T -X
%langpack -l or -n Odia -s ctl -X
%langpack -l pa -n Punjabi -s ctl -L pa-IN -p pa-IN -g pa_IN -j pa_IN -x pa-IN
%langpack -l pl -n Polish -X -m pl_PL -T
%langpack -l pt_BR -n Brazilian_Portuguese -m pt_BR -L pt-BR -p pt-BR -X  -g pt_BR -j pt_BR -T
%langpack -l pt_PT -n Portuguese -m pt_PT -L pt -x pt -p pt -q pt-PT -T
%langpack -l ro -n Romanian -M -X -T
%langpack -l ru -n Russian -X -m ru_RU -T
%langpack -l rw -n Kinyarwanda -X
%langpack -l sa_IN -n Sanskrit -L sa-IN -g sa_IN -j sa_IN -x sa-IN
%langpack -l sat -n Santali -X
%langpack -l sd -n Sindhi -X
%langpack -l si -n Sinhalese -S ctl -m si_LK -T -X
%langpack -l sid -n Sidamo -T -X
%langpack -l sk -n Slovak -X -m sk_SK -T
%langpack -l sl -n Slovenian -X -m sl_SI -T
%langpack -l sq -n Albanian -T -m sq_AL -X
%langpack -l sr -n Serbian -i sr-Latn -M -j sr -g sr -k sr@latin -o sr_Latn -x sr-Latn
%langpack -l ss -n Swati -X
%langpack -l st -n Southern_Sotho -X
%langpack -l sv -n Swedish -X -m sv_SE -T
%langpack -l sw_TZ -n Swahili -M -L sw-TZ -g sw_TZ -j sw_TZ -x sw-TZ
%langpack -l szl -n Silesian -X
%langpack -l ta -n Tamil -s ctl -T -X
%langpack -l te -n Telugu -m te_IN -X
%langpack -l tg -n Tajik -T -X
%langpack -l th -n Thai -s ctl -c ctlseqcheck_th -m th_TH -X
%langpack -l tl -n Tagalog -X -T
%langpack -l tn -n Tswana -X
%langpack -l tr -n Turkish -X -T -m tr_TR
%langpack -l ts -n Tsonga -X
%langpack -l tt -n Tatar -X
%langpack -l ug -n Uyghur -T -X
%langpack -l uk -n Ukrainian -m uk_UA -T -X
%langpack -l uz -n Uzbek -X
%langpack -l vi -n Vietnamese -T -X -M
%langpack -l ve -n Venda -X
%langpack -l vec -n Venetian -X
%langpack -l xh -n Xhosa -X
%langpack -l zh_CN -n Simplified_Chinese -p zh-CN -s cjk -L zh-CN -x zh-CN -q zh-Hans  -g zh_CN -j zh_CN -T
%langpack -l zh_TW -n Traditional_Chinese -p zh-TW -s cjk -L zh-TW -x zh-TW -q zh-Hant  -g zh_TW -j zh_TW -T
%langpack -l zu -n Zulu -m zu_ZA -X

%prep
%setup -q -b2 -b4
%if 0%{?suse_version} < 1500
# The rename of the configdir is needed only on older than factory for compat
%patch -P 1
%endif # Leap 42/SLE-12
%patch -P 2
%patch -P 3
%patch -P 4 -p1
%patch -P 6 -p1
%patch -P 9 -p1
%if 0%{?suse_version} < 1500
%patch -P 10 -p1
%patch -P 11 -p1
%endif
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 990 -p1
%patch -P 991 -p1
%if 0%{?suse_version} < 1550
%patch -P 992 -p1
%endif
%patch -P 996 -p1

# Disable some of the failing tests (some are random)
%if 0%{?suse_version} < 1330
sed -i -e '/CppunitTest_desktop_lib/d'  desktop/Module_desktop.mk
%endif
# Following two tests are really flaky
sed -i -e /CppunitTest_dbaccess_hsqldb_test/d dbaccess/Module_dbaccess.mk
sed -i -e s/CppunitTest_dbaccess_RowSetClones// dbaccess/Module_dbaccess.mk
# Fails due to diff caused by fonts
sed -i -e /CppunitTest_sw_rtfimport/d sw/Module_sw.mk
# only due to the above
sed -i -e /CppunitTest_sw_uiwriter/d sw/Module_sw.mk
# The gpg files are not loaded properly
sed -i -e /CPPUNIT_TEST\(testODFEncryptedGPG\)/d xmlsecurity/qa/unit/signing/signing.cxx
# breaks on LTO https://bugs.documentfoundation.org/show_bug.cgi?id=126442
sed -i -e /CppunitTest_sw_apitests/d sw/Module_sw.mk
# -flto=thin is not supported by gcc
sed -i -e s/-flto=thin/-flto/ solenv/gbuild/platform/com_GCC_defs.mk
# Disable failing tests on ppc64le for now
%ifarch ppc64le
sed -i -e /CppunitTest_sc_addin_functions_test/d sc/Module_sc.mk
sed -i -e /CppunitTest_sc_array_functions_test/d sc/Module_sc.mk
sed -i -e /CppunitTest_sc_dataprovider/d sc/Module_sc.mk # https://bugs.documentfoundation.org/show_bug.cgi?id=127099
sed -i -e /CppunitTest_sc_financial_functions_test/d sc/Module_sc.mk # https://bugs.documentfoundation.org/show_bug.cgi?id=127083
sed -i -e /CppunitTest_sc_statistical_functions_test/d sc/Module_sc.mk
%endif
if grep -q setSegmentInfoStartVersion /usr/include/CLucene/index/IndexWriter.h ; then
%patch -P 995 -p1
fi

# Do not generate doxygen timestamp
echo "HTML_TIMESTAMP = NO" >> odk/docs/cpp/Doxyfile
echo "HTML_TIMESTAMP = NO" >> odk/docs/idl/Doxyfile

%build
# Strip lto from %_lto_cflags as the project has --enable-lto option
%define _lto_cflags %{nil}
# do not eat all memory
# make sure that JAVA_HOME is set correctly
if [ -f %{_sysconfdir}/profile.d/alljava.sh ]; then
  . %{_sysconfdir}/profile.d/alljava.sh
elif [ -f %{_distconfdir}/profile.d/alljava.sh ]; then
  . %{_distconfdir}/profile.d/alljava.sh
fi
# use RPM_OPT_FLAGS, ...
# remove big debugsymbols as we simply consume too much space

### %if %{with lto}
### ARCH_FLAGS="`echo %{optflags} -flifetime-dse=1 | sed -e 's/^-g /-g1 /g' -e 's/ -g / -g1 /g' -e 's/ -g$/ -g1/g'`"
### %else
### ARCH_FLAGS="`echo %{optflags} | sed -e 's/^-g /-g1 /g' -e 's/ -g / -g1 /g' -e 's/ -g$/ -g1/g'`"
### %endif
### CFLAGS="$ARCH_FLAGS -fPIC -fstack-protector-all -D_FORTIFY_SOURCE=1"
### CXXFLAGS="-std=c++20 $ARCH_FLAGS"
### export ARCH_FLAGS CFLAGS CXXFLAGS

# Fake the epoch stuff in generated zip files
export SOURCE_DATE_EPOCH=$(date -d "$(head -n 2 %{_sourcedir}/%{name}.changes | tail -n 1 | cut -d- -f1 )" +%%s)

# Colada does not have .pc file and configure creator was really lazy
export OPENCOLLADA_CFLAGS='-I/usr/include/COLLADABaseUtils -I/usr/include/COLLADAFramework -I/usr/include/COLLADASaxFrameworkLoader -I/usr/include/GeneratedSaxParser'
export OPENCOLLADA_LIBS='-lOpenCOLLADABaseUtils -lOpenCOLLADAFramework -lOpenCOLLADASaxFrameworkLoader -lGeneratedSaxParser'

# Set up Google API keys, see http://www.chromium.org/developers/how-tos/api-keys
# Note: these are for the openSUSE Chromium builds ONLY. For your own distribution,
# please get your own set of keys.
google_api_key="AIzaSyD1hTe85_a14kr1Ks8T3Ce75rvbR1_Dx7Q"
google_default_client_id="4139804441.apps.googleusercontent.com"
google_default_client_secret="KDTRKEZk2jwT_7CDpcmMA--P"

%if %{with qt6}
export qt6_libexec_dirs="%{_libexecdir}/qt6"
export QT6DIR="%{_libdir}/qt6"
%endif

# do not run configure in autogen but use macro later
export NOCONFIGURE=yes
./autogen.sh
%configure \
        $(echo %{?_smp_mflags} | sed 's/-j/--with-parallelism=/') \
        --enable-ld=bfd \
%if %{with lto}
        --enable-lto \
%endif
        --enable-mergelibs \
        --docdir=%{_docdir}/%{name} \
        --with-compat-oowrappers \
        --with-system-headers \
        --with-system-libs \
        --with-system-jars \
        --with-system-dicts \
        --with-vendor=SUSE \
        --with-lang=ALL \
        --disable-fetch-external \
        --with-external-tar="$RPM_SOURCE_DIR" \
        --enable-gstreamer-1-0 \
        --enable-gtk3 \
%if %{with qt6}
        --enable-kf6 \
        --enable-qt6 \
%else
        --disable-kf6 \
        --disable-qt6 \
%endif
%if %{with qt5}
        --enable-gtk3-kde5 \
        --enable-kf5 \
        --enable-qt5 \
%else
        --disable-kf5 \
        --disable-qt5 \
%endif
%if 0%{?suse_version} >= 1500
        --enable-introspection \
%else
        --disable-introspection \
%endif
        --with-doxygen \
        --enable-release-build \
        --enable-split-app-modules \
        --enable-split-opt-features \
        --enable-cairo-canvas \
        --enable-largefile \
        --enable-randr \
        --without-fonts \
        --without-myspell-dicts \
        --with-jdk-home=$JAVA_HOME \
        --with-webdav=curl \
        --with-beanshell-jar=%{_datadir}/java/bsh2/bsh.jar \
        --with-ant-home=%{_datadir}/ant \
        --with-external-dict-dir=%{_datadir}/hunspell \
        --with-external-hyph-dir=%{_datadir}/hyphen \
        --with-external-thes-dir=%{_datadir}/mythes \
        --with-help=html \
        --without-export-validation \
        --enable-odk \
        --enable-evolution2 \
        --enable-dbus \
        --enable-ext-nlpsolver \
        --enable-ext-wiki-publisher \
        --enable-build-opensymbol \
        --disable-ccache \
        --enable-symbols \
        --with-gdrive-client-secret="${google_default_client_secret}" \
        --with-gdrive-client-id="${google_default_client_id}" \
        --with-libbase-jar=/usr/share/java/libbase.jar \
        --with-libxml-jar=/usr/share/java/libxml.jar \
        --with-flute-jar=/usr/share/java/flute.jar \
        --with-liblayout-jar=/usr/share/java/liblayout.jar \
        --with-libloader-jar=/usr/share/java/libloader.jar \
        --with-libformula-jar=/usr/share/java/libformula.jar \
        --with-librepository-jar=/usr/share/java/librepository.jar \
        --with-libfonts-jar=/usr/share/java/libfonts.jar \
        --with-libserializer-jar=/usr/share/java/libserializer.jar \
        %{support_abseil} \
        %{support_afdko} \
        %{support_argon2} \
        %{support_beanshell} \
        %{support_boost} \
        %{support_box2d} \
        %{support_breakpad} \
        %{support_cairo} \
        %{support_clucene} \
        %{support_coinmp} \
        %{support_cppunit} \
        %{support_curl} \
        %{support_dragonbox} \
        %{support_epm} \
        %{support_epoxy} \
        %{support_expat} \
        %{support_fast_float} \
        %{support_firebird} \
        %{support_fontconfig} \
        %{support_freetype} \
        %{support_frozen} \
        %{support_glm} \
        %{support_gpgme} \
        %{support_graphite} \
        %{support_harfbuzz} \
        %{support_hsqldb} \
        %{support_hunspell} \
        %{support_icu} \
        %{support_java_websocket} \
        %{support_jfreereport} \
        %{support_lcms2} \
        %{support_libabw} \
        %{support_libcdr} \
        %{support_libcmis} \
        %{support_libebook} \
        %{support_libeot} \
        %{support_libepubgen} \
        %{support_libetonyek} \
        %{support_libexttextcat} \
        %{support_libfixmath} \
        %{support_libfreehand} \
        %{support_libjpeg} \
        %{support_liblangtag} \
        %{support_libnumbertext} \
        %{support_libpng} \
        %{support_libtiff} \
        %{support_libwebp} \
        %{support_libxml} \
        %{support_libzmf} \
        %{support_lpsolve} \
        %{support_lzma} \
        %{support_mariadb} \
        %{support_md4c} \
        %{support_mdds} \
        %{support_mspub} \
        %{support_mwaw} \
        %{support_mythes} \
        %{support_nss} \
        %{support_odfgen} \
        %{support_onlineupdate} \
        %{support_openjpeg} \
        %{support_openldap} \
        %{support_openssl} \
        %{support_orcus} \
        %{support_pagemaker} \
        %{support_pdfium} \
        %{support_poppler} \
        %{support_postgresql} \
        %{support_python} \
        %{support_quickjs} \
        %{support_qxp} \
        %{support_redland} \
        %{support_revenge} \
        %{support_rhino} \
        %{support_skia} \
        %{support_sqlite3} \
        %{support_staroffice} \
        %{support_visio} \
        %{support_wpd} \
        %{support_wpg} \
        %{support_wps} \
        %{support_xmlsec} \
        %{support_zlib} \
        %{support_zstd} \
        %{support_zxcvbn} \
        %{support_zxing}
# no coinormp packages for coinmp

# just call make here as we added the jobs in configure
make verbose=t build

%check
export LANG=C.UTF-8
# Run tests only on x86_64 and ppc64le as they are resource hogs
%ifarch x86_64 ppc64le
# safeguard jarfires that can get magically overriden by the make
mkdir savejar
cp %{buildroot}%{_libdir}/%{name}/program/classes/*.jar savejar/
make
cp savejar/*.jar %{buildroot}%{_libdir}/%{name}/program/classes/
%endif

%install
make verbose=t DESTDIR=%{buildroot} distro-pack-install

# Do not pollute build log
set +x

# Split out gtk3 interface to -gtk3 subpackage
grep -v "%{_libdir}/libreoffice/program/libvclplug_gtk3lo.so" file-lists/gnome_list.txt > tmplist
mv tmplist file-lists/gnome_list.txt

# Remove firebird connector from main package filelist
%if %{with firebird}
grep -v "%{_libdir}/libreoffice/program/libfirebird_sdbclo.so" file-lists/common_list.txt > tmplist
mv tmplist file-lists/common_list.txt
%endif

# Remove the libanimcore from impress and put it to base (needed by draw too)
grep -v "%{_libdir}/libreoffice/program/libanimcorelo.so" file-lists/impress_list.txt > tmplist
mv tmplist file-lists/impress_list.txt
echo "%{_libdir}/libreoffice/program/libanimcorelo.so" >> file-lists/common_list.txt

################
# update desktop files
builddir=`pwd`
cd %{buildroot}%{_datadir}/applications
for desktop in * ; do
    # relative link is needed by %%suse_update_desktop_file
    relative_target=`readlink $desktop | sed "s|%{_libdir}|../../%{_lib}|"`
    # create the link
    ln -sf $relative_target $desktop
    # suse_update
    app=`echo $desktop | sed "s/.desktop//"`
    %suse_update_desktop_file $app
done
cd -
################
# compat stuff for noarch packages
mkdir -p %{buildroot}/%{_datadir}/%{name}/program
echo "%dir %{_libdir}/%{name}"                >>file-lists/common_list.txt
echo "%dir %{_datadir}/%{name}"               >>file-lists/common_list.txt
echo "%dir %{_datadir}/%{name}/program"       >>file-lists/common_list.txt
################
# helper script for noarch packages
# add missing directories to the file list
for dir in `find %{buildroot}/%{_datadir}/icons/hicolor -type d` ; do
    dir=`echo $dir | sed -e "s|%{buildroot}||"`
    echo "%dir $dir" >>file-lists/common_list.txt
done

#################################
# Move split noarch data to share
#################################
for i in %{buildroot}%{_libdir}/%{name}/program/resource/*/*/*.mo \
         %{buildroot}%{_libdir}/%{name}/share/registry/res/fcfg_langpack_*.xcd \
         %{buildroot}%{_libdir}/%{name}/share/registry/res/registry_*.xcd \
         %{buildroot}%{_libdir}/%{name}/share/registry/Langpack-*.xcd \
         %{buildroot}%{_libdir}/%{name}/share/config/images*.zip \
         %{buildroot}%{_libdir}/%{name}/share/registry/{cjk,ctl}_*.xcd \
         %{buildroot}%{_libdir}/%{name}/share/registry/ctlseqcheck_*.xcd \
         %{buildroot}%{_libdir}/%{name}/share/wizards/*.properties \
        ; do
    trg="`dirname "$i" | sed 's|%{_libdir}|%{_datadir}|'`"
    mkdir -p "$trg"
    mv "$i" "$trg"
done
# help files are luckily in just one folder
mkdir -p %{buildroot}/%{_datadir}/%{name}/help/
grep -v '%{_libdir}/%{name}/help' file-lists/common_list.txt > tmplist
mv tmplist file-lists/common_list.txt
echo "%dir %{_datadir}/%{name}/help" >>file-lists/common_list.txt
mv %{buildroot}/%{_libdir}/%{name}/help/ %{buildroot}/%{_datadir}/%{name}/
mkdir -p %{buildroot}/%{_libdir}/%{name}/help/
echo "%dir %{_libdir}/%{name}/help" >>file-lists/common_list.txt
for file in idxcaption.xsl idxcontent.xsl main_transform.xsl ; do
    mv "%{buildroot}/%{_datadir}/%{name}/help/$file" "%{buildroot}/%{_libdir}/%{name}/help/$file"
    echo "%{_libdir}/%{name}/help/$file" >> file-lists/common_list.txt
done
# autotext is another self contained dir
mkdir -p %{buildroot}/%{_datadir}/%{name}/share/autotext/
grep -v '%{_libdir}/%{name}/share/autotext' file-lists/common_list.txt > tmplist
mv tmplist file-lists/common_list.txt
mv %{buildroot}/%{_libdir}/%{name}/share/autotext/ %{buildroot}/%{_datadir}/%{name}/share/
# translations of java apps should be in lang pkgs too
grep -v '%{_libdir}/%{name}/share/wizards' file-lists/common_list.txt > tmplist
mv tmplist file-lists/common_list.txt
# the sr is dupe of sr_Latn
rm -rf %{buildroot}%{datadir}/%{name}/share/wizards/resources_sr.properties

################
# branding split
################
# create symlinks for all brandings to noarch pkg
mkdir -p %{buildroot}/%{_datadir}/%{name}/program/shell
echo "%{_datadir}/%{name}/program/shell" >> file-lists/branding_upstream.txt
for file in sofficerc \
            intro.png \
            intro-highres.png \
            shell/about.svg \
            shell/logo.svg \
            shell/logo_inverted.svg; do
    mv "%{buildroot}%{_libdir}/%{name}/program/$file" "%{buildroot}%{_datadir}/%{name}/program/$file"
    ln -sf "%{_datadir}/%{name}/program/$file" "%{buildroot}/%{_libdir}/%{name}/program/$file"
    echo "%{_datadir}/%{name}/program/$file" >> file-lists/branding_upstream.txt
done

# Fix autocorr names for various language mutations
%make_autocorr_aliases -l en-GB en-AG en-AU en-BS en-BW en-BZ en-CA en-DK en-GH en-HK en-IE en-IN en-JM en-NG en-NZ en-SG en-TT
%make_autocorr_aliases -l en-US en-PH
%make_autocorr_aliases -l en-ZA en-NA en-ZW
%make_autocorr_aliases -l af-ZA af-NA
%make_autocorr_aliases -l de de-DE de-AT de-BE de-CH de-LI de-LU
%make_autocorr_aliases -l es es-ES es-AR es-BO es-CL es-CO es-CR es-CU es-DO es-EC es-GT es-HN es-MX es-NI es-PA es-PE es-PR es-PY es-SV es-US es-UY es-VE
%make_autocorr_aliases -l fr fr-FR fr-BE fr-CA fr-CH fr-LU fr-MC
%make_autocorr_aliases -l it it-IT it-CH fur_IT lld_IT sc_IT vec_IT
%make_autocorr_aliases -l nl-NL nl-AW
%make_autocorr_aliases -l sv-SE sv-FI
pushd %{buildroot}%{_libdir}/%{name}/share/autocorr
files=""
for file in acor*.dat; do
    files="$files $file"
done
popd
for file in $files; do
    echo "%{_libdir}/%{name}/share/autocorr/$file" >> file-lists/common_list.txt
done

# we don't bother with serbian non-latin autocorr (as the lang logic allows us to dynamically allocate
# just one autotext filler and it does not make sense to have special case just for serbian
rm -r %{buildroot}%{_datadir}/libreoffice/share/autotext/sr/

# Install appdata files, so we're shown in gnome-software (and other, future app stores)
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
for appdata in base calc draw impress writer; do
  cp sysui/desktop/appstream-appdata/libreoffice-${appdata}.appdata.xml %{buildroot}%{_datadir}/metainfo/libreoffice-${appdata}.appdata.xml
  echo "%{_datadir}/metainfo/libreoffice-${appdata}.appdata.xml" >>file-lists/${appdata}_list.txt
%if 0%{?suse_version} < 1320
  echo "%dir %{_datadir}/metainfo/" >>file-lists/${appdata}_list.txt
%endif
done

%if !%{with qt}
rm -f %{buildroot}%{_datadir}/metainfo/org.libreoffice.kde.metainfo.xml
%endif

# Remove pointless readmes
rm -rf %{buildroot}%{_libdir}/%{name}/readmes/

# Prepare uno path detection, can't be patched in because it breaks tests
echo "import sys, os" > uno.py
echo "sys.path.append('%{_libdir}/%{name}/program')" >> uno.py
echo "os.putenv('URE_BOOTSTRAP', 'vnd.sun.star.pathname:%{_libdir}/libreoffice/program/fundamentalrc')" >> uno.py
cat %{buildroot}%{_libdir}/%{name}/program/uno.py >> uno.py
cp uno.py %{buildroot}%{_libdir}/%{name}/program/uno.py

# Generate python cache files
%py3_compile %{buildroot}/%{_libdir}/libreoffice/program/
%py3_compile %{buildroot}/%{_libdir}/libreoffice/share/extensions/
%py3_compile %{buildroot}/%{_libdir}/libreoffice/share/Scripts/python/
%py3_compile %{buildroot}/%{_libdir}/libreoffice/sdk/examples/python/
# Add python cache dir to respective filelist
for filelist in file-lists/*.txt; do
    # For each python file in the filelist
    for pyfile in `cat "${filelist}" | grep '\.py$'`; do
        pydir=`dirname ${pyfile}`
        pyname=`basename ${pyfile}`
        # If the bytecode for this python file exists, add it to the filelist
        if compgen -G "%{buildroot}${pydir}/__pycache__/${pyname%.*}*.pyc" > /dev/null; then
            echo "%dir ${pydir}/__pycache__/" >> "${filelist}"
            echo "${pydir}/__pycache__/${pyname%.*}*.pyc" >> "${filelist}"
        fi
    done
done

# Install color palette
cp %{SOURCE6} %{buildroot}%{_libdir}/libreoffice/share/palette/SUSE.soc
echo "%{_libdir}/libreoffice/share/palette/SUSE.soc" >> file-lists/common_list.txt

# Symlink gtk3 libreofficekit to libdir
ln -s %{_libdir}/%{name}/program/liblibreofficekitgtk.so %{buildroot}%{_libdir}/liblibreofficekitgtk.so

# Libreofficekit headers
mkdir -p %{buildroot}%{_includedir}/LibreOfficeKit/
install -m 0644 include/LibreOfficeKit/* %{buildroot}%{_includedir}/LibreOfficeKit/

%if 0%{?suse_version} >= 1500
# typelib data
mkdir -p %{buildroot}%{_libdir}/girepository-1.0/
install -m 0644 workdir/CustomTarget/sysui/share/libreoffice/LOKDocView-0.1.typelib %{buildroot}%{_libdir}/girepository-1.0/
mkdir -p %{buildroot}%{_datadir}/gir-1.0/
install -m 0644 workdir/CustomTarget/sysui/share/libreoffice/LOKDocView-0.1.gir %{buildroot}%{_datadir}/gir-1.0/
%endif

# Symlink uno.py and unohelper.py so that python can find them
# This is done after the cache files generating on purpose
mkdir -p %{buildroot}%{python3_sitelib}
ln -s %{_libdir}/libreoffice/program/uno.py %{buildroot}%{python3_sitelib}/uno.py
ln -s %{_libdir}/libreoffice/program/unohelper.py %{buildroot}%{python3_sitelib}/unohelper.py
ln -s %{_libdir}/libreoffice/program/officehelper.py %{buildroot}%{python3_sitelib}/officehelper.py
echo "%{python3_sitelib}/uno.py" >> file-lists/pyuno_list.txt
echo "%{python3_sitelib}/unohelper.py" >> file-lists/pyuno_list.txt
echo "%{python3_sitelib}/officehelper.py" >> file-lists/pyuno_list.txt

# move glade catalog to system glade dir
install -m 0755 -d %{buildroot}%{_datadir}/glade/catalogs
mv %{buildroot}%{_libdir}/%{name}/share/glade/libreoffice-catalog.xml %{buildroot}%{_datadir}/glade/catalogs
install -m 0755 -d %{buildroot}%{_datadir}/glade3/catalogs
ln -s %{_datadir}/glade/catalogs/libreoffice-catalog.xml %{buildroot}%{_datadir}/glade3/catalogs
grep -v '%{_libdir}/%{name}/share/glade/libreoffice-catalog.xml' file-lists/common_list.txt > tmplist
mv tmplist file-lists/common_list.txt

# install gdb pretty printers
export DESTDIR=%{buildroot}
export SRCDIR="./"
./solenv/bin/install-gdb-printers -a %{_datadir}/gdb/auto-load%{_libdir}/%{name} -c -i %{_libdir}/%{name} -p %{_datadir}/libreoffice/gdb

# Why would the mysql lib which is only USED by base not be IN THE BASE PACKAGE?!?
grep -v "%{_libdir}/libreoffice/program/libmysqlclo.so" file-lists/common_list.txt > tmplist
mv tmplist file-lists/common_list.txt
echo "%{_libdir}/libreoffice/program/libmysqlclo.so" >> file-lists/base_list.txt

# Remove empty files
rm %{buildroot}%{_libdir}/libreoffice/share/extensions/*/help/*.done
rm %{buildroot}%{_libdir}/libreoffice/share/extensions/*/help/*/*.ht_
rm %{buildroot}%{_libdir}/libreoffice/share/extensions/wiki-publisher/help/sa-IN/help.key_
rm %{buildroot}%{_libdir}/libreoffice/share/extensions/nlpsolver/locale/NLPSolverCommon_en_US.default

%if 0%{?suse_version} > 1500
strip-all-nondeterminism %{buildroot}%{_libdir}/libreoffice
strip-all-nondeterminism %{buildroot}%{_datadir}/%{name}
%endif

# We have ton of duped files so run over it
%fdupes %{buildroot}%{_prefix}

%post
/sbin/ldconfig
%if 0%{?suse_version} < 1500
%mime_database_post
%desktop_database_post
%icon_theme_cache_post
%endif

%preun
uno_cache="%{_libdir}/%{name}/share/uno_packages/cache/uno_packages/"
if [ "$1" = "0" ] ; then
    test -d "$uno_cache" && rm -rf "$uno_cache"/*
fi
exit 0

%postun
/sbin/ldconfig
%if 0%{?suse_version} < 1500
%icon_theme_cache_postun
%desktop_database_postun
%mime_database_postun
%endif

%if 0%{?suse_version} < 1500
%post base
%desktop_database_post

%postun base
%desktop_database_postun

%post calc
%desktop_database_post

%postun calc
%desktop_database_postun

%post draw
%desktop_database_post

%postun draw
%desktop_database_postun

%post math
%desktop_database_post

%postun math
%desktop_database_postun

%post impress
%desktop_database_post

%postun impress
%desktop_database_postun

%post writer
%desktop_database_post

%postun writer
%desktop_database_postun
%endif

%_link_noarch_files icon-themes

%files -f file-lists/common_list.txt
# ignore helper files for brp-symlink check
%exclude %{_datadir}/%{name}/program/sofficerc
%exclude %{_datadir}/%{name}/program/*.png
%exclude %{_datadir}/%{name}/program/shell/*.svg
%if 0%{?suse_version} < 1330
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%dir %{_datadir}/icons/hicolor/512x512/mimetypes
%endif

%files -n libreofficekit
%if 0%{?suse_version} >= 1500
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/LOKDocView-0.1.typelib
%endif
%{_libdir}/liblibreofficekitgtk.so
%dir %{_libdir}/libreoffice/share/libreofficekit
%{_libdir}/libreoffice/share/libreofficekit/handle_image_end.png
%{_libdir}/libreoffice/share/libreofficekit/handle_image_middle.png
%{_libdir}/libreoffice/share/libreofficekit/handle_image_start.png

%files -n libreofficekit-devel
%if 0%{?suse_version} >= 1500
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/LOKDocView-0.1.gir
%endif
%dir %{_includedir}/LibreOfficeKit
%{_includedir}/LibreOfficeKit/*

%files glade
%dir %{_datadir}/glade
%dir %{_datadir}/glade/catalogs
%{_datadir}/glade/catalogs/libreoffice-catalog.xml
%dir %{_datadir}/glade3
%dir %{_datadir}/glade3/catalogs
%{_datadir}/glade3/catalogs/libreoffice-catalog.xml

%files gdb-pretty-printers
%{_datadir}/gdb/auto-load/%{_libdir}/%{name}
%{_datadir}/libreoffice/gdb

%files -f file-lists/base_list.txt base

%files -f file-lists/calc_list.txt calc

%files -f file-lists/draw_list.txt draw

%files -f file-lists/math_list.txt math

%files -f file-lists/impress_list.txt impress

%files -f file-lists/writer_list.txt writer

%files -f file-lists/postgresql_list.txt base-drivers-postgresql

%if %{with firebird}
%files base-drivers-firebird
%{_libdir}/libreoffice/program/libfirebird_sdbclo.so
%endif

%files -f file-lists/filters_list.txt filters-optional

%files -f file-lists/mailmerge_list.txt mailmerge

%files -f file-lists/pyuno_list.txt pyuno
%exclude %{_libdir}/libreoffice/share/Scripts/python/LibreLogo
%exclude %{_libdir}/libreoffice/share/registry/librelogo.xcd

%files librelogo
%{_libdir}/libreoffice/share/registry/librelogo.xcd
%{_libdir}/libreoffice/share/Scripts/python/LibreLogo

%files -f file-lists/gnome_list.txt gnome

%files gtk3
%{_libdir}/libreoffice/program/libvclplug_gtk3lo.so

%if %{with qt5}
%files qt5
%{_libdir}/libreoffice/program/libkf5be1lo.so
%{_libdir}/libreoffice/program/libvclplug_kf5lo.so
%{_libdir}/libreoffice/program/libvclplug_qt5lo.so
%{_libdir}/libreoffice/program/libvclplug_gtk3_kde5lo.so
%{_libdir}/libreoffice/program/lo_kde5filepicker
%endif

%if %{with qt6}
%files qt6
%{_libdir}/libreoffice/program/libvclplug_kf6lo.so
%{_libdir}/libreoffice/program/libvclplug_qt6lo.so
%endif

%if %{with qt}
%files kdeintegration
%{_datadir}/metainfo/org.libreoffice.kde.metainfo.xml
%endif

%files -f file-lists/officebean_list.txt officebean

%files -f file-lists/sdk_list.txt sdk
%dir %{_libdir}/libreoffice/sdk/lib

%files -f file-lists/sdk_doc_list.txt sdk-doc

%files calc-extensions
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/extensions
%{_libdir}/%{name}/share/extensions/nlpsolver

%files writer-extensions
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/share
%dir %{_libdir}/%{name}/share/extensions
%{_libdir}/%{name}/share/extensions/wiki-publisher

%files icon-themes
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/share
%dir %{_datadir}/%{name}/share/config
%{_datadir}/%{name}/share/config/images_*.zip

%files -f file-lists/branding_upstream.txt branding-upstream

%changelog
