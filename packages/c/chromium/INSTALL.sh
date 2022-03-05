#!/bin/bash
set -x
while getopts s:o:l:i: option
do
case "${option}" in
s) STAGEDIR=${OPTARG};;
o) OUTPUTDIR=${OPTARG};;
l) LIBDIR=${OPTARG};;
i) ICUDATAFILE=${OPTARG};;
esac
done
SHLIB_PERMS="755"
PROGNAME="chrome"
PACKAGE="chromium-browser"
MENUNAME="Chromium Web Browser"
CHANNEL="stable"
INSTALLDIR="${LIBDIR}/chromium"

install -m 755 -d \
    "${STAGEDIR}/${INSTALLDIR}" \
    "${STAGEDIR}/usr/bin" \
    "${STAGEDIR}/usr/share/applications" \
    "${STAGEDIR}/usr/share/metainfo" \
    "${STAGEDIR}/usr/share/man/man1"

# app
buildfile="${OUTPUTDIR}/${PROGNAME}"
install -m 755 "${buildfile}" "${STAGEDIR}/${INSTALLDIR}/${PROGNAME}"

# crashpad
buildfile="${OUTPUTDIR}/chrome_crashpad_handler"
install -m 755 "${buildfile}" "${STAGEDIR}/${INSTALLDIR}/chrome_crashpad_handler"

# resources
install -m 644 "${OUTPUTDIR}/resources.pak" "${STAGEDIR}/${INSTALLDIR}/"
install -m 644 "${OUTPUTDIR}/chrome_100_percent.pak" "${STAGEDIR}/${INSTALLDIR}/"
install -m 644 "${OUTPUTDIR}/chrome_200_percent.pak" "${STAGEDIR}/${INSTALLDIR}/"

# ICU data file; Necessary when the GN icu_use_data_file flag is true.
if [ "x$ICUDATAFILE" == "xtrue" ]; then
    install -m 644 "${OUTPUTDIR}/icudtl.dat" "${STAGEDIR}/${INSTALLDIR}/"
fi

# V8 snapshot files; Necessary when the GN v8_use_external_startup_data flag
  # is true.
  # Use v8_context_snapshot.bin instead of snapshot_blob.bin if it is available.
  # TODO(crbug.com/764576): Unship snapshot_blob.bin on ChromeOS and drop this branch
install -m 644 "${OUTPUTDIR}/v8_context_snapshot.bin" "${STAGEDIR}/${INSTALLDIR}/"

# l10n paks
install -m 755 -d "${STAGEDIR}/${INSTALLDIR}/locales/"
find "${OUTPUTDIR}/locales" -type f -name '*.pak' -print -exec \
    cp -a {} "${STAGEDIR}/${INSTALLDIR}/locales/" \;
find "${STAGEDIR}/${INSTALLDIR}/locales" -type f -print -exec chmod 644 {} \;

# ANGLE
if [ -f "${OUTPUTDIR}/libEGL.so" ]; then
    for file in libEGL.so libGLESv2.so;
    do
        buildfile="${OUTPUTDIR}/${file}"
        install -m ${SHLIB_PERMS} "${buildfile}" "${STAGEDIR}/${INSTALLDIR}/${file}"
    done
fi

# ANGLE's libvulkan library
if [ -f "${OUTPUTDIR}/libvulkan.so.1" ]; then
    file="libvulkan.so.1"
    buildfile="${OUTPUTDIR}/${file}"
    install -m 755 "${buildfile}" "${STAGEDIR}/${INSTALLDIR}/${file}"
fi

# SwiftShader ES
if [ -f "${OUTPUTDIR}/swiftshader/libEGL.so" ]; then
    install -m 755 -d "${STAGEDIR}/${INSTALLDIR}/swiftshader/"
    for file in libEGL.so libGLESv2.so;
    do
        buildfile="${OUTPUTDIR}/swiftshader/${file}"
        install -m ${SHLIB_PERMS} "${buildfile}" "${STAGEDIR}/${INSTALLDIR}/swiftshader/${file}"
    done
fi

# SwiftShader VK
if [ -f "${OUTPUTDIR}/libvk_swiftshader.so" ]; then
    install -m 755 -d "${STAGEDIR}/${INSTALLDIR}/"
    file="libvk_swiftshader.so"
    buildfile="${OUTPUTDIR}/${file}"
    install -m ${SHLIB_PERMS} "${buildfile}" "${STAGEDIR}/${INSTALLDIR}/${file}"
fi
sed -e 's|${ICD_LIBRARY_PATH}|./libvk_swiftshader.so|g' third_party/swiftshader/src/Vulkan/vk_swiftshader_icd.json.tmpl > ${OUTPUTDIR}/vk_swiftshader_icd.json
# Install the ICD json file to point ANGLE to libvk_swiftshader.so
install -m 644 "${OUTPUTDIR}/vk_swiftshader_icd.json" "${STAGEDIR}/${INSTALLDIR}/"

# default apps
if [ -d "${OUTPUTDIR}/default_apps" ]; then
    cp -a "${OUTPUTDIR}/default_apps" "${STAGEDIR}/${INSTALLDIR}/"
    find "${STAGEDIR}/${INSTALLDIR}/default_apps" -type d -exec chmod 755 '{}' \;
    find "${STAGEDIR}/${INSTALLDIR}/default_apps" -type f -exec chmod 644 '{}' \;
fi

# launcher script and symlink
sed \
    -e "s#@@PROGNAME@@#${PROGNAME}#g" \
    -e "s#@@CHANNEL@@#${CHANNEL}#g" \
    "chrome/installer/linux/common/wrapper" > "${STAGEDIR}/${INSTALLDIR}/chrome-wrapper"
chmod 755 "${STAGEDIR}/${INSTALLDIR}/chrome-wrapper"
ln -s "${INSTALLDIR}/chrome-wrapper" "${STAGEDIR}/usr/bin/${PACKAGE}" 

# app icons
for size in 16 32;
do
    icon="chrome/app/theme/default_100_percent/chromium/product_logo_${size}.png"
    installpath="${STAGEDIR}/usr/share/icons/hicolor/${size}x${size}/apps/chromium-browser.png"
    install -D -m 644 ${icon} ${installpath}
done
for size in 24 48 64 128 256;
do
    icon="chrome/app/theme/chromium/product_logo_${size}.png"
    installpath="${STAGEDIR}/usr/share/icons/hicolor/${size}x${size}/apps/chromium-browser.png"
    install -D -m 644 ${icon} ${installpath}
done

# desktop integration
## AppData
install -m 644 "chrome/installer/linux/common/chromium-browser/chromium-browser.appdata.xml" \
"${STAGEDIR}/usr/share/metainfo/${PACKAGE}.appdata.xml"

## Desktop file
sed \
    -e "s#@@MENUNAME@@#${MENUNAME}#g" \
    -e "s#@@USR_BIN_SYMLINK_NAME@@#${PACKAGE}#g" \
    -e "s#@@PACKAGE@@#${PACKAGE}#g" \
    "chrome/installer/linux/common/desktop.template" > "${STAGEDIR}/usr/share/applications/${PACKAGE}.desktop"
chmod 644 "${STAGEDIR}/usr/share/applications/${PACKAGE}.desktop"

# documentation
sed \
    -e "s#@@MENUNAME@@#${MENUNAME}#g" \
    -e "s#@@PACKAGE@@#${PACKAGE}#g" \
    "chrome/app/resources/manpage.1.in" > "${STAGEDIR}/usr/share/man/man1/${PACKAGE}.1"
gzip -9n "${STAGEDIR}/usr/share/man/man1/${PACKAGE}.1"
chmod 644 "${STAGEDIR}/usr/share/man/man1/${PACKAGE}.1.gz"
