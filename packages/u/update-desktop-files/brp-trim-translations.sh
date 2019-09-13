#!/bin/bash
# This script goes through all polkit actions, appstream metadata and mimeinfo xml data
# and copies the .xml files into a .tar.xz for each kind. Then the xml:lang values are
# stripped out.

BASEDIR=`dirname $RPM_SOURCE_DIR`/OTHER

if ! test -f /.buildenv; then
   # this looks fishy, skip it
   echo "WARNING: I better not trim without a /.buildenv around"
   exit 0
fi

if ! test -w $BASEDIR; then
   echo "WARNING: Can't write to $BASEDIR, skipping"
   exit 0
fi

strip_xml_lang() {
  type="$1"
  file="$2"
  notrim="$3"

  if grep -q '^<!-- X-SuSE-translate=false -->' "$file"; then
    return
  fi

  nfile="${file#/$RPM_BUILD_ROOT}"
  mkdir -p "$(dirname "${BASEDIR}/${type}/${nfile}")"
  cp "${file}" "${BASEDIR}/${type}/${nfile}"

  if [ -n "${notrim}" ]; then
      return # Extraction only
  fi

  doctype=
  if [ "$type" = "polkitactions" ]; then
    doctype='<xsl:output doctype-public="-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN" doctype-system="http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd"/>'
  elif [ "$type" = "appstream" ]; then
    doctype=''
    return # For now
  elif [ "$type" = "mimetypes" ]; then
    doctype=''
  else
    echo "Unknown type '${type}'!"
  fi

  xsltproc --novalid --nonet - "$file" > "${file}_" << EOF
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output indent="yes" encoding="UTF-8" />
  $doctype
  <xsl:strip-space elements="*"/>
  <!-- Remove nodes with xml:lang attribute -->
  <xsl:template match="node()[@xml:lang]"/>

  <!-- Copy everything else recursively -->
  <xsl:template match="node()|@*">
    <xsl:copy>
      <xsl:apply-templates select="node()|@*"/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
EOF

  if [ $? -ne 0 ]; then
    echo "XSL processing failed - invalid XML?"
  else
    mv -- "${file}_" "${file}"
    echo "trimmed output to ${BASEDIR}/${type}/${nfile}"
  fi
}

strip_desktop_lang() {
  type="$1"
  file="$2"

  if grep -q ^X-SuSE-translate= "${file}"; then
    return
  fi

  nfile="${file#/$RPM_BUILD_ROOT}"
  mkdir -p "$(dirname "${BASEDIR}/${type}/${nfile}")"
  cp "${file}" "${BASEDIR}/${type}/${nfile}"
  echo "trimmed output to ${BASEDIR}/${type}/${nfile}"
  echo "trimmed output to $BASEDIR/$RPM_PACKAGE_NAME.desktopfiles"

  # Remove translations for Name,GenericName and Comment only in the [Desktop Entry] section
  awk '/^\[/ { translate=0 } /^\[Desktop Entry\]/ { translate=1; print $0; print "X-SuSE-translate=true"; next } /^(Name\[|GenericName\[|Comment\[)/ && translate==1 { next; } { print $0 }' "${file}" > "${file}_" && mv "${file}_" "${file}"
}

# Handle polkit actions
find "/$RPM_BUILD_ROOT/usr/share/polkit-1/actions/" -type f -name '*.policy' | while read -r file; do
    strip_xml_lang "polkitactions" "$file" "notrim"
done

# Handle mimetype info
find "/$RPM_BUILD_ROOT/usr/share/mime/" -type f -name '*.xml' | while read -r file; do
    strip_xml_lang "mimetypes" "$file" "notrim"
done

# Handle appstream metainfo
find "/$RPM_BUILD_ROOT/usr/share/metainfo/" "/$RPM_BUILD_ROOT/usr/share/appdata/" -type f -name '*.xml' | while read -r file; do
    strip_xml_lang "appstream" "$file" "notrim"
done

# Handle desktop files
find "/$RPM_BUILD_ROOT/opt/kde3/share/applications/kde/" \
  "/$RPM_BUILD_ROOT/opt/kde3/share/applnk/" \
  "/$RPM_BUILD_ROOT/usr/share/xsessions/" \
  "/$RPM_BUILD_ROOT/usr/share/applications/" \
  "/$RPM_BUILD_ROOT/usr/share/mimelnk/" \
  "/$RPM_BUILD_ROOT/usr/share/gnome/apps/" \
  "/$RPM_BUILD_ROOT/usr/share/autostart/" \
  "/$RPM_BUILD_ROOT/etc/xdg/autostart/" \
  "/$RPM_BUILD_ROOT/usr/share/wallpapers/" \
  "/$RPM_BUILD_ROOT/usr/share/autoinstall/" \
    -type f \( -name '*.desktop' -o -name '.directory' \) 2>/dev/null | while read -r file; do
        strip_desktop_lang "desktopfiles" "$file"
done


# Pack all files into tars
for type in desktopfiles polkitactions mimetypes appstream; do
    [ -d "${BASEDIR}/${type}" ] || continue
    pushd "${BASEDIR}/${type}"
    tar -cjf "${BASEDIR}/${RPM_PACKAGE_NAME}-${type}.tar.bz2" *
    popd
    rm -rf "${BASEDIR}/${type}"
done
