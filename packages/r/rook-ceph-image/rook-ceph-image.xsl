<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<xsl:comment> OBS-ExclusiveArch: aarch64 x86_64 </xsl:comment>
<xsl:comment>
		This file is generated,
		don't manually modify this file,
		please check README
</xsl:comment>
<image schemaversion="6.9" name="rook-ceph-image" xmlns:suse_label_helper="com.suse.label_helper">

  <description type="system">
    <author>SUSE LLC</author>
    <contact>https://bugs.opensuse.org</contact>
    <specification>Rook container for Ceph</specification>
  </description>

  <preferences>
    <type image="docker">
      <xsl:attribute name="derived_from">
        <xsl:value-of select="param/image" />
      </xsl:attribute>
      <containerconfig
        tag="latest"
        maintainer="SUSE LLC (https://bugs.opensuse.org)">
        <xsl:attribute name="additionaltags"><xsl:value-of select="param/tags" />,%PKG_VERSION%,%PKG_VERSION%.%PKG_COMMIT_NUM%,%PKG_VERSION%.%PKG_COMMIT_NUM%.%RELEASE%</xsl:attribute>
        <xsl:attribute name="name">
          <xsl:value-of select="param/name" />
        </xsl:attribute>

        <entrypoint execute="/tini">
            <argument name="--"/>
            <argument name="/usr/bin/rook"/>
        </entrypoint>

         <labels>

          <suse_label_helper:add_prefix>
            <xsl:attribute name="prefix">
              <xsl:value-of select="param/prefix" />
            </xsl:attribute>

            <label name="org.opencontainers.image.title">
              <xsl:attribute name="value">
                <xsl:value-of select="param/title" />
              </xsl:attribute>
            </label>

            <label name="org.opencontainers.image.description" value="Rook container for Ceph"/>
            <label name="org.opencontainers.image.version" value="%PKG_VERSION%.%PKG_COMMIT_NUM%.%RELEASE%"/>
            <label name="org.opencontainers.image.created" value="%BUILDTIME%"/>
            <label name="org.opencontainers.image.vendor" value="SUSE LLC"/>

            <label name="org.opencontainers.image.url">
              <xsl:attribute name="value">
                <xsl:value-of select="param/url" />
              </xsl:attribute>
            </label>

            <label name="org.openbuildservice.disturl" value="%DISTURL%"/>

            <label name="org.opensuse.reference">
              <xsl:attribute name="value">
                <xsl:value-of select="param/reference" />
              </xsl:attribute>
            </label>

          </suse_label_helper:add_prefix>

          <xsl:for-each select="param/labels/label">
            <label>
              <xsl:attribute name="name">
                <xsl:value-of select="name" />
              </xsl:attribute>
              <xsl:attribute name="value">
                <xsl:value-of select="value" />
              </xsl:attribute>
            </label>
          </xsl:for-each>

        </labels>

        <history author="SUSE LLC">Install rook and configuration</history>
     </containerconfig>
    </type>
    <version>1.0.0</version>
    <packagemanager>zypper</packagemanager>
    <rpm-check-signatures>false</rpm-check-signatures>
    <rpm-excludedocs>true</rpm-excludedocs>
    <locale>en_US</locale>
    <keytable>us.map.gz</keytable>
  </preferences>

  <repository type='rpm-md'>
    <source path='obsrepositories:/'/>
  </repository>

  <packages type="image">
    <package name="ca-certificates"/>
    <package name="tini"/>
    <package name="rook"/>
    <package name="rook-rookflex"/>
    <package name="rook-k8s-yaml"/>
    <package name="coreutils"/>
    <package name="krb5"/>
    <package name="netcfg"/>

    <xsl:for-each select="param/packages_image/package">
      <package>
        <xsl:attribute name="name">
          <xsl:value-of select="name" />
        </xsl:attribute>
      </package>
    </xsl:for-each>

  </packages>

  <packages type='bootstrap'>
    <package name='filesystem'/>
    <package name='glibc-locale-base'/>

    <xsl:for-each select="param/packages_boot/package">
      <package>
        <xsl:attribute name="name">
          <xsl:value-of select="name" />
        </xsl:attribute>
      </package>
    </xsl:for-each>

  </packages>

</image>

</xsl:template>

</xsl:stylesheet>
