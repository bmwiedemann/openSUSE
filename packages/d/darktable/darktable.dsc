Format: 3.0 (quilt)
Source: darktable
Section: graphics
Priority: optional
Binary: darktable darktable-tools-basecurve darktable-tools-noise
Architecture: any-amd64 any-arm64 any-ppc64el
Version: 5.0.0-1.1
Homepage: http://www.darktable.org/
#               libavif-dev (>= 0.9.1),
Build-Depends: cmake (>= 3.18),
               debhelper (>= 10),
               gcc (>= 12),
               gcc-13 | gcc-12,
               g++-13 | g++-12,
               intltool,
               iso-codes,
               libcairo2-dev,
               libcolord-dev,
               libcolord-gtk-dev,
               libcups2-dev,
               libcurl4-gnutls-dev | libcurl-dev,
               libexiv2-dev,
               libflickcurl-dev,
               libglib2.0-dev,
               libgmic-dev,
               libgphoto2-dev,
               libgraphicsmagick1-dev,
               libgtk-3-dev (>= 3.24.5),
               libheif-dev,
               libjpeg-dev,
               libjson-glib-dev,
               liblcms2-dev,
               liblensfun-dev,
               liblua5.4-dev | liblua5.3-dev,
               libncurses-dev,
               libopenexr-dev,
               libopenjp2-7-dev,
               libosmgpsmap-1.0-dev,
               libpng-dev,
               libportmidi-dev,
               libpugixml-dev,
               librsvg2-dev,
               libsdl2-dev,
               libsecret-1-dev,
               libsoup2.4-dev,
               libsqlite3-dev,
               libtiff-dev,
               libwebp-dev,
               lsb-release,
               xsltproc
Standards-Version: 3.9.8
Package-List:
 darktable deb graphics optional arch=any-amd64,any-arm64,any-ppc64el
DEBTRANSFORM-RELEASE: 1
